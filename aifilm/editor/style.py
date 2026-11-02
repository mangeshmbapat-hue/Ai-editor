"""Editing-style breakdown of a reference video: measured cut rhythm, colour, loudness and
silence, plus one frame per shot for Mann to study. The measurements are facts; the
style sheet's craft sections (transitions, type, motion graphics, sound design, VFX) are
written by Mann after looking at the frames, and are labelled as observations."""

import shutil
from pathlib import Path

from ..core import now, require, write_json
from . import media
from .edl import tc

MAX_SHOT_FRAMES = 60


def shots_from_cuts(cuts, duration):
    edges = [0.0] + [c for c in cuts if 0.05 < c < duration - 0.05] + [duration]
    return [{"start": round(a, 3), "end": round(b, 3), "duration": round(b - a, 3)} for a, b in zip(edges, edges[1:]) if b - a > 0.04]


def pace_curve(shots, duration, window=10.0):
    curve, t = [], 0.0
    while t < duration:
        cuts = sum(1 for s in shots[1:] if t <= s["start"] < t + window)
        curve.append({"from": round(t, 1), "cuts": cuts})
        t += window
    return curve


def stats(values):
    v = sorted(values)
    if not v:
        return {}
    mid = len(v) // 2
    return {"mean": round(sum(v) / len(v), 2), "median": round(v[mid] if len(v) % 2 else (v[mid - 1] + v[mid]) / 2, 2),
            "min": round(v[0], 2), "max": round(v[-1], 2)}


def words_per_second(srt_path):
    import re
    text = Path(srt_path).read_text(encoding="utf-8-sig")
    spans = re.findall(r"(\d+):(\d+):(\d+)[,.](\d+)\s*-->\s*(\d+):(\d+):(\d+)[,.](\d+)", text)
    lines = [l for l in text.splitlines() if l.strip() and not re.match(r"^\d+$", l.strip()) and "-->" not in l]
    words = sum(len(l.split()) for l in lines)
    secs = 0.0
    for h1, m1, s1, ms1, h2, m2, s2, ms2 in spans:
        secs += (int(h2) * 3600 + int(m2) * 60 + int(s2) + int(ms2) / 1000.0) - (int(h1) * 3600 + int(m1) * 60 + int(s1) + int(ms1) / 1000.0)
    return round(words / secs, 2) if secs else None


def analyze(video, workdir, name, threshold=0.3, transcript=None):
    video, workdir = Path(video), Path(workdir)
    info = media.probe(video)
    require(info["has_video"] and info["duration"] > 0, "Reference has no playable video")
    workdir.mkdir(parents=True, exist_ok=True)
    frames_dir = workdir / "frames"
    if frames_dir.exists():
        shutil.rmtree(frames_dir)
    cuts = media.scene_cuts(video, threshold)
    shots = shots_from_cuts(cuts, info["duration"])
    step = max(1, -(-len(shots) // MAX_SHOT_FRAMES))
    sampled, pixels, tones = [], [], []
    for i, shot in enumerate(shots):
        mid = shot["start"] + shot["duration"] / 2
        px = media.frame_rgb(video, mid)
        tone = media.tone(px)
        shot.update(tone)
        tones.append(tone)
        pixels.extend(px[::3])
        if i % step == 0:
            name_ = "S{:03d}_{}.jpg".format(i + 1, tc(mid).replace(":", "m") + "s")
            media.save_frame(video, mid, frames_dir / name_, width=540)
            sampled.append({"shot": i + 1, "file": "frames/" + name_, "at": round(mid, 2)})
    lengths = [s["duration"] for s in shots]
    loud = media.loudness(video) if info["has_audio"] else None
    quiet = media.silences(video, -40, 0.7) if info["has_audio"] else []
    analysis = {
        "name": name, "analyzed": now(), "source": {k: info.get(k) for k in ("duration", "width", "height", "fps", "has_audio")},
        "aspect": "9:16" if info.get("height", 0) > info.get("width", 0) else ("1:1" if info.get("height") == info.get("width") else "16:9"),
        "scene_threshold": threshold,
        "pace": {"shots": len(shots), "shot_seconds": stats(lengths),
                 "cuts_per_10s": round(10.0 * (len(shots) - 1) / info["duration"], 2),
                 "first_cut_seconds": shots[0]["duration"] if shots else None,
                 "fast_shots_under_1s": sum(1 for x in lengths if x < 1.0),
                 "long_shots_over_4s": sum(1 for x in lengths if x > 4.0),
                 "curve_per_10s": pace_curve(shots, info["duration"])},
        "colour": {"palette": [{"hex": h, "share": s} for h, s in media.palette(pixels, 6)],
                   "luma": stats([t["luma"] for t in tones]), "saturation": stats([t["saturation"] for t in tones]),
                   "warmth_r_minus_b": stats([t["warmth"] for t in tones])},
        "audio": {"loudness": loud, "silences_over_0_7s": quiet},
        "speech": {"words_per_second": words_per_second(transcript)} if transcript else None,
        "shots": shots, "frames": sampled,
    }
    write_json(workdir / "analysis.json", analysis)
    (workdir / "STYLE_SHEET.draft.md").write_text(sheet(analysis), encoding="utf-8")
    return analysis


def suggest_grade(colour):
    luma, sat, warm = colour["luma"].get("mean", 128), colour["saturation"].get("mean", 0.3), colour["warmth_r_minus_b"].get("mean", 0)
    if sat < 0.06:
        return "bw-contrast"
    if luma < 80:
        return "moody-dark" if warm >= 0 else "cool-night"
    if warm > 25 and sat < 0.35:
        return "warm-film"
    if sat > 0.45:
        return "punchy-social"
    if warm > 10:
        return "teal-orange"
    return "bright-clean" if luma > 150 else "neutral"


def targets(analysis):
    p = analysis["pace"]
    return {"aspect": analysis["aspect"], "average_shot_seconds": p["shot_seconds"].get("mean"),
            "median_shot_seconds": p["shot_seconds"].get("median"), "cuts_per_10s": p["cuts_per_10s"],
            "first_cut_seconds": p["first_cut_seconds"], "grade_preset": suggest_grade(analysis["colour"]),
            "palette": [c["hex"] for c in analysis["colour"]["palette"]],
            "loudness_lufs": (analysis["audio"]["loudness"] or {}).get("lufs")}


def sheet(a):
    p, c = a["pace"], a["colour"]
    t = targets(a)
    curve = " ".join(str(x["cuts"]) for x in p["curve_per_10s"])
    loud = a["audio"]["loudness"] or {}
    lines = [
        "# Style sheet: {}".format(a["name"]), "",
        "Status: **draft**. The Measured section is from FFmpeg. Every other section is Mann's observation from the frames and must be written before this sheet is used.", "",
        "## Measured", "",
        "- Source: {}s, {}x{}, {} fps, aspect {}".format(round(a["source"]["duration"], 1), a["source"]["width"], a["source"]["height"], a["source"]["fps"], a["aspect"]),
        "- Shots: {} · shot length mean {}s, median {}s, range {}–{}s".format(p["shots"], p["shot_seconds"].get("mean"), p["shot_seconds"].get("median"),
                                                                           p["shot_seconds"].get("min"), p["shot_seconds"].get("max")),
        "- Cuts per 10 s: {} overall; per 10 s window: {}".format(p["cuts_per_10s"], curve),
        "- Hook: first cut at {}s · shots under 1 s: {} · shots over 4 s: {}".format(p["first_cut_seconds"], p["fast_shots_under_1s"], p["long_shots_over_4s"]),
        "- Palette: {}".format(", ".join("{} ({:.0%})".format(x["hex"], x["share"]) for x in c["palette"])),
        "- Luma mean {} · saturation mean {} · warmth (R−B) mean {}".format(c["luma"].get("mean"), c["saturation"].get("mean"), c["warmth_r_minus_b"].get("mean")),
        "- Loudness: {} LUFS, true peak {} dBTP, LRA {}".format(loud.get("lufs"), loud.get("true_peak"), loud.get("lra")),
        "- Silences over 0.7 s: {}".format(len(a["audio"]["silences_over_0_7s"])),
    ]
    if a.get("speech"):
        lines.append("- Speech rate: {} words/s".format(a["speech"]["words_per_second"]))
    lines += ["", "## Targets for an edit in this style (machine-readable copy in style.json)", "",
              "- Average shot {}s, cuts per 10 s {}, first cut by {}s".format(t["average_shot_seconds"], t["cuts_per_10s"], t["first_cut_seconds"]),
              "- Starting grade preset `{}` (check against the frames; adjust or build a LUT)".format(t["grade_preset"]), ""]
    for head, prompt in [
        ("Hook and structure", "What happens in the first 0.5 s, 3 s and 10 s; where the re-hooks land; how it ends or loops."),
        ("Cutting", "Cut types (hard cut, jump cut, J/L cut, match cut, smash cut, speed ramp), and what motivates the cuts (beat, word, action)."),
        ("Camera and framing", "Shot sizes, punch-ins and zooms, handheld vs locked, reframes for 9:16."),
        ("Transitions", "Which transitions, how long, how often; whoosh or swish pairs."),
        ("Typography and captions", "Font family and weight, size, case, colour, outline/box, position, words per caption, animation (pop, karaoke, typewriter)."),
        ("Motion graphics", "Lower thirds, callouts, arrows, maps, counters, stickers; how they enter and exit; Hyperframes build notes."),
        ("Colour", "Contrast, saturation, skin tones, highlights/shadows tint, grain, vignette; matching LUT or grade preset."),
        ("Sound design", "Music genre/tempo, drops on cuts, risers, whooshes, hits, ambience, silence use, voice processing."),
        ("VFX", "Screen shake, glitches, light leaks, overlays, masks, freeze frames, speed ramps."),
        ("Do / don't", "The 5 rules that make this style recognisable, and the mistakes that would break it."),
    ]:
        lines += ["## {}".format(head), "", "_Mann: {}_".format(prompt), ""]
    lines += ["## Frames studied", ""] + ["- `{}` shot {} at {}".format(f["file"], f["shot"], tc(f["at"])) for f in a["frames"]]
    return "\n".join(lines) + "\n"


def publish(workdir, styles_root, slug):
    """Copy a finished style sheet and its targets into editor/styles/<slug>/ (no frames, no video)."""
    import json
    workdir, dest = Path(workdir), Path(styles_root) / slug
    analysis = json.loads((workdir / "analysis.json").read_text(encoding="utf-8"))
    sheet_path = workdir / "STYLE_SHEET.md"
    require(sheet_path.exists(), "Write {} (from the draft, with every observation section filled) first".format(sheet_path))
    text = sheet_path.read_text(encoding="utf-8")
    require("_Mann:" not in text, "STYLE_SHEET.md still has unfilled `_Mann:` sections")
    dest.mkdir(parents=True, exist_ok=True)
    (dest / "STYLE_SHEET.md").write_text(text.replace("Status: **draft**", "Status: **learned**"), encoding="utf-8")
    slim = {k: v for k, v in analysis.items() if k not in ("shots", "frames")}
    write_json(dest / "style.json", {"slug": slug, "targets": targets(analysis), "analysis": slim})
    return dest
