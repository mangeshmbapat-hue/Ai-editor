---
name: faceless-edit
argument-hint: "[voiceover MP3] [CTA] [subtitles Hindi|English]"
description: Make a faceless video with the Faceless Editor - the owner sends a voiceover (plus images or clips if they have them) and gets back a storyboard, then the video on OK. Corporate design system (one designed colour theme, clean text, glass only where it fits), real-photo cutouts with smooth varied entrances, a different text treatment per scene, no SFX, slow corporate music under the VO, subtitles only on request. Use when the owner says "faceless video banao", sends a VO for a faceless edit, or names the Faceless Editor.
---

# Faceless edit

Run the **faceless-editor** agent (`.claude/agents/faceless-editor.md`) with the owner's files and words. If the session does not list it, use `general-purpose` with "Read `.claude/agents/faceless-editor.md` and act as that agent". The agent reads `studio/LEARNINGS.md` first, and the newest owner rule wins. Everything below is the owner's standing rules, in one place.

## 1. Fast path (owner, 2026-11-10)
- **A VO arrives: start at once.**
  - Ask nothing and write no progress updates.
  - The VO is the locked script, so there is no script step.
  - Only a topic with no VO goes through `skills/ai-writer` and the owner's script approval first.
- **Style:** the house style is already approved. Record it with `approve-style <edit> faceless-collage-explainer --words "badlne hatane jesa kch nhi h (house style approved 2026-11-09)"`.
- **Language:** whatever the VO is (Hindi, English or Hinglish).
- **Music:** your own choice: a slow, soft, corporate bed.
- **CTA:** use the owner's CTA if given; otherwise make a clean end card and invent no handle.
- **Subtitles:** only when the owner asks for them (Hindi or English): `faceless-plan --captions`.
- **Target:** the storyboard reaches the owner within about 15 minutes.

## 2. Look: think like a designer (owner, 2026-11-13)
- **Theme:** one designed theme per video from `editor/faceless/palettes.json`, chosen by the topic's mood (`faceless-themes` lists them):
  - navy-ivory: business, the default
  - graphite-crimson: news and crime
  - mono-silver: history and courts
  - teal-sand: health and education
  - plum-rose: lifestyle
  - forest-gold: money and gold
  - midnight-electric: tech and AI
  - ivory-navy-light: reports

  Each follows 60-30-10: a deep base gradient, glass surfaces in the same hue, and one accent at most 10 %. Every text colour comes from the theme. Never copy the colours the owner names, and never use yellow, bokeh, paper or table backgrounds.
- **Text:**
  - clean: no outline, a soft shadow, Poppins + Hind
  - one text block per scene, at most two lines, fitted to the real font width
- **Treatments, decided per scene by what the text is:**

  | Treatment | Used for |
  |---|---|
  | `plain` | headlines and statements |
  | `emphasis` | turns and claims; the key word in the accent |
  | `tag` | dates, places, names; a solid accent label |
  | `glass` | numbers, quotes, the CTA, any text over a busy photo |
  | `bgword` | hooks; a huge faint word behind the object |

- **Variety:** never one effect everywhere. No treatment in two consecutive scenes, none in more than about a third of the scenes, and a different treatment mix in every video.
- **Layout:** an object and its text never overlap. A whole object sits high with its text below. A photo cut off at the bottom rises from the frame edge with its text on top.

## 3. Visuals: real, clean, smooth
- **Objects, animals, places and devices are real photos, never cartoons:**
  - `editor/library/stock/` first (free licences, `CREDITS.json`)
  - NASA, or Wikimedia fetched slowly, only when something is missing
  - never random Google images
  - never a real person's face
- **People** the owner does not supply may be drawn or AI figures: realistic, with visible faces of the right age and gender, generic, and without white borders.
- **Finish:** real objects get the soft 2D finish (`soft2d`, on by default): real but smooth and a little cute, never a paper cutout. Objects stay modest in size (about half the frame width).
- **Show what each sentence says** (owner, 2026-11-13):
  - Never fill a video with the same few objects; use an object at most twice per video and never back to back.
  - Abstract ideas (sizes, effects, colours, steps, before/after) get a designed demo graphic in the theme. Kinds: `faceless.design`: timeline, icons with a scale, effects (overload or clean), checklist, cards3, beforeafter, spotlight, palette, ruler. Save them as `raw/design-*.png`; they stay crisp, with no reflection.
  - Concrete things named in the VO get a real photo (a diamond for "special", gold for "luxury").
  - Drop any photo with a brand name or a messy cutout.
- **Edit variety and motion** (owner, 2026-11-13: never one template repeated):
  - Mix layouts: hero objects, text-only kinetic title cards (`raw/title-card-N.png` with a text pick), and build-ups.
  - Build-ups are `raw/build-<kind>.png` plus a `.json` of settings. Parts animate on their own times: checklist lines, cards that deal in, icons that really shrink 25 %, a moving playhead, an effect that switches from overload to clean, a journey from Beginner to Pro. Kinds are in `faceless.design_parts`.
  - Text reveals word by word.
  - Every other object scene gets a slow camera push.
  - Transitions are smooth (fade, smooth slides, circle); no dips to black.
  - No graphic, object or layout twice in one video.
- **Own text picks:** for tips and explainers, choose the key phrase of each scene yourself and pass it with `faceless-plan --texts texts.json` ({scene number: words}). The direction pass still picks the treatment.
- **Cutouts:**
  - use `cutout` / `faceless-card`; they come out hole-free and get a soft shadow and reflection
  - the cut edge never shows
  - check each one by eye, and use another image if it looks bad
- **Social media:** the owner's logos from `editor/library/social/` (Facebook, X, Instagram, WhatsApp, Snapchat). Never hearts or generic icons. TV channel logos come only from the owner (`editor/library/media/`).
- **Motion:**
  - each object enters smoothly (rise, slide-left, slide-right, pop, fade-up), holds still, and leaves smoothly
  - never the same entrance twice in a row, and never a shake
  - the image and its text land on the spoken word
  - nothing extra runs along the bottom of the frame
- **Pace:** one clearly matching visual per sentence, about 2.0–2.5 s per scene. The gap cuts stay; the owner likes them.

## 4. Sound
- **No SFX at all:** no whooshes, bells or pops.
- **Music:** only a slow, soft corporate bed under the VO, at least 14 LU under it. Run `faceless-level`.

## 5. Commands, in order
1. `ingest <edit> <files>`. Put objects in `raw/` and places in `raw/places/`.
2. `transcribe <edit>/raw/<vo> <edit>/tr --language hi|en`: start this at once, in the background.
3. `faceless-plan <edit> --voice raw/<vo> --words tr/<vo>.json --theme <id> --visuals <images in story order> [--cta "..."] [--music raw/<bed>] [--captions]`. This sets the timing, the treatments, the varied entrances and the animated scene clips.
4. Check every frame. Then run `faceless-level <edit>`, `craft-check` and `storyboard`.

## 6. The gate
- **Stop at the storyboard.** Send the numbered frames, each with its timecode and a few words, and nothing else.
- **OK** (ok, theek hai, haan, banao): record it with `approve --words`, then `render`, `qc`, and send exactly 2 files: the video, and one zip with everything else.
- **Changes:** apply them scoped (the whole video or one part), show only the changed frames, and wait for OK.
- **Learning:** record every correction or preference with `/studio-learn` in the same turn. The owner will not repeat a lesson.
