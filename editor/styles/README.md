# Learned editing styles

Each folder is one style Mann has broken down with `/mann-style-lab`:

- `STYLE_SHEET.md`: measured numbers (FFmpeg) plus Mann's observations from the frames: hook, cutting, framing, transitions, typography, motion graphics, colour, sound design, VFX, do/don't.
- `style.json`: machine-readable targets (average shot length, cuts per 10 s, first cut, grade preset, palette, loudness). An EDL with `"style": "<slug>"` is checked against them by `qc`.

No reference video or frame is committed here; those stay in `projects/_style-lab/` (git-ignored). The folder is empty until the owner shares the first reference.
