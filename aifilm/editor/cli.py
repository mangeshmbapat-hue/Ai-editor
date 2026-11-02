"""`python3 -m aifilm.editor` (alias `mann`): Mann, the AI video editor's command line.

Flow: doctor -> ingest -> transcribe -> (Mann writes edl.json) -> storyboard -> owner approves
-> render -> qc -> owner approves the final cut. Style lab: fetch -> analyze-style -> publish-style.
"""

import argparse
import json
import sys
from pathlib import Path

from ..core import ProductionError
from . import edl as E
from . import media as M
from . import render as R
from . import style as S
from . import tools as T


def parser():
    root = argparse.ArgumentParser(prog="mann", description="Mann: AI video editor (FFmpeg, Whisper, yt-dlp, Hyperframes)")
    c = root.add_subparsers(dest="command", required=True)
    c.add_parser("doctor", help="Check which editing tools are installed")
    p = c.add_parser("ingest", help="Copy the owner's raw files into <edit>/raw and record probe + sha256")
    p.add_argument("edit")
    p.add_argument("files", nargs="+")
    p.add_argument("--link", action="store_true", help="Symlink instead of copying (large footage)")
    p = c.add_parser("transcribe", help="Whisper transcript + word-timed phone captions")
    p.add_argument("media")
    p.add_argument("out_dir")
    p.add_argument("--model", default="small")
    p.add_argument("--language", help="e.g. hi, en; omit to auto-detect")
    p.add_argument("--max-words", type=int, default=4)
    p = c.add_parser("scenes", help="List detected cuts in a video")
    p.add_argument("video")
    p.add_argument("--threshold", type=float, default=0.3)
    p = c.add_parser("validate", help="Validate <edit>/edl.json and print the timeline")
    p.add_argument("edit")
    p = c.add_parser("storyboard", help="Render numbered storyboard frames + STORYBOARD.md for the owner's approval")
    p.add_argument("edit")
    p.add_argument("--two", action="store_true", help="Two frames per clip (start and end)")
    p = c.add_parser("approve", help="Record the owner's explicit approval (their exact words)")
    p.add_argument("edit")
    p.add_argument("--words", required=True)
    p.add_argument("--final", action="store_true", help="Approve the final cut instead of the storyboard")
    p = c.add_parser("render", help="Render the approved EDL to renders/master.mp4 (+ 720p preview)")
    p.add_argument("edit")
    p.add_argument("--no-preview", action="store_true")
    p = c.add_parser("qc", help="Measure the master against the EDL, editor/rules.json and the style target")
    p.add_argument("edit")
    p.add_argument("--frames", type=float, default=1.5, help="Also export QC frames every N seconds (0 = none)")
    p = c.add_parser("fetch", help="Download a reference video with yt-dlp (for style study)")
    p.add_argument("url")
    p.add_argument("dest")
    p = c.add_parser("analyze-style", help="Break down a reference video's editing style")
    p.add_argument("video")
    p.add_argument("workdir")
    p.add_argument("--name", required=True)
    p.add_argument("--threshold", type=float, default=0.3)
    p.add_argument("--transcript", help="SRT of the reference, for speech rate")
    p = c.add_parser("publish-style", help="Save a finished STYLE_SHEET.md + targets to editor/styles/<slug>/")
    p.add_argument("workdir")
    p.add_argument("slug")
    p = c.add_parser("mg-new", help="Scaffold a Hyperframes motion-graphics composition in <edit>/mg/<name>")
    p.add_argument("edit")
    p.add_argument("name")
    p.add_argument("--resolution", default="portrait")
    p = c.add_parser("mg-render", help="Render <edit>/mg/<name> to a .mov with alpha for an overlay")
    p.add_argument("edit")
    p.add_argument("name")
    p.add_argument("--opaque", action="store_true", help="Render .mp4 without alpha")
    return root


def main(argv=None):
    args = parser().parse_args(argv)
    try:
        cmd = args.command
        if cmd == "doctor":
            result = T.doctor()
        elif cmd == "ingest":
            result = T.ingest(args.edit, args.files, args.link)
        elif cmd == "transcribe":
            result = T.transcribe(args.media, args.out_dir, args.model, args.language, args.max_words)
        elif cmd == "scenes":
            result = {"cuts": M.scene_cuts(args.video, args.threshold)}
        elif cmd == "validate":
            edl = E.load(args.edit)
            rows, total = E.timeline(edl)
            result = {"total": total, "pace": E.pace(edl), "timeline": rows, "storyboard_approved": E.approved(args.edit, edl)}
        elif cmd == "storyboard":
            rec = E.storyboard(args.edit, 2 if args.two else 1)
            result = {"storyboard": str(Path(args.edit) / "storyboard" / "STORYBOARD.md"), "frames": [f["file"] for f in rec["frames"]],
                      "pace": rec["pace"], "changes": rec["changes_since_previous"]}
        elif cmd == "approve":
            result = E.approve(args.edit, args.words, kind="final" if args.final else "storyboard")
        elif cmd == "render":
            result = R.render(args.edit, preview=not args.no_preview)
        elif cmd == "qc":
            rec = R.qc(args.edit)
            frames = R.contact_frames(args.edit, args.frames) if args.frames else []
            result = {"passed": rec["passed"], "checks": rec["checks"], "qc_frames": len(frames), "report": str(Path(args.edit) / "renders" / "QC.md")}
            print(json.dumps(result, indent=2, ensure_ascii=False))
            return 0 if rec["passed"] else 1
        elif cmd == "fetch":
            result = {"file": T.fetch(args.url, args.dest)}
        elif cmd == "analyze-style":
            a = S.analyze(args.video, args.workdir, args.name, args.threshold, args.transcript)
            result = {"draft": str(Path(args.workdir) / "STYLE_SHEET.draft.md"), "targets": S.targets(a), "frames": len(a["frames"])}
        elif cmd == "publish-style":
            result = {"saved": str(S.publish(args.workdir, R.STYLES, args.slug))}
        elif cmd == "mg-new":
            result = {"composition": T.mg_new(args.edit, args.name, args.resolution)}
        elif cmd == "mg-render":
            result = {"file": T.mg_render(args.edit, args.name, alpha=not args.opaque)}
        print(json.dumps(result, indent=2, ensure_ascii=False))
        return 0
    except ProductionError as exc:
        print("error: {}".format(exc), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
