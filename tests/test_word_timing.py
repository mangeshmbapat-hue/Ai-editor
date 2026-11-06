"""Checks for studio/word_timing.py, the offline word aligner.

Everything here uses SYNTHETIC FIXTURES: tone "words" with their own spectra stand in for speech, so the tests need only
numpy and no voice model. The measured accuracy on real Kokoro speech is recorded in studio/SKILL_HARNESS.md."""

import sys
import unittest
import zlib
from pathlib import Path

try:
    import numpy as np
except ImportError:  # the core needs numpy; without it there is nothing to test
    np = None

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "studio"))


def tone_word(word: str, dur: float, sr: int) -> "np.ndarray":
    """A synthetic 'word': three partials chosen from the word, with a soft attack and release."""
    seed = zlib.crc32(word.encode())  # well spread, so different words get clearly different spectra
    f = [180 + seed % 220, 700 + (seed >> 8) % 900, 1800 + (seed >> 16) % 1500]
    t = np.arange(int(dur * sr)) / sr
    x = sum(np.sin(2 * np.pi * fk * t) / (k + 1) for k, fk in enumerate(f))
    env = np.minimum(1, np.minimum(t / 0.02, (dur - t) / 0.03))
    return 0.3 * x * env


@unittest.skipIf(np is None, "the word aligner needs numpy")
class WordTimingTest(unittest.TestCase):
    def setUp(self):
        import word_timing as WT
        self.WT = WT

    def test_tokenize_keeps_punctuation_on_the_shown_word(self):
        lines = self.WT.tokenize("राम, सीता और लक्ष्मण।\n\n  hello , world!\n")
        self.assertEqual(lines, [[("राम,", "राम"), ("सीता", "सीता"), ("और", "और"), ("लक्ष्मण।", "लक्ष्मण")],
                                 [("hello ,", "hello"), ("world!", "world")]])
        with self.assertRaises(SystemExit):
            self.WT.tokenize(" ।। \n")

    def test_reference_spans_are_exact_and_pause_at_punctuation(self):
        WT = self.WT
        ref, spans, line_spans = WT.build_reference(WT.tokenize("ab cd, ef\ngh"), lambda w: np.ones(int(0.1 * WT.SR)))
        n = int(0.1 * WT.SR)
        (a, b), (c, d), (e, f) = spans[0]
        self.assertEqual((b - a, d - c, f - e), (n, n, n))
        self.assertEqual(c - b, int(WT.WORD_GAP * WT.SR))
        self.assertEqual(e - d, int(WT.PUNCT_GAP * WT.SR))  # "cd," ends with a comma
        self.assertEqual(spans[1][0][0] - line_spans[0][1], int(WT.LINE_GAP * WT.SR))
        self.assertEqual(len(ref), line_spans[1][1] + int(WT.LEAD * WT.SR))

    def test_dtw_keeps_the_slope_between_half_and_double(self):
        WT = self.WT
        ref = np.repeat(np.eye(4), 10, axis=0)
        cells, _ = WT.dtw_path(ref, np.repeat(np.eye(4), 15, axis=0))
        steps = {(b[0] - a[0], b[1] - a[1]) for a, b in zip(cells, cells[1:])}
        self.assertTrue(steps <= {(1, 1), (0, 1), (1, 0)})  # cells inside a (1,2) or (2,1) step are listed one by one
        self.assertEqual([c[0] for c in cells][0], 0)
        self.assertEqual(cells[-1][0], len(ref) - 1)
        with self.assertRaises(ValueError):
            WT.dtw_path(ref, ref[:10])  # a window under half the reference cannot hold it

    def test_words_land_on_a_time_warped_recording(self):
        WT = self.WT
        text = "aa bb cc dd\nee ff gg"
        rng = np.random.default_rng(3)
        rec, truth, pos = [np.zeros(int(0.6 * WT.SR))], [], int(0.6 * WT.SR)
        for line in WT.tokenize(text):
            for _, spoken in line:
                x = tone_word(spoken, rng.uniform(0.18, 0.45), WT.SR)
                rec.append(x)
                truth.append((pos / WT.SR, (pos + len(x)) / WT.SR))
                pos += len(x)
                gap = np.zeros(int(rng.uniform(0.04, 0.15) * WT.SR))  # the pauses of normal speech
                rec.append(gap)
                pos += len(gap)
            gap = np.zeros(int(1.2 * WT.SR))
            rec.append(gap)
            pos += len(gap)
        rec = np.concatenate(rec) + rng.normal(0, 0.001, pos)
        out = WT.run(rec, text, [("tones", lambda w: tone_word(w, 0.3, WT.SR))])
        self.assertEqual([w["w"] for w in out["words"]], ["aa", "bb", "cc", "dd", "ee", "ff", "gg"])
        for w, (s, e) in zip(out["words"], truth):
            self.assertLess(abs(w["s"] - s), 0.03, w)
            self.assertLess(abs(w["e"] - e), 0.06, w)
        self.assertEqual([ln["line"] for ln in out["lines"]], [1, 2])
        self.assertFalse(any(ln["check"] for ln in out["lines"]))

    def test_speaker_pitch(self):
        WT = self.WT
        t = np.arange(int(1.0 * WT.SR)) / WT.SR
        for f0 in (120, 210):
            voiced = sum(np.sin(2 * np.pi * f0 * k * t) / k for k in range(1, 6))
            self.assertAlmostEqual(WT.speaker_pitch(voiced), f0, delta=f0 * 0.05)
        self.assertEqual(WT.speaker_pitch(np.zeros(WT.SR)), 0.0)

    def test_srt_time(self):
        self.assertEqual(self.WT.srt_time(3723.0456), "01:02:03,046")


if __name__ == "__main__":
    unittest.main()
