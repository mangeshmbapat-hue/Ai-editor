---
name: mann-style-lab
argument-hint: "[video URL or file] [style name]"
description: Mann's learning lab - break down a reference video, viral edit or AI-video style into a measured editing breakdown (cut rhythm, shot lengths, pace curve, palette, grade, loudness, silences) plus Mann's frame-by-frame observations (hook, cuts, transitions, typography, motion graphics, sound design, colour, VFX), and save it as a reusable style sheet in editor/styles/. Use when the owner shares a reel, short, ad or AI video and says "is style ko samjho", "iska breakdown karo", "style sheet banao", or wants a future edit in that style.
---

# Mann style lab: learn a style, write the style sheet

The owner wants Mann to understand AI videos and editing styles, break them down, and keep a style sheet for each one. Run the **mann** agent (`.claude/agents/mann.md`) on this, or do it yourself when the job is small.

## Steps
1. **Get the reference.** A file the owner shares, or `python3 -m aifilm.editor fetch <url> projects/_style-lab/<slug>/` (yt-dlp). If the site is blocked by the network, say which host and ask the owner for the file. References are for study only; never put them in a film.
2. **Measure.** `python3 -m aifilm.editor analyze-style <video> projects/_style-lab/<slug>/ --name "<Style name>"`. Add `--transcript <srt>` (from `transcribe`) for speech rate. Lower `--threshold` (0.2) if dissolves or soft cuts are missed; raise it (0.4) for busy motion that fakes cuts.
3. **Study the frames.** Look at every frame in `frames/` (one per shot) and the timings in `analysis.json`. Watch for: the first 0.5 s and 3 s, how each cut is motivated, transitions, caption font/size/position/animation, motion graphics, colour of skin and shadows, effects, and how sound lines up with cuts (from the loudness, silences and shot timings; say plainly that you cannot hear it).
4. **Write the sheet.** Copy `STYLE_SHEET.draft.md` to `STYLE_SHEET.md` in the same folder and replace every `_Mann: …_` prompt with concrete, buildable instructions: numbers, fonts, durations, presets, Hyperframes notes. Keep the Measured section as it is. Separate facts (measured) from observations.
5. **Save it.** `python3 -m aifilm.editor publish-style projects/_style-lab/<slug>/ <slug>` writes `editor/styles/<slug>/STYLE_SHEET.md` and `style.json` (targets, no frames, no video). Commit only those two files with `editor: learn style <slug>`.
6. **Show the owner** a short breakdown in Hinglish: the 5 signature moves, the pace numbers, the palette and grade, and how Mann will use it. If the owner corrects the breakdown, fix the sheet and record the correction with `/studio-learn`.

## Using a style
Set `"style": "<slug>"` in an EDL. Mann follows the sheet's do/don't list and targets; QC compares the edit's average shot length with the style's (`style_pace_tolerance` in `editor/rules.json`).

## Comparing styles
For two or more sheets, write a side-by-side table (pace, hook, type, colour, sound, VFX) in `editor/styles/COMPARE-<a>-vs-<b>.md` when the owner asks.
