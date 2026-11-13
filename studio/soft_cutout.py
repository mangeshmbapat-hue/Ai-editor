#!/usr/bin/env python3
"""Soft, theme-friendly product cutouts for the Animation Editor (owner rules 2026-11-13: no cutout may look cut out;
soft feathered edges, a 2D finish, whole products only, no broken people).

    python3 -m pip install rembg onnxruntime opencv-python-headless scipy
    python3 studio/soft_cutout.py <photo> <out.png> [--model isnet-general-use|u2net] [--warm] [--flush right,bottom]

- removes the background (rembg; isnet-general-use is best for products, u2net for people) and keeps the largest piece
  (--keep 2 keeps the two largest, for one photo of two people standing apart, e.g. two founders)
- repaints the edge fringe from the inside, so no light or dark halo from the old background
- a light edge-preserving smoothing for the soft 2D look, then a feathered alpha
- --warm: a brown-to-cream duotone for old black-and-white photos so they sit in a warm theme
- --flush: sides that stay hard because they will sit flush against the frame edge (a person cut at the shoulders)
It never splits a group photo into pieces: use whole products only (ask the owner for single-product images).
"""
import argparse

import cv2
import numpy as np
from PIL import Image
from scipy import ndimage


def crop(a, thr=8):
    ys, xs = np.where(a[..., 3] > thr)
    return a[ys.min():ys.max() + 1, xs.min():xs.max() + 1]


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("src"); ap.add_argument("out")
    ap.add_argument("--model", default="isnet-general-use")
    ap.add_argument("--warm", action="store_true")
    ap.add_argument("--flush", default="")
    ap.add_argument("--keep", type=int, default=1, help="how many of the largest pieces to keep (2 for two people in one photo)")
    ap.add_argument("--size", type=int, default=900, help="upscale so the longest side is at least this")
    a = ap.parse_args(argv)
    from rembg import new_session, remove
    rgba = np.array(remove(Image.open(a.src).convert("RGB"), session=new_session(a.model)))
    m = rgba[..., 3] > 30
    lab, n = ndimage.label(m)
    if n > 1:
        sizes = ndimage.sum(m, lab, range(1, n + 1))
        keep = np.isin(lab, np.argsort(sizes)[::-1][:max(1, a.keep)] + 1)
        rgba[..., 3] = np.where(ndimage.binary_dilation(keep, iterations=3), rgba[..., 3], 0)
    x = crop(rgba, 40)
    h, w = x.shape[:2]; k = max(1.0, a.size / max(h, w))
    x = cv2.resize(x, (int(w * k), int(h * k)), interpolation=cv2.INTER_LANCZOS4)
    p = 30; x = cv2.copyMakeBorder(x, p, p, p, p, cv2.BORDER_CONSTANT, value=(0, 0, 0, 0))
    bgr = cv2.cvtColor(np.ascontiguousarray(x[..., :3]), cv2.COLOR_RGB2BGR); al = x[..., 3].astype(np.float32) / 255
    solid = (al > 0.85).astype(np.uint8)
    bgr = cv2.inpaint(bgr, (1 - solid) * 255, 5, cv2.INPAINT_TELEA)
    bgr = cv2.addWeighted(bgr, 0.5, cv2.edgePreservingFilter(bgr, flags=1, sigma_s=35, sigma_r=0.28), 0.5, 0)
    if a.warm:
        g = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY).astype(np.float32) / 255
        lo = np.array([24, 20, 60], np.float32); hi = np.array([226, 246, 255], np.float32)
        bgr = (lo + (hi - lo) * g[..., None]).clip(0, 255).astype(np.uint8)
    mm = cv2.erode((al > 0.5).astype(np.uint8) * 255, np.ones((5, 5), np.uint8))
    r = max(3, int(min(x.shape[:2]) * 0.007))
    mm = cv2.GaussianBlur(mm, (r * 2 + 1, r * 2 + 1), 0)
    out = crop(np.dstack([cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB), mm]))
    for side in filter(None, a.flush.split(",")):
        if side == "right": out = out[:, :-r - p // 2]
        if side == "bottom": out = out[:-r - p // 2]
        if side == "left": out = out[:, r + p // 2:]
    Image.fromarray(out).save(a.out)
    print(a.out, out.shape[1], "x", out.shape[0])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
