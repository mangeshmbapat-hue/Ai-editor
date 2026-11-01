# Manga Screentone — Style Prompt

> Black-and-white comic printing set in motion: pressure-tapered pen ink, mechanical dot tones cut to shape, speed and focus lines, and a page whose panel borders are the cuts.
> References (grammar only): post-war Japanese story manga and 1960s–70s gekiga for panel-to-panel cutting and ink weight; 1970s shōjo manga for borderless panels, flower and sparkle tones and floating monologue; adhesive-tone practice (cut, burnish, scrape) for the texture; limited-animation TV adaptations for pans across held drawings and impact frames. Never copy a character, layout, sound-effect lettering or series logo, and never name them in the film.

## 1. Essence, and what it is not

- **Two values on the plate: ink and paper.** Every grey is a dot screen at a fixed pitch and angle, never an opacity, blur or gradient fill.
- **Tones are cut, not shaded**: a patch has a knife edge; highlights are **scraped out** as white strokes; a gradient is a gradation tone (dot size ramps).
- **Speed lines and focus lines** replace camera motion and blur.
- **The page is the editor.** Panels with white gutters frame the shots; the camera reads them in order; a border is a cut.
- **Hand-lettered sound effects** live inside the art, crossing borders.

Not Halftone Dossier (no cream archive paper, coloured inks or stamps; tones are sheets cut to regions, not one screen over everything), not 1980s Cel Anime (no colour cels, no CRT), not Ink Wash (no brush gradation), and not a threshold filter over 3D renders: lines and tones are designed region by region.

## 2. Materials & rendering

- **Paper**: print white, faint grain, offset ink spread (dilate blacks 1 px, blur 0.5 px, re-threshold).
- **Pen**: Catmull-Rom centrelines as variable-width ribbons with a pressure curve (thin entry, swell, flicked exit), 1.5–7 px at 1080p; 1 px fine pen for hair and backgrounds. Hatching in tapered parallel sets, cross-hatch only in deep shadow; solid blacks as filled regions inside a pen outline.
- **Tone pass** (WebGL2): the scene paints a **tone-ID canvas** (region = index into a tone table); the shader thresholds `length(fract(R(θ)·p/pitch) − .5)` against a radius from the level, anti-aliased over 1 px. Kinds: flat dot tones 10–60 % (pitch 5–8 px, 45°), gradation tones, line tones, sand tone, pattern tiles (sparkles, flowers, storm streaks) drawn once at load.
- **Anchoring**: background tones are fixed to the panel; pitch never scales with a zoom. A tone on a moving figure is offset by that figure's translation per drawing (never rotated or scaled), so it travels with it.
- **Scraping**: white strokes cut with `destination-out` on the tone layer only, knife-tapered along hair and folds.
- **Effects**: speed lines (tapered, 4–9 px apart, seeded lengths), focus lines around a white void, impact bursts, smear shapes.
- **Panels**: border 3–5 px, gutters 12–24 px; panels may slant, bleed, or be broken by a figure. Each renders offscreen and is composited into the page; a final pass forces every pixel to ink or paper except 1 px edges. Everything is a function of t with seeded jitter.

## 3. Colour logic

- **No hue in story panels.** Paper → 10 % → 20–30 % → 40–60 % or line tone → solid black.
- One black mass anchors every panel; skin stays paper or 10 %; at most 2–3 tone values per panel.
- A dark tone across the upper face is an emotional signal; never put it there by accident.
- A **single spot colour** may appear only as a second ink on a title or chapter page. Example: paper `#f7f5f0`, ink `#111111`, spot red `#d7263d`.
- Example variant, newsprint: paper `#ece6d6`, ink `#1a1a1a`, heavier ink spread.

## 4. Type & subtitles

- **Speech balloons are the subtitles**: white oval, 2.5 px ink border, tail to the speaker; Comic Neue Bold 34–40 px; Devanagari in Kalam Bold or Hind SemiBold. Narration in rectangular caption boxes (Noto Serif 32–36 px). A second language sits in the same balloon under a thin rule at ~70 % size.
- **Sound effects**: Bangers or Permanent Marker outlines, distorted per glyph (rotation, scale growing toward the action, white keyline around black). Devanagari SFX: rasterise Baloo 2 ExtraBold with `fillText` and distort the bitmap, keeping the headline stroke whole.
- **Titles**: Bebas Neue or Anton, 160–320 px, filled with a gradation tone, black keyline.
- Balloons follow the reading direction and never cover faces. Hold ≥ max(1.8 s, speech + 0.6 s).

## 5. Motion quality

- 24 fps. **Characters on threes** with long holds; pans and push-ins across held panels on ones (`eio`).
- Pose → hold → pose, one smear drawing between fast keys; impacts snap with no ease.
- **Impact frame**: 2–4 frames of the inverted plate or one white flash.
- Speed lines are re-ruled every 2 frames with a new seed; ink otherwise never boils (it is print).
- Panels appear as a ruled border, then the drawing; tones are laid with a hard wipe along a knife line.
- Never moves: paper, gutters, the dot lattice relative to its panel.

## 6. Camera grammar

A reader's eye moving over a page. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Panel-to-panel cut in reading order | sequential time | a conversation; a chase; a process |
| Pan across a held wide panel | a place laid out | a city; a stadium; a valley |
| Push into a close-up as focus lines grow | emotion rising | a realisation; fear; resolve |
| Slanted panel | instability | a fall; a brawl; a crash |
| Full-page splash | the big moment | an arrival; a reveal; a scale shock |
| Eye strip (thin panel of eyes) | tension | a duel; a stare; a choice |
| Borderless bleed, floating monologue | inner voice | a memory; love; grief |
| Page turn | a jump in time or place | the next day; a flashback; a new chapter |

Framing: ≤ 4 panels on screen; push in before a panel carries dialogue. One reading direction per film (left-to-right for Latin and Devanagari). Transitions: panel cuts, page turns, impact flash, black flood; a fade is a tone ramp (dots growing), never an opacity crossfade.

## 7. Sound palette

- Music with hard transients: violins_spic, cellos_spic, piano ostinati, gran_cassa and toms, electric_guitar, electric_bass, drum_kit; a lone piano or vibraphone_bowed for a borderless memory.
- **Every drawn SFX has a sound**: whooshes = filtered-noise sweeps; impacts = kick + noise burst + low sine drop (`core/audio/sfx.py`); a drawn ellipsis = silence.
- Paper foley: page turns, pen scratch as a border is ruled, a soft burnish as a tone is laid, a knife scrape for scraped highlights.
- Silence: before a splash, hard-cut all beds; one heartbeat or breath at most.
- Voice: close, dry, acted dialogue; narration slightly roomier. Music ducked 8–10 dB; −14 LUFS.

## 8. Native moves

- **Focus-line freeze.** Focus lines snap in around a face; the background drops to white or black. *Fits content like:* a goalkeeper's decision; a student reading a result; a chef tasting the sauce.
- **Tone as weather of the mind.** The background flips to a pattern tone on an emotional beat. *Fits content like:* a first meeting; a rejection; an idea arriving.
- **Impact frame.** Inverted plate, burst and SFX for 2–4 frames. *Fits content like:* a racket strike; a slammed door; a server crash.
- **Panel break.** A figure bursts through a border into the gutter or the next panel. *Fits content like:* a runner crossing the line; a launch; a cat refusing to stay in the story.
- **Speed-line background.** The world becomes speed lines; the subject stays crisp. *Fits content like:* a cyclist downhill; a delivery rider; a falling phone.
- **Page-turn reveal.** The last panel asks; the turn answers with a splash. *Fits content like:* a product unveiled; a creature's size; a finished building.

## 9. Pitfalls of the medium

- **Moiré** → pitch ≥ 5 px at output size, never rescale a toned frame, anti-alias dot edges, never stack two dot tones at different angles.
- **Shower-door dots** under a moving figure → offset its tone lattice by its translation.
- **Grey creeping in** from blur, depth of field or crossfades → final ink/paper threshold; tone-ramp transitions.
- **Mud** → one black mass and white space per panel, 2–3 tones maximum.
- **Lost reading order** → one direction per film; balloons and panels follow it.
- **Speed lines pointing the wrong way** → parallel to the motion, sparse end trailing.
- **Panels too small at video size** → dialogue only in a panel filling ≥ 40 % of the frame.

## 10. Engine

No demo engine yet (draft). A first demo should build:
- `pen.js`: `stroke(pts, {w, taper, seed})`, hatch sets, solid fills. Start from `styles/engraving/demo/engine/burin.js` (variable-width lines in cutting order) and the affine stack of `styles/rubber-hose/demo/toon.js` (constant screen-space width).
- `tone.js`: tone-ID → dots pass, tone table `{kind, level, pitch, angle, grad, tile}`, scrape layer, per-figure lattice offsets. Start from the screens in `styles/risograph/demo/riso.js` and the pass wrapper in `styles/microgame/demo/glpass.js`.
- `fx.js`: `speedLines(rect, dir, gap, seed)`, `focusLines(cx, cy, r0, n, seed)`, `burst()`, `smear()`.
- `page.js`: panels, gutters, bleed, page turn, a reading camera `readTo(panel, t)`.
- `letter.js`: balloons, captions, SFX outlines via opentype.js as in `styles/spy-titles/demo/glyph.js`; Devanagari as `fillText` bitmaps (opentype.js does not shape conjuncts reliably).
- Seeds from `core/lib.js`; render with `core/render/still.mjs` / `video.mjs`; SFX cues via `core/render/events.mjs`; `core/render/srt.py`; music via `core/audio/sampler.py`.

## 11. Variation space

The agent decides the genre, the reading direction, panel density, the tone vocabulary, how much animates versus holds, and the cast.

- Structures: **one page, one take** (the camera reads a single dense page); **a serial** (three short chapters, each ending on a question panel); **a training montage** (the same panel repeated as the figure improves and the tones darken).
- Openings: **a colour title page** whose spot ink drains away; **an eye strip** widening into the first panel; **a blank page** on which the pen rules the first border.
- Endings: **pull back to the whole page**, every panel read at once as one image; **a final splash** frozen while its tones are laid in; **a border drawn closed** around one small figure in a field of white.

---

Status: **draft** — no demo film yet. Before this is used as a library style it needs a demo film, `DEMO.md`, stills and the checks in the Lemo-Opuscar `MAINTAINING.md` ("Gates").
