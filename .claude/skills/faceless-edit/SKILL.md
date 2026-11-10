---
name: faceless-edit
argument-hint: "[voiceover + images/clips] [CTA]"
description: Make a faceless video with the Faceless Editor agent - the owner's voiceover plus images, AI clips or footage, edited in the house style learned from the owner's 4 samples (moving stills and paper collage, kinetic text on every number, date and name, seamless transitions, hook text in 1 s, end card with the owner's CTA). Use when the owner says "faceless video banao", sends a VO with images or clips for a faceless edit, or names the Faceless Editor.
---

# Faceless edit

Run the **faceless-editor** agent (`.claude/agents/faceless-editor.md`) with the owner's files and words. If the session does not list it, use `general-purpose` with "Read `.claude/agents/faceless-editor.md` and act as that agent".

1. Collect the VO, the visuals and the **end-card CTA for this video**. Ask once for whatever is missing. Without a VO or script, the script goes through `skills/ai-writer` and needs the owner's approval first.
2. The agent follows its process: ingest, transcribe, `faceless-stills`, `faceless-plan`, hand refinement, storyboard.
   Before the storyboard, check the agent's **Owner rules checklist**:
   - subtitles only on request
   - quiet SFX and music under the VO
   - no shake
   - people with faces and no white borders
   - the owner's social logos
3. **Stop at the storyboard.** Show the numbered frames and wait for the owner's explicit approval before the render.
4. After QC, send exactly 2 files: the video, and one zip with everything else.
5. Record any owner feedback with `/studio-learn` in the same turn.
