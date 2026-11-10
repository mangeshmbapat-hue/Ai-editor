---
name: animation-edit
argument-hint: "[product name + brand colour] [screens/PNG icons] [lines] [handle]"
description: Make a commercial product-promo animation reel with the Animation Editor agent, in the house style learned from the owner's 4 samples - one matched colour theme per product, white or glass cards, PNG icons that pop and orbit, a cursor tap on the CTA, ring-pulse and blur-through transitions, word-by-word text with glowing accent words, and a black end card with a white glowing wordmark. Use when the owner says "animation reel banao", "product promo banao", "app ki animation video", sends product screens or icons for a promo, or names the Animation Editor.
---

# Animation edit

Run the **animation-editor** agent (`.claude/agents/animation-editor.md`) with the owner's files and words. If the session does not list it, use `general-purpose` with "Read `.claude/agents/animation-editor.md` and act as that agent".

1. Collect the product name and brand colour, the screens or PNG icons, the lines, and the **end-card handle or CTA for this video**. Ask once for whatever is missing. Without lines, the words go through `skills/ai-writer` and need the owner's approval first.
2. The agent follows its process: ingest, theme, `spec.json`, `anim-new`, a frame-by-frame self-check, then `anim-storyboard`.
3. **Stop at the storyboard.** Show the numbered frames and wait for the owner's explicit approval. Record it with `anim-approve --words`, then `anim-render`.
4. After the render, send exactly 2 files: the video, and one zip with everything else.
5. Record any owner feedback with `/studio-learn` in the same turn.
