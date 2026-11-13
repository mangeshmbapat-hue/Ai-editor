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
TRANSITIONS = ["fade", "smoothleft", "circleopen", "slideup", "smoothright"]   # smooth moves; no dips to black or white flashes on dark themes
TURN_WORDS = {"but", "why", "however", "yet", "lekin", "magar", "kyun", "kyon", "लेकिन", "मगर", "क्यों"}   # not "par"/"पर": it also means "on"
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
    joined = []
    for w in sorted(words, key=lambda w: w["start"]):
        if joined and w["word"] in ("%", "%.", "%,", "-end", "-end."):   # Whisper splits "25 %" and "high -end"
            joined[-1] = dict(joined[-1], word=joined[-1]["word"] + w["word"].lstrip("-") if not w["word"].startswith("-") else joined[-1]["word"] + w["word"], end=w["end"])
        else:
            joined.append(w)
    words = joined
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
        if cur and (re.search(r"[.!?।,;:]$", cur[-1]["word"]) or bare(w["word"]) in TURN_WORDS or bare(w["word"]) in ("number", "step", "tip")):
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
    merged, pending = [], []
    for g in pieces:
        if pending:
            g, pending = pending + g, []
        if bare(g[0]["word"]) in ("number", "step", "tip") and span(g) < 0.9:
            pending = g                  # "Number one," opens the next scene, it never trails the last one
            continue
        turn = bare(g[0]["word"]) in TURN_WORDS
        across = merged and SENTENCE_END.search(merged[-1][-1]["word"])
        if merged and not turn and (span(g) < (0.6 if across else 0.9) or span(merged[-1]) < (0.6 if across else 0.9)) \
                and span(merged[-1]) + span(g) <= hi + (0.6 if across else 1.2):   # a scrap inside a sentence always joins
            merged[-1] = merged[-1] + g
        else:
            merged.append(g)
    if pending:
        merged.append(pending)
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


def plan(root, voice, words_file, visuals=None, cta=None, title=None, captions=False, music=None,
         aspect="9:16", end_card=END_CARD, transition_s=0.3, theme_name=None, texts=None):
    root = Path(root)
    W, H = E_size(aspect)
    th = theme(theme_name)        # one colour theme for the whole video (owner rule 2026-11-13)
    vinfo = media.probe(inside(root, voice))
    require(vinfo["has_audio"], "Voiceover has no audio: " + voice)
    words = load_words(inside(root, words_file))
    visuals = list(visuals or default_visuals(root))
    require(visuals, "No visuals: put the owner's clips in raw/ (run `faceless-stills` for images) or pass --visuals")
    probes = {v: media.probe(inside(root, v)) for v in visuals}
    for v, p in probes.items():
        require(p["has_video"], "Visual has no picture: " + v)
        if is_image(v):
            p["duration"] = 600.0          # an image becomes an animated scene clip of exactly its scene's length
    sources = {"V{}".format(i + 1): v for i, v in enumerate(visuals)}

    def zone_of(v):
        # raw/stills/<name>.mp4 is made from raw/<name>.jpg; faceless-card wrote raw/<name>.layout.json
        p = Path(root) / "raw" / (Path(v).stem + ".layout.json")
        return json.loads(p.read_text(encoding="utf-8"))["text_zone"] if p.exists() else "lower"
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
                "zoom": {"from": 1.04, "to": 1.0} if i % 3 == 2 else {"from": 1.0, "to": 1.04}}   # slow, steady drift (owner: no shake)
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
            items.append({"value": wrap(title or " ".join(hook), 8 if max(len(x) for x in hook) <= 8 else 10, 8), "clean": True, "role": "title" if max(len(x) for x in hook) <= 8 else "headline", "position": "top" if zone_of(pick) == "top" else "bottom", "start": 0.05, "end": round(dur, 3),
                          "animate": "pop", "color": th["accent"]})
        runs, prev_key, prev = [], False, None
        for j, w in enumerate(g):
            key = is_key(w["word"], sentence_start)
            if key and prev_key:
                runs[-1].append(w)          # "Edvard Munch", "Project A119", "$381 billion" stay one graphic
            elif key:
                # "Supreme Court": a capitalised sentence opener belongs to the name that follows it
                opener = prev is not None and prev["word"][:1].isupper() and prev["word"].isalpha() and runs_start_ok(prev)
                runs.append(([prev] if opener else []) + [w])
            elif prev_key and runs and any(ch.isdigit() for ch in runs[-1][-1]["word"]) and w["word"].strip(".,").isalpha() and len(w["word"]) <= 9:
                runs[-1].append(w)          # a number keeps its unit: "12 logon", "2000 crore", "30 second"
                key = True
            prev_key = key and not re.search(r"[,.;:!?।]$", w["word"])
            sentence_start = bool(SENTENCE_END.search(w["word"]))
            prev = w
        runs = [r_ for r_ in runs if dur - (r_[0]["start"] - a) >= 0.9]   # a word said in the last moment of a scene gets no flash of text
        for run in runs[:3 - len(items)]:
            value = " ".join(x["word"] for x in run).strip(" ,;:!?।\"'“”").rstrip(".")
            number = any(ch.isdigit() for ch in value)
            try:
                value = wrap(value, 10, 2)        # headline size: about 10 characters per line fit the 9:16 safe zone
            except E.ProductionError:
                continue                      # too long for a graphic; the agent places it by hand
            zone = zone_of(pick)
            pos = "top" if zone == "top" else ("lower" if "\n" in value else "bottom")
            if items:
                continue                      # one text block per scene, in the zone the card left free for it
            items.append({"value": value, "clean": True, "role": "headline", "position": pos, "start": round(max(run[0]["start"] - a, 0.0), 3),
                          "end": round(dur, 3), "animate": "pop", "color": th["highlight"] if number else th["text"], "box": True})
        if turn and not items:             # a turn ("But...", "Why?") gets its own short line
            phrase = []
            for w in g:
                if phrase and (len(phrase) >= 4 or len(" ".join(phrase + [w["word"]])) > 20):
                    break                      # a short, whole phrase: "Lekin asli sawaal", "But the strangest part?"
                phrase.append(w["word"])
                if SENTENCE_END.search(w["word"]):
                    break
            items.append({"value": " ".join(phrase).strip(" ,"), "role": "headline", "position": "bottom",
                          "start": round(max(g[0]["start"] - a, 0.0), 3), "end": round(dur, 3), "animate": "fade", "color": th["text"]})
        if texts and str(i + 1) in texts:   # the editor's own pick of on-screen words for this scene
            line = texts[str(i + 1)]
            first = line.split()[0].strip("#").lower() if line.split() else ""
            at = next((w["start"] - a for w in g if bare(w["word"]).startswith(first[:4])), 0.15) if first else 0.15
            at = min(at, max(0.1, dur - 1.6))     # on the word, but always long enough to read
            items = ([items[0]] if i == 0 and items else []) or [{"value": line, "role": "headline", "position": "bottom",
                                                                   "start": round(max(at, 0.05), 3), "end": round(dur, 3), "animate": "pop",
                                                                   "color": th["text"], "statement": not any(ch.isdigit() for ch in line)}]
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
            "out": round(min(end_card, probes[last]["duration"]), 3), "beat": "end card", "transition_in": {"type": "fade", "duration": 0.4},
            "zoom": {"from": 1.0, "to": 1.03}}
    if cta:
        card["text"] = [{"value": wrap(cta, 14, 4), "role": "headline", "position": "center", "start": 0.3, "end": round(card["out"] - 0.2, 3), "animate": "pop", "box": True}]
    else:
        notes.append("End card has no CTA yet: the owner gives it with each video (`--cta`).")
    if not music:
        notes.append("No music yet: add a bed (`--music`) so the end card is not dead air.")
    for m in social_mentions(groups):
        notes.append("{} names {}: animate the owner's logo `{}` in this scene{}.".format(
            clips[m["scene"]]["id"], m["platform"], m["file"], "" if m["available"] else " (not in the library yet: ask the owner for it)"))
    clips.append(card)
    edl = {"version": 1, "title": title or " ".join(w["word"] for w in groups[0])[:60], "style": HOUSE_STYLE,
           "format": {"width": W, "height": H, "fps": 30, "fit": "cover"}, "sources": sources, "clips": clips,
           "typography": {"pairing": "poppins-hind"}, "colour_theme": th["id"],
           "grade": {"preset": "bw-contrast" if th.get("mono") else "neutral"},
           "audio": {"keep_source": False, "source_gain_db": 0, "voice": {"file": voice, "gain_db": 0}},
           "master": {"lufs": -14, "true_peak": -1},
           "notes": ["Faceless plan from `{}` on {}: {} scenes at {:.2f}s average, cuts {}s before their word, key words as text on the spoken word.".format(
               words_file, now()[:10], len(groups), vo_end / len(groups), PRELAP),
               "Hand work before the storyboard: prop/paper collage and number counters as Hyperframes overlays (`mg-new`), an SFX on every transition, music."] + notes}
    if music:
        edl["audio"]["music"] = {"file": music, "gain_db": music_gain(root, voice, music), "duck": True, "fade_out": 1.5}
    edl["subtitles_requested"] = bool(captions)
    if captions:
        write_caption_files(root, words)
        edl["subtitles"] = {"file": "captions.srt", "burn": True, "size": 0.035, "position": "bottom", "box": True,
                            "animate": "highlight", "highlight_color": "yellow", "words": "captions.words.json"}
    if any(is_image(v) for v in visuals):
        direct(root, edl, {}, objects_place={v for v in visuals if "/places/" in v or Path(v).name.startswith("place-")})
    fit_text(edl)
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


def music_gain(root, voice, music, under=None):
    """Gain that puts the music `under` LU below the VO (editor/rules.json music_under_voice_db),
    measured, so the bed never presses on the owner's voice."""
    from ..core import read_json
    from .render import REPO
    under = under if under is not None else read_json(REPO / "editor" / "rules.json")["rules"]["music_under_voice_db"]
    vo, mu = media.loudness(inside(root, voice))["lufs"], media.loudness(inside(root, music))["lufs"]
    if vo is None or mu is None:
        return -24.0
    return round(min(vo - under - mu - 2.0, 0.0), 1)


def sfx_gain(root, voice, sfx, under=None):
    """Gain for an SFX hit that keeps it well under the VO (editor/rules.json sfx_under_voice_lu)."""
    from ..core import read_json
    from .render import REPO
    under = under if under is not None else read_json(REPO / "editor" / "rules.json")["rules"]["sfx_under_voice_lu"]
    vo, fx = media.loudness(inside(root, voice))["lufs"], media.loudness(inside(root, sfx))["lufs"]
    if vo is None or fx is None:
        return -24.0
    return round(min(vo - under - fx - 2.0, 0.0), 1)


def level(root):
    """Set every SFX and the music in edl.json to the owner's voice-first levels and drop banned
    FX (shake). Run it after adding SFX by hand, before the storyboard."""
    from ..core import project_lock, read_json
    from .render import REPO
    root = Path(root)
    banned = set(read_json(REPO / "editor" / "rules.json")["rules"].get("banned_fx", []))
    with project_lock(root):
        edl = read_json(root / "edl.json")
        audio = edl.get("audio", {})
        voice = (audio.get("voice") or {}).get("file")
        require(voice, "level needs a voiceover track (audio.voice)")
        changes = []
        if audio.get("music"):
            g = music_gain(root, voice, audio["music"]["file"])
            if audio["music"].get("gain_db", 0) > g:
                changes.append("music {} -> {} dB".format(audio["music"].get("gain_db", 0), g))
                audio["music"]["gain_db"] = g
        for sfx in audio.get("sfx", []):
            g = sfx_gain(root, voice, sfx["file"])
            if sfx.get("gain_db", 0) > g:
                changes.append("{} at {}s {} -> {} dB".format(sfx["file"], sfx["at"], sfx.get("gain_db", 0), g))
                sfx["gain_db"] = g
        for c in edl["clips"]:
            kept = [fx for fx in E.as_list(c.get("fx")) if fx not in banned]
            if len(kept) != len(E.as_list(c.get("fx"))):
                changes.append("{}: removed {}".format(c["id"], ", ".join(sorted(set(E.as_list(c.get("fx"))) & banned))))
                c["fx"] = kept
                if not kept:
                    del c["fx"]
        E.validate(root, edl)
        write_json(root / "edl.json", edl)
    return {"changes": changes}


def social_mentions(groups):
    """Scenes whose words name a social platform (or social media in general), with the owner's
    logo files from editor/library/social/ (owner rule 2026-11-10: real logos, not heart icons)."""
    from ..core import read_json
    from .render import REPO
    lib = REPO / "editor" / "library" / "social"
    cfg = read_json(lib / "platforms.json")
    out = []
    for i, g in enumerate(groups):
        said = {bare(w["word"]) for w in g}
        names = [n for n, p in cfg["platforms"].items() if said & set(p["words"])]
        if not names and said & set(cfg["general"]):
            names = list(cfg["platforms"])
        for n in names:
            f = lib / cfg["platforms"][n]["file"]
            out.append({"scene": i, "platform": n, "file": str(f.relative_to(REPO)), "available": f.exists()})
    return out


def write_caption_files(root, words):
    from .tools import srt_time
    cues = caption_cues(words)
    # each cue stays up until the next one starts (or 0.9 s), so short words are still readable
    ends = [max(c[-1]["end"], min(n[0]["start"], c[0]["start"] + 0.9)) for c, n in zip(cues, cues[1:])] + [cues[-1][-1]["end"]]
    srt = "".join("{}\n{} --> {}\n{}\n\n".format(n, srt_time(c[0]["start"]), srt_time(e), " ".join(w["word"] for w in c))
                  for n, (c, e) in enumerate(zip(cues, ends), 1))
    (Path(root) / "captions.srt").write_text(srt, encoding="utf-8")
    write_json(Path(root) / "captions.words.json", words)


def solid_cutout(photo, alpha):
    """Owner rule 2026-11-13: no holes or bites inside a cutout. The matte from rembg can punch
    holes in flat, bright objects (a banknote lost 7.6 % of its inside). Fill every hole that does
    not touch the frame border, take the pixels from the original photo, and soften the edge."""
    from PIL import Image, ImageDraw, ImageFilter
    import numpy as np
    a = np.array(alpha) > 110
    mask = Image.fromarray(np.pad(~a, 1, constant_values=True).astype(np.uint8) * 255).copy()   # writable copy for floodfill
    ImageDraw.floodfill(mask, (0, 0), 128)                       # the outside background becomes 128
    outside = (np.array(mask)[1:-1, 1:-1] == 128)
    solid = Image.fromarray(((~outside) * 255).astype(np.uint8)).filter(ImageFilter.MedianFilter(5)).filter(ImageFilter.GaussianBlur(1.2))
    out = photo.convert("RGBA")
    out.putalpha(solid)
    return out


def cutout_quality(img):
    """0..1: how clean a cutout is (1 = one solid shape). Low scores fall back to a framed photo."""
    import numpy as np
    from PIL import Image
    a = np.array(img.split()[3]) > 128
    if not a.any():
        return 0.0
    rows, cols = np.where(a)
    box = (rows.max() - rows.min() + 1) * (cols.max() - cols.min() + 1)
    # ragged edges: compare the outline length with that of a smooth blob of the same area
    edge = (a ^ np.roll(a, 1, 0)).sum() + (a ^ np.roll(a, 1, 1)).sum()
    smooth = 4 * (a.sum() ** 0.5)
    return float(max(0.0, min(1.0, smooth / max(edge, 1) * 1.6)) * min(1.0, a.sum() / box / 0.35))


def cutout(src, out):
    """Background-removed PNG of a real photo (rembg, u2net), for an object placed where the VO
    names it. The model (176 MB) downloads from GitHub on first use."""
    try:
        from rembg import new_session, remove
        from PIL import Image
    except ImportError as exc:
        raise E.ProductionError("Cutouts need rembg: python3 -m pip install rembg onnxruntime") from exc
    out = Path(out)
    out.parent.mkdir(parents=True, exist_ok=True)
    photo = Image.open(src).convert("RGB")
    img = remove(photo, session=new_session("u2net"))
    img = solid_cutout(photo, img.split()[3])
    box = img.getbbox()
    (img.crop(box) if box else img).save(out)
    return str(out)


# ---- look v3 (owner rule 2026-11-13): professional gradients, one colour theme, realistic cutouts ----

def themes():
    from ..core import read_json
    from .render import REPO
    return read_json(REPO / "editor" / "faceless" / "palettes.json")


def theme(name=None):
    data = themes()
    name = name or data["default"]
    require(name in data["themes"], "Unknown theme {!r}; choose from {}".format(name, sorted(data["themes"])))
    return dict(data["themes"][name], id=name)


def _rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def gradient(theme_name=None, size=(1080, 1920), seed=7):
    """A smooth vertical gradient with a soft radial light near the top and a very light grain:
    the clean, corporate background the owner asked for (no bokeh, no paper, no table)."""
    from PIL import Image, ImageFilter
    import random
    t = theme(theme_name)
    W, H = size
    top, bottom, light = _rgb(t["bg"][0]), _rgb(t["bg"][1]), _rgb(t["light"])
    import numpy as np
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
    f = (yy / (H - 1))[..., None]
    base = np.array(top, np.float32) + (np.array(bottom, np.float32) - np.array(top, np.float32)) * f
    d = np.sqrt((xx - W * 0.5) ** 2 + (yy - H * 0.32) ** 2) / (max(W, H) * 0.55)
    g = (np.clip(1.0 - d, 0, 1) ** 2 * 0.55)[..., None]
    arr = base + (np.array(light, np.float32) - base) * g
    img = Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8), "RGB")
    rnd = random.Random(seed)
    noise = Image.effect_noise((W // 4, H // 4), 8).resize((W, H)).filter(ImageFilter.GaussianBlur(1))
    return Image.blend(img, Image.merge("RGB", (noise, noise, noise)), 0.025)


def card(src, out, theme_name=None, size=(1080, 1920), width=0.52, y=0.34, mono=None, panel=None, layer_only=False, soft=True):
    """Put a real-photo cutout on the theme gradient with a soft 2D/3D touch: a contact shadow,
    a soft drop shadow, a faint light wrap from the background and a subtle floor reflection.
    `src` is a cutout PNG (with alpha) or a photo; photos are cut out first (rembg)."""
    from PIL import Image, ImageFilter, ImageOps
    t = theme(theme_name)
    W, H = size
    src = Path(src)
    obj = Image.open(src)
    if obj.mode != "RGBA" or obj.getextrema()[3][0] == 255:
        tmp = Path(out).with_suffix(".cut.png")
        obj = Image.open(cutout(src, tmp)).convert("RGBA")
    else:
        obj = obj.convert("RGBA")
    if mono if mono is not None else t.get("mono"):
        a = obj.split()[3]
        obj = ImageOps.grayscale(obj.convert("RGB")).convert("RGBA")
        obj.putalpha(a)
    box = obj.getbbox()
    if box:
        obj = obj.crop(box)
    else:                                   # an empty object ("Less is more"): a clean frame, no stray shadow
        empty = Image.new("RGBA", size, (0, 0, 0, 0)) if layer_only else gradient(t["id"], size).convert("RGBA")
        out = Path(out)
        out.parent.mkdir(parents=True, exist_ok=True)
        (empty.save(out) if layer_only else empty.convert("RGB").save(out, quality=94))
        write_json(out.with_suffix(".layout.json"), {"text_zone": "lower", "theme": t["id"]})
        return str(out)
    if soft and not src.name.startswith("design-"):    # designed graphics stay crisp
        obj = soft2d(obj)
    import numpy as np
    al = np.array(obj.split()[3])
    flat_bottom = (al[-3:] > 200).mean() > 0.35          # photo cut off at the bottom (a dog's bust, a person)
    left_cut, right_cut = (al[:, :3] > 200).mean() > 0.30, (al[:, -3:] > 200).mean() > 0.30
    cut_side = None if (flat_bottom or left_cut == right_cut) else ("left" if left_cut else "right")   # cut on both sides: a whole flat object
    designed = src.name.startswith("design-")
    if designed:
        flat_bottom, cut_side = False, None
        width = max(width, 0.84)
    if flat_bottom:
        pass                                             # placed on the frame's bottom edge below, so the cut never shows
    elif obj.width / float(obj.height) > 1.8 and not ((al[:, :3] > 200).mean() > 0.30 or (al[:, -3:] > 200).mean() > 0.30):   # tilt only whole flat objects            # flat objects (a note, a card) get a slight 3D tilt
        obj = obj.rotate(-7, resample=Image.BICUBIC, expand=True)
    # Layout (owner 2026-11-13: an object and its text never overlap): a whole object sits in the
    # upper zone (about 16-52 % of the height) with its text below; a photo cut off at the bottom
    # rises from the frame edge (bottom 48 %) with its text in the top zone.
    scale = min(W * max(width, 0.80) / obj.width, H * 0.44 / obj.height) if flat_bottom else min(W * width / obj.width, H * (0.38 if designed else 0.28) / obj.height)   # objects modest; designed demos large enough to read
    obj = obj.resize((max(1, int(obj.width * scale)), max(1, int(obj.height * scale))), Image.LANCZOS)
    bg = Image.new("RGBA", size, (0, 0, 0, 0)) if layer_only else gradient(t["id"], size).convert("RGBA")
    if flat_bottom:
        # Owner rule 2026-11-13: a photo cut off at the bottom rises from the frame's bottom edge,
        # so the cut edge sits outside the picture and never looks odd.
        x, top = (W - obj.width) // 2, H - obj.height + 2
    elif cut_side:
        # a photo cut off at a side (a hand holding a phone) enters from that frame edge
        top = int(H * y - obj.height / 2)
        x = -2 if cut_side == "left" else W - obj.width + 2
    else:
        x, top = (W - obj.width) // 2, int(H * y - obj.height / 2)
    alpha = obj.split()[3]
    # soft drop shadow
    sh = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    sh.paste((0, 0, 0, 150), (x + int(obj.width * 0.03), top + int(obj.height * 0.05)), alpha)
    bg = Image.alpha_composite(bg, sh.filter(ImageFilter.GaussianBlur(max(8, obj.width // 22))))
    # contact shadow (an ellipse under the object) and floor reflection, only for whole objects
    if flat_bottom or cut_side:
        bg.alpha_composite(obj, (x, top))
        zone = "top" if flat_bottom else "lower"
        if panel:
            glass(bg, zone, t)
        out = Path(out)
        out.parent.mkdir(parents=True, exist_ok=True)
        (bg.save(out) if layer_only else bg.convert("RGB").save(out, quality=94))   # a layer keeps its alpha
        write_json(out.with_suffix(".layout.json"), {"text_zone": zone, "theme": t["id"]})
        return str(out)
    from PIL import ImageDraw
    cs = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(cs).ellipse([x + obj.width * 0.12, top + obj.height * 0.95, x + obj.width * 0.88, top + obj.height * 1.05], fill=(0, 0, 0, 120))
    bg = Image.alpha_composite(bg, cs.filter(ImageFilter.GaussianBlur(max(6, obj.width // 30))))
    # faint floor reflection (real objects only; a designed graphic gets none)
    refl = ImageOps.flip(obj) if not designed else Image.new("RGBA", obj.size, (0, 0, 0, 0))
    ra = refl.split()[3].point(lambda v: int(v * 0.08))
    fade = Image.linear_gradient("L").resize(refl.size).point(lambda v: 255 - v)
    from PIL import ImageChops
    refl.putalpha(ImageChops.multiply(ra, fade))
    bg.alpha_composite(refl, (x, min(H - 1, top + obj.height + 4)))
    # light wrap: a whisper of the theme light on the edges, so the cutout sits in the scene
    edge = alpha.filter(ImageFilter.GaussianBlur(3))
    wrap = Image.new("RGBA", obj.size, _rgb(t["light"]) + (0,))
    wrap.putalpha(ImageChops.subtract(edge, alpha.filter(ImageFilter.MinFilter(5))).point(lambda v: int(v * 0.35)))
    bg.alpha_composite(obj, (x, top))
    bg.alpha_composite(wrap, (x, top))
    if panel:
        glass(bg, "lower", t)
    out = Path(out)
    out.parent.mkdir(parents=True, exist_ok=True)
    (bg.save(out) if layer_only else bg.convert("RGB").save(out, quality=94))   # a layer keeps its alpha
    write_json(out.with_suffix(".layout.json"), {"text_zone": "lower", "theme": t["id"]})
    return str(out)


def photo_card(src, out, theme_name=None, size=(1080, 1920), panel=True):
    """A place or scene photo (building, crowd, street) full-bleed, with the theme's gradient
    laid over the top and bottom so text sits on a clean band and the colours stay in theme."""
    from PIL import Image, ImageOps
    t = theme(theme_name)
    W, H = size
    img = ImageOps.fit(Image.open(src).convert("RGB"), size, Image.LANCZOS)
    if t.get("mono"):
        img = ImageOps.grayscale(img).convert("RGB")
    top, bottom = _rgb(t["bg"][0]), _rgb(t["bg"][1])
    import numpy as np
    f = np.linspace(0, 1, H, dtype=np.float32)[:, None]
    a = np.where(f < 0.32, 235 * (0.32 - f) / 0.32, np.where(f > 0.62, 245 * (f - 0.62) / 0.38, 0)).repeat(W, 1)
    rgb = np.where((f < 0.5)[..., None], np.array(top, np.float32), np.array(bottom, np.float32)).repeat(W, 1)
    ov = Image.fromarray(np.dstack([rgb, a[..., None]]).astype(np.uint8), "RGBA")
    res = Image.alpha_composite(img.convert("RGBA"), ov)
    if panel:
        glass(res, "lower", t)            # text over a busy photo always sits on glass
    out = Path(out)
    out.parent.mkdir(parents=True, exist_ok=True)
    res.convert("RGB").save(out, quality=94)
    write_json(out.with_suffix(".layout.json"), {"text_zone": "lower", "theme": t["id"]})
    return str(out)


GLASS_BANDS = {"top": (0.155, 0.335), "lower": (0.545, 0.70), "center": (0.42, 0.58), "bottom": (0.545, 0.70)}   # each holds two lines (top text from 18 %, lower from 57 %)


def glass(img, where, t, radius=44, margin=0.07):
    """Frosted-glass panel drawn into `img` (RGBA, in place) where on-screen text will sit.
    Research values (2026-11-13): 12-20 px blur, 12-25 % tint, a hairline border at about 20-30 %
    opacity and a soft shadow, on a calm background, for labels, numbers, names, quotes and the CTA.
    Not for long body text. The text keeps at least 4.5:1 contrast (theme text on the theme surface)."""
    from PIL import Image, ImageDraw, ImageFilter
    W, H = img.size
    y0, y1 = GLASS_BANDS[where] if isinstance(where, str) else where
    box = (int(W * margin), int(H * y0), int(W * (1 - margin)), int(H * y1))
    region = img.crop(box).filter(ImageFilter.GaussianBlur(18))
    tint = Image.new("RGBA", region.size, _rgb(t.get("surface", t["bg"][0])) + (int(255 * (0.55 if t.get("light_theme") else 0.42)),))
    region = Image.alpha_composite(region.convert("RGBA"), tint)
    m = Image.new("L", region.size, 0)
    ImageDraw.Draw(m).rounded_rectangle([0, 0, region.size[0] - 1, region.size[1] - 1], radius, fill=255)
    sh = Image.new("RGBA", img.size, (0, 0, 0, 0))
    ImageDraw.Draw(sh).rounded_rectangle([box[0], box[1] + 14, box[2], box[3] + 14], radius, fill=(0, 0, 0, 90))
    img.alpha_composite(sh.filter(ImageFilter.GaussianBlur(22)))
    img.paste(region, box[:2], m)
    edge = Image.new("RGBA", img.size, (0, 0, 0, 0))
    ImageDraw.Draw(edge).rounded_rectangle(box, radius, outline=_rgb(t.get("border", "#FFFFFF")) + (60,), width=2)
    img.alpha_composite(edge)
    return box


def fit_text(edl, max_width=0.70, max_lines=2):
    """Wrap every text item by its real rendered width (the role's font and size) so it stays inside
    the 9:16 safe zone and the glass band: at most two lines; a title that would need more
    drops to headline size. Items in the lower zone move to `lower` when they take two lines."""
    from PIL import ImageFont
    from . import craft
    W = edl["format"]["width"]
    for c in edl["clips"]:
        for it in E.as_list(c.get("text")):
            chain = {"title": ["title", "headline", "body"], "headline": ["headline", "body"]}.get(it.get("role"), [it.get("role")])
            if it.get("position") in ("bottom", "lower", "glass-lower") and chain[0] == "title":
                chain = chain[1:]                     # the lower zone holds headline size at most
            for role in chain:
                trial = dict(it, role=role)
                size, file_, _ = craft.resolve_text(edl, trial)
                if not file_:
                    break
                font = ImageFont.truetype(file_, size)
                lines, cur = [], ""
                for word in it["value"].replace("\n", " ").split():
                    test = (cur + " " + word).strip()
                    if cur and font.getlength(test) > W * max_width:
                        lines.append(cur)
                        cur = word
                    else:
                        cur = test
                lines.append(cur)
                limit = max_lines + 1 if (it.get("treatment") not in (None, "glass", "tag") and it.get("position") in ("top", "glass-top")) else max_lines   # open text at the top may take three lines
                too_wide = any(font.getlength(l) > W * max_width for l in lines)   # one long word ("High-end") at title size
                if (len(lines) <= limit and not too_wide) or role == chain[-1]:
                    it["role"], it["value"] = role, "\n".join(lines)      # never drop the owner's words
                    break
            tr = it.get("treatment")
            if tr in (None, "glass") and it.get("glass", True):
                if it.get("position") in ("bottom", "lower", "glass-lower"):
                    it["position"] = "glass-lower"      # centred in the lower glass band, one or two lines
                elif it.get("position") in ("top", "glass-top"):
                    it["position"] = "glass-top"
            elif it.get("position") in ("bottom", "lower"):
                it["position"] = "lower" if "\n" in it["value"] else "bottom"
            if it.get("position") == "center" and len(lines) > 3:
                it["role"] = "headline"
    return edl


# ---- variety (owner rule 2026-11-13): many text treatments and entrances, chosen by content, never repeated back to back ----

TREATMENTS = {
    # id: (what it is, when the editor uses it)
    "plain":    "clean off-white text on the gradient: headlines, statements, the hook",
    "emphasis": "a clean line with the key word(s) in the accent colour: turns, claims, 'but the strangest part'",
    "tag":      "a solid accent-coloured tag (text in the theme's ink): dates, places, names, categories, short labels",
    "glass":    "a frosted-glass card: numbers and stats, quotes, the CTA, any text over a busy photo",
    "bgword":   "one huge, faint word behind the object for depth, with a small plain line: topic openers, hooks",
}
ENTRANCES = ["rise", "slide-left", "pop", "fade-up", "slide-right"]   # all eased, smooth in and out; never shake


def runs_start_ok(w):
    return bare(w["word"]) not in TURN_WORDS and len(w["word"]) > 2


def kind_of_text(i, g, key_value, turn):
    if i == 0:
        return "hook"
    if turn:
        return "turn"
    if key_value and any(ch.isdigit() for ch in key_value):
        return "number"
    if key_value:
        return "name"
    if turn:
        return "turn"
    return None


CANDIDATES = {"hook": ["bgword", "emphasis", "plain"], "number": ["glass", "tag", "emphasis"],
              "statement": ["plain", "emphasis", "tag", "glass"],
              "name": ["tag", "glass", "emphasis"], "turn": ["emphasis", "plain", "tag"]}


def choose(kind, history, photo=False, cap=0.35):
    """The first fitting treatment that is not the previous scene's and not over its share of the video.
    Text over a busy photo always gets a backing (glass or tag)."""
    options = [o for o in CANDIDATES[kind] if not photo or o in ("glass", "tag")] or ["glass"]
    n = max(1, len(history))
    for o in options:
        if (not history or history[-1] != o) and history.count(o) / float(n) <= cap:
            return o
    return next((o for o in options if not history or history[-1] != o), options[0])


def is_image(path):
    return Path(path).suffix.lower() in STILL_EXT


def render_scene(root, cid, image, t, seconds, treatment, entrance, place=False, bg_word=None, size=(1080, 1920), fps=30):
    """One scene as a clip: the theme background (with a glass panel or a faint background word when
    the treatment asks for one) and the real-photo object animating in on `entrance`, holding still,
    and fading out smoothly. A place photo fills the frame instead. Returns the clip path (in raw/scenes)."""
    from PIL import Image, ImageDraw, ImageFont
    root = Path(root)
    W, H = size
    folder = root / "raw" / "scenes"
    folder.mkdir(parents=True, exist_ok=True)
    src = inside(root, image)
    if place:
        bgp = folder / (cid + ".bg.jpg")
        photo_card(src, bgp, t["id"], size, panel=(treatment == "glass"))
        zone = "lower"
        layer = None
    else:
        lay = folder / (cid + ".obj.png")
        card(src, lay, t["id"], size, layer_only=True)
        zone = json.loads(lay.with_suffix(".layout.json").read_text(encoding="utf-8"))["text_zone"]
        bg = gradient(t["id"], size).convert("RGBA")
        if treatment == "bgword" and bg_word:
            from . import craft, fonts as FN
            fnt = FN.resolve("Poppins", 800) or FN.resolve("Poppins", 700)
            if fnt:
                word = bg_word.upper()
                fs = int(W * 0.30)
                font = ImageFont.truetype(fnt, fs)
                while font.getlength(word) > W * 0.96 and fs > 60:
                    fs = int(fs * 0.9)
                    font = ImageFont.truetype(fnt, fs)
                word_layer = Image.new("RGBA", size, (0, 0, 0, 0))
                wy = H * (0.70 if zone == "top" else 0.30)          # behind the object, away from the text zone
                ImageDraw.Draw(word_layer).text((W / 2, wy), word, font=font, fill=_rgb(t["text"]) + (26,), anchor="mm")
                bg.alpha_composite(word_layer)      # blended, so the word stays faint behind the object
        if treatment == "glass":
            glass(bg, zone, t)
        bgp = folder / (cid + ".bg.png")
        bg.save(bgp)
        layer = lay
    out = folder / (cid + ".mp4")
    D = max(seconds, 0.5)
    ease = "(1-pow(1-min(t/0.6,1),3))"      # ease-out cubic over 0.6 s (quoted in the filter, so commas are safe)
    if layer is None:
        graph = "[0:v]format=yuv420p[v]"
        inputs = ["-loop", "1", "-t", "{:.3f}".format(D), "-i", str(bgp)]
    else:
        inputs = ["-loop", "1", "-t", "{:.3f}".format(D), "-i", str(bgp), "-loop", "1", "-t", "{:.3f}".format(D), "-i", str(layer)]
        fade = "format=rgba,fade=t=in:st=0:d=0.35:alpha=1,fade=t=out:st={:.3f}:d=0.3:alpha=1".format(max(D - 0.3, 0.4))
        pos = {"rise": ("0", "{h}*0.30*(1-{e})"), "slide-left": ("-{w}*0.6*(1-{e})", "0"), "slide-right": ("{w}*0.6*(1-{e})", "0"),
               "fade-up": ("0", "70*(1-{e})"), "pop": ("(main_w-overlay_w)/2", "(main_h-overlay_h)/2")}[entrance]
        x, y = (p.format(w=W, h=H, e=ease) for p in pos)
        scale = ",scale=w='iw*(0.86+0.14*{e})':h='ih*(0.86+0.14*{e})':eval=frame".format(e=ease) if entrance == "pop" else ""
        graph = "[1:v]{}{}[o];[0:v][o]overlay=x='{}':y='{}':eval=frame:format=auto,format=yuv420p[v]".format(fade, scale, x, y)
    media.run(["ffmpeg", "-hide_banner", "-y", *inputs, "-filter_complex", graph, "-map", "[v]", "-r", str(fps),
               "-c:v", "libx264", "-preset", "veryfast", "-crf", "16", "-t", "{:.3f}".format(D), str(out)])
    write_json(out.with_suffix(".layout.json"), {"text_zone": zone, "theme": t["id"], "treatment": treatment, "entrance": entrance})
    return out


def direct(root, edl, words_by_clip, objects_place=(), seed=0):
    """The direction pass after the timing plan (owner rule 2026-11-13: every video varies). For each
    scene: pick the text treatment by what the text is, never the same twice in a row; pick an
    entrance for its object, never the same twice in a row; render image scenes as animated clips;
    and dress the text items in the chosen treatment and the theme's roles."""
    t = theme(edl.get("colour_theme"))
    history, last_entrance = [], None
    for i, c in enumerate(edl["clips"]):
        card_end = c.get("beat") == "end card"
        src = edl["sources"][c["source"]]
        items = E.as_list(c.get("text"))
        key = items[0]["value"].replace("\n", " ") if items and i else None
        kind = None if card_end else kind_of_text(i, words_by_clip.get(c["id"], []), key, "flash" in E.as_list(c.get("fx")))
        if kind == "name" and items and items[0].get("statement"):
            kind = "statement"
        place = src in objects_place
        treatment = ("glass" if items else None) if card_end else (choose(kind, history, photo=place) if kind else None)
        if treatment and not card_end:
            history.append(treatment)
        name = Path(src).name
        if name.startswith("title-card") and treatment in ("glass", "tag", "bgword"):
            treatment = "emphasis" if (not history or history[-1] != "emphasis") else "plain"   # a title card is open text
            if history:
                history[-1] = treatment
        if is_image(src) and name.startswith("build-"):
            kind_b = Path(src).stem[len("build-"):]
            kind_b = {"timeline-clutter": "timeline", "palette-dull": "palette", "palette-harsh": "palette"}.get(kind_b, kind_b)
            side = inside(root, src).with_suffix(".json")
            kw = json.loads(side.read_text(encoding="utf-8")) if side.exists() else {}
            clip_path = render_build(root, c["id"], t, c["out"] - c["in"], design_parts(kind_b, t["id"], **kw),
                                     size=(edl["format"]["width"], edl["format"]["height"]), panel=(treatment == "glass"))
            sid = "S" + c["id"][1:]
            edl["sources"][sid] = str(Path(clip_path).relative_to(root))
            c["source"], c["in"], c["out"] = sid, 0.0, round(c["out"] - c["in"], 3)
            c.pop("zoom", None)
            zone = "lower"
        elif is_image(src):
            ent = ENTRANCES[(i + seed) % len(ENTRANCES)]
            if ent == last_entrance:
                ent = ENTRANCES[(i + seed + 1) % len(ENTRANCES)]
            last_entrance = ent
            words_here = (key or (items[0]["value"] if items else "")).replace("\n", " ").split()
            topic = max(words_here, key=len).strip(".,!?") if (treatment == "bgword" and words_here) else None   # the strongest word, not "Ek"
            clip_path = render_scene(root, c["id"], src, t, c["out"] - c["in"], treatment, ent, place=place, bg_word=topic,
                                     size=(edl["format"]["width"], edl["format"]["height"]))
            sid = "S" + c["id"][1:]
            edl["sources"][sid] = str(Path(clip_path).relative_to(root))
            c["source"], c["in"], c["out"] = sid, 0.0, round(c["out"] - c["in"], 3)
            if i % 2:
                c["zoom"] = {"from": 1.0, "to": 1.05}   # a slow camera push on every other object scene
            else:
                c.pop("zoom", None)
            zone = json.loads(Path(clip_path).with_suffix(".layout.json").read_text(encoding="utf-8"))["text_zone"]
        else:
            zone = "lower"
        title_card = name.startswith("title-card")
        for it in items:
            it["clean"] = True
            if treatment != "tag":
                it.update(reveal="word", reveal_step=0.14)
            it["position"] = ("glass-top" if zone == "top" else "glass-lower") if treatment == "glass" else ("top" if zone == "top" else "bottom")
            if treatment == "tag":
                it.update(box_color=t["accent"], color=t["accent_ink"], role="headline")
                it.pop("clean", None)
            elif treatment == "emphasis":
                words = it["value"].replace("\n", " ").split()
                it.update(color=t["text"], accent_color=t["accent"], accent_words=[max(words, key=len)] if words else [])
            elif treatment == "glass":
                it["color"] = t["highlight"] if any(ch.isdigit() for ch in it["value"]) else t["text"]
            elif treatment in ("plain", "bgword"):
                it["color"] = t["text"]
                if treatment == "bgword":
                    words = it["value"].replace("\n", " ").split()
                    it.update(accent_color=t["accent"], accent_words=[max(words, key=len)] if words else [])
            if treatment != "tag":
                it.pop("box", None)          # only a tag has a box; glass, plain, emphasis and bgword text sit clean
            if title_card:                       # a text-only scene: big kinetic words in the middle
                short = len(it["value"].split()) <= 2 and max(len(w) for w in it["value"].split()) <= 8
                it.update(position="center", role="title", size=int(edl["format"]["height"] * (0.095 if short else 0.075)))
            it["treatment"] = treatment
    used = [h for h in history]
    edl.setdefault("notes", []).append("Direction: treatments {} · no treatment or entrance repeats back to back.".format(", ".join(used)))
    return edl



def soft2d(img):
    """Owner rule 2026-11-13: real, but with a soft 2D finish (smooth, clean, a little cute), never a
    paper cutout. An edge-preserving smooth keeps the shapes real while it simplifies the texture;
    a touch more colour and a faint glow soften it. Alpha is kept."""
    try:
        import cv2
    except ImportError:
        return img
    import numpy as np
    from PIL import Image, ImageEnhance, ImageFilter
    a = img.split()[3] if img.mode == "RGBA" else None
    rgb = np.array(img.convert("RGB"))[:, :, ::-1]
    sm = cv2.edgePreservingFilter(rgb, flags=1, sigma_s=60, sigma_r=0.45)
    p = Image.fromarray(sm[:, :, ::-1])
    p = ImageEnhance.Contrast(ImageEnhance.Color(p).enhance(1.15)).enhance(0.95)
    p = Image.blend(p, p.filter(ImageFilter.GaussianBlur(6)), 0.18)
    p = p.convert("RGBA")
    if a is not None:
        p.putalpha(a)
    return p


# ---- designed demo graphics (owner rule 2026-11-13: abstract ideas get a graphic that shows the idea) ----

def _font(size, weight=700):
    from PIL import ImageFont
    from . import fonts as FN
    f = FN.resolve("Poppins", weight) or FN.resolve("Poppins", 700)
    return ImageFont.truetype(f, size) if f else ImageFont.load_default()


def _shadowed(layer, blur=18, offset=(0, 18), alpha=110):
    from PIL import Image, ImageFilter
    sh = Image.new("RGBA", layer.size, (0, 0, 0, 0))
    sh.paste((0, 0, 0, alpha), offset, layer.split()[3])
    out = sh.filter(ImageFilter.GaussianBlur(blur))
    out.alpha_composite(layer)
    return out


def _icon(d, box, kind, fill, ink):
    x0, y0, x1, y1 = box
    r = (x1 - x0) * 0.24
    d.rounded_rectangle(box, radius=r, fill=fill)
    cx, cy, s = (x0 + x1) / 2, (y0 + y1) / 2, (x1 - x0) * 0.26
    if kind == "play":
        d.polygon([(cx - s * 0.7, cy - s), (cx - s * 0.7, cy + s), (cx + s, cy)], fill=ink)
    elif kind == "circle":
        d.ellipse([cx - s, cy - s, cx + s, cy + s], outline=ink, width=max(4, int(s * 0.28)))
    elif kind == "bars":
        for k, h in enumerate((0.6, 1.0, 0.8)):
            bx = cx - s + k * s * 0.75
            d.rounded_rectangle([bx, cy + s - 2 * s * h, bx + s * 0.5, cy + s], radius=s * 0.12, fill=ink)
    else:  # star-ish diamond
        d.polygon([(cx, cy - s), (cx + s * 0.8, cy), (cx, cy + s), (cx - s * 0.8, cy)], fill=ink)


def design(kind, out, theme_name=None, **kw):
    """A designed demo graphic as a transparent PNG (`design-*.png`, so it gets no rembg and no soft2d):
    timeline, icons (scale=1.0 oversized or 0.75 with a -25 % badge), effects (overload=True or one clean glow),
    checklist (items=[...]), cards3 (labels=[...]), beforeafter, spotlight, palette (colors=[...], labels=[...])."""
    from PIL import Image, ImageDraw, ImageFilter
    t = theme(theme_name)
    W, H = kw.get("size", (1000, 900))
    surf, acc, txt, mut = _rgb(t.get("surface", t["bg"][0])), _rgb(t["accent"]), _rgb(t["text"]), _rgb(t["muted"])
    card_fill = tuple(min(255, c + 22) for c in surf) + (255,)
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    if kind == "timeline":
        clutter = kw.get("clutter", False)
        d.rounded_rectangle([20, 140, W - 20, H - 140], 36, fill=card_fill)
        for k in range(4):
            y = 220 + k * 120
            d.rounded_rectangle([60, y, W - 60, y + 80], 18, fill=tuple(max(0, c - 10) for c in surf) + (255,))
            segs = [(80, 380), (400, 620), (640, 900)] if k % 2 == 0 else [(80, 260), (280, 700), (720, 900)]
            for j, (a, b) in enumerate(segs):
                col = acc if (j + k) % 3 == 0 else mut
                d.rounded_rectangle([a, y + 10, min(b, W - 80), y + 70], 14, fill=col + (255,))
        d.rectangle([520, 170, 526, H - 170], fill=txt + (255,))
        d.polygon([(504, 160), (542, 160), (523, 186)], fill=txt + (255,))
        if clutter:   # oversized icons and shapes crowd the frame: the beginner look
            for (x, y, s, k) in [(40, 60, 300, "play"), (420, 20, 260, "circle"), (700, 420, 300, "bars"), (120, 520, 260, "diamond")]:
                _icon(d, [x, y, x + s, y + s], k, acc + (255,) if k in ("play", "bars") else (230, 70, 70, 255), (255, 255, 255, 255))
    elif kind == "icons":
        sc = float(kw.get("scale", 1.0))
        base = 300 * sc
        gap = 40 * sc
        total = 3 * base + 2 * gap
        x = (W - total) / 2
        for k, (kk, col) in enumerate([("play", acc), ("circle", mut), ("bars", acc)]):
            _icon(d, [x + k * (base + gap), H / 2 - base / 2, x + k * (base + gap) + base, H / 2 + base / 2], kk, col + (255,), surf + (255,))
        if sc < 1.0:
            f = _font(64)
            d.rounded_rectangle([W / 2 - 150, H - 200, W / 2 + 150, H - 100], 50, fill=acc + (255,))
            d.text((W / 2, H - 150), "-25%", font=f, fill=_rgb(t["accent_ink"]) + (255,), anchor="mm")
    elif kind == "effects":
        over = kw.get("overload", True)
        box = [W / 2 - 220, H / 2 - 150, W / 2 + 220, H / 2 + 150]
        if over:
            for k, col in enumerate([(255, 0, 80), (0, 200, 255), (255, 220, 0), (160, 0, 255)]):
                g = Image.new("RGBA", (W, H), (0, 0, 0, 0))
                ImageDraw.Draw(g).rounded_rectangle([box[0] - 30 - k * 14, box[1] - 30 - k * 14, box[2] + 30 + k * 14, box[3] + 30 + k * 14], 60, outline=col + (200,), width=18)
                img.alpha_composite(g.filter(ImageFilter.GaussianBlur(10 + k * 6)))
            d = ImageDraw.Draw(img)
            d.rounded_rectangle(box, 48, fill=(255, 40, 120, 255), outline=(255, 255, 0, 255), width=10)
            f = _font(80, 800)
            d.text((W / 2 + 8, H / 2 + 8), "WOW", font=f, fill=(0, 255, 255, 255), anchor="mm")
            d.text((W / 2, H / 2), "WOW", font=f, fill=(255, 255, 255, 255), anchor="mm")
        else:
            g = Image.new("RGBA", (W, H), (0, 0, 0, 0))
            ImageDraw.Draw(g).rounded_rectangle([box[0] - 10, box[1] - 10, box[2] + 10, box[3] + 10], 56, fill=acc + (90,))
            img.alpha_composite(g.filter(ImageFilter.GaussianBlur(30)))
            d = ImageDraw.Draw(img)
            d.rounded_rectangle(box, 48, fill=card_fill)
            d.text((W / 2, H / 2), "Clean", font=_font(80, 700), fill=txt + (255,), anchor="mm")
    elif kind == "checklist":
        items = kw.get("items", ["Size", "Effects", "Colour"])
        f = _font(64, 600)
        d.rounded_rectangle([60, 80, W - 60, H - 80], 40, fill=card_fill)
        for k, it in enumerate(items):
            y = 200 + k * 200
            d.ellipse([130, y - 50, 230, y + 50], fill=acc + (255,))
            d.line([(155, y), (175, y + 22), (208, y - 22)], fill=_rgb(t["accent_ink"]) + (255,), width=14, joint="curve")
            d.text((280, y), it, font=f, fill=txt + (255,), anchor="lm")
    elif kind == "cards3":
        labels = kw.get("labels", ["Size", "Effects", "Colour"])
        f = _font(54, 700)
        for k, lab in enumerate(labels):
            c = Image.new("RGBA", (280, 380), (0, 0, 0, 0))
            cd = ImageDraw.Draw(c)
            cd.rounded_rectangle([0, 0, 279, 379], 34, fill=card_fill)
            cd.ellipse([90, 70, 190, 170], fill=(acc if k != 1 else mut) + (255,))
            cd.text((140, 270), lab, font=f, fill=txt + (255,), anchor="mm")
            c = c.rotate((k - 1) * -7, resample=Image.BICUBIC, expand=True)
            img.alpha_composite(c, (int(40 + k * 300), int(200 + abs(k - 1) * 40)))
    elif kind == "beforeafter":
        f = _font(48, 700)
        for k, (lab, clutter) in enumerate([("Beginner", True), ("Pro", False)]):
            x0 = 30 + k * 490
            d.rounded_rectangle([x0, 140, x0 + 450, H - 140], 34, fill=card_fill)
            d.text((x0 + 225, 200), lab, font=f, fill=(mut if clutter else acc) + (255,), anchor="mm")
            if clutter:
                for (x, y, s, kk, col) in [(x0 + 30, 260, 230, "play", (230, 60, 60)), (x0 + 200, 330, 220, "circle", (255, 200, 0)), (x0 + 60, 470, 240, "bars", (0, 180, 255))]:
                    _icon(d, [x, y, x + s, y + s], kk, col + (255,), (255, 255, 255, 255))
            else:
                for j, kk in enumerate(("play", "circle", "bars")):
                    _icon(d, [x0 + 70 + j * 110, 420, x0 + 160 + j * 110, 510], kk, (acc if j != 1 else mut) + (255,), surf + (255,))
    elif kind == "spotlight":
        g = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        ImageDraw.Draw(g).ellipse([W / 2 - 260, H / 2 - 260, W / 2 + 260, H / 2 + 260], fill=acc + (110,))
        img.alpha_composite(g.filter(ImageFilter.GaussianBlur(60)))
        d = ImageDraw.Draw(img)
        for j, (x, kk) in enumerate([(W / 2 - 330, "circle"), (W / 2 - 110, "play"), (W / 2 + 130, "bars")]):
            s = 220 if j == 1 else 150
            _icon(d, [x + (0 if j == 1 else 35), H / 2 - s / 2, x + (0 if j == 1 else 35) + s, H / 2 + s / 2], kk, (acc if j == 1 else mut) + (255,), surf + (255,))
    elif kind == "palette":
        cols = kw.get("colors", [(79, 109, 122), (107, 143, 113), (194, 184, 163)])
        labels = kw.get("labels", ["Blue", "Green", "Sand"])
        f = _font(38, 600)
        for k, (c, lab) in enumerate(zip(cols, labels)):
            cc = Image.new("RGBA", (300, 520), (0, 0, 0, 0))
            cd = ImageDraw.Draw(cc)
            cd.rounded_rectangle([0, 0, 299, 519], 26, fill=(250, 248, 243, 255))
            cd.rounded_rectangle([18, 18, 281, 390], 16, fill=tuple(c) + (255,))
            cd.text((150, 455), lab, font=f, fill=(70, 70, 70, 255), anchor="mm")
            cc = cc.rotate((k - 1) * -8, resample=Image.BICUBIC, expand=True)
            img.alpha_composite(cc, (int(40 + k * 300), int(150 + abs(k - 1) * 40)))
    elif kind == "ruler":
        d.rounded_rectangle([40, H / 2 - 120, W - 40, H / 2 + 120], 22, fill=acc + (255,))
        f = _font(44, 700)
        for k in range(0, 31):
            x = 80 + k * (W - 160) / 30.0
            h = 90 if k % 5 == 0 else (60 if k % 5 == 0 else 40)
            d.line([(x, H / 2 - 120), (x, H / 2 - 120 + h)], fill=_rgb(t["accent_ink"]) + (255,), width=5 if k % 5 == 0 else 3)
            if k % 5 == 0:
                d.text((x, H / 2 + 40), str(k // 5), font=f, fill=_rgb(t["accent_ink"]) + (255,), anchor="mm")
    else:
        raise E.ProductionError("Unknown design kind " + kind)
    img = _shadowed(img)
    out = Path(out)
    out.parent.mkdir(parents=True, exist_ok=True)
    img.save(out)
    return str(out)


# ---- build-ups (owner rule 2026-11-13: graphics build on the words, nothing is a static template) ----

def design_parts(kind, theme_name=None, **kw):
    """A designed graphic split into parts that animate one after another: [(RGBA canvas 1000x900, at seconds, anim)].
    anim: fade-up, pop, slide-left, shrink (scale to 75 %), sweep (moves across), out (visible, then fades at `at`)."""
    from PIL import Image, ImageDraw, ImageFilter
    t = theme(theme_name)
    W, H = 1000, 900
    surf, acc, txt, mut = _rgb(t.get("surface", t["bg"][0])), _rgb(t["accent"]), _rgb(t["text"]), _rgb(t["muted"])
    ink = _rgb(t["accent_ink"])
    card_fill = tuple(min(255, c + 22) for c in surf) + (255,)

    def canvas():
        return Image.new("RGBA", (W, H), (0, 0, 0, 0))

    def done(img):
        return _shadowed(img, blur=16, offset=(0, 14), alpha=100)
    parts = []
    if kind == "checklist":
        items = kw.get("items", ["Size", "Effects", "Colour"])
        base = canvas()
        ImageDraw.Draw(base).rounded_rectangle([60, 80, W - 60, H - 80], 40, fill=card_fill)
        parts.append((done(base), 0.0, "fade-up"))
        f = _font(64, 600)
        for k, it in enumerate(items):
            row = canvas()
            d = ImageDraw.Draw(row)
            y = 220 + k * 200
            d.ellipse([130, y - 50, 230, y + 50], fill=acc + (255,))
            d.line([(155, y), (175, y + 22), (208, y - 22)], fill=ink + (255,), width=14, joint="curve")
            d.text((280, y), it, font=f, fill=txt + (255,), anchor="lm")
            parts.append((row, 0.45 + k * 0.45, "slide-left"))
    elif kind in ("palette",):
        cols = kw.get("colors", [(79, 109, 122), (107, 143, 113), (194, 184, 163)])
        labels = kw.get("labels", ["Blue", "Green", "Sand"])
        f = _font(38, 600)
        for k, (c, lab) in enumerate(zip(cols, labels)):
            cc = Image.new("RGBA", (300, 520), (0, 0, 0, 0))
            cd = ImageDraw.Draw(cc)
            cd.rounded_rectangle([0, 0, 299, 519], 26, fill=(250, 248, 243, 255))
            cd.rounded_rectangle([18, 18, 281, 390], 16, fill=tuple(c) + (255,))
            cd.text((150, 455), lab, font=f, fill=(70, 70, 70, 255), anchor="mm")
            cc = cc.rotate((k - 1) * -8, resample=Image.BICUBIC, expand=True)
            img = canvas()
            img.alpha_composite(cc, (int(40 + k * 300), int(150 + abs(k - 1) * 40)))
            parts.append((done(img), 0.1 + k * 0.32, "pop"))
    elif kind == "cards3":
        labels = kw.get("labels", ["Size", "Effects", "Colour"])
        f = _font(54, 700)
        for k, lab in enumerate(labels):
            c = Image.new("RGBA", (280, 380), (0, 0, 0, 0))
            cd = ImageDraw.Draw(c)
            cd.rounded_rectangle([0, 0, 279, 379], 34, fill=card_fill)
            cd.ellipse([90, 70, 190, 170], fill=(acc if k != 1 else mut) + (255,))
            cd.text((140, 270), lab, font=f, fill=txt + (255,), anchor="mm")
            c = c.rotate((k - 1) * -7, resample=Image.BICUBIC, expand=True)
            img = canvas()
            img.alpha_composite(c, (int(40 + k * 300), int(200 + abs(k - 1) * 40)))
            parts.append((done(img), 0.15 + k * 0.4, "fade-up"))
    elif kind == "icons-shrink":
        img = canvas()
        d = ImageDraw.Draw(img)
        base, gap = 300, 40
        x = (W - (3 * base + 2 * gap)) / 2
        for k, (kk, col) in enumerate([("play", acc), ("circle", mut), ("bars", acc)]):
            _icon(d, [x + k * (base + gap), H / 2 - base / 2, x + k * (base + gap) + base, H / 2 + base / 2], kk, col + (255,), surf + (255,))
        parts.append((done(img), 0.7, "shrink"))
        badge = canvas()
        bd = ImageDraw.Draw(badge)
        bd.rounded_rectangle([W / 2 - 150, H - 170, W / 2 + 150, H - 70], 50, fill=acc + (255,))
        bd.text((W / 2, H - 120), "-25%", font=_font(64), fill=ink + (255,), anchor="mm")
        parts.append((badge, 1.3, "pop"))
    elif kind == "icons-big":
        sizes = [(40, 120, 380, "play", acc), (340, 300, 360, "circle", mut), (600, 80, 400, "bars", acc)]
        for k, (x, y, s, kk, col) in enumerate(sizes):
            img = canvas()
            _icon(ImageDraw.Draw(img), [x, y, x + s, y + s], kk, col + (255,), surf + (255,))
            parts.append((done(img), 0.05 + k * 0.28, "pop"))
    elif kind == "shapes":
        for k, (box, shape, col) in enumerate([([20, 60, 560, 600], "circle", (230, 90, 80)), ([380, 260, 980, 860], "rect", acc),
                                                ([160, 420, 620, 880], "tri", mut)]):
            img = canvas()
            d = ImageDraw.Draw(img)
            if shape == "circle":
                d.ellipse(box, fill=col + (235,))
            elif shape == "rect":
                d.rounded_rectangle(box, 60, fill=col + (235,))
            else:
                d.polygon([(box[0], box[3]), ((box[0] + box[2]) / 2, box[1]), (box[2], box[3])], fill=col + (235,))
            parts.append((done(img), 0.05 + k * 0.3, "pop"))
    elif kind == "timeline":
        clutter = kw.get("clutter", False)
        base = canvas()
        d = ImageDraw.Draw(base)
        d.rounded_rectangle([20, 140, W - 20, H - 140], 36, fill=card_fill)
        for k in range(4):
            y = 220 + k * 120
            d.rounded_rectangle([60, y, W - 60, y + 80], 18, fill=tuple(max(0, c - 10) for c in surf) + (255,))
            segs = [(80, 380), (400, 620), (640, 900)] if k % 2 == 0 else [(80, 260), (280, 700), (720, 900)]
            for j, (a, b) in enumerate(segs):
                d.rounded_rectangle([a, y + 10, min(b, W - 80), y + 70], 14, fill=(acc if (j + k) % 3 == 0 else mut) + (255,))
        parts.append((done(base), 0.0, "fade-up"))
        ph = canvas()
        pd = ImageDraw.Draw(ph)
        pd.rectangle([497, 170, 503, H - 170], fill=txt + (255,))
        pd.polygon([(481, 160), (519, 160), (500, 186)], fill=txt + (255,))
        parts.append((ph, 0.0, "sweep"))
        if clutter:
            for k, (x, y, s, kk) in enumerate([(40, 60, 300, "play"), (420, 20, 260, "circle"), (700, 420, 300, "bars"), (120, 520, 260, "diamond")]):
                img = canvas()
                _icon(ImageDraw.Draw(img), [x, y, x + s, y + s], kk, acc + (255,) if kk in ("play", "bars") else (230, 70, 70, 255), (255, 255, 255, 255))
                parts.append((done(img), 0.35 + k * 0.22, "pop"))
    elif kind == "beforeafter":
        f = _font(48, 700)
        for k, (lab, clutter) in enumerate([("Beginner", True), ("Pro", False)]):
            img = canvas()
            d = ImageDraw.Draw(img)
            x0 = 30 + k * 490
            d.rounded_rectangle([x0, 140, x0 + 450, H - 140], 34, fill=card_fill)
            d.text((x0 + 225, 200), lab, font=f, fill=(mut if clutter else acc) + (255,), anchor="mm")
            if clutter:
                for (x, y, s, kk, col) in [(x0 + 30, 260, 230, "play", (230, 60, 60)), (x0 + 200, 330, 220, "circle", (255, 200, 0)), (x0 + 60, 470, 240, "bars", (0, 180, 255))]:
                    _icon(d, [x, y, x + s, y + s], kk, col + (255,), (255, 255, 255, 255))
            else:
                for j, kk in enumerate(("play", "circle", "bars")):
                    _icon(d, [x0 + 70 + j * 110, 420, x0 + 160 + j * 110, 510], kk, (acc if j != 1 else mut) + (255,), surf + (255,))
            parts.append((done(img), 0.1 + k * 0.8, "slide-left" if k == 0 else "fade-up"))
    elif kind == "effects-switch":
        over = Image.open(design("effects", "/tmp/_fx_over.png", t["id"], overload=True)).convert("RGBA").resize((W, H))
        clean = Image.open(design("effects", "/tmp/_fx_clean.png", t["id"], overload=False)).convert("RGBA").resize((W, H))
        parts.append((over, kw.get("switch", 0.9), "out"))
        parts.append((clean, kw.get("switch", 0.9), "fade-up"))
    elif kind == "effects-over":
        parts.append((Image.open(design("effects", "/tmp/_fx_over.png", t["id"], overload=True)).convert("RGBA").resize((W, H)), 0.05, "pop"))
    elif kind == "spotlight":
        glow = canvas()
        ImageDraw.Draw(glow).ellipse([W / 2 - 260, H / 2 - 260, W / 2 + 260, H / 2 + 260], fill=acc + (120,))
        icons = canvas()
        d = ImageDraw.Draw(icons)
        for j, (x, kk) in enumerate([(W / 2 - 330, "circle"), (W / 2 - 110, "play"), (W / 2 + 130, "bars")]):
            s = 220 if j == 1 else 150
            _icon(d, [x + (0 if j == 1 else 35), H / 2 - s / 2, x + (0 if j == 1 else 35) + s, H / 2 + s / 2], kk, (acc if j == 1 else mut) + (255,), surf + (255,))
        parts.append((done(icons), 0.0, "fade-up"))
        parts.append((glow.filter(ImageFilter.GaussianBlur(60)), 0.7, "fade-up"))
    elif kind == "journey":
        f = _font(58, 700)
        for k, (lab, x, col, tc) in enumerate([("Beginner", 230, mut, surf), ("Pro", 770, acc, ink)]):
            img = canvas()
            d = ImageDraw.Draw(img)
            d.rounded_rectangle([x - 190, H / 2 - 70, x + 190, H / 2 + 70], 70, fill=col + (255,))
            d.text((x, H / 2), lab, font=f, fill=tc + (255,), anchor="mm")
            parts.append((done(img), 0.1 if k == 0 else 1.1, "pop"))
        arrow = canvas()
        ad = ImageDraw.Draw(arrow)
        ad.line([(440, H / 2), (560, H / 2)], fill=txt + (255,), width=12)
        ad.polygon([(560, H / 2 - 26), (600, H / 2), (560, H / 2 + 26)], fill=txt + (255,))
        parts.append((arrow, 0.6, "slide-left"))
    else:
        raise E.ProductionError("No build-up for design kind " + kind)
    return parts


def render_build(root, cid, t, seconds, parts, size=(1080, 1920), fps=30, panel=False):
    """A designed scene whose parts animate in on their own times (build-up), over the theme gradient,
    holding still and fading out together at the end. No shake: every move is eased and settles."""
    from PIL import Image
    root = Path(root)
    W, H = size
    folder = root / "raw" / "scenes"
    folder.mkdir(parents=True, exist_ok=True)
    bgp = folder / (cid + ".bg.png")
    bg = gradient(t["id"], size).convert("RGBA")
    if panel:
        glass(bg, "lower", t)
    bg.save(bgp)
    Wc = int(W * 0.86)
    Hc = int(900 * Wc / 1000.0)
    x0, y0 = (W - Wc) // 2, int(H * 0.33 - Hc / 2)
    D = max(seconds, 0.5)
    inputs = ["-loop", "1", "-t", "{:.3f}".format(D), "-i", str(bgp)]
    graph, last = [], "0:v"
    latest = max([float(at) for _, at, an in parts if an not in ("sweep",)] + [0.01])
    squeeze = min(1.0, (D * 0.55) / latest)          # every part of the build lands within the first half of a short scene
    for k, (img, at, anim) in enumerate(parts):
        at = float(at) * squeeze
        p = folder / "{}.part{}.png".format(cid, k)
        img.resize((Wc, Hc), Image.LANCZOS).save(p)
        inputs += ["-loop", "1", "-t", "{:.3f}".format(D), "-i", str(p)]
        a = min(float(at), max(D - 0.6, 0.0))
        e = "(1-pow(1-min(max((t-{a})/0.5,0),1),3))".format(a=a)
        chain = ["format=rgba"]
        if anim == "out":
            chain += ["fade=t=in:st=0:d=0.3:alpha=1", "fade=t=out:st={:.3f}:d=0.3:alpha=1".format(a)]
        else:
            chain += ["fade=t=in:st={:.3f}:d=0.3:alpha=1".format(a if anim not in ("shrink", "sweep") else 0.0),
                      "fade=t=out:st={:.3f}:d=0.3:alpha=1".format(max(D - 0.3, a + 0.3))]
        x, y = str(x0), str(y0)
        if anim == "fade-up":
            y = "{}+60*(1-{})".format(y0, e)
        elif anim == "slide-left":
            x = "{}-{}*0.18*(1-{})".format(x0, W, e)
        elif anim in ("pop", "shrink"):
            k_ = "(0.86+0.14*{e})".format(e=e) if anim == "pop" else "(1-0.25*(1-pow(1-min(max((t-{a})/0.7,0),1),3)))".format(a=a)
            chain.append("scale=w='{w}*{k}':h='{h}*{k}':eval=frame".format(w=Wc, h=Hc, k=k_))
            x, y = "{}+({}-overlay_w)/2".format(x0, Wc), "{}+({}-overlay_h)/2".format(y0, Hc)
        elif anim == "sweep":
            x = "{}+{}*(-0.32+0.64*min(t/{:.3f},1))".format(x0, Wc, D)
        graph.append("[{}:v]{}[p{}]".format(k + 1, ",".join(chain), k))
        graph.append("[{}][p{}]overlay=x='{}':y='{}':eval=frame:format=auto[o{}]".format(last, k, x, y, k))
        last = "o{}".format(k)
    graph.append("[{}]format=yuv420p[v]".format(last))
    out = folder / (cid + ".mp4")
    media.run(["ffmpeg", "-hide_banner", "-y", *inputs, "-filter_complex", ";".join(graph), "-map", "[v]", "-r", str(fps),
               "-c:v", "libx264", "-preset", "veryfast", "-crf", "16", "-t", "{:.3f}".format(D), str(out)])
    write_json(out.with_suffix(".layout.json"), {"text_zone": "lower", "theme": t["id"], "build": len(parts)})
    return out
