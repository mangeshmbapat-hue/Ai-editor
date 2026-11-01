# Pinscreen — Style Prompt

> A white board pierced by a dense grid of pins, lit from one low side: pins pushed out cast long shadows (black), pins flush cast none (white), and everything between is a velvety engraved grey that is pushed, rolled and re-formed into each next image.
> References (grammar only): the pinscreen films of Alexandre Alexeieff and Claire Parker (1930s–1970s) and the National Film Board of Canada's later pinscreen work (soft tonal metamorphosis, figures emerging from darkness, roller and tool textures); mezzotint and aquatint printmaking for tone without line. Never copy their images, compositions or music, and never name them in the film.

## 1. Essence, and what it is not

- **Tone is shadow length.** Every value is made by how far pins stand out of a white board under an oblique light. Deep black = long shadows; white = flush pins; greys are velvet.
- **A visible grid of points.** Close up, the image is thousands of pin heads and their shadow strokes, all pointing away from the light; at normal distance it reads as soft engraving.
- **Images emerge and dissolve.** Figures rise out of black or white like a memory; one picture is rolled into the next and traces of the old one linger.
- **Directional relief.** Edges facing the light are crisp, edges away from it soften into shadow: the light's direction is part of every frame.

Not Copperplate Engraving (lines cut with a burin, paper, ink; here there are no lines, only point shadows), not Halftone Dossier (printed dots in inks on cream paper), not 1920s Silent Film (inked contours and hatching on projected silver), not airbrush or charcoal (no smudge, no spray; tone has grain and direction).

## 2. Materials & rendering

- **Pin field**: a height grid `h(i,j) ∈ [0,1]` (pin pitch 2.5–4 px at 1080p, square or staggered rows), anchored to the board. Images are authored as tone targets (Canvas 2D greyscale paintings, or three.js renders' luminance with soft GTAO), mapped to height by `h = f(1 − tone)` with a gamma that spreads the mid-greys.
- **Lighting shader** (WebGL2, per pixel): march 8–16 steps upstream along the light direction; the pixel is shadowed if an upstream pin's shadow (`h · cot(elevation)`) reaches it. Light elevation 15–35°, one azimuth per film. Add the pin itself: a dark shaft stub and a small bright head highlight (steel), stronger where pins stand out.
- **Board**: matte warm or cool white with faint fibre noise; slight falloff across the board from the lamp.
- **Tools change the field**, not crossfades: `roll(path, width)` moves `h` toward the next target only where a roller passes, leaving parallel roller texture (striped noise along the stroke); `needle(path)` lifts a single row of pins; `ball(x, y, r)` presses a soft round dent; `push(region, dir)` drags tone sideways.
- **Residue**: the board is never fully reset; keep 5–15 % of the previous image's height under the new one so ghosts remain.
- **Pure function of `t`**: `h(t) = mix(prevImage, nextImage, toolMask(t)) + residue + boil`, with tool masks from seeded paths; no simulation state.
- **Boil**: per drawing, a seeded ±2–4 % height noise per pin, the trace of a hand re-setting pins.
- **Oblique 3D view** (for reveals only): instanced cylinders in three.js under the same light, the board seen as a forest of pins.

## 3. Colour logic

- **Monochrome.** One board tone and its shadow; the whole film is one temperature (warm ivory, cool silver or sepia) chosen once.
- 7–10 readable steps between black and white; deepest black only in long-shadow areas, pure white only where pins are flush under full light.
- No hue anywhere. A single tint, if any, is applied to the whole frame.
- Value is meaning: let important things emerge from the opposite value (a pale face out of black, a dark bird out of white).
- Example: board `#ebe6da`, mid `#8a857b`, shadow `#1b1916`.
- Example (cool): board `#e2e5e6`, mid `#7d8285`, shadow `#141617`.

## 4. Type & subtitles

- **Titles are pinned** into the board from a glyph mask (IM Fell English, EB Garamond or Cormorant Garamond; Tiro Devanagari Hindi for Devanagari), at ≥ 110 px cap height so the pin grid can carry the letterforms; they emerge and are rolled away like any image.
- **Subtitles** are typeset, not pinned: EB Garamond 34–40 px in board white over a soft dark halo on the darkest band (or board-shadow colour on a pale band), no box. Devanagari: Tiro Devanagari Hindi or Noto Serif Devanagari. Two lines max.
- Hold each subtitle ≥ max(1.8 s, speech + 0.6 s).

## 5. Motion quality

- **24 fps output, the board changes on twos** (12 drawings/s); slow metamorphoses may step on threes.
- Movement of a figure is re-pinning: the old pose rolled down, the new one raised. Smooth translation of a whole figure is allowed only as a held drawing sliding with the camera.
- Slow, breathing easing (`ss`, `eio`); a metamorphosis takes 1.5–6 s.
- **Appear** by rising out of black or white; **disappear** by being rolled under. Nothing pops.
- **Never moves**: the pin grid and the light (except as a deliberate move). The grid must not shift relative to the board, or the image shimmers.

## 6. Camera grammar

A frontal board; most "camera moves" are painted into the pins. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Locked frontal board | Contemplation; the image breathing | a portrait; a landscape at night; a vigil |
| Re-pinned push (the image redrawn larger) | A dream drawing closer | a face remembered; a house approached |
| Real push to macro until pins show | The illusion revealed | how memory is made; scale; the grain of time |
| Light sweep (azimuth or elevation turns) | The same world seen anew | dawn; a revelation; a searchlight |
| Oblique pan over the pin forest | Relief and depth | a city at night; a field; a crowd |
| Slow lateral drift across a wide board | Passage, procession | a journey; a funeral; migrating birds |
| Rolled-through metamorphosis on a locked frame | One thing becoming another | grief; growth; a transformation |

Framing: one subject, generous dark or light space around it, nothing important within 6 % of the edge. Transitions: roller wipe, rise from black, sink to white, light sweep; never a crossfade, digital wipe or hard cut between unrelated pictures.

## 7. Sound palette

- **Sparse chamber timbres**: low `piano`, `cellos`, `contrabass`, `clarinet`, `harp`, `vibraphone_bowed`, `glass`, `tubular_bells`, a music box via `pluck('music_box', …)`. One instrument at a time is often enough; a long drone (numpy) under night images.
- **Foley of the board**: a granular tick of metal pins (short high-passed impulses 4–9 kHz, density following how many pins move), a roller's soft rumble, a wooden board knock, a breath. World sounds (wind, a dog, bells) are distant and filtered.
- **Silence** is the board at rest: room tone and the faintest ticking.
- **Voice**: a low, unhurried narrator or a poem read aloud; music ducked ~8 dB under voice; final −14 LUFS.

## 8. Native moves

- **Emergence.** A figure rises out of black (pins sinking) or white (pins rising). *Fits content like:* a face from the past; a ship out of fog; a name remembered.
- **Roller metamorphosis.** A roller crosses the board and leaves the next picture behind it, the old one lingering as residue. *Fits content like:* a village becoming a city; a child becoming old; a forest after fire.
- **Light sweep.** The lamp moves; every shadow turns and the relief changes character. *Fits content like:* a lighthouse beam; a day passing in one room; a truth seen from a new angle.
- **Negative turn.** Pins pushed from behind invert the image: what was dark becomes light. *Fits content like:* a photographic negative; a mirror world; a reversal of fortune.
- **Pin reveal.** The camera dives until single pins and their shadows fill the frame. *Fits content like:* a crowd made of individuals; data points; grains of a memory.
- **Ghost residue.** A previous image stays faintly under the new one. *Fits content like:* a house that once stood; a lost person; an earlier version of a plan.

## 9. Pitfalls of the medium

- Smooth tone that looks like blur or airbrush → visible pin pitch and directional shadow strokes in every frame.
- Moiré when the camera zooms over the grid → render at 2× and downsample; fade the pin detail when pitch drops below ~2 px on screen; real zooms are slow.
- Thin lines and small text fall apart → minimum feature = 2–3 pins; subtitles are typeset.
- Top lighting flattens the relief → keep the lamp low (15–35°) and on one side.
- Too many tones read as a photograph → limit to 7–10 steps and keep big dark and light masses.
- Crossfading two pinned images gives grey mush → change the field with tool masks and residue.
- The grid sliding relative to the board shimmers → the grid is world-anchored; only the camera moves.

## 10. Engine

No demo engine yet (draft). A first demo should build:
- `pins.js`: pin field from tone targets (`fromTone(img, gamma)`), tools (`roll(path, w)`, `needle(path)`, `ball(x, y, r)`, `push(region, dir)`), residue and seeded boil, all as functions of `t` using `mulberry`, `vnoise`, `ss` and `seg` from `core/lib.js`.
- `pinlight.js`: the WebGL2 shadow-march shader (light azimuth/elevation, pin head highlight, board albedo, falloff); take the full-screen pass structure from `styles/shadow-puppet/demo/gl.js` and the luminance/edge handling from `styles/silent-film/demo/engine/redraw.js`.
- `targets.js`: tonal source paintings in Canvas 2D, or three.js renders of soft forms with GTAO and grade from `core/three/post.js`.
- `forest.js`: instanced pin cylinders for oblique reveals, with a desk-light setup after `styles/brick-toy/demo/set.js`.
- `mix.py`: pin ticks and roller rumble via `core/audio/sfx.py`, music via `core/audio/sampler.py` / `core/audio/pluck.py`, voice via `core/tts/tts.py`.

## 11. Variation space

You decide the subject, the board temperature, the light direction, how much residue each change leaves, the opening, the ending and whether the medium is ever revealed.

- Structures: **a nocturne** (one place through one night, each hour rolled out of the last); **a family album** (portraits emerging and sinking, each leaving a ghost under the next); **a single journey** (a slow drift across one wide board with re-pinned pushes into stops along the way).
- Openings: **pure black board** with one point of light rising; **the pin forest in oblique light** before the camera turns to face the board; **a light sweep** across an image already there.
- Endings: **sinking to white** until only the grid remains; **the lamp lowered** until the shadows swallow everything; **a final ghost**: the last image rolled away but its residue still visible.

---

Status: **draft** — no demo film yet. Before this is used as a library style it needs a demo film, `DEMO.md`, stills and the checks in the Lemo-Opuscar `MAINTAINING.md` ("Gates").
