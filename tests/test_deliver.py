"""Checks for studio/deliver.py: a finished film goes to the owner as exactly 2 files (owner rule, 2026-11-02).

Uses a SYNTHETIC FIXTURE: small placeholder files in a temporary folder, not film assets."""

import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "studio"))
import deliver as D  # noqa: E402


def fixture(root: Path) -> Path:
    final = root / "synthetic-film" / "final"
    for rel, data in {
        "synthetic-film.mp4": b"master" * 100,
        "synthetic-film_720p.mp4": b"preview",
        "synthetic-film.srt": b"1\n00:00:00,000 --> 00:00:01,000\nsynthetic\n",
        "cover.jpg": b"jpg",
        "CREDITS": b"synthetic fixture",
        "editor/README.md": b"readme",
        "editor/Synthetic.xml": b"<xmeml/>",
        "editor/media/V_picture.mp4": b"picture",
        "editor/media/VO_L1.wav": b"wav" * 50,
        "editor.partial/leftover.wav": b"half-built",
    }.items():
        p = final / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(data)
    return final


class DeliverTest(unittest.TestCase):
    def test_two_files_the_video_and_everything_else(self):
        with tempfile.TemporaryDirectory() as tmp:
            final = fixture(Path(tmp))
            film, zpath = D.deliver(final, final / "synthetic-film.mp4")
            self.assertEqual(sorted(p.name for p in (final / "deliver").iterdir()),
                             ["synthetic-film.mp4", "synthetic-film_files.zip"])
            self.assertEqual(film.read_bytes(), (final / "synthetic-film.mp4").read_bytes())
            with zipfile.ZipFile(zpath) as z:
                names = sorted(z.namelist())
                self.assertEqual(names, sorted(f"synthetic-film_files/{n}" for n in [
                    "CREDITS", "cover.jpg", "editor/README.md", "editor/Synthetic.xml", "editor/media/VO_L1.wav",
                    "editor/media/V_picture.mp4", "synthetic-film.srt"]))
                self.assertEqual(z.getinfo("synthetic-film_files/editor/media/V_picture.mp4").compress_type,
                                 zipfile.ZIP_STORED)
            film2, zpath2 = D.deliver(final, final / "synthetic-film.mp4")  # repeatable: the deliver/ folder is skipped
            with zipfile.ZipFile(zpath2) as z:
                self.assertEqual(len(z.namelist()), 7)

    def test_refuses_files_over_the_limit(self):
        with tempfile.TemporaryDirectory() as tmp:
            final = fixture(Path(tmp))
            with self.assertRaisesRegex(D.DeliveryError, "final video"):
                D.deliver(final, final / "synthetic-film.mp4", limit=100)
            with self.assertRaisesRegex(D.DeliveryError, "--crf 18"):
                D.deliver(final, final / "synthetic-film.mp4", limit=700)
            self.assertFalse(any(p.name.endswith(".partial") for p in (final / "deliver").iterdir()))

    def test_needs_the_video_and_something_to_zip(self):
        with tempfile.TemporaryDirectory() as tmp:
            final = Path(tmp) / "final"
            final.mkdir()
            with self.assertRaises(D.DeliveryError):
                D.deliver(final, final / "missing.mp4")
            (final / "film.mp4").write_bytes(b"x")
            with self.assertRaisesRegex(D.DeliveryError, "nothing to zip"):
                D.deliver(final, final / "film.mp4")


if __name__ == "__main__":
    unittest.main()
