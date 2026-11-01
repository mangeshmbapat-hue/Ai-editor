# Kinetic Typography — Style Prompt

> The words are the cast: the spoken text is set in type, and every word enters, acts and leaves on its own syllable, so reading and listening become one motion.
> References (grammar only): 1950s–60s film title sequences (Saul Bass and his contemporaries) for type cut to a musical cue and lines that become architecture; Futurist "words-in-freedom" pages for size as loudness and words breaking the line; concrete poetry for a word whose shape is its meaning; speech-synced motion-design pieces of the 2000s for syllable timing and a camera that travels between phrases. Never copy a title sequence, layout, logotype or typeface design.

## 1. Essence, and what it is not

- **Words are characters**: a word can be shy, heavy, late or broken; pictures, if any, are made of letters.
- **Locked to the voice**: each word lands on its spoken syllable; stress becomes size and weight.
- **One reading point**: the eye always knows where to read; past words dim or leave, future words are never visible.
- **Type as space**: lines rotate 90°, stack and become floors and walls; the camera travels across a typographic landscape.
- **Hierarchy by typography only**: size, weight, case, and one accent colour.

Not Swiss Motion Graphics (no modular-grid ethic; here words fly, squash and fall), not 60s Spy Titles (no cut-paper silhouettes or sets; the type is the whole picture), not Pictogram Motion (no pictogram cast), and not a karaoke highlight on a static block of lyrics.

## 2. Materials & rendering

- **Glyphs are geometry**: OFL fonts loaded with opentype.js; each glyph is a path with its own transform, fill, stroke progress (draw-on by dash offset) and clip. Glyph positions come from the shaped, kerned layout; animation is an offset from those rest positions, never a re-layout.
- **Word track**: `words[] = {text, t0, t1, stress, phrase}` from the voice (TTS segment boundaries refined by a forced alignment); every motion is a function of `t − t0`.
- **Devanagari** is animated per word or per akshara (grapheme clusters from `Intl.Segmenter('hi', {granularity: 'grapheme'})`), rasterised with canvas `fillText` so conjuncts and matras shape correctly; never split by code point.
- **World layout**: phrases are placed in a 2D world (or 2.5D with a three.js camera and `ShapeGeometry` text); the camera path visits phrase anchors. A baseline grid holds all resting text.
- **Surface**: flat and crisp by default; one material per film at most (paper grain, chalk, neon tube, cut metal), chosen once.
- **Blur**: directional motion blur (4–8 sub-frame samples) only during transit, zero at rest.
- Glyph paths and layouts are cached; everything else is a pure function of t.

## 3. Colour logic

- **Ground + type + one accent.** The ground is flat; the accent belongs to one class of word (the key term, the number, the second speaker) for the whole film.
- Value order: the active word has the most contrast; spoken words dim to 30–50 % contrast; nothing un-spoken is shown.
- A section change inverts the frame (ground ↔ type), not the palette.
- Never: gradients inside letters, rainbow per letter, drop shadows that soften edges.
- Examples: night — ground `#111111`, type `#f2efe6`, accent `#ff4a1c`; paper — ground `#f4f1ea`, ink `#16161a`, accent `#2b50ff`.

## 4. Type & subtitles

- At most two families per film: a condensed display (Anton, Bebas Neue, Oswald) for loud words and a neutral grotesk (Inter or Space Grotesk, using the weight axis) for calm text; a mono (IBM Plex Mono, Space Mono) for numbers and asides; a marker (Permanent Marker, Caveat) only as a second voice.
- Devanagari: Baloo 2 (variable weight) for loud words, Mukta or Hind for neutral text, Rozha One for display contrast, Tiro Devanagari Hindi for literary texts.
- Sizes: hero word 200–600 px; phrase lines 80–160 px; asides 28–40 px; nothing meant to be read below 48 px.
- **Subtitles**: if the kinetic text shows every spoken word, no subtitles. If it shows only key words, a quiet static line at the bottom (Inter 34 px, 70 % contrast). A second language always goes in that static line (Mukta for Hindi), never animated beside the main text.
- Every phrase rests fully legible and still for ≥ max(1.8 s, speech + 0.6 s) in total; each word rests ≥ 0.3 s before it moves again.

## 5. Motion quality

- 24 fps on ones (30 or 60 fps allowed for screen-only work); type never steps.
- Entry leads the syllable onset by 1–2 frames; exit when the phrase ends or the next one needs the space.
- Easing: snap for punches (fast `eo` with `back` overshoot 1.2–1.5), `eio` for the camera, linear only for continuous scrolls.
- Weight: big words move slowly and land hard; small words zip. Letter squash and stretch ≤ ±12 %.
- **Verbs act, nouns hold**: "fall" drops, "split" splits, "grow" scales; a noun simply lands.
- Speech drives primary motion; the music beat drives only secondary pulses (2–4 % scale bumps), except in a sung lyric where the two coincide.
- Never moves: a word while it is being read; the baseline grid; the accent's meaning.

## 6. Camera grammar

The camera reads with the viewer. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Travel to the next phrase | thought continuing | a list; an argument; a journey |
| 90° roll: a vertical line becomes the floor | a change of perspective | a twist; "on the other hand"; a fall |
| Push through a letter's counter into the next scene | going deeper | a definition; a memory; a detail |
| Pull back: the words form a shape | the whole picture | a summary; a map; a portrait |
| Locked frame, words stacking | accumulation | a list; pressure building; a recipe |
| Whip pan between clusters | sudden change | an interruption; a joke; a second speaker |
| Slow drift on one word | weight, pause | a name; a number; a confession |
| Two columns side by side | dialogue | an argument; an interview; a duet |

Framing: the active word sits inside the central 70 %; one reading point per frame; new text never appears behind the current read. Transitions: through a counter, a giant word wiping the frame, an inversion cut, camera travel. No crossfades between text blocks: doubled text is unreadable.

## 7. Sound palette

- **The voice is the lead instrument**: one clear, dry, close voice (narrator, poet, speaker) or two contrasted voices.
- Music with clear transients for secondary motion: drum_kit, claps, electric_bass, piano stabs, violins_pizz, marimba, numpy synth bass; for a poem, sparse piano or vibraphone.
- **Typographic foley by weight**, quiet (about −18 dB under the voice): small words = clicks (claves, woodblock); heavy words = low thumps (gran_cassa, bass_drum); slides = filtered-noise whooshes; snapping letters = snare or claps; draw-on = pen scratch.
- Silence: one word alone, bed cut; the next word arrives into silence.
- Mix: music ducked 8–10 dB under the voice with a smoothed sidechain; −14 LUFS.

## 8. Native moves

- **The word acts its meaning.** A verb does what it says. *Fits content like:* "shrink" in a budget talk; "melt" in a climate piece; "jump" in a sports promo.
- **Sentence as architecture.** Lines become floors and stairs that the camera climbs. *Fits content like:* a career story; a building's history; a process with steps.
- **Emphasis by scale.** A stressed word fills the screen and shoves the others aside. *Fits content like:* a price; a deadline; a single "no".
- **Letters as matter.** Words shatter, pile up, pour into a container. *Fits content like:* data overload; a recipe's ingredients; rumours spreading.
- **Typographic portrait.** The words arrange into the shape of their subject. *Fits content like:* a city skyline of street names; a face of quotations; a tree of family names.
- **Interruption.** A second voice's word slams in and knocks the first off-frame. *Fits content like:* a debate; a sibling quarrel; a heckler at a speech.

## 9. Pitfalls of the medium

- **Unreadable motion** → one reading point, mandatory rest time, never animate text that is being read.
- **Words out of sync** with the voice → word times from alignment, entries 1–2 frames early; re-derive when the voice changes.
- **Broken Devanagari** (detached matras, split conjuncts, a cut headline) → per-word or per-akshara animation, browser shaping.
- **Lost kerning** when glyphs are placed one by one → offsets from the shaped layout.
- **Font salad** → two families, one accent class.
- **Constant beat-bounce** on everything reads as cheap → beat only for secondary motion.
- **Unchecked reading time** → expose every phrase through `window.TEXTS(t)` and run `core/render/readcheck.mjs`.

## 10. Engine

No demo engine yet (draft). A first demo should build:
- `glyphs.js`: font loading, shaped layout, glyph paths, per-glyph transforms and draw-on; start from `styles/spy-titles/demo/glyph.js` (opentype.js outlines to letter pieces).
- `timing.js`: `wordAt(t)`, `phraseAt(t)`, stress from the voice track; voices from `core/tts/tts.py`.
- `motion.js`: verb behaviours (`fall`, `split`, `grow`, `shake`, `pour`); easing from `styles/swiss-motion/demo/ease.js` (`cubicBezier`, `snap`, `steps`) and `core/lib.js` (`back`, `spring`, `seg`).
- `stage.js`: world layout, phrase anchors, `travel(fromId, toId, t)`, roll and counter push.
- `fx.js`: shatter glyph polygons, pile physics pre-simulated at a fixed rate, motion blur by sub-frame accumulation.
- Render with `core/render/still.mjs` / `video.mjs`; reading-time check with `core/render/readcheck.mjs`; foley cues from `core/render/events.mjs`; subtitles via `core/render/srt.py`.

## 11. Variation space

The agent decides the text and voice, the font pair, the accent class, the space the words build, and how literal the acting is.

- Structures: **one long sentence** travelling through a single unbroken landscape; **call and response** between two voices in two columns that finally merge; **a list that becomes a picture**, each item a brick of the final shape.
- Openings: **a blinking cursor** and one letter; **a word too large to read** that pulls back into a sentence; **silence**, then the first word slams in.
- Endings: **every word collapses into one**; **the last word left alone** as the voice stops; **pull back** to reveal the whole text as a page.

---

Status: **draft** — no demo film yet. Before this is used as a library style it needs a demo film, `DEMO.md`, stills and the checks in the Lemo-Opuscar `MAINTAINING.md` ("Gates").
