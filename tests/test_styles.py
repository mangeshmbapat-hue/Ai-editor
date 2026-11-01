"""Structure checks for the draft style library in styles/ (text files only; no rendering)."""

import json
import re
import subprocess
import sys
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
STYLES = REPO / "styles"
KEYS = ["slug", "num", "en", "hi", "cn", "category_en", "category_hi", "category_cn", "status", "film", "line", "line_hi", "line_cn", "uses", "nearest", "frame_sec", "dur"]
HEADINGS = ["## 1. Essence, and what it is not", "## 2. Materials & rendering", "## 3. Colour logic", "## 4. Type & subtitles", "## 5. Motion quality",
            "## 6. Camera grammar", "## 7. Sound palette", "## 8. Native moves", "## 9. Pitfalls of the medium", "## 10. Engine", "## 11. Variation space"]
CATEGORIES = {"Indian Traditions", "World Folk", "Animation Techniques", "Art Movements", "Internet & Digital", "Cinema Eras"}


def folders():
    return sorted(p for p in STYLES.iterdir() if p.is_dir() and not p.name.startswith(("_", ".")))


class StyleLibraryTest(unittest.TestCase):
    def test_every_folder_is_a_complete_draft_style(self):
        dirs = folders()
        self.assertGreaterEqual(len(dirs), 50)
        nums, slugs = set(), set()
        for d in dirs:
            with self.subTest(style=d.name):
                meta = json.loads((d / "style.json").read_text(encoding="utf-8"))
                self.assertEqual(list(meta), KEYS)
                self.assertEqual(meta["slug"], d.name)
                self.assertRegex(d.name, r"^[a-z0-9]+(-[a-z0-9]+)*$")
                self.assertRegex(meta["num"], r"^\d{2}$")
                self.assertIn(meta["category_en"], CATEGORIES)
                self.assertEqual(meta["status"], "draft")
                self.assertIsNone(meta["film"])
                self.assertTrue(meta["line"].startswith("Proposed demo: "))
                self.assertTrue(re.search(r"[ऀ-ॿ]", meta["hi"]), "Hindi name must be in Devanagari")
                self.assertEqual(len(meta["uses"]), 3)
                self.assertTrue(1 <= len(meta["nearest"]) <= 3)
                nums.add(meta["num"]); slugs.add(meta["slug"])
                text = (d / "STYLE.md").read_text(encoding="utf-8")
                self.assertTrue(text.startswith(f"# {meta['en']} — Style Prompt"), text[:80])
                positions = [text.find(h + "\n") for h in HEADINGS]
                self.assertNotIn(-1, positions, "missing a fixed section heading")
                self.assertEqual(positions, sorted(positions), "sections out of order")
                self.assertTrue(5_500 <= len(text.encode("utf-8")) <= 13_000, len(text.encode("utf-8")))
                self.assertIn("Status: **draft**", text)
                self.assertNotRegex(text, r"(?i)lemo ?lab ×|opus 5\.5")
        self.assertEqual(len(nums), len(dirs), "duplicate num")
        self.assertEqual(len(slugs), len(dirs))

    def test_index_is_up_to_date(self):
        result = subprocess.run([sys.executable, str(STYLES / "build_index.py"), "--check"], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
