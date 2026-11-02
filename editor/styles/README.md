# Editing style library

`INDEX.md` lists **50 publicly known editing styles** in five families (social, cinematic, documentary, music, experimental). Each folder has:

- `STYLE_SHEET.md`: hook, structure, cutting, camera, transitions, typography, motion graphics, colour, sound design, VFX, signature moves, what to avoid, unique twists, the footage it fits and the engine defaults.
- `style.json`: targets (average shot, cuts per 10 s, first cut, grade) and the `edl_defaults` that `autocut --style <slug>` applies. `qc` compares an edit's pace with these targets.

The source of truth is `catalog.json`; regenerate the sheets with `python3 editor/styles/build_styles.py`. Catalog pace numbers are **estimates** from public craft knowledge, not measurements. When the owner shares a reference, `/mann-style-lab` measures it and `publish-style` writes a `"measured": true` sheet that the build script never overwrites.

`known_from` names public examples for study only. No reference video or frame is committed here; those stay in `projects/_style-lab/` (git-ignored).
