---
name: explainer-edit
argument-hint: "[teach|make] + a long explainer sample to learn from  OR  VO/script (+ images/footage) [+ 16:9|9:16]"
description: Teach or use the Explainer Editor - long voiceover explainers of about 3, 4, 10 or 12 minutes in the style the owner teaches from sample videos. TEACH mode breaks down each sample (animation over the video, when text comes and which words become text, text colours, themes, the images that come with each theme, animation moves, infographics) and writes it into editor/styles/voiceover-explainer/. MAKE mode edits the owner's VO into an explainer in that style, with a storyboard first. Use when the owner says "explainer editor", "lambi explainer video banao", "3/4/10/12 min ki explainer", or sends a long explainer saying "isko seekho".
---

# Explainer edit

Run the **explainer-editor** agent (`.claude/agents/explainer-editor.md`) with the owner's files and words. If the session does not list it, use `general-purpose` with "Read `.claude/agents/explainer-editor.md` and act as that agent".

## 1. Pick the mode
- **Teach:** the owner sends a sample explainer. The agent follows its TEACH steps, updates `editor/styles/voiceover-explainer/` and `SAMPLES.md`, and reports what it learned under the seven headings and what is still *not seen yet*.
- **Make:** the owner sends a VO or script. The agent follows its MAKE steps, only in what the sheet has learned and the owner has approved.

## 2. Make: collect once
- The VO and the script (an owner script is locked word for word; without one, `skills/ai-writer` and approval first).
- The size (16:9 or 9:16); ask if not given.
- Any images, footage, logo, CTA and music preference.

## 3. Show, then render
- Storyboard first: send it and **stop** until the owner approves; record their words with `anim-approve`.
- Then `anim-render`, loudness check, and deliver the video plus one zip.
- Record any owner feedback with `/studio-learn` in the same turn.
