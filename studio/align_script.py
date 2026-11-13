#!/usr/bin/env python3
"""Word times for a KNOWN script on the owner's English voiceover, offline (pocketsphinx forced alignment).

The Animation Editor times every visual to its word with this (McDonald's explainer, 2026-11-13: 152 of 152 words
aligned). Whisper's weights are blocked in the cloud environment; pocketsphinx ships its English model in the wheel.

    python3 -m pip install pocketsphinx
    python3 studio/align_script.py <vo.mp3> <script.txt|.md> <words.json> [--say "1940=nineteen forty" ...]

The script text is everything between the first and the last double quote when there is one, else the whole file.
Numbers must be spelled as spoken: pass --say "1955=nineteen fifty five". Names the dictionary lacks are added with a
rough phone spelling (--phones "kroc=K R AA K"); the run lists any word it still cannot find. Writes
[{"word", "start", "end"}] in seconds.
"""
import argparse
import json
import re
import subprocess
import sys

GUESS = {"a": "AH", "e": "EH", "i": "IH", "o": "AA", "u": "AH", "y": "IY", "b": "B", "c": "K", "d": "D", "f": "F", "g": "G",
         "h": "HH", "j": "JH", "k": "K", "l": "L", "m": "M", "n": "N", "p": "P", "q": "K", "r": "R", "s": "S", "t": "T",
         "v": "V", "w": "W", "x": "K S", "z": "Z", "'": ""}


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("vo"); ap.add_argument("script"); ap.add_argument("out")
    ap.add_argument("--say", action="append", default=[], help='how a token is spoken, e.g. "1940=nineteen forty"')
    ap.add_argument("--phones", action="append", default=[], help='phones for a word, e.g. "kroc=K R AA K"')
    a = ap.parse_args(argv)
    from pocketsphinx import Decoder
    text = open(a.script, encoding="utf-8").read()
    if text.count('"') >= 2:
        text = text.split('"', 1)[1].rsplit('"', 1)[0]
    text = text.replace("’", "'").replace("‘", "'")
    for pair in a.say:
        k, v = pair.split("=", 1); text = text.replace(k, " " + v + " ")
    text = re.sub(r"(\w)-(\w)", r"\1 \2", text)
    words = re.sub(r"[^a-z' ]", " ", text.lower()).split()
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", a.vo, "-ac", "1", "-ar", "16000", "-f", "s16le", "-"], capture_output=True, check=True).stdout
    d = Decoder(samprate=16000, bestpath=False)
    extra = dict(p.split("=", 1) for p in a.phones)
    for w in sorted(set(words)):
        if d.lookup_word(w) is None:
            ph = extra.get(w) or " ".join(GUESS[c] for c in w if GUESS.get(c))
            d.add_word(w, ph, False)
            print("added", w, "=", ph, "(pass --phones to correct it)", file=sys.stderr)
    d.set_align_text(" ".join(words))
    d.start_utt(); d.process_raw(raw, full_utt=True); d.end_utt()
    seg = [{"word": s.word.split("(")[0], "start": round(s.start_frame / 100, 2), "end": round((s.end_frame + 1) / 100, 2)}
           for s in d.seg() if s.word not in ("<s>", "</s>", "<sil>", "(NULL)")]
    json.dump(seg, open(a.out, "w"), indent=0)
    print("{} of {} words aligned -> {}".format(len(seg), len(words), a.out))
    return 0 if len(seg) == len(words) else 1


if __name__ == "__main__":
    raise SystemExit(main())
