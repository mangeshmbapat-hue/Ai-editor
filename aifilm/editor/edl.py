"""Mann's edit decision list (EDL): validation, timeline maths, the filter graph per clip,
the storyboard and the owner's approval gate.

An edit project is a folder (normally `projects/<slug>/edit/`, git-ignored):

    BRIEF.md            the owner's script / direction (verbatim)
    raw/                the owner's footage, music and SFX (never modified)
    media.json          probe + sha256 of every ingested file
    edl.json            Mann's cut (this module's schema)
    storyboard/         numbered frames + STORYBOARD.md + storyboard.json
    approvals.json      the owner's explicit approvals, tied to an EDL fingerprint
    renders/            master.mp4, preview_720p.mp4, QC.md, qc.json
"""

import re
import shutil
import subprocess
import tempfile
from pathlib import Path

from ..core import ProductionError, file_hash, fingerprint, inside, now, project_lock, read_json, require, write_json
from . import media

TRANSITIONS = {
    "cut", "fade", "fadeblack", "fadewhite", "dissolve", "wipeleft", "wiperight", "wipeup", "wipedown",
    "slideleft", "slideright", "slideup", "slidedown", "smoothleft", "smoothright", "circleopen", "circleclose",
    "radial", "pixelize", "zoomin", "hblur", "distance", "squeezeh", "squeezev",
}
# Colour presets: FFmpeg filter chains. They are starting points, judged on the storyboard frames.
GRADES = {
    "neutral": "",
    "punchy-social": "eq=contrast=1.12:saturation=1.28:gamma=0.97,unsharp=5:5:0.4",
    "teal-orange": "colorbalance=rs=-0.06:gs=0.0:bs=0.09:rh=0.09:gh=0.02:bh=-0.08,eq=contrast=1.08:saturation=1.12",
    "warm-film": "colorbalance=rm=0.06:bm=-0.05:rh=0.04,eq=contrast=1.05:saturation=0.95,noise=alls=5:allf=t",
    "cool-night": "colorbalance=bs=0.10:bm=0.06:rh=-0.04,eq=brightness=-0.03:saturation=0.88:contrast=1.06",
    "bw-contrast": "hue=s=0,eq=contrast=1.30:gamma=0.95",
    "faded-vintage": "curves=preset=vintage,eq=saturation=0.85",
    "moody-dark": "eq=brightness=-0.05:contrast=1.15:saturation=0.85,vignette=PI/4.5",
    "bright-clean": "eq=brightness=0.03:contrast=1.04:saturation=1.08,colorbalance=rh=0.02:bh=0.02",
}
TEXT_POSITIONS = {"top": "h*0.18", "center": "(h-text_h)/2", "bottom": "h*0.66"}
DEVANAGARI = re.compile("[ऀ-ॿ]")


def load(root):
    root = Path(root)
    edl = read_json(root / "edl.json")
    validate(root, edl)
    return edl


def num(value, name, low=None, high=None):
    require(isinstance(value, (int, float)) and not isinstance(value, bool), name + " must be a number")
    require(low is None or value >= low, "{} must be >= {}".format(name, low))
    require(high is None or value <= high, "{} must be <= {}".format(name, high))
    return float(value)


def clip_duration(clip):
    return (clip["out"] - clip["in"]) / clip.get("speed", 1.0)


def transition(clip):
    t = clip.get("transition_in") or {"type": "cut"}
    return t.get("type", "cut"), (0.0 if t.get("type", "cut") == "cut" else float(t.get("duration", 0.5)))


def validate(root, edl):
    require(isinstance(edl, dict) and edl.get("version") == 1, "edl.json needs \"version\": 1")
    fmt = edl.get("format", {})
    for key in ("width", "height"):
        require(isinstance(fmt.get(key), int) and fmt[key] >= 16 and fmt[key] % 2 == 0, "format.{} must be an even integer".format(key))
    num(fmt.get("fps", 30), "format.fps", 1, 120)
    sources = edl.get("sources")
    require(isinstance(sources, dict) and sources, "sources must map ids to files in the edit folder")
    probes = {}
    for sid, rel in sources.items():
        require(re.fullmatch(r"[A-Za-z][A-Za-z0-9_-]*", sid) is not None, "Bad source id " + sid)
        probes[sid] = media.probe(inside(root, rel))
        require(probes[sid]["has_video"], "Source {} has no video stream".format(sid))
    clips = edl.get("clips")
    require(isinstance(clips, list) and clips, "clips must be a nonempty list")
    seen = set()
    for i, clip in enumerate(clips):
        cid = clip.get("id")
        require(isinstance(cid, str) and cid not in seen, "Clip {} needs a unique id".format(i + 1))
        seen.add(cid)
        require(clip.get("source") in sources, "{}: unknown source {!r}".format(cid, clip.get("source")))
        dur = probes[clip["source"]]["duration"]
        start, end = num(clip.get("in"), cid + ".in", 0), num(clip.get("out"), cid + ".out", 0)
        require(start < end, cid + ": in must be before out")
        require(end <= dur + 0.05, "{}: out {:.2f}s is past the end of {} ({:.2f}s)".format(cid, end, clip["source"], dur))
        num(clip.get("speed", 1.0), cid + ".speed", 0.25, 4.0)
        kind, tdur = transition(clip)
        require(kind in TRANSITIONS, "{}: unknown transition {!r}".format(cid, kind))
        require(i > 0 or kind == "cut", cid + ": the first clip cannot have a transition in")
        if i:
            shortest = min(clip_duration(clip), clip_duration(clips[i - 1]))
            require(0 <= tdur < shortest, "{}: transition {:.2f}s must be shorter than both clips".format(cid, tdur))
        grade = clip.get("grade")
        require(grade is None or grade in GRADES, "{}: unknown grade {!r}".format(cid, grade))
        zoom = clip.get("zoom")
        if zoom:
            num(zoom.get("from", 1.0), cid + ".zoom.from", 1.0, 3.0)
            num(zoom.get("to", 1.0), cid + ".zoom.to", 1.0, 3.0)
        for text in clip.get("text", []) if isinstance(clip.get("text"), list) else [clip["text"]] if clip.get("text") else []:
            require(isinstance(text.get("value"), str) and text["value"].strip(), cid + ": text needs a value")
            require(text.get("position", "bottom") in TEXT_POSITIONS, cid + ": text position must be top/center/bottom")
    grade = edl.get("grade", {})
    require(grade.get("preset", "neutral") in GRADES, "Unknown grade preset {!r}; choose from {}".format(grade.get("preset"), sorted(GRADES)))
    if grade.get("lut"):
        require(inside(root, grade["lut"]).is_file(), "LUT file missing: " + grade["lut"])
    audio = edl.get("audio", {})
    music = audio.get("music")
    if music:
        require(media.probe(inside(root, music["file"]))["has_audio"], "Music file has no audio")
    for sfx in audio.get("sfx", []):
        require(media.probe(inside(root, sfx["file"]))["has_audio"], "SFX {} has no audio".format(sfx["file"]))
        num(sfx.get("at"), "sfx.at", 0)
    for ov in edl.get("overlays", []):
        media.probe(inside(root, ov["file"]))
        num(ov.get("at", 0), "overlay.at", 0)
    subs = edl.get("subtitles")
    if subs:
        require(inside(root, subs["file"]).is_file(), "Subtitle file missing: " + subs["file"])
    return probes


def timeline(edl):
    """Start time of every clip on the final timeline, and the total duration."""
    rows, cursor = [], 0.0
    for i, clip in enumerate(edl["clips"]):
        _, tdur = transition(clip)
        start = cursor - tdur if i else 0.0
        dur = clip_duration(clip)
        rows.append({"id": clip["id"], "start": round(start, 3), "end": round(start + dur, 3), "duration": round(dur, 3)})
        cursor = start + dur
    return rows, round(cursor, 3)


def pace(edl):
    rows, total = timeline(edl)
    lengths = sorted(r["duration"] for r in rows)
    mid = len(lengths) // 2
    median = lengths[mid] if len(lengths) % 2 else (lengths[mid - 1] + lengths[mid]) / 2
    return {"total_seconds": total, "shots": len(rows), "average_shot_seconds": round(total / len(rows), 2),
            "median_shot_seconds": round(median, 2), "longest_shot_seconds": lengths[-1], "shortest_shot_seconds": lengths[0],
            "cuts_per_10s": round(10.0 * max(len(rows) - 1, 0) / total, 2) if total else 0}


def tc(seconds):
    m, s = divmod(max(seconds, 0), 60)
    return "{}:{:04.1f}".format(int(m), s)


def font_for(text, override=None):
    if override:
        return override
    pattern = "sans:bold:lang=hi" if DEVANAGARI.search(text) else "sans:bold"
    if shutil.which("fc-match"):
        found = subprocess.run(["fc-match", "-f", "%{file}", pattern], capture_output=True, text=True).stdout.strip()
        if found:
            return found
    return None


def esc(path):
    """Escape a path for use inside an FFmpeg filter option."""
    return str(path).replace("\\", "/").replace(":", "\\:").replace("'", "\\'").replace(",", "\\,")


def grade_chain(root, edl, clip):
    g = edl.get("grade", {})
    parts = [GRADES[clip.get("grade") or g.get("preset", "neutral")]]
    eq = []
    if g.get("exposure"):
        eq.append("brightness={}".format(num(g["exposure"], "grade.exposure", -0.5, 0.5)))
    if g.get("contrast"):
        eq.append("contrast={}".format(num(g["contrast"], "grade.contrast", 0.5, 2.0)))
    if g.get("saturation") is not None:
        eq.append("saturation={}".format(num(g["saturation"], "grade.saturation", 0.0, 3.0)))
    if eq:
        parts.append("eq=" + ":".join(eq))
    if g.get("temperature"):
        parts.append("colortemperature=temperature={}".format(int(num(g["temperature"], "grade.temperature", 1000, 40000))))
    if g.get("lut"):
        parts.append("lut3d=file='{}'".format(esc(inside(root, g["lut"]))))
    if g.get("vignette"):
        parts.append("vignette=PI/5")
    if g.get("grain"):
        parts.append("noise=alls={}:allf=t".format(int(num(g["grain"], "grade.grain", 1, 40))))
    return ",".join(p for p in parts if p)


def clip_video_chain(root, edl, clip, textfiles, t0=0.0):
    """FFmpeg filters that turn a trimmed source clip into a formatted, graded, titled shot.
    `t0` offsets time-based expressions so a single storyboard frame matches the moving render."""
    fmt = edl["format"]
    W, H, fps = fmt["width"], fmt["height"], fmt.get("fps", 30)
    speed = clip.get("speed", 1.0)
    dur = clip_duration(clip)
    chain = ["setpts=(PTS-STARTPTS)/{}".format(speed)] if speed != 1.0 else ["setpts=PTS-STARTPTS"]
    if fmt.get("fit", "cover") == "contain":
        chain += ["scale={W}:{H}:force_original_aspect_ratio=decrease".format(W=W, H=H),
                  "pad={W}:{H}:(ow-iw)/2:(oh-ih)/2:color=black".format(W=W, H=H)]
    else:
        chain += ["scale={W}:{H}:force_original_aspect_ratio=increase".format(W=W, H=H), "crop={W}:{H}".format(W=W, H=H)]
    zoom = clip.get("zoom")
    if zoom and (zoom.get("from", 1.0) != 1.0 or zoom.get("to", 1.0) != 1.0):
        z0, z1 = float(zoom.get("from", 1.0)), float(zoom.get("to", 1.0))
        expr = "({z0}+({z1}-{z0})*min(1,(t+{t0})/{d}))".format(z0=z0, z1=z1, t0=t0, d=dur)
        chain += ["scale=w='2*trunc({W}*{e}/2)':h='2*trunc({H}*{e}/2)':eval=frame".format(W=W, H=H, e=expr),
                  "crop={W}:{H}".format(W=W, H=H)]
    graded = grade_chain(root, edl, clip)
    if graded:
        chain.append(graded)
    texts = clip.get("text") or []
    texts = texts if isinstance(texts, list) else [texts]
    for item in texts:
        handle = tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False, encoding="utf-8")
        handle.write(item["value"])
        handle.close()
        textfiles.append(handle.name)
        font = font_for(item["value"], item.get("font"))
        size = int(item.get("size", round(H * 0.045)))
        start, end = float(item.get("start", 0)), float(item.get("end", dur))
        opts = ["textfile='{}'".format(esc(handle.name)), "fontsize={}".format(size), "fontcolor={}".format(item.get("color", "white")),
                "x=(w-text_w)/2", "y={}".format(TEXT_POSITIONS[item.get("position", "bottom")]),
                "borderw={}".format(max(2, size // 14)), "bordercolor=black@0.85",
                "enable='between(t+{t0},{s},{e})'".format(t0=t0, s=start, e=end)]
        if item.get("box"):
            opts += ["box=1", "boxcolor=black@0.55", "boxborderw={}".format(size // 3)]
        if font:
            opts.insert(0, "fontfile='{}'".format(esc(font)))
        chain.append("drawtext=" + ":".join(opts))
    chain += ["fps={}".format(fps), "format=yuv420p", "setsar=1", "settb=AVTB"]
    return ",".join(chain)


def edit_fingerprint(root, edl):
    files = sorted(set(list(edl["sources"].values())
                       + ([edl["audio"]["music"]["file"]] if edl.get("audio", {}).get("music") else [])
                       + [s["file"] for s in edl.get("audio", {}).get("sfx", [])]
                       + [o["file"] for o in edl.get("overlays", [])]
                       + ([edl["subtitles"]["file"]] if edl.get("subtitles") else [])
                       + ([edl["grade"]["lut"]] if edl.get("grade", {}).get("lut") else [])))
    return fingerprint({"edl": edl, "files": {f: file_hash(inside(root, f)) for f in files}})


def clip_summary(edl, row, clip):
    kind, tdur = transition(clip)
    texts = clip.get("text") or []
    texts = texts if isinstance(texts, list) else [texts]
    return {"id": clip["id"], "source": clip["source"], "in": clip["in"], "out": clip["out"], "speed": clip.get("speed", 1.0),
            "start": row["start"], "duration": row["duration"], "transition": kind if kind == "cut" else "{} {:.2f}s".format(kind, tdur),
            "grade": clip.get("grade") or edl.get("grade", {}).get("preset", "neutral"),
            "text": " | ".join(t["value"] for t in texts), "beat": clip.get("beat", ""), "zoom": clip.get("zoom")}


def diff(old, new):
    before = {c["id"]: c for c in old}
    after = {c["id"]: c for c in new}
    lines = ["- added {} ({}s at {})".format(i, after[i]["duration"], tc(after[i]["start"])) for i in after if i not in before]
    lines += ["- removed {}".format(i) for i in before if i not in after]
    for i in after:
        if i in before:
            changed = [k for k in ("source", "in", "out", "speed", "transition", "grade", "text", "beat", "zoom") if before[i].get(k) != after[i].get(k)]
            if changed:
                lines.append("- changed {}: {}".format(i, ", ".join("{} {!r} -> {!r}".format(k, before[i].get(k), after[i].get(k)) for k in changed)))
    if [c["id"] for c in old if c["id"] in after] != [c["id"] for c in new if c["id"] in before]:
        lines.append("- clip order changed")
    return lines


def global_summary(edl):
    return {"format": edl["format"], "grade": edl.get("grade", {}), "audio": edl.get("audio", {}),
            "overlays": edl.get("overlays", []), "subtitles": edl.get("subtitles"), "master": edl.get("master", {}), "style": edl.get("style")}


def flatten(value, prefix=""):
    if isinstance(value, dict):
        out = {}
        for k, v in value.items():
            out.update(flatten(v, "{}.{}".format(prefix, k) if prefix else k))
        return out
    if isinstance(value, list) and value and all(isinstance(x, dict) for x in value):
        out = {}
        for i, v in enumerate(value):
            out.update(flatten(v, "{}[{}]".format(prefix, i)))
        return out
    return {prefix: value}


def diff_globals(old, new):
    if not old:
        return []
    a, b = flatten(old), flatten(new)
    return ["- changed {}: {} -> {}".format(k, json_short(a.get(k)), json_short(b.get(k)))
            for k in sorted(set(a) | set(b)) if a.get(k) != b.get(k)]


def json_short(value):
    import json
    text = json.dumps(value, ensure_ascii=False, sort_keys=True)
    return text if len(text) <= 160 else text[:157] + "..."


def still_frames(root, edl, indices, out):
    """Pull exact frames out of the full edit graph (transitions, overlays, subtitles included)
    without writing a video file: what the owner approves is what will render."""
    from .render import build_graph
    probes = validate(root, edl)
    textfiles = []
    try:
        inputs, graph, v, a, total = build_graph(root, edl, probes, textfiles)
        select = "+".join("eq(n\\,{})".format(i) for i in sorted(set(indices)))
        graph += ";[{}]select='{}'[sb];[{}]anullsink".format(v, select, a)
        media.run(["ffmpeg", "-hide_banner", "-y"] + inputs + ["-filter_complex", graph, "-map", "[sb]", "-fps_mode", "passthrough",
                   "-q:v", "3", "-t", "{:.3f}".format(total), str(out / ".all-%04d.jpg")])
    finally:
        for f in textfiles:
            Path(f).unlink(missing_ok=True)
    written = sorted(out.glob(".all-*.jpg"))
    unique = sorted(set(indices))
    require(len(written) == len(unique), "Storyboard extraction returned {} of {} frames".format(len(written), len(unique)))
    by_index = dict(zip(unique, written))
    for n, i in enumerate(indices, 1):
        target = out / ".still-{:04d}.jpg".format(n)
        target.write_bytes(by_index[i].read_bytes())
    for f in written:
        f.unlink()


def storyboard(root, frames_per_clip=1):
    """Render one graded, formatted, titled frame per clip (two when asked) and write STORYBOARD.md.
    This is the owner's gate: nothing is rendered in full until the owner approves this exact EDL."""
    root = Path(root)
    with project_lock(root):
        edl = load(root)
        rows, total = timeline(edl)
        out = root / "storyboard"
        previous = read_json(out / "storyboard.json") if (out / "storyboard.json").exists() else None
        if out.exists():
            for f in out.glob("F*.jpg"):
                f.unlink()
        out.mkdir(parents=True, exist_ok=True)
        frames, summaries, picks = [], [], []
        fps = float(edl["format"].get("fps", 30))
        for row, clip in zip(rows, edl["clips"]):
            summaries.append(clip_summary(edl, row, clip))
            for frac in ([0.5] if frames_per_clip == 1 else [0.15, 0.85]):
                picks.append((clip["id"], min(int(round((row["start"] + row["duration"] * frac) * fps)), int(total * fps) - 1)))
        still_frames(root, edl, [p[1] for p in picks], out)
        for n, (cid, index) in enumerate(picks, 1):
            name = "F{:02d}_{}_{}.jpg".format(n, cid, tc(index / fps).replace(":", "m") + "s")
            (out / ".still-{:04d}.jpg".format(n)).replace(out / name)
            frames.append({"file": name, "clip": cid, "timeline": round(index / fps, 2)})
        stats = pace(edl)
        globals_now = global_summary(edl)
        changes = (diff(previous["clips"], summaries) + diff_globals(previous.get("globals", {}), globals_now)) if previous else []
        record = {"edl_fingerprint": edit_fingerprint(root, edl), "created": now(), "frames": frames, "clips": summaries,
                  "globals": globals_now, "pace": stats, "changes_since_previous": changes}
        write_json(out / "storyboard.json", record)
        (out / "STORYBOARD.md").write_text(storyboard_markdown(edl, record, total), encoding="utf-8")
        return record


def storyboard_markdown(edl, record, total):
    fmt = edl["format"]
    p = record["pace"]
    lines = ["# Storyboard: {}".format(edl.get("title", "untitled")), "",
             "Status: **waiting for owner approval** (`python3 -m aifilm.editor approve <edit-dir> --words \"<owner's words>\"`).",
             "Fingerprint: `{}`".format(record["edl_fingerprint"][:16]), "",
             "Format {}x{} @ {} fps · total {} · {} shots · average shot {}s · {} cuts per 10 s · grade `{}`{}".format(
                 fmt["width"], fmt["height"], fmt.get("fps", 30), tc(total), p["shots"], p["average_shot_seconds"], p["cuts_per_10s"],
                 edl.get("grade", {}).get("preset", "neutral"), " · style `{}`".format(edl["style"]) if edl.get("style") else ""), ""]
    if record["changes_since_previous"]:
        lines += ["## Changes since the previous storyboard", ""] + record["changes_since_previous"] + [""]
    lines += ["## Frames", "", "| # | Frame | Timeline | Clip | Source in-out | Shot | Transition in | Grade | On-screen text | Beat |",
              "|---|---|---|---|---|---|---|---|---|---|"]
    by_id = {c["id"]: c for c in record["clips"]}
    for i, f in enumerate(record["frames"], 1):
        c = by_id[f["clip"]]
        lines.append("| {} | `{}` | {} | {} | {} {:.2f}-{:.2f}s{} | {:.2f}s | {} | {} | {} | {} |".format(
            i, f["file"], tc(f["timeline"]), c["id"], c["source"], c["in"], c["out"],
            " x{}".format(c["speed"]) if c["speed"] != 1.0 else "", c["duration"], c["transition"], c["grade"],
            c["text"].replace("|", "/") or "-", c["beat"].replace("|", "/") or "-"))
    audio = edl.get("audio", {})
    lines += ["", "## Sound plan", ""]
    music = audio.get("music")
    lines.append("- Music: {}".format("`{}` at {} dB{}".format(music["file"], music.get("gain_db", -16),
                                                              ", ducked under voice" if music.get("duck", True) else "") if music else "none"))
    lines.append("- Source audio: {}".format("kept at {} dB".format(audio.get("source_gain_db", 0)) if audio.get("keep_source", True) else "muted"))
    for s in audio.get("sfx", []):
        lines.append("- SFX `{}` at {} ({} dB)".format(s["file"], tc(s["at"]), s.get("gain_db", 0)))
    for o in edl.get("overlays", []):
        lines.append("- Motion graphic `{}` at {}".format(o["file"], tc(o.get("at", 0))))
    if edl.get("subtitles"):
        lines.append("- Subtitles `{}` ({})".format(edl["subtitles"]["file"], "burned in" if edl["subtitles"].get("burn", True) else "sidecar"))
    master = edl.get("master", {})
    lines.append("- Master loudness {} LUFS, true peak <= {} dBTP".format(master.get("lufs", -14), master.get("true_peak", -1)))
    lines += ["", "## Rules applied (Mann fills this before showing the owner)", "",
              "For each Editor rule in `studio/LEARNINGS.md` and `editor/rules.json`, one line: how this cut follows it.", ""]
    return "\n".join(lines) + "\n"


def approve(root, words, by="owner", kind="storyboard"):
    """Record the owner's explicit approval of the current storyboard (or final cut), tied to the EDL fingerprint."""
    root = Path(root)
    require(isinstance(words, str) and words.strip(), "Quote the owner's exact approval words with --words")
    require(kind in ("storyboard", "final"), "kind must be storyboard or final")
    with project_lock(root):
        edl = load(root)
        current = edit_fingerprint(root, edl)
        if kind == "storyboard":
            board = root / "storyboard" / "storyboard.json"
            require(board.exists(), "No storyboard yet; run `storyboard` and show it to the owner first")
            require(read_json(board)["edl_fingerprint"] == current, "The EDL changed after the storyboard was made; rebuild and re-show it")
        else:
            qc = root / "renders" / "qc.json"
            require(qc.exists() and read_json(qc).get("edl_fingerprint") == current, "Run render and qc for this EDL before final approval")
        path = root / "approvals.json"
        log = read_json(path) if path.exists() else {"approvals": []}
        entry = {"kind": kind, "edl_fingerprint": current, "by": by, "words": words.strip(), "at": now()}
        log["approvals"].append(entry)
        write_json(path, log)
        return entry


def approved(root, edl, kind="storyboard"):
    path = Path(root) / "approvals.json"
    if not path.exists():
        return False
    current = edit_fingerprint(root, edl)
    return any(a["kind"] == kind and a["edl_fingerprint"] == current for a in read_json(path)["approvals"])


def require_approval(root, edl):
    if not approved(root, edl, "storyboard"):
        raise ProductionError("Storyboard not approved for this exact EDL. Run `storyboard`, show the frames to the owner, "
                              "and record their words with `approve` before rendering.")
