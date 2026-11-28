#!/usr/bin/env python3
"""Vox paper-cutout kit: paper grounds and torn-edge photo prints (PIL + numpy, offline).

    python3 paper.py ground <out.png> --tone cream|kraft|ink [--size 1920x1080]
    python3 paper.py print <photo> <out.png> [--width 900] [--border 14] [--seed 3] [--crop x0,y0,x1,y1]

`print` makes the house photo treatment: warm black-and-white (saturation ~0.15), a cream uneven border
(4-8 px at 864 px scale, so ~10-16 px at 1920), a rough torn outer edge and a soft paper fibre rim, as an RGBA PNG.
"""
import argparse
import numpy as np
from PIL import Image, ImageFilter, ImageOps, ImageEnhance

TONES = {"cream": (235, 229, 220), "kraft": (163, 139, 115), "ink": (35, 30, 26), "grid": (220, 205, 188)}


def noise(w, h, scale, rng):
    small = rng.random((max(2, h // scale), max(2, w // scale))).astype(np.float32)
    return np.asarray(Image.fromarray((small * 255).astype(np.uint8)).resize((w, h), Image.BICUBIC), np.float32) / 255.0


def ground(out, tone, size, seed=1):
    w, h = size
    rng = np.random.default_rng(seed)
    base = np.array(TONES[tone], np.float32)
    n = 0.55 * noise(w, h, 180, rng) + 0.3 * noise(w, h, 40, rng) + 0.15 * noise(w, h, 6, rng)
    amp = 16 if tone != "ink" else 10
    img = base[None, None, :] + (n[..., None] - 0.5) * amp
    # fibres: short faint strokes
    fib = np.zeros((h, w), np.float32)
    for _ in range(int(w * h / 2600)):
        x, y = rng.integers(0, w), rng.integers(0, h)
        L, a = rng.integers(6, 26), rng.random() * np.pi
        for t in range(L):
            xx, yy = int(x + t * np.cos(a)), int(y + t * np.sin(a))
            if 0 <= xx < w and 0 <= yy < h:
                fib[yy, xx] = 1
    fib = np.asarray(Image.fromarray((fib * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(0.6)), np.float32) / 255
    img += (fib[..., None] * (10 if tone != "ink" else 14)) * (1 if tone == "ink" else -1)
    # soft vignette
    yy, xx = np.mgrid[0:h, 0:w]
    d = np.sqrt(((xx - w / 2) / (w / 2)) ** 2 + ((yy - h / 2) / (h / 2)) ** 2)
    img *= (1 - 0.16 * np.clip(d - 0.55, 0, 1) ** 1.4)[..., None]
    Image.fromarray(np.clip(img, 0, 255).astype(np.uint8)).save(out)


def torn_mask(w, h, inset, rng, rough=1.0):
    """White inside a rectangle whose edges wobble like torn paper."""
    m = Image.new("L", (w, h), 0)
    arr = np.zeros((h, w), np.uint8)
    def edge(n):
        low = np.interp(np.arange(n), np.linspace(0, n, max(3, n // 60)), rng.random(max(3, n // 60) + 0) * 1.0 if False else rng.random(max(3, n // 60)))
        hi = rng.random(n)
        return (low * 0.7 + np.convolve(hi, np.ones(3) / 3, "same") * 0.3) * inset * rough
    top, bot, lef, rig = edge(w), edge(w), edge(h), edge(h)
    yy, xx = np.mgrid[0:h, 0:w]
    inside = (yy >= top[xx]) & (yy <= h - 1 - bot[xx]) & (xx >= lef[yy]) & (xx <= w - 1 - rig[yy])
    arr[inside] = 255
    return Image.fromarray(arr).filter(ImageFilter.GaussianBlur(0.7))


def make_print(photo, out, width=900, border=14, seed=3, crop=None, contrast=1.12):
    rng = np.random.default_rng(seed)
    im = Image.open(photo).convert("RGB")
    if crop:
        im = im.crop(crop)
    im = im.resize((width, int(im.height * width / im.width)), Image.LANCZOS)
    g = ImageOps.grayscale(im)
    g = ImageOps.autocontrast(g, cutoff=1)
    g = ImageEnhance.Contrast(g).enhance(contrast)
    a = np.asarray(g, np.float32) / 255
    warm = np.stack([a * 255 * 1.0 + 10 * (1 - a), a * 246 + 6 * (1 - a), a * 228 + 2 * (1 - a)], -1)  # warm B&W
    photo_rgb = Image.fromarray(np.clip(warm, 0, 255).astype(np.uint8))
    W, H = width + 2 * border, photo_rgb.height + 2 * border
    canvas = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    cream = Image.new("RGBA", (W, H), (238, 231, 218, 255))
    outer = torn_mask(W, H, border * 0.75, rng, 1.0)
    canvas.paste(cream, (0, 0), outer)
    inner = torn_mask(width, photo_rgb.height, border * 0.35, rng, 0.8)
    canvas.paste(photo_rgb.convert("RGBA"), (border, border), inner)
    canvas.save(out)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    g = sub.add_parser("ground"); g.add_argument("out"); g.add_argument("--tone", default="cream"); g.add_argument("--size", default="1920x1080"); g.add_argument("--seed", type=int, default=1)
    p = sub.add_parser("print"); p.add_argument("photo"); p.add_argument("out"); p.add_argument("--width", type=int, default=900)
    p.add_argument("--border", type=int, default=14); p.add_argument("--seed", type=int, default=3); p.add_argument("--crop")
    a = ap.parse_args()
    if a.cmd == "ground":
        ground(a.out, a.tone, tuple(map(int, a.size.split("x"))), a.seed)
    else:
        make_print(a.photo, a.out, a.width, a.border, a.seed, tuple(map(int, a.crop.split(","))) if a.crop else None)
