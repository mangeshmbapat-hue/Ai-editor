"""Faceless Editor: plan a faceless edit (voiceover + the owner's visuals, no presenter) in the
house style learned from the owner's four samples (editor/faceless/HOUSE_STYLE.md).

The plan is a draft EDL for the storyboard gate, never approved by itself. It sets the timing
the samples share: the picture changes every 1.5-2.5 s, a scene cuts about 0.15 s before the
word it belongs to, every number, date and name lands as on-screen text on its spoken word,
the hook line is on screen in the first second, every image moves, and the video ends on a
4-6 s end card with the owner's CTA for that video. The Faceless Editor agent then refines it
by hand (prop collage, Hyperframes graphics, SFX) before showing the owner."""

import json
import re
from pathlib import Path

from ..core import inside, now, require, write_json
from . import edl as E
from . import media

PRELAP = 0.15            # scene changes lead their word (measured on the samples: 0.1-0.2 s)
SCENE_MIN, SCENE_MAX = 1.5, 2.2   # group spans; scenes land at 1.5-2.5 s (samples: a change every 1.5-2.5 s)
END_CARD = 5.0
HOOK_MAX = 2.1
TRANSITIONS = ["fadewhite", "zoomin", "circleopen", "slideup", "fadeblack"]
TURN_WORDS = {"but", "why", "however", "yet", "lekin", "par", "magar", "kyun", "kyon", "लेकिन", "पर", "मगर", "क्यों"}
KEY = re.compile(r"^[\$₹€£]?[0-9०-९][0-9०-९,.:/]*(%|s|st|nd|rd|th|k|m|bn)?$|^[0-9०-९]+%$", re.I)
SENTENCE_END = re.compile(r"[.!?।]$")
STILL_EXT = {".jpg", ".jpeg", ".png", ".webp", ".bmp"}
HOUSE_STYLE = "faceless-collage-explainer"


def load_words(path):
    """Word timings from Whisper JSON (`transcribe`), studio/word_timing.py, or a plain list."""
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if isinstance(data, dict) and "segments" in data:
        raw = [w for s in data["segments"] for w in s.get("words", [])]
    elif isinstance(data, dict) and "words" in data:
        raw = data["words"]
    else:
        raw = data
    words = []
    for w in raw:
        text = (w.get("word") or w.get("w") or "").strip()
        start, end = w.get("start", w.get("s")), w.get("end", w.get("e"))
        if text and start is not None and end is not None:
            words.append({"word": text, "start": float(start), "end": float(end)})
    require(words, "No word timings in {}; run `transcribe` on the voiceover (or studio/word_timing.py with the script)".format(path))
    return sorted(words, key=lambda w: w["start"])


def bare(word):
    return word.strip(" \"'“”‘’()[],;:!?.।").lower()


def is_key(word, first_in_sentence):
    w = word.strip(" \"'“”‘’()[],;:!?।")
    w = w.rstrip(".") if not re.search(r"\d\.\d", w) else w
    if KEY.match(w) or (any(ch.isdigit() for ch in w) and len(w) <= 12):
        return True
    return bool(not first_in_sentence and len(w) > 2 and w[0].isupper() and w[1:].islower() and w.isalpha())


def wrap(text, width=14, max_lines=3):
    """Break on-screen text into short lines (the samples stack 1-3 words per line)."""
    lines, cur = [], ""
    for word in text.split():
        if cur and len(cur) + 1 + len(word) > width:
            lines.append(cur)
            cur = word
        else:
            cur = (cur + " " + word).strip()
    lines.append(cur)
    require(len(lines) <= max_lines, "On-screen text {!r} needs {} lines (max {}); shorten it".format(text, len(lines), max_lines))
    return "\n".join(lines)


def scenes(words, lo=SCENE_MIN, hi=SCENE_MAX):
    """Group the VO into scenes of about 1.5-2.5 s. Sentences, clauses and turn words ("But",
    "Why", "लेकिन") start scenes; a long clause is split evenly; a scrap under 0.9 s joins its
    neighbour (never across a turn word). The first scene ends by HOOK_MAX."""
    clauses, cur = [], []
    for w in words:
        if cur and (re.search(r"[.!?।,;:]$", cur[-1]["word"]) or bare(w["word"]) in TURN_WORDS):
            clauses.append(cur)
            cur = []
        cur.append(w)
    if cur:
        clauses.append(cur)

    def span(g):
        return g[-1]["end"] - g[0]["start"]

    pieces = []
    for c in clauses:
        n = max(1, int(round(span(c) / ((lo + hi) / 2.0))))
        if span(c) <= hi + 0.4 or len(c) < 2:
            n = 1
        size = -(-len(c) // n)
        pieces += [c[i:i + size] for i in range(0, len(c), size)]
    merged = []
    for g in pieces:
        turn = bare(g[0]["word"]) in TURN_WORDS
        across = merged and SENTENCE_END.search(merged[-1][-1]["word"])
        if merged and not turn and (span(g) < (0.6 if across else 0.9) or span(merged[-1]) < (0.6 if across else 0.9)) \
                and span(merged[-1]) + span(g) <= hi + 0.6:
            merged[-1] = merged[-1] + g
        else:
            merged.append(g)
    if merged and span(merged[0]) > HOOK_MAX and len(merged[0]) > 1:
        first = merged.pop(0)
        k = next((i for i, w in enumerate(first) if w["start"] - first[0]["start"] >= HOOK_MAX - 0.4), len(first) - 1) or 1
        if span(first[:k]) >= 0.9 and span(first[k:]) >= 0.9:
            merged = [first[:k], first[k:]] + merged
        else:
            merged = [first] + merged      # QC warns on a long hook shot; the samples hold their title that long too
    return merged


def stills(root, seconds=8.0, aspect="9:16", fps=30):
    """Turn every still image in raw/ into a still video (raw/stills/<name>.mp4) the EDL can cut and
    move (zoom). The images stay untouched; the clip is long enough for any scene."""
    root = Path(root)
    W, H = E_size(aspect)
    out_dir = root / "raw" / "stills"
    out_dir.mkdir(parents=True, exist_ok=True)
    made = []
    for img in sorted((root / "raw").iterdir()):
        if img.suffix.lower() not in STILL_EXT:
            continue
        target = out_dir / (img.stem + ".mp4")
        if not target.exists() or target.stat().st_mtime < img.stat().st_mtime:
            media.run(["ffmpeg", "-hide_banner", "-y", "-loop", "1", "-framerate", str(fps), "-t", "{:.2f}".format(seconds), "-i", str(img),
                       "-vf", "scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},format=yuv420p".format(W=W, H=H),
                       "-c:v", "libx264", "-preset", "veryfast", "-crf", "14", "-an", str(target)])
        made.append("raw/stills/" + target.name)
    return made


def E_size(aspect):
    from .engine import SIZES
    require(aspect in SIZES, "aspect must be one of {}".format(sorted(SIZES)))
    return SIZES[aspect]


def default_visuals(root):
    root = Path(root)
    found = []
    for p in sorted((root / "raw").rglob("*")):
        if p.is_file() and p.suffix.lower() in (".mp4", ".mov", ".mkv", ".webm", ".m4v"):
            info = media.probe(p)
            if info["has_video"]:
                found.append(str(p.relative_to(root)))
    return found


def plan(root, voice, words_file, visuals=None, cta=None, title=None, captions=True, music=None,
         aspect="9:16", end_card=END_CARD, transition_s=0.3):
    root = Path(root)
    W, H = E_size(aspect)
    vinfo = media.probe(inside(root, voice))
    require(vinfo["has_audio"], "Voiceover has no audio: " + voice)
    words = load_words(inside(root, words_file))
    visuals = list(visuals or default_visuals(root))
    require(visuals, "No visuals: put the owner's clips in raw/ (run `faceless-stills` for images) or pass --visuals")
    probes = {v: media.probe(inside(root, v)) for v in visuals}
    for v, p in probes.items():
        require(p["has_video"], "Visual has no picture: " + v)
    sources = {"V{}".format(i + 1): v for i, v in enumerate(visuals)}
    sid = {v: k for k, v in sources.items()}
    groups = scenes(words)
    vo_end = min(vinfo["duration"], words[-1]["end"] + 0.4)
    starts = [0.0] + [max(g[0]["start"] - PRELAP, 0.05) for g in groups[1:]]
    if len(starts) > 1:
        starts[1] = min(starts[1], HOOK_MAX + 0.3)   # the hook scene never runs past 2.4 s, even over a pause
    ends = starts[1:] + [vo_end]
    clips, notes, used = [], [], {v: 0.0 for v in visuals}
    sentence_start, sentences = True, 0
    for i, (g, a, b) in enumerate(zip(groups, starts, ends)):
        dur = b - a
        turn = bare(g[0]["word"]) in TURN_WORDS
        new_sentence = i and SENTENCE_END.search(groups[i - 1][-1]["word"])
        if new_sentence:
            sentences += 1
        # Seamless moves on turns and every other new sentence; the rest are hard cuts on the word.
        trans = {"type": TRANSITIONS[i % len(TRANSITIONS)], "duration": transition_s} if i and (turn or (new_sentence and sentences % 2 == 0)) else None
        need = dur + (transition_s if i + 1 < len(groups) else 0)
        pick = next((v for v in visuals[i % len(visuals):] + visuals[:i % len(visuals)]
                     if probes[v]["duration"] - used[v] >= need or probes[v]["duration"] >= need), visuals[i % len(visuals)])
        offset = used[pick] if probes[pick]["duration"] - used[pick] >= need else 0.0
        if probes[pick]["duration"] < need:
            notes.append("{} is {:.1f}s, shorter than the {:.1f}s scene {}; replace it or add a still.".format(pick, probes[pick]["duration"], need, i + 1))
        out = min(offset + need, probes[pick]["duration"])
        used[pick] = out
        clip = {"id": "C{:02d}".format(i + 1), "source": sid[pick], "in": round(offset, 3), "out": round(out, 3),
                "beat": " ".join(w["word"] for w in g),
                "zoom": {"from": 1.12, "to": 1.0} if i % 3 == 2 else {"from": 1.0, "to": 1.12}}
        if trans:
            clip["transition_in"] = trans
        if turn:
            clip["fx"] = ["flash"]
        items = []
        if i == 0:
            hook = []
            for w in g:
                hook.append(w["word"])
                if SENTENCE_END.search(w["word"]):
                    break
            hook = hook if len(hook) <= 5 else hook[:3]   # a long first sentence keeps only its first words: "Destroying the moon"
            items.append({"value": wrap(title or " ".join(hook), 9, 5), "role": "title" if max(len(x) for x in hook) <= 7 else "headline", "position": "top", "start": 0.05, "end": round(dur, 3),
                          "animate": "slam", "color": "#c44536"})
        runs, prev_key = [], False
        for w in g:
            key = is_key(w["word"], sentence_start)
            if key and prev_key:
                runs[-1].append(w)          # "Edvard Munch", "Project A119", "$381 billion" stay one graphic
            elif key:
                runs.append([w])
            prev_key = key and not re.search(r"[,.;:!?।]$", w["word"])
            sentence_start = bool(SENTENCE_END.search(w["word"]))
        for run in runs[:3 - len(items)]:
            value = " ".join(x["word"] for x in run).strip(" ,;:!?।\"'“”").rstrip(".")
            number = any(ch.isdigit() for ch in value)
            try:
                value = wrap(value)
            except E.ProductionError:
                continue                      # too long for a graphic; the agent places it by hand
            items.append({"value": value, "role": "headline", "position": "center", "start": round(max(run[0]["start"] - a, 0.0), 3),
                          "end": round(dur, 3), "animate": "pop", "color": "yellow" if number else "white", "box": True})
        if items:
            clip["text"] = items
        clips.append(clip)
    # Keep the cut times on the VO: a transition overlaps the previous clip, so that clip runs
    # longer by the transition; drop the transition where its source has no room for that.
    for i, c in enumerate(clips):
        src_dur = probes[sources[c["source"]]]["duration"]
        nxt = clips[i + 1] if i + 1 < len(clips) else None
        if nxt and nxt.get("transition_in") and c["in"] + ends[i] - starts[i] + nxt["transition_in"]["duration"] > src_dur:
            del nxt["transition_in"]
        extra = nxt["transition_in"]["duration"] if nxt and nxt.get("transition_in") else 0.0
        c["out"] = round(min(c["in"] + ends[i] - starts[i] + extra, src_dur), 3)
    last = visuals[(len(groups)) % len(visuals)]
    card = {"id": "C{:02d}".format(len(clips) + 1), "source": sid[last], "in": 0.0,
            "out": round(min(end_card, probes[last]["duration"]), 3), "beat": "end card", "transition_in": {"type": "fadeblack", "duration": 0.4},
            "zoom": {"from": 1.0, "to": 1.06}}
    if cta:
        card["text"] = [{"value": wrap(cta, 14, 4), "role": "headline", "position": "center", "start": 0.3, "end": round(card["out"] - 0.2, 3), "animate": "pop", "box": True}]
    else:
        notes.append("End card has no CTA yet: the owner gives it with each video (`--cta`).")
    if not music:
        notes.append("No music yet: add a bed (`--music`) so the end card is not dead air.")
    clips.append(card)
    edl = {"version": 1, "title": title or " ".join(w["word"] for w in groups[0])[:60], "style": HOUSE_STYLE,
           "format": {"width": W, "height": H, "fps": 30, "fit": "cover"}, "sources": sources, "clips": clips,
           "typography": {"pairing": "rozha-hind", "theme": "earth-doc"},
           "grade": {"preset": "warm-film", "vignette": True},
           "audio": {"keep_source": False, "source_gain_db": 0, "voice": {"file": voice, "gain_db": 0}},
           "master": {"lufs": -14, "true_peak": -1},
           "notes": ["Faceless plan from `{}` on {}: {} scenes at {:.2f}s average, cuts {}s before their word, key words as text on the spoken word.".format(
               words_file, now()[:10], len(groups), vo_end / len(groups), PRELAP),
               "Hand work before the storyboard: prop/paper collage and number counters as Hyperframes overlays (`mg-new`), an SFX on every transition, music."] + notes}
    if music:
        edl["audio"]["music"] = {"file": music, "gain_db": -20, "duck": True, "fade_out": 1.5}
    if captions:
        write_caption_files(root, words)
        edl["subtitles"] = {"file": "captions.srt", "burn": True, "size": 0.035, "position": "bottom", "box": True,
                            "animate": "highlight", "highlight_color": "yellow", "words": "captions.words.json"}
    E.validate(root, edl)
    rows, total = E.timeline(edl)
    drift = max(abs(r["start"] - s) for r, s in zip(rows, starts))
    require(drift < 0.05, "Scene times drifted {:.2f}s from the voiceover; check the visuals' lengths".format(drift))
    write_json(root / "edl.json", edl)
    return {"edl": str(root / "edl.json"), "scenes": len(groups), "seconds": total, "average_scene": round(vo_end / len(groups), 2),
            "text_items": sum(len(c.get("text", [])) for c in clips), "notes": edl["notes"]}


def caption_cues(words, max_words=4, min_seconds=0.9, max_cps=17, max_chars=28):
    """Group words into phone captions: at most max_words, at least min_seconds unless a sentence
    ends, and slow enough to read (max_cps characters per second)."""
    cues, cur = [], []
    for w in words:
        if cur:
            span = w["start"] - cur[0]["start"]
            chars = len(" ".join(x["word"] for x in cur))
            if len(cur) >= max_words or chars + 1 + len(w["word"]) > max_chars or (span >= min_seconds and (chars / max(span, 0.01) <= max_cps or SENTENCE_END.search(cur[-1]["word"]))):
                cues.append(cur)
                cur = []
        cur.append(w)
    if cur:
        cues.append(cur)
    return cues


def write_caption_files(root, words):
    from .tools import srt_time
    cues = caption_cues(words)
    # each cue stays up until the next one starts (or 0.9 s), so short words are still readable
    ends = [max(c[-1]["end"], min(n[0]["start"], c[0]["start"] + 0.9)) for c, n in zip(cues, cues[1:])] + [cues[-1][-1]["end"]]
    srt = "".join("{}\n{} --> {}\n{}\n\n".format(n, srt_time(c[0]["start"]), srt_time(e), " ".join(w["word"] for w in c))
                  for n, (c, e) in enumerate(zip(cues, ends), 1))
    (Path(root) / "captions.srt").write_text(srt, encoding="utf-8")
    write_json(Path(root) / "captions.words.json", words)
