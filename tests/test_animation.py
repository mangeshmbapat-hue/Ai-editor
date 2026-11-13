"""Animation Editor tests. SYNTHETIC fixtures only: the made-up 'Kartly' spec and a flat-colour PNG icon.
No owner sample, product or real footage is used."""

import json
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from aifilm.core import ProductionError, write_json
from aifilm.editor import animation as A
from aifilm.editor.cli import main

REPO = Path(__file__).resolve().parents[1]
EXAMPLE = REPO / "editor" / "styles" / "animation-product-promo" / "spec.example.json"
HAVE_RENDER = all(shutil.which(x) for x in ("node", "ffmpeg")) and subprocess.run(
    ["node", "-e", "require('playwright')"], capture_output=True).returncode == 0


def spec(**over):
    s = json.loads(EXAMPLE.read_text(encoding="utf-8"))
    s.update(over)
    return s


class SpecTest(unittest.TestCase):
    def test_example_is_valid_and_in_the_house_length(self):
        total = A.validate(spec())
        self.assertGreaterEqual(total, 17)
        self.assertLessEqual(total, 24)

    def test_rejects_bad_scenes(self):
        with self.assertRaises(ProductionError):
            A.validate({"scenes": [{"type": "explode", "dur": 2}]})
        with self.assertRaises(ProductionError):
            A.validate({"scenes": [{"type": "words", "dur": 20, "text": "x"}]})
        with self.assertRaises(ProductionError):  # the end card must be last and carry the owner's handle
            A.validate({"scenes": [{"type": "endcard", "dur": 5}, {"type": "words", "dur": 2, "text": "x"}]})

    def test_brand_theme_follows_the_learned_recipe(self):
        light = A.theme_from_brand("#ff6600", "lavender")
        self.assertEqual(light["accents"]["primary"], "#ff6600")
        ground = light["grounds"]["light"]
        self.assertTrue(all(int(ground[i:i + 2], 16) > 220 for i in (1, 3, 5)), ground)  # a light tint
        dark = A.theme_from_brand("#ff6600", "midnight")
        self.assertIn("linear-gradient", dark["grounds"]["deep"])
        self.assertEqual(A.THEMES["lavender"]["accents"]["primary"], "#9b00ca")  # learned themes untouched
        for name, t in A.THEMES.items():
            self.assertLessEqual(len([k for k in t["accents"] if k not in ("glow", "gold")]), 3, name)


class BuildAndGateTest(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.edit = self.tmp / "edit"
        (self.edit / "raw").mkdir(parents=True)
        self.addCleanup(shutil.rmtree, self.tmp)

    def make(self, s):
        p = self.tmp / "spec.json"
        p.write_text(json.dumps(s), encoding="utf-8")
        with mock.patch.object(A, "vendor_gsap", lambda proj: None):
            return A.anim_new(self.edit, p)

    def test_build_writes_a_composition_with_assets(self):
        (self.edit / "raw" / "box.png").write_bytes(b"\x89PNG synthetic")
        s = spec()
        s["scenes"][2]["items"][0]["icon"] = "box.png"
        info = self.make(s)
        proj = Path(info["project"])
        html = (proj / "index.html").read_text(encoding="utf-8")
        self.assertIn('data-composition-id="main"', html)
        self.assertIn('"#9b00ca"', html)
        self.assertTrue((proj / "runtime.js").exists() and (proj / "assets" / "box.png").exists())
        self.assertEqual(info["size"], "1080x1080")
        self.assertEqual(info["scenes"][-1]["type"], "endcard")

    def test_props_are_assets(self):
        s = spec()
        s["scenes"][1]["props"] = [{"image": "cup.png", "x": 0.5, "y": 0.3, "w": 0.3}]
        self.assertIn("cup.png", A.assets_of(s))
        with self.assertRaises(ProductionError):  # a prop that is not in raw/ is refused
            self.make(s)

    def test_missing_asset_is_refused(self):
        s = spec()
        s["scenes"][0]["image"] = "logo.png"
        with self.assertRaises(ProductionError):
            self.make(s)

    def test_render_needs_approval_of_the_exact_spec(self):
        self.make(spec())
        with self.assertRaises(ProductionError):
            A.anim_render(self.edit)
        with self.assertRaises(ProductionError):  # no storyboard shown yet
            A.anim_approve(self.edit, "promo", "ok")
        sb = A.project_dir(self.edit, "promo") / "storyboard"
        sb.mkdir()
        (sb / "STORYBOARD.md").write_text("synthetic", encoding="utf-8")
        A.anim_approve(self.edit, "promo", "SYNTHETIC test approval")
        A.require_anim_approval(self.edit, "promo")
        changed = spec()
        changed["scenes"][3]["label"] = "Buy now"
        self.make(changed)
        with self.assertRaises(ProductionError):
            A.require_anim_approval(self.edit, "promo")

    def test_cli_themes(self):
        self.assertEqual(main(["anim-themes", "--brand", "#00aa88"]), 0)


class CompositionModeTest(unittest.TestCase):
    def test_hand_built_composition_is_gated_on_its_files(self):
        tmp = Path(tempfile.mkdtemp()); self.addCleanup(shutil.rmtree, tmp)
        edit = tmp / "edit"; proj = A.project_dir(edit, "x"); (proj / "assets").mkdir(parents=True)
        (proj / "page.html").write_text("<html>SYNTHETIC</html>", encoding="utf-8")
        (proj / "assets" / "a.png").write_bytes(b"synthetic")
        write_json(proj / "spec.json", {"composition": "page.html", "aspect": "16:9", "duration": 10, "storyboard": [{"t": 1, "what": "beat"}]})
        with mock.patch.object(A, "vendor_gsap", lambda p: None):
            info = A.build(edit, "x")
        self.assertEqual(info["size"], "1920x1080")
        (proj / "storyboard").mkdir(); (proj / "storyboard" / "STORYBOARD.md").write_text("synthetic", encoding="utf-8")
        A.anim_approve(edit, "x", "SYNTHETIC test approval")
        A.require_anim_approval(edit, "x")
        (proj / "assets" / "a.png").write_bytes(b"changed")  # any asset change needs a new approval
        with self.assertRaises(ProductionError):
            A.require_anim_approval(edit, "x")


class ProductLibraryTest(unittest.TestCase):
    def test_every_category_has_a_sheet_and_honest_status(self):
        lib = json.loads((REPO / "editor" / "product-styles" / "LIBRARY.json").read_text(encoding="utf-8"))
        self.assertLessEqual({"makeup-beauty", "food-drinks", "fashion-clothing", "automobile"}, set(lib["categories"]))
        for slug, c in lib["categories"].items():
            sheet = (REPO / c["sheet"]).read_text(encoding="utf-8")
            if c["status"] == "not learned":  # a template must never read as a learned style
                self.assertIn("not learned yet", sheet, slug)


@unittest.skipUnless(HAVE_RENDER, "needs node, Playwright's Chromium and FFmpeg")
class RenderTest(unittest.TestCase):
    def test_storyboard_frames(self):
        tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, tmp)
        edit = tmp / "edit"
        edit.mkdir()
        p = tmp / "spec.json"
        p.write_text(json.dumps(spec()), encoding="utf-8")
        try:
            A.anim_new(edit, p)
        except ProductionError as exc:  # GSAP comes from the npm registry
            self.skipTest(str(exc))
        out = A.storyboard(edit)
        frames = sorted((A.project_dir(edit, "promo") / "storyboard").glob("*.png"))
        self.assertEqual(len(frames), out["frames"])
        self.assertEqual(len(frames), len(spec()["scenes"]))


if __name__ == "__main__":
    unittest.main()
