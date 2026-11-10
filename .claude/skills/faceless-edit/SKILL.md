---
name: faceless-edit
argument-hint: "[voiceover + images/clips] [CTA]"
description: Make a faceless video with the Faceless Editor agent - the owner's voiceover plus images, AI clips or footage, edited in the house style learned from the owner's 4 samples (moving stills and paper collage, kinetic text on every number, date and name, seamless transitions, hook text in 1 s, end card with the owner's CTA). Use when the owner says "faceless video banao", sends a VO with images or clips for a faceless edit, or names the Faceless Editor.
---

# Faceless edit

Run the **faceless-editor** agent (`.claude/agents/faceless-editor.md`) with the owner's files and words. If the session does not list it, use `general-purpose` with "Read `.claude/agents/faceless-editor.md` and act as that agent".

1. **A VO arrived? Start at once, with no questions and no updates** (owner rule 2026-11-10). The agent's **Fast path** applies:
   - the VO is the locked script
   - the house style is already approved
   - music is your choice
   - the CTA only if the owner gave one

   Only a topic with no VO goes through `skills/ai-writer` and the owner's script approval first.
2. The agent follows its process: ingest, transcribe, `faceless-stills`, `faceless-plan`, hand refinement, storyboard.
   Before the storyboard, check the agent's **Owner rules checklist**:
   - subtitles only on request
   - quiet SFX and music under the VO
   - no shake
   - people with faces and no white borders
   - the owner's social logos
3. **Stop at the storyboard.** Send the numbered frames and nothing else.
   - **OK:** record it, then render, run QC and deliver at once.
   - **Changes:** apply them and show only the changed frames.
4. After QC, send exactly 2 files: the video, and one zip with everything else.
5. Record any owner feedback with `/studio-learn` in the same turn.
