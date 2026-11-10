"""Faceless Editor tests. SYNTHETIC fixtures only: flat-colour PNG stills, a tone "voiceover"
and hand-written word timings. No owner sample or real footage is used."""

import json
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

from aifilm.core import ProductionError, write_json
from aifilm.editor import edl as E
from aifilm.editor import faceless as F
from aifilm.editor import render as R
from aifilm.editor import tools as T
from aifilm.editor.cli import main

HAVE_FFMPEG = shutil.which("ffmpeg") is not None

SCRIPT = ("What if fear could be turned into a painting? In 1892, Edvard Munch painted the Scream. "
          "But it became famous after the war. It shows 4 versions, and one hides a note. "
          "That is why it became a symbol of fear itself.")


def synthetic_words(text=SCRIPT, rate=2.7, start=0.0):
    words, t = [], start
    for w in text.split():
        d = max(0.18, len(w) / (rate * 5.0))
        words.append({"start": round(t, 3), "end": round(t + d, 3), "word": " " + w})
        t += 1.0 / rate + (0.35 if w.endswith((".", "?")) else 0.0)
    return words


def ff(*args):
    subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", *map(str, args)], check=True)


class PlanLogicTest(unittest.TestCase):
    def test_scenes_are_short_and_start_on_sentences(self):
        words = [dict(w, word=w["word"].strip()) for w in synthetic_words()]
        groups = F.scenes(words)
        spans = [g[-1]["end"] - g[0]["start"] for g in groups]
        self.assertLessEqual(max(spans), 3.2)
        self.assertTrue(any(g[0]["word"] == "But" for g in groups), "a turn word opens its own scene")
        self.assertEqual(sum(len(g) for g in groups), len(words))
        self.assertLessEqual(groups[1][0]["start"], F.HOOK_MAX + 0.6)

    def test_key_words_numbers_dates_and_names(self):
        self.assertTrue(F.is_key("1892,", False))
        self.assertTrue(F.is_key("$381", False))
        self.assertTrue(F.is_key("80%.", False))
        self.assertTrue(F.is_key("A119.", False))
        self.assertTrue(F.is_key("Munch", False))
        self.assertFalse(F.is_key("What", True))
        self.assertFalse(F.is_key("painting", False))

    def test_wrap_never_drops_text(self):
        self.assertEqual(F.wrap("Destroying the moon", 9, 5), "Destroying\nthe moon")
        with self.assertRaises(ProductionError):
            F.wrap("one two three four five six seven eight nine ten", 5, 2)

    def test_caption_cues_follow_reading_rules(self):
        words = [dict(w, word=w["word"].strip()) for w in synthetic_words()]
        cues = F.caption_cues(words)
        self.assertEqual(sum(len(c) for c in cues), len(words))
        self.assertTrue(all(len(c) <= 4 and len(" ".join(w["word"] for w in c)) <= 32 for c in cues))

    def test_word_formats(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "w.json"
            p.write_text(json.dumps({"segments": [{"words": [{"start": 0, "end": 0.3, "word": " Hi"}]}]}))
            self.assertEqual(F.load_words(p)[0]["word"], "Hi")
            p.write_text(json.dumps({"words": [{"s": 0.1, "e": 0.4, "w": "नमस्ते"}]}))
            self.assertEqual(F.load_words(p)[0]["word"], "नमस्ते")

    def test_text_entrances_are_ass_tags(self):
        self.assertIn("\\t(", E.text_motion("pop"))
        self.assertEqual(E.text_motion(None), "")
        for kind in ("pop", "fade", "slam"):
            self.assertRegex(E.text_motion(kind), r"\\fad\(\d+,1[0-9]{2}\)", "text also leaves smoothly")

    def test_house_style_is_learned_and_measured(self):
        style = json.loads((R.STYLES / F.HOUSE_STYLE / "style.json").read_text(encoding="utf-8"))
        self.assertTrue(style["measured"])
        self.assertEqual(style["targets"]["prelap_seconds"], F.PRELAP)
        self.assertEqual(len(style["samples"]), 4)
        sheet = (R.STYLES / F.HOUSE_STYLE / "STYLE_SHEET.md").read_text(encoding="utf-8")
        self.assertIn("Status: **learned**", sheet)
        self.assertIn("## Timing", sheet)


@unittest.skipUnless(HAVE_FFMPEG, "media tests need FFmpeg")
class PlanMediaTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        src = Path(self.temp.name) / "src"
        src.mkdir()
        for i, colour in enumerate(["0x5a3a2a", "0x2a3a5a", "0x3a5a2a", "0x6a2a2a"]):
            ff("-f", "lavfi", "-i", "color=c={}:s=360x640".format(colour), "-frames:v", "1", src / "still{}.png".format(i + 1))
        words = synthetic_words()
        length = words[-1]["end"] + 0.6
        ff("-f", "lavfi", "-i", "sine=f=200:d={:.2f}".format(length), "-c:a", "aac", src / "vo.m4a")
        ff("-f", "lavfi", "-i", "sine=f=330:d=40,volume=0.5", src / "bed.wav")
        self.edit = Path(self.temp.name) / "edit"
        T.ingest(self.edit, sorted(src.iterdir()))
        write_json(self.edit / "words.json", {"segments": [{"words": words}]})

    def test_stills_plan_storyboard_and_render_keep_the_vo_in_sync(self):
        made = F.stills(self.edit, seconds=6)
        self.assertEqual(len(made), 4)
        r = F.plan(self.edit, "raw/vo.m4a", "words.json", cta="Follow for part 2", music="raw/bed.wav")
        edl = json.loads((self.edit / "edl.json").read_text(encoding="utf-8"))
        rows, total = E.timeline(edl)
        self.assertEqual(edl["audio"]["voice"]["file"], "raw/vo.m4a")
        self.assertFalse(edl["audio"]["keep_source"])
        self.assertEqual(edl["clips"][-1]["beat"], "end card")
        self.assertEqual(edl["clips"][-1]["text"][0]["value"], "Follow for\npart 2")
        self.assertEqual(edl["clips"][0]["text"][0]["role"] in ("title", "headline"), True)
        self.assertLessEqual(rows[1]["start"], 2.5, "the hook scene changes by 2.5 s")
        values = [t["value"] for c in edl["clips"] for t in c.get("text", [])]
        self.assertIn("1892", values)
        self.assertIn("Edvard Munch", values)
        self.assertTrue(edl["subtitles"]["burn"])
        self.assertTrue(all(1.0 <= row["duration"] <= 4.0 for row in rows[1:-1]), rows)
        self.assertGreater(r["scenes"], 5)
        # owner gates still apply: no storyboard approval, no render
        E.approve_style(self.edit, F.HOUSE_STYLE, "SYNTHETIC TEST approval")
        with self.assertRaises(ProductionError):
            R.render(self.edit)
        E.storyboard(self.edit)
        E.approve(self.edit, "SYNTHETIC TEST approval")
        R.render(self.edit, preview=False, quality="draft")
        qc = R.qc(self.edit)
        checks = {c["check"]: c for c in qc["checks"]}
        self.assertEqual(checks["duration"]["result"], "pass")
        self.assertEqual(checks["true peak"]["result"], "pass", checks["true peak"])

    def test_cli_plan_without_cta_notes_it(self):
        F.stills(self.edit, seconds=6)
        code = main(["faceless-plan", str(self.edit), "--voice", "raw/vo.m4a", "--words", "words.json", "--no-captions"])
        self.assertEqual(code, 0)
        edl = json.loads((self.edit / "edl.json").read_text(encoding="utf-8"))
        self.assertNotIn("subtitles", edl)
        self.assertTrue(any("CTA" in n for n in edl["notes"]))

    def test_owner_rules_quiet_sfx_and_no_shake(self):
        """Owner rules 2026-11-10: SFX and music stay well under the VO; nothing shakes."""
        from aifilm.editor import craft as C
        F.stills(self.edit, seconds=6)
        ff("-f", "lavfi", "-i", "anoisesrc=d=0.4:c=pink:a=0.9", self.edit / "raw" / "whoosh.wav")
        F.plan(self.edit, "raw/vo.m4a", "words.json", cta="x", music="raw/bed.wav")
        edl = json.loads((self.edit / "edl.json").read_text(encoding="utf-8"))
        self.assertTrue(all(c.get("zoom", {}).get("from", 1) <= 1.05 and c.get("zoom", {}).get("to", 1) <= 1.05 for c in edl["clips"]))
        edl["audio"]["sfx"] = [{"file": "raw/whoosh.wav", "at": 2.0, "gain_db": 0}]
        edl["audio"]["music"]["gain_db"] = 0
        edl["clips"][2]["fx"] = ["shake"]
        write_json(self.edit / "edl.json", edl)
        found = {f["check"]: f["result"] for f in C.check(self.edit, edl, sample_contrast=False)}
        self.assertEqual(found["banned effects"], "fail")
        self.assertEqual(found["SFX under voiceover"], "fail")
        self.assertEqual(found["music under voiceover"], "fail")
        r = F.level(self.edit)
        self.assertTrue(r["changes"])
        edl = json.loads((self.edit / "edl.json").read_text(encoding="utf-8"))
        found = {f["check"]: f["result"] for f in C.check(self.edit, edl, sample_contrast=False)}
        self.assertEqual(found["banned effects"], "pass")
        self.assertEqual(found["SFX under voiceover"], "pass")
        self.assertEqual(found["music under voiceover"], "pass")

    def test_sub_edl_shifts_the_voice(self):
        F.stills(self.edit, seconds=6)
        F.plan(self.edit, "raw/vo.m4a", "words.json", cta="x")
        edl = json.loads((self.edit / "edl.json").read_text(encoding="utf-8"))
        part, offset, _ = E.sub_edl(edl, [edl["clips"][3]["id"]])
        self.assertAlmostEqual(part["audio"]["voice"]["start"], offset, places=3)
        self.assertEqual(part["audio"]["voice"]["at"], 0)


if __name__ == "__main__":
    unittest.main()
