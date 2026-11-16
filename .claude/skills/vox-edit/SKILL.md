---
name: vox-edit
argument-hint: "[make|teach] + VO/script (+ images/footage) [+ 16:9|9:16]  OR  a Vox-style reference video to learn from"
description: Make a Vox-style paper-cutout explainer with the Vox Editor agent, or teach it from a new reference. In MAKE mode the owner sends a voiceover or script and gets back a storyboard, then the video on OK. The video has cream, kraft or grid paper, warm black-and-white photo cutouts with torn cream borders, one yellow key word per line on a red carrier, and red brush swipes, red ellipses and yellow highlighter boxes that land on the spoken word, in 16:9 or 9:16. In TEACH mode the owner sends a Vox-style sample, and the agent breaks it down frame by frame (VO timing, text, underlines, colour) and updates the style sheet. Use when the owner says "vox style", "vox video banao", "paper cutout explainer", "vox editor", or sends a Vox-style video saying "isko seekho / analyse karo".
---

# Vox edit

Run the **vox-editor** agent (`.claude/agents/vox-editor.md`) with the owner's files and words. If the session does not list it, use `general-purpose` with "Read `.claude/agents/vox-editor.md` and act as that agent".

## 1. Pick the mode
- **Teach:** the owner sends a reference video to learn from. The agent follows its TEACH steps, updates `editor/styles/vox-paper-cutout/` and `SAMPLES.md`, and reports back what it learned and what is still *not seen yet*.
- **Make:** the owner sends a VO or script for a new video. The agent follows its MAKE steps.

## 2. Collect, once (Make)
- The VO and the script (a script the owner wrote is locked word for word; without one, the words go through `skills/ai-writer` and need approval first).
- The size: 9:16 or 16:9. Ask if it is not given.
- Any images, footage or logo the owner has; the agent sources old engravings and public-domain props for the rest.
- The CTA or handle for the end card, and music if the owner has a preference.

## 3. Build, check and show
- Make the say-it-show-it plan, the paper cutouts, the composition and the self-checks.
- Then the **storyboard**: one frame per scene. Send it and **stop** until the owner approves. Record their words with `anim-approve`.

## 4. Render and deliver
- `anim-render` with the VO and music mix. Check the loudness and compare the frames with the storyboard.
- Send exactly 2 files: the video, and one zip with everything else.
- Record any owner feedback with `/studio-learn` in the same turn.
