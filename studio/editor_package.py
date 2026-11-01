#!/usr/bin/env python3
"""Editor package: open a finished film in an NLE (Premiere Pro, DaVinci Resolve) for small corrections.

The director writes a manifest, `editor.json`, at the mix step and runs:

    python3 studio/editor_package.py <film>/editor.json projects/<slug>/final/editor
        [--codec h264|prores] [--crf 16] [--media-root PATH] [--force]

The package is built in `<out>.partial` and moved into place only when every step has passed:

    <out>/
      README.md          how to open it in Premiere Pro or DaVinci Resolve, what is inside, the limits (Hinglish)
      <title>.xml        Final Cut Pro 7 XML (xmeml 4): the picture cut into shots on V1, every stem on its own
                         stereo track, markers on the voice lines and sync points
      timeline.csv       every shot, sound and marker with its timecode
      media/             one flat folder, so a single relink finds every file
        V_picture.mp4    the picture: H.264 without B-frames (default), or ProRes 422 HQ .mov (--codec prores)
        VO_*.wav, MUS_*.wav, ...   48 kHz stereo WAV, padded so every clip starts and ends on the frame grid
        <title>.srt      the subtitles, when the manifest has them

Manifest (paths are relative to the manifest; times are seconds on the film's timeline):

    {
      "title": "Ramayana",
      "fps": 24,
      "picture": "out/video_textless.mp4",
      "picture_textless": true,
      "picture_filter": "noise=c0s=2:allf=t",
      "subtitles": "ramayana.srt",
      "shots": [{"name": "open", "start": 0, "end": 9}, {"name": "ayodhya", "start": 9, "end": 18}],
      "audio": [{"track": "VO", "name": "L1", "file": "stems/VO_L1.wav", "start": 9.6, "text": "..."},
                {"track": "MUS drone", "file": "stems/MUS_drone.wav", "start": 0}],
      "markers": [{"t": 47.0, "name": "leap hit"}],
      "notes": ["Grain is baked into the picture, as in the master."]
    }

- `shots` must cover the picture back to back, from 0 to its last frame.
- Audio stems are post-fader and pre-master: each sits at the level it has in the mix (ducking included), so
  at 0 dB they sum to the mix before the final loudness step. An optional `gain_db` is baked into the copy.
- `picture_filter` (optional) is an ffmpeg filter applied while encoding: a finishing pass the master also
  had, such as grain. `picture_textless` says whether subtitles are burned into the picture.
- The XML points at `--media-root` (the folder media/ will sit in on the editing machine, for example
  D:\\Edits\\Ramayana\\media); by default it points at this package's own media folder, and the NLE asks
  to relink once.

Standard library only. The media steps need ffmpeg and ffprobe on PATH.
"""
from __future__ import annotations

import argparse
import csv
import json
import math
import re
import shutil
import subprocess
import sys
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Callable, Optional
from urllib.parse import quote

SR = 48000
CHECKED = "2026-11-01"
DOCS = [
    ("Premiere Pro imports Final Cut Pro 7 XML with File > Import",
     "https://helpx.adobe.com/si/premiere-pro/how-to/migrate-from-final-cut-pro.html"),
    ("DaVinci Resolve imports AAF, EDL, XML, FCPXML and OTIO timelines (File > Import Timeline; manual 18.6)",
     "https://www.steakunderwater.com/VFXPedia/__man/Resolve18-6/DaVinciResolve18_Manual_files/part1410.htm"),
    ("Loudness Normalization on export (Adobe Media Encoder, used by Premiere Pro export)",
     "https://helpx.adobe.com/media-encoder/desktop/encoding-and-exporting/automatic-loudness-correction.html"),
]


class PackageError(ValueError):
    """A manifest or media problem the director must fix; the message says what and where."""


# ---------------------------------------------------------------- time
def parse_fps(value) -> Fraction:
    """A whole frame rate (24, 25, 30 ...) or an NTSC rate (23.976, 29.97, 59.94, or "24000/1001")."""
    try:
        f = Fraction(str(value))
    except (ValueError, ZeroDivisionError):
        raise PackageError(f"fps: not a frame rate: {value!r}") from None
    for base in (24, 30, 60):
        if abs(float(f) - base * 1000 / 1001) < 0.005:
            return Fraction(base * 1000, 1001)
    if f.denominator != 1 or not 1 <= f <= 120:
        raise PackageError(f"fps must be a whole number or an NTSC rate (23.976, 29.97, 59.94), got {value!r}")
    return f


def timebase(fps: Fraction) -> tuple[int, bool]:
    return (round(fps), True) if fps.denominator == 1001 else (int(fps), False)


def seconds(value, what: str) -> Fraction:
    try:
        t = Fraction(str(value))
    except (ValueError, TypeError, ZeroDivisionError):
        raise PackageError(f"{what}: not a time in seconds: {value!r}") from None
    if t < 0:
        raise PackageError(f"{what}: negative time {value}")
    return t


def timecode(frame: int, fps: Fraction) -> str:
    tb, _ = timebase(fps)
    s, f = divmod(int(frame), tb)
    m, s = divmod(s, 60)
    h, m = divmod(m, 60)
    return f"{h:02d}:{m:02d}:{s:02d}:{f:02d}"


def align(start: Fraction, n_samples: int, fps: Fraction, sr: int = SR) -> tuple[int, int, int]:
    """Put a sound that starts at `start` seconds and lasts `n_samples` on the frame grid.

    Returns (start_frame, lead, frames): the copied file starts on `start_frame` with `lead` samples of
    silence, so the sound itself still starts exactly at `start`, and it lasts a whole number of frames.
    Exact arithmetic: 9.6 s at 24 fps is frame 230 plus 800 samples, never 230.39999."""
    start_frame = math.floor(start * fps)
    lead = round((start - Fraction(start_frame) / fps) * sr)
    frames = max(1, math.ceil(Fraction(lead + n_samples, sr) * fps))
    return start_frame, lead, frames


def frame_samples(frames: int, fps: Fraction, sr: int = SR) -> int:
    return round(Fraction(frames * sr) / fps)


# ---------------------------------------------------------------- plan
@dataclass
class Shot:
    name: str
    start: int  # timeline frames, end exclusive
    end: int


@dataclass
class Clip:
    track: str
    name: str
    src: Path
    start_s: Fraction
    text: str = ""
    gain_db: float = 0.0
    channels: int = 2
    n: int = 0          # source length in samples at 48 kHz
    lane: str = ""      # the track it lands on ("VO", or "VO 2" when lines overlap)
    start: int = 0      # timeline frame of the copied file's first sample
    lead: int = 0       # samples of silence before the sound
    frames: int = 0     # copied file length in frames
    file: str = ""      # file name in media/
    depth: int = 24

    @property
    def label(self) -> str:
        return f"{self.name} {self.text[:40]}".strip() if self.text else self.name


def safe(name: str) -> str:
    return re.sub(r"[^A-Za-z0-9_-]+", "_", str(name)).strip("_") or "item"


def plan_shots(raw, picture_frames: int, fps: Fraction) -> list[Shot]:
    if not isinstance(raw, list) or not raw:
        raise PackageError("shots: give at least one shot; together they must cover the whole picture")
    shots, prev = [], 0
    for i, s in enumerate(raw, 1):
        if not isinstance(s, dict):
            raise PackageError(f"shots[{i}]: expected {{name, start, end}}, got {s!r}")
        name = str(s.get("name") or f"shot {i}")
        a = round(seconds(s.get("start"), f"shots[{i}] {name} start") * fps)
        b = round(seconds(s.get("end"), f"shots[{i}] {name} end") * fps)
        if b <= a:
            raise PackageError(f"shots[{i}] {name}: ends at or before it starts ({s.get('start')} to {s.get('end')} s)")
        if a != prev:
            kind = "gap" if a > prev else "overlap"
            raise PackageError(f"shots[{i}] {name}: {kind} at {timecode(min(a, prev), fps)}; shots must run back to back from 0")
        shots.append(Shot(name, a, b))
        prev = b
    if prev != picture_frames:
        raise PackageError(f"the shots end at {timecode(prev, fps)} (frame {prev}) but the picture has {picture_frames} "
                           f"frames ({timecode(picture_frames, fps)}); fix the last shot's end or the picture")
    return shots


def assign_lanes(clips: list[Clip]) -> list[str]:
    """Each manifest track gets one lane; a sound that overlaps an earlier one on its track moves to "<track> 2" and so on.
    Returns the lanes in manifest track order."""
    order: list[str] = []
    lanes: dict[str, list[list]] = {}
    for c in clips:
        if c.track not in lanes:
            lanes[c.track] = []
            order.append(c.track)
    for c in sorted(clips, key=lambda c: c.start):
        ls = lanes[c.track]
        for lane in ls:
            if lane[1] <= c.start:
                lane[1] = c.start + c.frames
                c.lane = lane[0]
                break
        else:
            name = c.track if not ls else f"{c.track} {len(ls) + 1}"
            ls.append([name, c.start + c.frames])
            c.lane = name
    return [lane[0] for t in order for lane in lanes[t]]


# ---------------------------------------------------------------- xml (Final Cut Pro 7 xmeml, as Premiere Pro exports it)
def file_url(root: str, name: str) -> str:
    """A file URL the way Premiere Pro writes them: file://localhost/Users/... or file://localhost/D%3a/Edits/..."""
    r = str(root).replace("\\", "/").rstrip("/")
    m = re.match(r"^([A-Za-z]):(/.*)?$", r)
    if m:
        return "file://localhost/" + m.group(1) + "%3a" + quote((m.group(2) or "") + "/" + name)
    if not r.startswith("/"):
        raise PackageError(f"--media-root must be an absolute path, got {root!r}")
    return "file://localhost" + quote(r + "/" + name)


def _el(parent, tag, text=None, **attrs):
    e = ET.SubElement(parent, tag, {k: str(v) for k, v in attrs.items()})
    if text is not None:
        e.text = str(text)
    return e


def _rate(parent, fps):
    tb, ntsc = timebase(fps)
    r = _el(parent, "rate")
    _el(r, "timebase", tb)
    _el(r, "ntsc", "TRUE" if ntsc else "FALSE")


def _timecode(parent, fps):
    tc = _el(parent, "timecode")
    _rate(tc, fps)
    _el(tc, "string", "00:00:00:00")
    _el(tc, "frame", 0)
    _el(tc, "displayformat", "NDF")


def build_xml(title: str, fps: Fraction, width: int, height: int, picture: dict, shots: list[Shot],
              clips: list[Clip], lanes: list[str], markers: list[tuple[int, str, str]],
              url: Callable[[str], str]) -> str:
    """The timeline. Stereo stems are written as Premiere Pro writes them: an exploded pair of tracks (left
    channel, right channel) whose clips are linked, so Premiere rebuilds one stereo track per stem."""
    root = ET.Element("xmeml", version="4")
    seq = _el(root, "sequence", id="sequence-1")
    duration = max([shots[-1].end] + [c.start + c.frames for c in clips])
    _el(seq, "name", title)
    _el(seq, "duration", duration)
    _rate(seq, fps)
    media = _el(seq, "media")

    defined: set[str] = set()

    def file_el(parent, fid, name, frames, kind, depth=24):
        if fid in defined:
            _el(parent, "file", id=fid)
            return
        defined.add(fid)
        f = _el(parent, "file", id=fid)
        _el(f, "name", name)
        _el(f, "pathurl", url(name))
        _rate(f, fps)
        _el(f, "duration", frames)
        _timecode(f, fps)
        m = _el(f, "media")
        if kind == "video":
            s = _el(_el(m, "video"), "samplecharacteristics")
            _rate(s, fps)
            for k, v in (("width", width), ("height", height), ("anamorphic", "FALSE"),
                         ("pixelaspectratio", "square"), ("fielddominance", "none")):
                _el(s, k, v)
        else:
            a = _el(m, "audio")
            s = _el(a, "samplecharacteristics")
            _el(s, "depth", depth)
            _el(s, "samplerate", SR)
            _el(a, "channelcount", 2)

    video = _el(media, "video")
    sc = _el(_el(video, "format"), "samplecharacteristics")
    _rate(sc, fps)
    for k, v in (("width", width), ("height", height), ("anamorphic", "FALSE"), ("pixelaspectratio", "square"),
                 ("fielddominance", "none"), ("colordepth", 24)):
        _el(sc, k, v)
    v1 = _el(video, "track")
    n = 0
    for i, sh in enumerate(shots, 1):
        n += 1
        c = _el(v1, "clipitem", id=f"clipitem-{n}")
        _el(c, "name", f"S{i:02d} {sh.name}")
        _el(c, "enabled", "TRUE")
        _el(c, "duration", picture["frames"])
        _rate(c, fps)
        for k, v in (("start", sh.start), ("end", sh.end), ("in", sh.start), ("out", sh.end)):
            _el(c, k, v)
        _el(c, "alphatype", "none")
        _el(c, "pixelaspectratio", "square")
        _el(c, "anamorphic", "FALSE")
        file_el(c, "file-1", picture["file"], picture["frames"], "video")
    _el(v1, "enabled", "TRUE")
    _el(v1, "locked", "FALSE")

    audio = _el(media, "audio")
    _el(audio, "numOutputChannels", 2)
    af = _el(_el(audio, "format"), "samplecharacteristics")
    _el(af, "depth", 16)
    _el(af, "samplerate", SR)
    outs = _el(audio, "outputs")
    for ch in (1, 2):
        g = _el(outs, "group")
        _el(g, "index", ch)
        _el(g, "numchannels", 1)
        _el(g, "downmix", 0)
        _el(_el(g, "channel"), "index", ch)
    file_ids: dict[str, str] = {}
    for li, lane in enumerate(lanes):
        items = sorted((c for c in clips if c.lane == lane), key=lambda c: c.start)
        tl, tr = 2 * li + 1, 2 * li + 2
        pair = [_el(audio, "track", currentExplodedTrackIndex=x, totalExplodedTrackCount=2,
                    premiereTrackType="Stereo") for x in (0, 1)]
        for k, c in enumerate(items, 1):
            idl, idr = f"clipitem-{n + 1}", f"clipitem-{n + 2}"
            n += 2
            fid = file_ids.setdefault(c.file, f"file-{len(file_ids) + 2}")
            for track_el, cid, ch in ((pair[0], idl, 1), (pair[1], idr, 2)):
                ci = _el(track_el, "clipitem", id=cid, premiereChannelType="stereo")
                _el(ci, "name", c.label)
                _el(ci, "enabled", "TRUE")
                _el(ci, "duration", c.frames)
                _rate(ci, fps)
                for kk, v in (("start", c.start), ("end", c.start + c.frames), ("in", 0), ("out", c.frames)):
                    _el(ci, kk, v)
                file_el(ci, fid, c.file, c.frames, "audio", c.depth)
                st = _el(ci, "sourcetrack")
                _el(st, "mediatype", "audio")
                _el(st, "trackindex", ch)
                for lid, ti in ((idl, tl), (idr, tr)):
                    ln = _el(ci, "link")
                    _el(ln, "linkclipref", lid)
                    _el(ln, "mediatype", "audio")
                    _el(ln, "trackindex", ti)
                    _el(ln, "clipindex", k)
                    _el(ln, "groupindex", 1)
        for track_el, ch in ((pair[0], 1), (pair[1], 2)):
            _el(track_el, "enabled", "TRUE")
            _el(track_el, "locked", "FALSE")
            _el(track_el, "outputchannelindex", ch)

    _timecode(seq, fps)
    for frame, name, comment in markers:
        mk = _el(seq, "marker")
        _el(mk, "comment", comment)
        _el(mk, "name", name)
        _el(mk, "in", frame)
        _el(mk, "out", -1)
    ET.indent(root, space="  ")
    return '<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE xmeml>\n' + ET.tostring(root, encoding="unicode") + "\n"


# ---------------------------------------------------------------- media
def run(cmd) -> subprocess.CompletedProcess:
    cmd = [str(c) for c in cmd]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        raise PackageError(f"{cmd[0]} failed ({r.returncode}) on {cmd[-1]}:\n{r.stderr.strip()[-800:]}")
    return r


def probe(path: Path) -> dict:
    return json.loads(run(["ffprobe", "-v", "error", "-print_format", "json", "-show_streams", "-show_format", path]).stdout)


def _stream(info: dict, kind: str, path: Path) -> dict:
    for s in info.get("streams", []):
        if s.get("codec_type") == kind:
            return s
    raise PackageError(f"{path}: no {kind} stream")


def _duration(stream: dict, info: dict) -> Fraction:
    if stream.get("duration_ts") and stream.get("time_base"):
        return int(stream["duration_ts"]) * Fraction(stream["time_base"])
    d = stream.get("duration") or info.get("format", {}).get("duration")
    if not d:
        raise PackageError("cannot tell the duration of a media file")
    return Fraction(d)


def picture_frames(path: Path, fps: Fraction) -> int:
    info = probe(path)
    st = _stream(info, "video", path)
    if st.get("nb_frames") and st.get("r_frame_rate") and Fraction(st["r_frame_rate"]) == fps:
        return int(st["nb_frames"])
    return round(_duration(st, info) * fps)


def count_frames(path: Path) -> int:
    out = run(["ffprobe", "-v", "error", "-count_packets", "-select_streams", "v:0",
               "-show_entries", "stream=nb_read_packets", "-of", "csv=p=0", path]).stdout
    return int(out.strip().split(",")[0])


def encode_picture(src: Path, dst: Path, fps: Fraction, codec: str, extra_vf: Optional[str], crf: int = 16) -> None:
    st = _stream(probe(src), "video", src)
    rate = f"{fps.numerator}/{fps.denominator}"
    vf = f"fps={rate}" + (f",{extra_vf}" if extra_vf else "")
    color = []
    for key, flag in (("color_space", "-colorspace"), ("color_primaries", "-color_primaries"),
                      ("color_transfer", "-color_trc"), ("color_range", "-color_range")):
        v = st.get(key)
        if v and v not in ("unknown", "unspecified", "reserved"):
            color += [flag, v]
    if codec == "prores":
        enc = ["-c:v", "prores_ks", "-profile:v", "3", "-vendor", "apl0", "-pix_fmt", "yuv422p10le"]
    else:  # no B-frames: no composition offset, so no NLE can shift the picture against the sound
        enc = ["-c:v", "libx264", "-preset", "slow", "-crf", str(crf), "-bf", "0", "-g", str(timebase(fps)[0]),
               "-pix_fmt", "yuv420p", "-movflags", "+faststart"]
    run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-i", src, "-map", "0:v:0", "-an", "-sn", "-dn",
         "-vf", vf, *enc, *color, "-r", rate, dst])


def plan_audio(raw, base: Path, fps: Fraction) -> list[Clip]:
    if raw is None:
        return []
    if not isinstance(raw, list):
        raise PackageError("audio: expected a list of {track, file, start}")
    clips = []
    for i, a in enumerate(raw, 1):
        if not isinstance(a, dict):
            raise PackageError(f"audio[{i}]: expected {{track, file, start}}, got {a!r}")
        track = str(a.get("track") or "").strip()
        if not track:
            raise PackageError(f"audio[{i}]: missing the track name")
        src = (base / str(a.get("file") or "")).resolve()
        if not src.is_file():
            raise PackageError(f"audio[{i}] {track}: file not found: {src}")
        c = Clip(track=track, name=str(a.get("name") or track), src=src,
                 start_s=seconds(a.get("start", 0), f"audio[{i}] {track} start"),
                 text=str(a.get("text") or ""), gain_db=float(a.get("gain_db") or 0))
        info = probe(src)
        st = _stream(info, "audio", src)
        c.channels = int(st.get("channels") or 0)
        if c.channels not in (1, 2):
            raise PackageError(f"audio[{i}] {track}: {c.channels} channels; give mono or stereo stems")
        c.n = round(_duration(st, info) * SR)
        c.start, c.lead, c.frames = align(c.start_s, c.n, fps)
        clips.append(c)
    return clips


def _peak_db(src: Path, af: str) -> float:
    r = subprocess.run(["ffmpeg", "-nostdin", "-hide_banner", "-nostats", "-i", str(src), "-map", "0:a:0",
                        "-af", af + ",astats", "-f", "null", "-"], capture_output=True, text=True)
    vals = re.findall(r"Peak level dB:\s*(-?inf|[-+\d.]+)", r.stderr)
    if r.returncode != 0 or not vals:
        raise PackageError(f"ffmpeg could not measure {src}:\n{r.stderr.strip()[-600:]}")
    return float("-inf") if "inf" in vals[-1] else float(vals[-1])


def convert_audio(c: Clip, dst: Path, fps: Fraction) -> None:
    total = frame_samples(c.frames, fps)
    chain = [f"aresample={SR}"]
    if c.channels == 1:
        chain.append("pan=stereo|c0=c0|c1=c0")
    if c.gain_db:
        chain.append(f"volume={c.gain_db}dB")
    if c.lead:
        chain.append(f"adelay=delays={c.lead}S:all=1")
    chain += [f"apad=whole_len={total}", f"atrim=end_sample={total}"]
    af = ",".join(chain)
    # 24-bit unless the stem goes over full scale; then 32-bit float, so nothing is clipped on the way
    c.depth = 32 if _peak_db(c.src, af) > -0.01 else 24
    run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-i", c.src, "-map", "0:a:0", "-af", af,
         "-c:a", "pcm_f32le" if c.depth == 32 else "pcm_s24le", dst])


# ---------------------------------------------------------------- package
def load_manifest(path: Path) -> dict:
    try:
        m = json.loads(Path(path).read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise PackageError(f"manifest not found: {path}") from None
    except json.JSONDecodeError as e:
        raise PackageError(f"{path}: not valid JSON ({e})") from None
    if not isinstance(m, dict):
        raise PackageError(f"{path}: expected a JSON object")
    missing = [k for k in ("fps", "picture", "shots") if k not in m]
    if missing:
        raise PackageError(f"{path}: missing {', '.join(missing)}")
    return m


def collect_markers(m: dict, clips: list[Clip], fps: Fraction) -> list[tuple[int, str, str]]:
    out = [(math.floor(c.start_s * fps), c.name, c.text) for c in clips if c.text]
    for i, mk in enumerate(m.get("markers") or [], 1):
        if not isinstance(mk, dict):
            raise PackageError(f"markers[{i}]: expected {{t, name}}")
        t = seconds(mk.get("t"), f"markers[{i}] t")
        out.append((math.floor(t * fps), str(mk.get("name") or f"marker {i}"), str(mk.get("comment") or "")))
    return sorted(out, key=lambda x: x[0])


def write_csv(path: Path, shots: list[Shot], clips: list[Clip], markers, fps: Fraction) -> None:
    with open(path, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["kind", "name", "track", "start_tc", "end_tc", "start_s", "end_s", "text"])
        for i, s in enumerate(shots, 1):
            w.writerow(["shot", f"S{i:02d} {s.name}", "V1", timecode(s.start, fps), timecode(s.end, fps),
                        f"{float(s.start / fps):.3f}", f"{float(s.end / fps):.3f}", ""])
        for c in sorted(clips, key=lambda c: (c.start_s, c.lane)):
            end = c.start_s + Fraction(c.n, SR)
            w.writerow(["sound", c.name, c.lane, timecode(math.floor(c.start_s * fps), fps),
                        timecode(math.ceil(end * fps), fps), f"{float(c.start_s):.3f}", f"{float(end):.3f}", c.text])
        for frame, name, comment in markers:
            w.writerow(["marker", name, "", timecode(frame, fps), "", f"{float(frame / fps):.3f}", "", comment])


def readme(title: str, xml_name: str, fps: Fraction, size: tuple[int, int], codec: str, pic: dict,
           lanes: list[str], clips: list[Clip], shots: list[Shot], srt: Optional[str], m: dict,
           media_root: Optional[str]) -> str:
    tb, ntsc = timebase(fps)
    rate = f"{float(fps):.3f}".rstrip("0").rstrip(".")
    codec_txt = "ProRes 422 HQ (.mov)" if codec == "prores" else "H.264 (.mp4, B-frames nahi, har second keyframe)"
    textless = m.get("picture_textless")
    if textless is True:
        pic_txt = "textless: subtitles picture mein burned nahi hain, unhe SRT se lagao"
    elif textless is False:
        pic_txt = "**subtitles picture mein burned hain**; SRT sirf platform upload ya reference ke liye hai"
    else:
        pic_txt = "manifest mein nahi likha ki subtitles picture mein burned hain ya nahi; ek baar dekh lena"
    def lane_row(i: int, lane: str) -> str:
        names = sorted({c.name for c in clips if c.lane == lane})
        return f"| A{i} | {lane} | " + (", ".join(names) if len(names) <= 6 else f"{len(names)} clips") + " |"
    rows = "\n".join(lane_row(i, lane) for i, lane in enumerate(lanes, 1))
    notes = "".join(f"- {n}\n" for n in (m.get("notes") or []))
    relink = ("XML files ko `" + media_root + "` mein dhundhegi: `media/` wahin rakho to relink nahi karna padega."
              if media_root else
              "XML mein us folder ka path hai jahan package bana tha, isliye pehli baar media offline dikhega. Neeche "
              "Premiere ya Resolve ke step 2 se ek baar relink karo; saari files ek hi folder mein hain, sab ek saath "
              "mil jayengi.")
    srt_line = f"  - `{srt}`: subtitles\n" if srt else ""
    docs = "\n".join(f"- [{t}]({u})" for t, u in DOCS)
    return f"""# {title}: editor package (NLE)

Ye folder film ko Premiere Pro ya DaVinci Resolve mein kholne ke liye hai, taki chhoti corrections khud kar sako:
cut trim karna, shot aage-peeche karna, music/VO/SFX ka level, kisi line ya SFX ki timing, subtitles.

## Andar kya hai
- `{xml_name}`: timeline (Final Cut Pro 7 XML). Premiere Pro aur DaVinci Resolve dono isse import karte hain.
- `timeline.csv`: har shot, sound aur marker ka timecode.
- `media/`: saari files ek hi folder mein
  - `{pic['file']}`: picture, {size[0]}x{size[1]}, {rate} fps, {codec_txt}; {pic_txt}
  - `*.wav`: 48 kHz stereo stems, har stem alag track pe
{srt_line}
## Timeline
| Track | Kya hai | Clips |
|---|---|---|
| V1 | picture | {len(shots)} shots (S01 ... S{len(shots):02d}), har shot alag clip |
{rows}

- Premiere mein har stem ek stereo track banta hai (A1, A2 ...). Resolve kabhi ek stem ko do mono tracks (left, right)
  mein bhi la sakta hai; awaaz wahi rahegi.
- Saare audio clips 0 dB pe hain. Sab saath bajen to wahi mix banta hai jo final film mein hai, final loudness step se
  pehle. Isliye timeline final film se thodi dheemi sunai degi; export pe loudness normalize karo (neeche).
- Voice ki har line ek alag clip hai, uske shuru mein marker hai aur marker comment mein line ke shabd.
- Sequence: {rate} fps (timebase {tb}{' NTSC' if ntsc else ''}), timecode 00:00:00:00 se.

## Pehle ye
Poora folder saath rakho: XML aur `media/` ek hi jagah. {relink}

## Premiere Pro
1. File > Import > `{xml_name}`. Project panel mein ek bin aayega jisme sequence aur clips honge.
2. Media offline dikhe to Link Media > Locate, `media/` ki koi bhi ek file chuno. "Relink others automatically" on
   rakho, baaki files khud link ho jayengi.
3. Subtitles: `media/{srt or '<film>.srt'}` import karke sequence pe drag karo, caption track ban jayega.
4. Export: Effects > Loudness Normalization > ITU BS.1770-3, target -14 LUFS, true peak limiter -1 dBTP.

## DaVinci Resolve
1. Pehle `media/` ki saari files Media Pool mein import karo.
2. File > Import > Timeline > `{xml_name}`. Dialog mein "Automatically import source clips into media pool" dikhe
   to off karo: media pehle se pool mein hai, Resolve naam se jod lega.
3. Subtitles: SRT Media Pool mein import karke timeline pe drag karo.
4. Export: Deliver > Audio > Normalize Audio, -14 LUFS, -1 dBTP (apne Resolve version mein option check kar lena).

## Seedhi baat: kya yahan nahi badlega
- **Handles nahi hain.** Picture ek continuous file hai: kisi shot ka edge khichoge to agle ya pichle shot ke frames
  aa jayenge. Shot lamba chahiye ya naya frame chahiye to director se re-render.
- **Animation, puppet ki movement, camera, lighting** picture ke andar baked hai. NLE mein trim, order, speed, colour
  aur zoom ho sakta hai; animation badalni ho to director code mein karega.
- **Shabd locked hain.** Line hata ya khiska sakte ho; naye shabd chahiye to writer ke paas, phir approval.
- **Music ki ducking baked hai.** VO line ko door khiskaoge to music ka dip purani jagah rahega; wahan music track pe
  keyframe se level theek karo, ya director se re-mix.
{notes}
## Kya check hua
- Timeline XML ka structure Premiere Pro ke apne XML export jaisa hai (stereo stems = linked left/right track pair).
- Har audio file frame grid pe padded hai, picture ka frame count shots se match hai.
- Ye package yahan Premiere ya Resolve mein khol ke nahi dekha ja sakta tha; pehli baar kholo to kuch ajeeb lage to batao.

Docs checked {CHECKED}:
{docs}
"""


def build_package(manifest_path, out_dir, codec: str = "h264", media_root: Optional[str] = None,
                  force: bool = False, log: Callable[[str], None] = print, crf: int = 16) -> Path:
    for tool in ("ffmpeg", "ffprobe"):
        if not shutil.which(tool):
            raise PackageError(f"{tool} not found on PATH; the media steps need FFmpeg")
    if codec not in ("h264", "prores"):
        raise PackageError(f"codec must be h264 or prores, got {codec!r}")
    if not 0 <= int(crf) <= 51:
        raise PackageError(f"crf must be 0-51, got {crf!r}")
    mpath = Path(manifest_path).resolve()
    base = mpath.parent
    m = load_manifest(mpath)
    fps = parse_fps(m["fps"])
    title = str(m.get("title") or base.name)
    slug = safe(title)
    out = Path(out_dir).resolve()
    if out.exists() and not force:
        raise PackageError(f"{out} already exists; pass --force to replace it")
    if media_root is not None:
        file_url(media_root, "check")  # fail early on a relative root

    src_pic = (base / str(m["picture"])).resolve()
    if not src_pic.is_file():
        raise PackageError(f"picture not found: {src_pic}")
    expected = picture_frames(src_pic, fps)
    shots = plan_shots(m["shots"], expected, fps)           # fail fast, before any encode
    clips = plan_audio(m.get("audio"), base, fps)
    lanes = assign_lanes(clips)
    markers = collect_markers(m, clips, fps)
    srt_src = (base / str(m["subtitles"])).resolve() if m.get("subtitles") else None
    if srt_src and not srt_src.is_file():
        raise PackageError(f"subtitles not found: {srt_src}")

    tmp = out.with_name(out.name + ".partial")
    shutil.rmtree(tmp, ignore_errors=True)
    try:
        _build_into(tmp, out, m, fps, title, slug, codec, media_root, src_pic, expected, shots, clips, lanes,
                    markers, srt_src, log, crf)
    except BaseException:
        shutil.rmtree(tmp, ignore_errors=True)  # never leave a half-built package behind
        raise
    if out.exists():
        old = out.with_name(out.name + ".old")
        shutil.rmtree(old, ignore_errors=True)
        out.rename(old)
        tmp.rename(out)
        shutil.rmtree(old)
    else:
        tmp.rename(out)
    return out


def _build_into(tmp: Path, out: Path, m: dict, fps: Fraction, title: str, slug: str, codec: str,
                media_root: Optional[str], src_pic: Path, expected: int, shots: list[Shot], clips: list[Clip],
                lanes: list[str], markers, srt_src: Optional[Path], log: Callable[[str], None],
                crf: int = 16) -> None:
    media = tmp / "media"
    media.mkdir(parents=True)
    pic = {"file": "V_picture" + (".mov" if codec == "prores" else ".mp4")}
    log(f"picture: {src_pic.name} -> media/{pic['file']} ({codec}, {expected} frames)")
    encode_picture(src_pic, media / pic["file"], fps, codec, m.get("picture_filter"), crf)
    pic["frames"] = count_frames(media / pic["file"])
    if pic["frames"] != expected:
        raise PackageError(f"the encoded picture has {pic['frames']} frames, the source {expected}; not packaging a "
                           f"picture that drifts against the sound")
    vs = _stream(probe(media / pic["file"]), "video", media / pic["file"])
    size = (int(vs["width"]), int(vs["height"]))

    used: set[str] = set()
    for c in clips:
        stem = safe(c.track) + ("" if c.name == c.track else "_" + safe(c.name))
        name, k = stem, 2
        while name.lower() in used:
            name, k = f"{stem}_{k}", k + 1
        used.add(name.lower())
        c.file = name + ".wav"
        convert_audio(c, media / c.file, fps)
        log(f"sound: {c.src.name} -> media/{c.file} on {c.lane} at {timecode(c.start, fps)} (+{c.lead} samples)")
    srt = None
    if srt_src:
        srt = slug + ".srt"
        shutil.copyfile(srt_src, media / srt)

    root = media_root or str(out / "media")
    xml_name = slug + ".xml"
    (tmp / xml_name).write_text(build_xml(title, fps, size[0], size[1], pic, shots, clips, lanes, markers,
                                          lambda n: file_url(root, n)), encoding="utf-8")
    write_csv(tmp / "timeline.csv", shots, clips, markers, fps)
    (tmp / "README.md").write_text(readme(title, xml_name, fps, size, codec, pic, lanes, clips, shots, srt, m,
                                          media_root), encoding="utf-8")


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description="Build an NLE editor package (Premiere Pro / DaVinci Resolve XML "
                                            "timeline, stems, subtitles) from a film's editor.json.")
    p.add_argument("manifest", help="the film's editor.json")
    p.add_argument("out", help="the package folder to create, e.g. projects/<slug>/final/editor")
    p.add_argument("--codec", choices=("h264", "prores"), default="h264",
                   help="picture codec: h264 (small download, default) or prores (ProRes 422 HQ, large)")
    p.add_argument("--media-root", help="absolute path of media/ on the editing machine, e.g. D:\\Edits\\Ramayana\\media; "
                                        "default: this package's own media folder (the NLE asks to relink once)")
    p.add_argument("--crf", type=int, default=16,
                   help="H.264 quality (default 16). 18 is still visually lossless and about a third smaller: use it "
                        "when the package has to fit a 400 MB upload")
    p.add_argument("--force", action="store_true", help="replace an existing package")
    a = p.parse_args(argv)
    try:
        out = build_package(a.manifest, a.out, a.codec, a.media_root, a.force, crf=a.crf)
    except PackageError as e:
        print(f"editor_package: {e}", file=sys.stderr)
        return 2
    print(out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
