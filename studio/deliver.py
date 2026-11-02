#!/usr/bin/env python3
"""Deliver a finished film to the owner as exactly 2 files (owner rule, 2026-11-02):

  1. the final rendered video, on its own
  2. one zip with everything else in final/: the editor package, subtitles, cover, credits, QC note

    python3 studio/deliver.py projects/<slug>/final --video projects/<slug>/final/<slug>.mp4

It writes final/deliver/<video name> (a hard link, or a copy) and final/deliver/<slug>_files.zip, then prints both
paths for SendUserFile. Every subfolder of final/ goes into the zip whole (the editor package keeps its own picture,
which its timeline needs). Other video files at the top of final/, such as a 720p preview, stay out: the final video
is file 1. A file over 400 MiB, the limit for sending a file from a cloud session, is refused with what to change.
Standard library only.
"""
from __future__ import annotations

import argparse
import os
import shutil
import sys
import zipfile
from pathlib import Path

LIMIT = 400 * 1024 * 1024
VIDEO = {".mp4", ".mov", ".m4v", ".mkv", ".webm"}
ALREADY_COMPRESSED = VIDEO | {".jpg", ".jpeg", ".png", ".webp", ".zip", ".mp3", ".aac", ".m4a"}
SKIP_DIRS = {"deliver"}


class DeliveryError(ValueError):
    """Something the director must fix before the owner can get the 2 files."""


def mib(n: int) -> str:
    return f"{n / 1048576:.1f} MiB"


def files_for_zip(final: Path, video: Path) -> list[Path]:
    picked = []
    for p in sorted(final.rglob("*")):
        rel = p.relative_to(final)
        if not p.is_file() or rel.parts[0] in SKIP_DIRS or any(part.endswith((".partial", ".old")) for part in rel.parts):
            continue
        if p.resolve() == video or (len(rel.parts) == 1 and p.suffix.lower() in VIDEO):
            continue  # the final video is file 1; other top-level videos (previews) stay out
        picked.append(p)
    return picked


def deliver(final_dir, video, limit: int = LIMIT) -> tuple[Path, Path]:
    final = Path(final_dir).resolve()
    video = Path(video).resolve()
    if not final.is_dir():
        raise DeliveryError(f"not a folder: {final}")
    if not video.is_file():
        raise DeliveryError(f"final video not found: {video}")
    if video.stat().st_size > limit:
        raise DeliveryError(f"the final video is {mib(video.stat().st_size)}, over the {mib(limit)} limit: encode a "
                            f"smaller master (higher CRF) or send the 720p version as file 1 and say so")
    slug = final.parent.name if final.name == "final" else final.name
    out = final / "deliver"
    out.mkdir(exist_ok=True)

    film = out / video.name
    if film.exists():
        film.unlink()
    try:
        os.link(video, film)
    except OSError:
        shutil.copy2(video, film)

    members = files_for_zip(final, video)
    if not members:
        raise DeliveryError(f"nothing to zip in {final} besides the final video; build the editor package first")
    zpath = out / f"{slug}_files.zip"
    tmp = zpath.with_name(zpath.name + ".partial")
    try:
        with zipfile.ZipFile(tmp, "w") as z:
            for p in members:
                kind = zipfile.ZIP_STORED if p.suffix.lower() in ALREADY_COMPRESSED else zipfile.ZIP_DEFLATED
                z.write(p, f"{slug}_files/{p.relative_to(final).as_posix()}", compress_type=kind)
        size = tmp.stat().st_size
        if size > limit:
            raise DeliveryError(f"the zip is {mib(size)}, over the {mib(limit)} limit: rebuild the editor package with "
                                f"--crf 18 (or higher) so its picture is smaller")
        tmp.replace(zpath)
    finally:
        if tmp.exists():
            tmp.unlink()
    return film, zpath


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description="Deliver a finished film as 2 files: the final video, and one zip of "
                                            "everything else in final/.")
    p.add_argument("final", help="the project's final/ folder")
    p.add_argument("--video", required=True, help="the final rendered video (file 1)")
    a = p.parse_args(argv)
    try:
        film, zpath = deliver(a.final, a.video)
    except DeliveryError as e:
        print(f"deliver: {e}", file=sys.stderr)
        return 2
    for f in (film, zpath):
        print(f"{f}  ({mib(f.stat().st_size)})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
