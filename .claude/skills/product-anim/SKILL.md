---
name: product-anim
argument-hint: "[teach|make] + category (food, drinks, makeup, electronics, furniture, automobile) + sample videos OR product photos and script"
description: Teach or use the Product Animator - product hero animations where the physical product is the star, each category in its own style learned from the owner's samples. Food (a burger opening layer by layer, a bottle that turns, uncaps and shows its mango shake), makeup and personal care (face wash with water splashes and how it is used), electronics (phone, headphones, watch with every feature zoomed and explained), furniture, automobiles. TEACH mode breaks the owner's sample videos down frame by frame into the category's sheet; MAKE mode makes a video only in a taught and approved category, with a storyboard first. Use when the owner says "product animation", "product video banao", "khane ki / makeup ki / phone ki video", or sends product ads to learn from.
---

# Product animation

Run the **product-animator** agent (`.claude/agents/product-animator.md`) with the owner's files and words. If the session does not list it, use `general-purpose` with "Read `.claude/agents/product-animator.md` and act as that agent".

## 1. Pick the mode and the category
- **Teach:** the owner sends sample videos. Find the category in `editor/product-styles/LIBRARY.json` (add one if it is new). The agent follows its TEACH steps and reports back what each sample taught.
- **Make:** the owner asks for a product video. If the category is `not learned`, say so and ask for samples.

## 2. Teach: for each sample
- Save it in `projects/_product-train/<category>/s<N>/` (git-ignored).
- Measure it, then go frame by frame: reveal, camera, feature moves (open, layers, zooms, splashes), light, colours, text, transitions, pace, end card, sound.
- Say how each move can be made with our pipeline, and which needs a tool we do not have.
- Fill the category sheet, show the owner the breakdown with key frames, and wait for their approval before the status changes.

## 3. Make
- Collect the product photos (every side, open, inside, each feature), the logo, the script or VO, the size (9:16 or 16:9) and the CTA.
- Plan, cut out, compose, self-check, then the **storyboard**. Send it and **stop** until the owner approves; record their words with `anim-approve`.
- `anim-render`, check loudness and frames, and send exactly 2 files: the video and one zip.

Record every owner correction or preference with `/studio-learn` in the same turn.
