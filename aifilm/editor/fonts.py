"""Open-licensed fonts for Mann: fetched from the npm registry (@fontsource/<family>), merged
into one TTF per weight (Latin + Latin-ext + Devanagari, so mixed Hindi/English text renders
with a single font file in FFmpeg drawtext), and installed where fontconfig finds them (libass
subtitles and Chromium/Hyperframes use the same files).

Needs `npm` and the `fonttools` Python package (installed by editor/install.sh)."""

import os
import re
import shutil
import subprocess
import tarfile
import tempfile
from pathlib import Path

from ..core import now, read_json, require, write_json

SUBSETS = ("latin", "latin-ext", "devanagari")


def font_dir():
    return Path(os.environ.get("MANN_FONTS") or Path.home() / ".local" / "share" / "fonts" / "mann")


def slug(family):
    return re.sub(r"[^a-z0-9]+", "-", family.lower()).strip("-")


def file_name(family, weight):
    return "{}-{}.ttf".format(family.replace(" ", ""), int(weight))


def installed(family, weight):
    path = font_dir() / file_name(family, weight)
    return path if path.exists() else None


def install(family, weights=(400, 700)):
    """Install `family` (e.g. "Poppins", "Tiro Devanagari Hindi") at the given weights."""
    require(shutil.which("npm") is not None, "npm is required to fetch fonts")
    try:
        from fontTools.merge import Merger
        from fontTools.ttLib import TTFont
    except ImportError as exc:
        raise ImportError("fonttools is required: python3 -m pip install fonttools") from exc
    dest = font_dir()
    dest.mkdir(parents=True, exist_ok=True)
    done = []
    with tempfile.TemporaryDirectory() as tmp:
        packed = subprocess.run(["npm", "pack", "@fontsource/" + slug(family), "--silent"], cwd=tmp, capture_output=True, text=True, timeout=600)
        require(packed.returncode == 0, "npm could not fetch @fontsource/{}: {}".format(slug(family), packed.stderr.strip()[-300:]))
        with tarfile.open(Path(tmp) / packed.stdout.strip().splitlines()[-1]) as tar:
            try:
                tar.extractall(tmp, filter="data")
            except TypeError:  # Python without extraction filters
                tar.extractall(tmp)
        files = Path(tmp) / "package" / "files"
        for weight in weights:
            parts = []
            for sub in SUBSETS:
                src = files / "{}-{}-{}-normal.woff".format(slug(family), sub, int(weight))
                if src.exists():
                    font = TTFont(str(src))
                    font.flavor = None
                    out = Path(tmp) / "{}-{}.ttf".format(sub, weight)
                    font.save(str(out))
                    parts.append(str(out))
            if not parts:
                continue
            target = dest / file_name(family, weight)
            if len(parts) == 1:
                shutil.copyfile(parts[0], target)
            else:
                Merger().merge(parts).save(str(target))
            done.append({"family": family, "weight": int(weight), "file": str(target),
                         "devanagari": any("devanagari" in p for p in parts)})
    require(done, "No files for {} at weights {}".format(family, list(weights)))
    if shutil.which("fc-cache"):
        subprocess.run(["fc-cache", "-f", str(dest)], capture_output=True, timeout=300)
    index = dest / "mann-fonts.json"
    log = read_json(index) if index.exists() else {"fonts": []}
    log["fonts"] = [f for f in log["fonts"] if not (f["family"] == family and f["weight"] in {d["weight"] for d in done})] + done
    log["updated"] = now()
    write_json(index, log)
    return done


def install_pairing(pairing):
    out = []
    out += install(pairing["display"], sorted({pairing.get("display_weight", 700), 400}))
    if pairing["text"] != pairing["display"]:
        out += install(pairing["text"], sorted({pairing.get("text_weight", 500), 400}))
    return out


def resolve(family, weight):
    """Best installed file for a family and weight (nearest weight), or None."""
    dest = font_dir()
    candidates = sorted(dest.glob(family.replace(" ", "") + "-*.ttf")) if dest.exists() else []
    if not candidates:
        return None
    def w(p):
        m = re.search(r"-(\d+)\.ttf$", p.name)
        return int(m.group(1)) if m else 400
    return str(min(candidates, key=lambda p: abs(w(p) - int(weight))))
