# Product style: Animated explainer (corporate SaaS motion graphics)

Status: **breakdown done, waiting for the owner's approval** (2026-11-13). Learned from 1 sample the owner called the best animation sample: a 52 s product explainer for an AI product-management tool. The file stays in the git-ignored `projects/_product-train/explainer-collato/` as study material. **Learn the style, never the sample's brand, logo, script, characters, UI or music.**

How it was studied: 1 fps and 4 fps frame sheets of the whole video, full-resolution stills for fonts and colours, OpenCV colour sampling, FFmpeg loudness, silence and cut detection, and word timings from offline speech recognition (pocketsphinx). The recognition was rough, so the script below was **reconstructed** by matching it to the on-screen text. Its word times are good to about 0.2 s; some words are my reading and are marked (?). The sound was measured, not heard.

## What the owner asked me to notice (owner's words, 2026-11-13)
- Whatever is said arrives on screen at that moment, as text or as a visual, and animates right then: people's icons with faces when people are named, a globe when "globe" is said, the logo and then the logo's name, stars when "five star" is said.
- When text comes in and when the font changes.
- The colour theme: purple sometimes, white sometimes, but the theme is never left. No random colours. The look must be professional and corporate.
- The whole video: text, font, background, what animates when, and what is said on which line.

## Measured
| | Value |
|---|---|
| Format | 1920×1080 (16:9), 25 fps, 52.0 s |
| Hard cuts | **0** (the scene detector found none: every change is a wipe, a camera move or a morph) |
| Voice | starts at 0.1 s and runs nearly without a gap to 49.0 s, about 2.6 words per second |
| Loudness | −19.1 LUFS, LRA 3.1 LU, peak −3.6 dBFS (calm VO plus a soft bed) |
| Ending | silence for the last 2.1 s (49.98 → 52.1 s) on the held CTA |
| Dark ground | radial purple: deep `#150728` corners, body `#3d1f6c`–`#4b247e`, a lighter `#5c329a`–`#6b39b8` glow behind the subject |
| Light ground | off-white `#f8f8f8`, white cards `#fefefe`, soft lilac shadows `#dfd8e3` |
| Text | white on purple, dark slate `#49475f` on white, grey `#908f9b` for UI text |
| Accents | purples `#622caf`, `#7842ae`, lilac `#b668df`/`#c184e1` (buttons), CTA purple `#654db3` |
| Brand gradient | violet `#7b5cf5` → pink `#f2788a` → peach `#f6b38e`, **only** on the logo, its orb and the wordmark |

## The theme rule (why it looks corporate)
1. **Two grounds, one family:** deep purple scenes and off-white scenes alternate. The rhythm is dark 0–14 s, white 14–17.5, dark 17.5–23.3, white 23.3–28, dark 28–46, white 46–52. The switch always comes through a wipe in the theme's own colours.
2. **Every colour on screen comes from the brand:** purples, lilac, white, slate and grey. The warm pink and peach appear only inside the brand gradient (the logo, the glowing orb, the wordmark). Real product icons (Docs, Sheets, PDF, Figma, Jira, Notion) keep their own small colours, and that is the only exception.
3. **One type family**, a bold geometric sans (it reads like Gilroy or Gordita; the closest open fonts are Plus Jakarta Sans and Outfit). Headlines are bold, sentence case, white or slate, usually 2 lines. UI text uses the same family at small sizes. The "font change" is **weight and size**, not a new typeface.
4. **Soft depth:** cards float with large soft shadows, the dark scenes have a vignette and light glows, and glass and neon edges appear on hero UI (the timer card).
5. **Faces are real photos in round badges** (a thin white ring, sometimes three small stars above them), never cartoons.

## Line-by-line: what is said, what appears, what moves
| Time (s) | Spoken (reconstructed) | On screen at that moment | Motion |
|---|---|---|---|
| 0.1–1.1 | "As a **product manager**," | a laptop with typing hands and app windows on purple; a pill badge with a real face and **"Product Manager"** | the windows fly in tilted in 3D; the badge pops in at 0.5 s, 0.15 s before the words |
| 1.6–2.9 | "your goal is to **make an impact**." | the headline **"Make an impact"** (2 lines, white bold), and a curved peach line that draws around the laptop | the headline slides in at 2.0 s, on "goal is to", about 0.4 s before "make"; the line draws for 1 s |
| 3.4–5.6 | "But **tedious chores** like **getting updates**" | the camera flies off the laptop into a dark space full of floating DOC, PDF, PRD, Sheets and calendar cards and task lists | at 3.5–4.0 s the scene tilts and recedes; cards fly in with parallax, 0.1 s apart, about 0.3 s before "tedious" |
| 5.7–8.2 | "and **endless documentation**, they eat up most of your day (?)." | more documents pile up (PDF Requirements, PRD) | slow drift; the pile grows on "documentation" |
| 8.2–8.7 | — | everything sweeps out to the left | a fast push with motion blur |
| 9.0–13.1 | "**Imagine** having more time to focus on the parts of your job you actually enjoy." | a rising area chart; **people's face badges with 3 stars** pop up one by one along it; a glowing brand orb travels along the curve | the chart grows from left to right on "imagine"; a badge every 0.5 s; the orb rolls from 11 s to 13.8 s |
| 13.9–15.5 | "Introducing **Collato** (the product name)," | white ground; the orb becomes the **logomark**, then the **wordmark** slides out of it | white wipe at 14.0 s; mark at 14.25 s; the name reveals at 15.0–15.5 s, landing on the spoken name (15.2 s) |
| 15.8–17.5 | "the **AI assistant for product teams**." | the logo moves up; the tagline in 2 lines; an "Ask anything" input with an **Ask** button; a cursor | the tagline lands on "AI assistant"; the input rises with a soft shadow |
| 17.5–19.3 | "What used to take **hours**" | a purple wave wipes from the right; a neon-edged **timer card "4 hr 35 min 58 sec"** that ticks | the wave lasts 0.7 s; the timer counts up live |
| 19.3–20.8 | "will take **seconds**." | a magic wand with sparkles hits the timer, and it drops to **"0 hr 0 min 01 sec" → "03 sec"** | the wand swings at 18.5–19.5 s; the hours and minutes dim; the seconds tick on "seconds" (19.8 s) |
| 20.8–22.5 | "**Connect your tools**" | tool icons in a column on the left (Notion, Jira, Docs, Confluence, Figma); a settings panel with checkboxes; a Connect button that the cursor clicks; a wireframe **brain** in a circle | the icons stagger in from the left; the checkboxes tick; the click lands about 21.7 s |
| 21.8–23.2 | "and **let Collato handle the rest**." | the tool icons fly into the brain, and its nodes light up as a network | the icons arc into the brain at 22.5–23.2 s |
| 23.3–25.0 | "**Need to draft release notes**," | a white wave rises from the bottom; the headline **"Need to draft release notes?"**; the input types "Draft a release note for …" | the wave at 23.3 s; typing letter by letter about 0.07 s per character |
| 25.1–27.0 | "**a requirements doc, or a help article**?" | the headline swaps to **"a requirements doc, or a help article?"**; typing continues | the old line fades up and the new one fades in on "requirements" |
| 27.0–28.0 | "**Just ask Collato**." | the camera zooms into the input (about 2×), **"Just ask Collato"**, and the cursor clicks **Ask** | the zoom from 26.75 s; the click on "ask" (27.7 s) and the button presses |
| 28.0–30.9 | "Collato goes through **hundreds of sources** (?)" | a purple ground; the generated **release-note card** with a list of sources rises | the card rises at 28.25–28.75 s; the cursor hovers over the sources |
| 31.0–34.6 | "like **Confluence pages**, Figma files, **notes** and **Jira tickets**" | source cards fly in from the right, each with the named tool's icon (Technical specifications, Communications plan, Epic: Tagging feature) | **one card per named source, on its word**, staggered about 1 s |
| 35.2–36.9 | "or **wherever you store your product knowledge**." | the cards fan out into a collage (Competitor analysis, Design specifications, …) | the cards spread out, then all blur away at 36.5 s |
| 37.4–39.0 | "With Collato **by your side**," | a glowing brand **orb**, then the logomark on deep purple | the orb grows from a point with a soft glow |
| 39.5–41.0 | "you can **focus on what matters most**:" | **"Focus on what matters most"** slides out to the right of the mark | it lands on "focus" (39.75 s) |
| 41.4–42.9 | "**shaping your product**," | a brain in a circle sits on a "plug" with the logo (a product lightbulb); the title **"Shaping your product"**; face badges orbit | the title lands on "shaping"; the badges pop in one by one |
| 43.0–44.2 | "**guiding your team**," | the title swaps to **"Guiding your team"**; the badges link with arrows | the title crossfades on the word |
| 44.3–46.0 | "and **making an impact**." | **"Making an impact"**; the arrows pass between the people | the title crossfades on the word |
| 46.0–48.0 | "Visit **collato.com**" | a white wave from the bottom; the orb drops in; a URL pill types **"collato.com"**; the wordmark reveals | the URL types on "dot com" (47.4 s) |
| 48.1–52.0 | "and **start for free today**." | the URL pill morphs into the CTA button **"Start for free today"** under the logo | the morph on "start" (48.1 s); a still hold, and silence from 50 s |

## Timing rules (from the table)
- **Every named thing appears on its word.** Visuals and scene changes arrive **0.1–0.4 s before** the word, so the picture is ready when it is said. Headlines land **on** their keyword and swap phrase by phrase.
- People named → real **face badges** (round, white ring, sometimes stars). A tool or app named → its **real icon**. A time or number said → a **live counter**. An action said ("ask", "connect") → a **cursor clicks** it on the word. The brand said → the **logo and then the name**.
- There is **one idea per beat of 1.5–3 s**; nothing sits still for more than about 3 s.
- **No hard cuts.** The changes are colour waves (purple from the side, white from the bottom), camera fly-throughs, zooms into the UI, and morphs (orb → logo, URL → button).

## Motion language
- Eases are smooth and expensive: a long `power3/expo.out`, no bounce on the text, and a gentle overshoot only on the badges and icons.
- The camera is always moving slowly (drift and push), with parallax between the layers in the 3D card scenes.
- Text slides in a short way with a fade (it never pops), line by line.
- Glows are soft: the brand orb, the neon edge on the timer, the sparkles on the wand.

## Sound (measured, not heard)
- A calm, clear voiceover at about 2.6 words per second over a soft bed, about −19 LUFS here. For our reels we deliver −14 LUFS with a −1 dBTP ceiling.
- The ending is silent for 2 s on the CTA.

## What this means for our videos
- Script first (VO or text). Mark **every noun and action** in it and give each one a visual on its word.
- Pick **one brand theme** (dark ground + light ground + accents + one brand gradient) and use nothing outside it.
- Use 16:9 as in the sample, or 9:16 for reels with the same rules.

## Brand styles in this category
_None yet._

## Rules from the owner's corrections
_None yet._
