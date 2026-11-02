"""Mann (AI video editor) tests. All media are SYNTHETIC FFmpeg fixtures (test patterns,
sine tones, pink noise), never real footage. They prove the pipeline's mechanics, not edit quality."""

import io
import json
import shutil
import subprocess
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path

from aifilm.core import ProductionError, read_json, write_json
from aifilm.editor import edl as E
from aifilm.editor import media, render as R, style as S, tools as T
from aifilm.editor.cli import main

REPO = Path(__file__).resolve().parents[1]
HAS_FFMPEG = shutil.which("ffmpeg") is not None and shutil.which("ffprobe") is not None


def ff(*args):
    subprocess.run(["ffmpeg", "-v", "error", "-y"] + [str(a) for a in args], check=True, timeout=120)


@unittest.skipUnless(HAS_FFMPEG, "FFmpeg is required for media tests")
class EditorCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fixtures = Path(tempfile.mkdtemp(prefix="mann-fixtures-"))
        f = cls.fixtures
        ff("-f", "lavfi", "-i", "testsrc2=size=640x360:rate=30:d=4", "-f", "lavfi", "-i", "sine=frequency=330:duration=4",
           "-c:v", "libx264", "-pix_fmt", "yuv420p", "-c:a", "aac", "-shortest", f / "A.mp4")
        ff("-f", "lavfi", "-i", "smptebars=size=480x360:rate=25:d=3", "-c:v", "libx264", "-pix_fmt", "yuv420p", f / "B_silent.mp4")
        ff("-f", "lavfi", "-i", "sine=frequency=110:duration=2", "-c:a", "libmp3lame", f / "music.mp3")
        ff("-f", "lavfi", "-i", "anoisesrc=d=0.3:c=pink", f / "whoosh.wav")
        # Three solid colours, hard cuts at 1.0 s and 2.0 s, for cut detection.
        ff("-f", "lavfi", "-i", "color=c=red:s=320x180:r=25:d=1", "-f", "lavfi", "-i", "color=c=blue:s=320x180:r=25:d=1",
           "-f", "lavfi", "-i", "color=c=green:s=320x180:r=25:d=1", "-filter_complex", "[0][1][2]concat=n=3:v=1:a=0",
           "-c:v", "libx264", "-pix_fmt", "yuv420p", f / "cuts.mp4")
        (f / "subs.srt").write_text("1\n00:00:00,000 --> 00:00:01,500\nSynthetic fixture caption\n", encoding="utf-8")

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.fixtures, ignore_errors=True)

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.edit = Path(self.temp.name) / "edit"
        T.ingest(self.edit, [self.fixtures / n for n in ("A.mp4", "B_silent.mp4", "music.mp3", "whoosh.wav", "subs.srt")])
        self.edl = {
            "version": 1, "title": "Synthetic fixture edit", "format": {"width": 360, "height": 640, "fps": 30},
            "sources": {"A": "raw/A.mp4", "B": "raw/B_silent.mp4"},
            "clips": [
                {"id": "C01", "source": "A", "in": 0.2, "out": 1.4, "beat": "hook", "zoom": {"from": 1.0, "to": 1.2},
                 "text": {"value": "हुक HOOK", "position": "top", "box": True}},
                {"id": "C02", "source": "B", "in": 0.5, "out": 2.0, "transition_in": {"type": "dissolve", "duration": 0.3}, "grade": "warm-film"},
                {"id": "C03", "source": "A", "in": 2.0, "out": 3.2, "speed": 1.5},
            ],
            "grade": {"preset": "punchy-social"},
            "audio": {"music": {"file": "raw/music.mp3", "gain_db": -14, "fade_out": 0.4},
                      "sfx": [{"file": "raw/whoosh.wav", "at": 1.0, "gain_db": -6}]},
            "subtitles": {"file": "raw/subs.srt"},
            "master": {"lufs": -14, "true_peak": -1},
        }
        self.save()

    def save(self):
        write_json(self.edit / "edl.json", self.edl)

    def test_ingest_records_hashes_and_probes(self):
        log = read_json(self.edit / "media.json")["files"]
        self.assertEqual(len(log["raw/A.mp4"]["sha256"]), 64)
        self.assertTrue(log["raw/A.mp4"]["probe"]["has_audio"])
        self.assertFalse(log["raw/B_silent.mp4"]["probe"]["has_audio"])

    def test_timeline_and_pace(self):
        rows, total = E.timeline(self.edl)
        self.assertEqual([r["start"] for r in rows], [0.0, 0.9, 2.4])
        self.assertAlmostEqual(total, 1.2 + 1.5 + 0.8 - 0.3, places=3)
        self.assertEqual(E.pace(self.edl)["shots"], 3)

    def test_validation_rejects_bad_edits(self):
        cases = [
            (lambda d: d["clips"][0].update(out=99), "past the end"),
            (lambda d: d["clips"][0].update(transition_in={"type": "dissolve", "duration": 0.2}), "first clip"),
            (lambda d: d["clips"][1].update(transition_in={"type": "dissolve", "duration": 1.3}), "shorter than both"),
            (lambda d: d["clips"][1].update(transition_in={"type": "spin3d"}), "unknown transition"),
            (lambda d: d["grade"].update(preset="nope"), "grade preset"),
            (lambda d: d["sources"].update(A="../escape.mp4"), "escapes"),
        ]
        for mutate, message in cases:
            with self.subTest(message=message):
                data = json.loads(json.dumps(self.edl))
                mutate(data)
                with self.assertRaisesRegex(ProductionError, message):
                    E.validate(self.edit, data)

    def test_storyboard_gate_render_and_qc(self):
        board = E.storyboard(self.edit)
        self.assertEqual([f["clip"] for f in board["frames"]], ["C01", "C02", "C03"])
        for f in board["frames"]:
            info = media.probe(self.edit / "storyboard" / f["file"])
            self.assertEqual((info["width"], info["height"]), (360, 640))
        self.assertIn("waiting for owner approval", (self.edit / "storyboard" / "STORYBOARD.md").read_text(encoding="utf-8"))
        with self.assertRaisesRegex(ProductionError, "not approved"):
            R.render(self.edit)
        with self.assertRaisesRegex(ProductionError, "exact approval words"):
            E.approve(self.edit, "  ")
        E.approve(self.edit, "synthetic fixture approval")
        out = R.render(self.edit)
        info = media.probe(out["master"])
        self.assertEqual((info["width"], info["height"]), (360, 640))
        self.assertAlmostEqual(info["duration"], out["expected_seconds"], delta=0.07)
        self.assertTrue((self.edit / "renders" / "preview_720p.mp4").exists())
        record = R.qc(self.edit)
        checks = {c["check"]: c for c in record["checks"]}
        self.assertEqual(checks["loudness"]["result"], "pass", checks["loudness"])
        self.assertEqual(checks["duration"]["result"], "pass")
        self.assertTrue(record["passed"], record["checks"])
        self.assertGreaterEqual(len(R.contact_frames(self.edit, 1.0)), 3)
        # A changed EDL voids the approval and the change list names the change.
        self.edl["clips"][2]["grade"] = "cool-night"
        self.save()
        with self.assertRaisesRegex(ProductionError, "not approved"):
            R.render(self.edit)
        with self.assertRaisesRegex(ProductionError, "qc for this EDL"):
            E.approve(self.edit, "final ok", kind="final")
        again = E.storyboard(self.edit)
        self.assertTrue(any("C03" in line and "cool-night" in line for line in again["changes_since_previous"]))

    def test_changed_source_file_voids_approval(self):
        E.storyboard(self.edit)
        E.approve(self.edit, "synthetic fixture approval")
        self.assertTrue(E.approved(self.edit, E.load(self.edit)))
        shutil.copyfile(self.fixtures / "whoosh.wav", self.edit / "raw" / "music.mp3")
        self.assertFalse(E.approved(self.edit, E.load(self.edit)))

    def test_qc_flags_missing_subtitles_and_dead_air(self):
        self.edl["subtitles"] = None
        self.edl["audio"] = {"keep_source": False}
        self.save()
        E.storyboard(self.edit)
        E.approve(self.edit, "synthetic fixture approval")
        R.render(self.edit, preview=False)
        record = R.qc(self.edit)
        failed = {c["check"] for c in record["checks"] if c["result"] == "fail"}
        self.assertFalse(record["passed"])
        self.assertIn("subtitles", failed)
        self.assertIn("loudness", failed)

    def test_cli_exit_codes(self):
        with redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()) as err:
            self.assertEqual(main(["validate", str(self.edit)]), 0)
            self.assertEqual(main(["render", str(self.edit)]), 2)
        self.assertIn("not approved", err.getvalue())

    def test_style_analysis_finds_hard_cuts(self):
        work = Path(self.temp.name) / "lab"
        a = S.analyze(self.fixtures / "cuts.mp4", work, "Synthetic three colours")
        self.assertEqual(a["pace"]["shots"], 3)
        self.assertEqual([round(s["start"], 1) for s in a["shots"]], [0.0, 1.0, 2.0])
        self.assertEqual(len(list((work / "frames").glob("*.jpg"))), 3)
        hexes = {c["hex"] for c in a["colour"]["palette"]}
        self.assertTrue(any(h.startswith("#f") or h.startswith("#e") for h in hexes), hexes)
        draft = (work / "STYLE_SHEET.draft.md").read_text(encoding="utf-8")
        self.assertIn("## Measured", draft)
        with self.assertRaisesRegex(ProductionError, "Write"):
            S.publish(work, Path(self.temp.name) / "styles", "synthetic")
        (work / "STYLE_SHEET.md").write_text(draft, encoding="utf-8")
        with self.assertRaisesRegex(ProductionError, "unfilled"):
            S.publish(work, Path(self.temp.name) / "styles", "synthetic")
        (work / "STYLE_SHEET.md").write_text(draft.replace("_Mann:", "Observed:"), encoding="utf-8")
        dest = S.publish(work, Path(self.temp.name) / "styles", "synthetic")
        saved = read_json(dest / "style.json")
        self.assertAlmostEqual(saved["targets"]["average_shot_seconds"], 1.0, places=1)
        self.assertNotIn("frames", saved["analysis"])


class EditorStaticTest(unittest.TestCase):
    def test_rules_file(self):
        data = read_json(REPO / "editor" / "rules.json")
        for key in ["loudness_lufs", "true_peak_max_db", "max_dead_air_seconds", "short_form_max_shot_seconds",
                    "hook_first_cut_max_seconds", "short_form_requires_subtitles", "min_shot_seconds", "style_pace_tolerance",
                    "loudness_tolerance_lu", "max_black_seconds", "dead_air_noise_db", "short_form_max_seconds"]:
            self.assertIn(key, data["rules"])
        for h in data["history"]:
            self.assertRegex(h["date"], r"^\d{4}-\d{2}-\d{2}$")
            self.assertIn(h["kind"], {"owner", "observed", "result"})

    def test_srt_writer_splits_words(self):
        with tempfile.TemporaryDirectory() as tmp:
            seg = [{"start": 0.0, "end": 2.0, "text": "a b c d e",
                    "words": [{"start": i * 0.4, "end": i * 0.4 + 0.3, "word": w} for i, w in enumerate("abcde")]}]
            self.assertEqual(T.write_srt(seg, Path(tmp) / "x.srt", max_words=2), 3)
            self.assertIn("00:00:01,600 --> 00:00:01,900", (Path(tmp) / "x.srt").read_text(encoding="utf-8"))

    def test_vendor_gsap_rewrites_cdn_link_without_network_when_present(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp)
            (p / "vendor").mkdir()
            (p / "vendor" / "gsap.min.js").write_text("/* synthetic stand-in */", encoding="utf-8")
            (p / "compositions").mkdir()
            cdn = '<script src="https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js"></script>'
            (p / "index.html").write_text(cdn, encoding="utf-8")
            (p / "compositions" / "intro.html").write_text(cdn, encoding="utf-8")
            T.vendor_gsap(p)
            self.assertIn('src="vendor/gsap.min.js"', (p / "index.html").read_text(encoding="utf-8"))
            self.assertIn('src="../vendor/gsap.min.js"', (p / "compositions" / "intro.html").read_text(encoding="utf-8"))

    def test_atempo_chain(self):
        self.assertEqual(R.atempo(1.0), [])
        self.assertEqual(R.atempo(3.0), ["atempo=2.0", "atempo=1.50000"])
        self.assertEqual(R.atempo(0.25), ["atempo=0.5", "atempo=0.50000"])


if __name__ == "__main__":
    unittest.main()


CATALOG = REPO / "editor" / "styles" / "catalog.json"


class CatalogTest(unittest.TestCase):
    def test_fifty_styles_are_complete_and_engine_ready(self):
        data = read_json(CATALOG)
        styles = data["styles"]
        self.assertEqual(len(styles), 50)
        self.assertEqual(len({s["slug"] for s in styles}), 50)
        self.assertEqual({s["family"] for s in styles}, set(data["families"]))
        text_fields = ["name", "best_for", "aspect", "duration", "hook", "structure", "cutting", "camera", "transitions",
                       "type", "mg", "colour", "sound", "vfx"]
        for s in styles:
            with self.subTest(style=s["slug"]):
                for f in text_fields:
                    self.assertTrue(isinstance(s[f], str) and s[f].strip(), f)
                self.assertGreaterEqual(len(s["signature"]), 3)
                self.assertTrue(s["avoid"] and s["twists"] and s["known_from"])
                self.assertIn(s["fit"]["speech"], {"high", "low", "any"})
                self.assertIn(s["fit"]["motion"], {"low", "mid", "high", "any"})
                e = s["edl"]
                self.assertIn(e["grade"], E.GRADES)
                self.assertIn(e.get("transition", "cut"), E.TRANSITIONS)
                for fx in list((e.get("fx_every") or {})) + (e.get("fx_all") or []) + (e.get("fx_last") or []):
                    self.assertIn(fx, E.FX)
                if e.get("captions"):
                    self.assertIn(e["captions"]["color"], E.SUB_COLOURS)
                    self.assertIn(e["captions"]["position"], E.TEXT_POSITIONS)
                sheet = REPO / "editor" / "styles" / s["slug"] / "STYLE_SHEET.md"
                self.assertTrue(sheet.exists(), "run python3 editor/styles/build_styles.py")
                self.assertIn(s["hook"], sheet.read_text(encoding="utf-8"))
                self.assertEqual(read_json(sheet.parent / "style.json")["targets"]["average_shot_seconds"], s["pace"]["avg_shot"])
        index = (REPO / "editor" / "styles" / "INDEX.md").read_text(encoding="utf-8")
        for s in styles:
            self.assertIn("`{}`".format(s["slug"]), index)


@unittest.skipUnless(HAS_FFMPEG, "FFmpeg is required for media tests")
class EngineCase(unittest.TestCase):
    """SYNTHETIC fixtures: a flat-colour 'talking' clip with a gated tone, two moving test
    patterns as B-roll, a 120 BPM click track as music, pink noise as an SFX."""

    @classmethod
    def setUpClass(cls):
        cls.fixtures = Path(tempfile.mkdtemp(prefix="mann-engine-"))
        f = cls.fixtures
        ff("-f", "lavfi", "-i", "color=c=0x806050:s=320x180:r=30:d=9", "-f", "lavfi",
           "-i", "sine=f=220:d=9,volume='if(lt(mod(t,3),2.2),1,0)':eval=frame", "-c:v", "libx264", "-pix_fmt", "yuv420p",
           "-c:a", "aac", "-shortest", f / "talk.mp4")
        ff("-f", "lavfi", "-i", "testsrc2=s=320x180:r=30:d=6", "-c:v", "libx264", "-pix_fmt", "yuv420p", f / "broll1.mp4")
        ff("-f", "lavfi", "-i", "mandelbrot=s=320x180:r=30,trim=duration=5", "-c:v", "libx264", "-pix_fmt", "yuv420p", f / "broll2.mp4")
        ff("-f", "lavfi", "-i", "sine=f=1000:d=20,volume='if(lt(mod(t,0.5),0.05),1,0)':eval=frame", "-f", "lavfi", "-i", "sine=f=110:d=20",
           "-filter_complex", "[0][1]amix=inputs=2:weights=1 0.3", f / "music120.wav")
        ff("-f", "lavfi", "-i", "anoisesrc=d=0.3:c=pink", f / "whoosh.wav")

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.fixtures, ignore_errors=True)

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.edit = Path(self.temp.name) / "edit"
        T.ingest(self.edit, sorted(self.fixtures.iterdir()))
        (self.edit / "BRIEF.md").write_text("Synthetic fixture brief: travel recap\n", encoding="utf-8")

    def test_assets_beats_and_suggestions(self):
        from aifilm.editor import engine as G
        items = {a["file"]: a for a in G.assets(self.edit)}
        self.assertEqual(items["raw/music120.wav"]["kind"], "music")
        self.assertEqual(items["raw/whoosh.wav"]["kind"], "sfx")
        self.assertEqual(items["raw/talk.mp4"]["label"], "talking")
        self.assertAlmostEqual(items["raw/music120.wav"]["bpm"], 120, delta=3)
        r = G.suggest(self.edit, "9:16")
        self.assertEqual(len(r["recommended"]), 3)
        fams = {s["slug"]: s["family"] for s in G.catalog()}
        self.assertNotEqual(fams[r["experiment"]["styles"][0]], fams[r["experiment"]["styles"][1]])
        self.assertTrue(any("reframe" in p for p in r["problems"]))
        self.assertTrue(r["unique_ideas"])
        self.assertIn("Recommended styles", (self.edit / "SUGGESTIONS.md").read_text(encoding="utf-8"))

    def test_autocut_makes_a_valid_draft_in_every_style(self):
        from aifilm.editor import engine as G
        for s in G.catalog():
            with self.subTest(style=s["slug"]):
                out = G.autocut(self.edit, s["slug"], seconds=8)
                edl = read_json(self.edit / "edl.json")
                E.validate(self.edit, edl)
                self.assertEqual(edl["style"], s["slug"])
                self.assertGreater(out["seconds"], 1.0)
                self.assertEqual(edl["grade"]["preset"], s["edl"]["grade"])

    def test_owner_decisions_gate_the_storyboard(self):
        from aifilm.editor import engine as G
        G.autocut(self.edit, "interview-broll-doc", seconds=6)
        with self.assertRaisesRegex(ProductionError, "not finalised"):
            E.storyboard(self.edit)
        E.approve_style(self.edit, "interview-broll-doc", "synthetic fixture pick")
        (self.edit / "SCRIPT.md").write_text("Synthetic locked script line\n", encoding="utf-8")
        edl = read_json(self.edit / "edl.json")
        edl["script"] = "SCRIPT.md"
        write_json(self.edit / "edl.json", edl)
        with self.assertRaisesRegex(ProductionError, "not locked"):
            E.storyboard(self.edit)
        E.lock_script(self.edit, "SCRIPT.md", "synthetic lock")
        E.storyboard(self.edit)
        (self.edit / "SCRIPT.md").write_text("Changed after lock\n", encoding="utf-8")
        with self.assertRaisesRegex(ProductionError, "not locked"):
            E.storyboard(self.edit)

    def test_part_correction_touches_only_that_part(self):
        from aifilm.editor import engine as G
        G.autocut(self.edit, "beat-sync-montage", seconds=6)
        E.approve_style(self.edit, "beat-sync-montage", "synthetic fixture pick")
        E.storyboard(self.edit)
        E.approve(self.edit, "synthetic whole approval")
        self.assertEqual(E.status(self.edit, E.load(self.edit))["scope"], "none")
        edl = read_json(self.edit / "edl.json")
        target = edl["clips"][1]["id"]
        edl["clips"][1]["grade"] = "cool-night"
        write_json(self.edit / "edl.json", edl)
        st = E.status(self.edit, E.load(self.edit))
        self.assertEqual((st["scope"], st["changed_clips"]), ("part", [target]))
        with self.assertRaisesRegex(ProductionError, "changed part"):
            R.render(self.edit, preview=False)
        with self.assertRaisesRegex(ProductionError, "No part storyboard|changed after"):
            E.approve(self.edit, "too early", clips=[target])
        part = E.storyboard(self.edit, only=[target])
        self.assertEqual([f["clip"] for f in part["frames"]], [target])
        self.assertTrue(any(target in line and "cool-night" in line for line in part["changes_since_previous"]))
        preview = R.preview_part(self.edit, [target])
        self.assertIn(target, preview["clips"])
        self.assertGreater(media.probe(preview["file"])["duration"], 0.5)
        E.approve(self.edit, "synthetic part approval", clips=[target])
        self.assertEqual(E.status(self.edit, E.load(self.edit))["scope"], "none")
        R.render(self.edit, preview=False)
        edl = read_json(self.edit / "edl.json")
        edl["grade"]["preset"] = "bw-contrast"
        write_json(self.edit / "edl.json", edl)
        self.assertEqual(E.status(self.edit, E.load(self.edit))["scope"], "whole")
        with self.assertRaisesRegex(ProductionError, "whole storyboard"):
            E.approve(self.edit, "part only", clips=[target])

    def test_every_fx_renders_through_the_graph(self):
        clips = [{"id": "X{}".format(i), "source": "T", "in": 0.0, "out": 0.6, "fx": [fx]} for i, fx in enumerate(sorted(E.FX))]
        clips[-1]["freeze"] = 0.3
        clips[1]["inserts"] = [{"source": "B", "in": 0.0, "out": 0.4, "at": 0.1}]
        (self.edit / "caps.srt").write_text("1\n00:00:00,000 --> 00:00:01,000\nsynthetic caption\n", encoding="utf-8")
        write_json(self.edit / "edl.json", {"version": 1, "format": {"width": 180, "height": 320, "fps": 30},
                                            "sources": {"T": "raw/talk.mp4", "B": "raw/broll1.mp4"}, "clips": clips,
                                            "subtitles": {"file": "caps.srt", "uppercase": True, "color": "yellow", "box": True, "position": "center"}})
        rec = E.storyboard(self.edit)
        self.assertEqual(len(rec["frames"]), len(E.FX))
        staged = E.stage_subtitles(self.edit, E.load(self.edit))
        self.assertIn("SYNTHETIC CAPTION", staged.read_text(encoding="utf-8"))

    def test_sub_edl_retimes_the_part(self):
        edl = {"version": 1, "format": {"width": 180, "height": 320, "fps": 30}, "sources": {"T": "raw/talk.mp4"},
               "clips": [{"id": "A", "source": "T", "in": 0, "out": 2}, {"id": "B", "source": "T", "in": 2, "out": 4},
                         {"id": "C", "source": "T", "in": 4, "out": 6}, {"id": "D", "source": "T", "in": 6, "out": 8}],
               "audio": {"music": {"file": "raw/music120.wav", "start": 1.0}, "sfx": [{"file": "raw/whoosh.wav", "at": 0.5}, {"file": "raw/whoosh.wav", "at": 4.5}]}}
        part, offset, length = E.sub_edl(edl, ["C"])
        self.assertEqual([c["id"] for c in part["clips"]], ["B", "C", "D"])
        self.assertEqual((offset, length), (2.0, 6.0))
        self.assertEqual(part["audio"]["music"]["start"], 3.0)
        self.assertEqual([s["at"] for s in part["audio"]["sfx"]], [2.5])
        self.assertIn("00:00:01,500", E.shift_srt("00:00:03,500 --> 00:00:04,000", 2.0))
