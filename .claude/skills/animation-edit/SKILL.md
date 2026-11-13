---
name: animation-edit
argument-hint: "[explainer|promo] [brand/product] + script or VO + logo/product images [+ look A|B|C] [+ 16:9|9:16]"
description: Make an animated brand or product video with the Animation Editor agent, in the styles the owner taught - (1) a corporate ANIMATED EXPLAINER on the owner's voiceover, where every spoken name, number, product and action appears on screen on its word, in one brand theme (look A premium dark, B flat line-art or C health-tech), with soft whole-product cutouts, cartoon face badges, circle wipes and no text on any image (the McDonald's explainer is the reference); or (2) a short PRODUCT PROMO reel of app UI, icons and text. Use when the owner says "animation editor", "explainer banao", "animation video banao", "product promo banao", "brand ki story animate karo", or sends a script/VO with a logo and product images.
---

# Animation edit

Run the **animation-editor** agent (`.claude/agents/animation-editor.md`) with the owner's files and words. If the session does not list it, use `general-purpose` with "Read `.claude/agents/animation-editor.md` and act as that agent".

## 1. Pick the kind
- **Explainer:** the owner gives a script or a VO about a brand, product or story. Follow the agent's **Explainer** process. The style is `editor/product-styles/animated-explainer/STYLE_SHEET.md`. The reference standard is the McDonald's explainer (studio/LEARNINGS.md, 2026-11-13).
- **Promo reel:** the owner gives a product name, a brand colour and lines, with no VO. Follow the agent's **Promo** process (`editor/styles/animation-product-promo/`).
- **A product category** (makeup, food, fashion, cars): use only the category's sheet in `editor/product-styles/`. If it is `not learned`, say so in one line and ask for 3–4 sample ads.

## 2. Collect, once
- The script or VO, the logo, the product images (whole single products; PNG is best) and the people (photos, or cartoon badges are made).
- The look (A, B or C; pick one from the brand's colours when the owner leaves it open) and the size (16:9 by default, or 9:16).
- The music (otherwise compose an original bed) and the CTA or handle.
- Ask once for anything missing. A script the owner wrote is locked word for word. Without a script, the words go through `skills/ai-writer` and need the owner's approval first.

## 3. Build, check and show
- Make the word-by-word plan, the soft cutouts, the composition, the **text-over-image check** and a self-check of the motion.
- Then the **storyboard**: one frame per spoken beat. Send it and **stop** until the owner approves. Record their words with `anim-approve`.

## 4. Render and deliver
- `anim-render` with the VO and music mix. Check the loudness and compare the frames with the storyboard.
- Send exactly 2 files: the video, and one zip with everything else. If a send fails, say so and send again.
- Record any owner feedback with `/studio-learn` in the same turn.
