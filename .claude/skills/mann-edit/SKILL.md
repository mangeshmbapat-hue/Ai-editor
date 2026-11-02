---
name: mann-edit
argument-hint: "[raw files or folder] [script / direction]"
description: Edit the owner's raw footage into a finished video with Mann, the AI video editor agent - ingest, transcribe, log, cut plan (EDL), storyboard of numbered frames for the owner's approval, then render with motion graphics, sound design, colour and VFX, QC and the final-cut approval. Use when the owner shares raw videos, clips or audio with a script or direction and asks to edit, cut, "video edit karo", "isko edit kro", re-edit, add motion graphics, fix sound or colour.
---

# Mann edit: raw footage to final cut

You (the main session) coordinate; the **mann** agent (`.claude/agents/mann.md`) does the editing. If the session does not list the project agents, run `general-purpose` with "Read `.claude/agents/mann.md` and act as Mann".

## Start
1. Read `studio/LEARNINGS.md` (Global, Editor, Production) and `editor/rules.json`.
2. Pick a slug and create `projects/<slug>/edit/` (git-ignored). Save the owner's script or direction verbatim in `BRIEF.md`.
3. If there is no script and the owner wants narration or dialogue written, the script goes through `skills/ai-writer` and the owner's approval first (AGENTS.md script gate). An edit of existing footage to a direction needs no new script.
4. Talk to the owner in Hinglish. Do not ask about routine choices.

## Flow

| Step | Who | Output |
|---|---|---|
| 1. Tools | Mann | `python3 -m aifilm.editor doctor`; `bash editor/install.sh` if anything is missing |
| 2. Ingest + transcribe | Mann | `media.json`, `transcripts/`, `LOG.md` (best takes and moments) |
| 3. Cut plan | Mann | `edl.json` (+ Hyperframes compositions in `mg/` if needed) |
| 4. Storyboard | Mann | `storyboard/F01_….jpg …`, `STORYBOARD.md` with pace, sound plan, change list and "Rules applied" |
| **Gate S: storyboard** | owner | explicit approval, recorded with `approve --words "<exact words>"` |
| 5. Render | Mann | `renders/master.mp4`, `renders/preview_720p.mp4` |
| 6. QC | Mann | `renders/QC.md`, `qc.json`, `qc-frames/` |
| **Gate F: final cut** | owner | `approve --final --words "<exact words>"`, or notes → back to step 3 |
| 7. Learn | you | `/studio-learn` for every correction or preference |

## Showing the storyboard
- Send the frames one by one with SendUserFile, numbered, each captioned with its timecode, clip and what happens. Never one dense contact sheet (owner rule).
- Then the compact packet: total length, shots, average shot, cuts per 10 s, grade, music/SFX plan, motion graphics, subtitles, the changes since the previous storyboard, and one `experiment` option.
- Stop. Only the owner's explicit approval opens the render. The tool enforces it: a changed EDL or source file voids the approval.

## Revisions
Change only what the owner asked. Re-run `storyboard`; its "Changes since the previous storyboard" list is what you show. Every correction is recorded with `/studio-learn` (Editor section, plus `editor/rules.json` when it is measurable) in the same turn.

## Deliver
Tell the owner, in Hinglish: where the files are (`renders/`), what QC passed, what failed and what could not be checked, and the learnings recorded. Send the 720p preview with SendUserFile. Never upload or publish.
