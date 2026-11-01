# Kolam / Rangoli — Style Prompt

> Threshold drawings in powder brought to life: white rice-flour lines that loop around a grid of dots and close on themselves, and coloured powder poured by hand into festive fills, all seen from above on swept ground.
> References (grammar only): the daily kolam of Tamil Nadu and its South Indian relatives (muggulu, rangavalli) for the dot grid (pulli), the continuous knotted line (sikku) and the doorstep at dawn; rangoli across North and West India for festival colour, petals and lamps; the mathematics of mirror curves for how one loop threads a grid. Never copy a specific family's or festival's design, and never name them in the film.

## 1. Essence, and what it is not

- **Seen from above**: a doorstep, courtyard or floor, freshly swept and sprinkled with water; the drawing lies on the ground.
- **The grid comes first**: dots in square, diamond or tapering rows; lines go around them, never through them.
- **One line that never ends**: in a knotted kolam a single closed loop weaves around every dot and returns to its start, with 4-fold or mirror symmetry.
- **Powder, not ink**: lines are trails of granules let fall between finger and thumb: grainy, raised, uneven in width, scattered at the edges, heaped where the hand paused.
- **Rangoli colour** (festive variant): regions filled with bright powders, petals and small oil lamps, separated by white lines.

Not One-line (ink on paper drawing objects; here abstract loops bound to a grid, made of powder on ground), not Chalkboard (no slate, no lesson, no erasing), not a kaleidoscope (no mirrored camera image; symmetry is drawn), not a vector mandala generator: the grains, the ground and the hand's pace are the style.

## 2. Materials & rendering

- **Ground** (cached): wet earth, swept stone or cement; broom arcs, pebbles, the step edge; sprinkled water darkens patches 12–18 % and dries back over time.
- **Grid**: square n × n, diamond (1-3-5-…-5-3-1) or interleaved lattices; each dot a small heap (radius ≈ 0.35 × line width).
- **Line generation**: the mirror-curve method: between neighbouring dots place or omit a "mirror"; trace a path that runs diagonally between dots and reflects off mirrors and the border; it closes into loops around every dot. Choose mirrors for a single loop; build one quadrant and reflect for symmetry; turn each turn round a dot into an arc of radius 0.5–0.6 × spacing.
- **Powder deposit**: along the path up to progress p, scatter granules (≈ 2,000 per 1,000 px of line at 1080p) at normal offsets drawn from a narrow Gaussian (σ ≈ 0.28 × width) with heavier tails; grain size 0.6–1.8 px; add 30–50 % more grain and a bulge at every pause (about every 1–1.5 spacings, where the hand re-pinches).
- **Relief**: grains accumulate into a height-and-colour texture (instanced points, additive); a WebGL compositor derives normals and lights them with a low raking sun, plus soft contact shadow on the ground. Finished lines bake into the ground texture; only the growing tip is live.
- **The hand** (optional): a forearm and pinch from above with its shadow, or only a stream of grains above the tip.
- **Rangoli fills**: grains scattered inside a region mask until opaque, edges sieved soft but never blended into a neighbour; a white or contrasting line on top; petals as sprites; clay lamps with flicker and warm pools.
- **Disturbance**: wind drifts the top grains (curl noise), a footstep stamps a mask and a smear, rain dots soften and darken lines.
- Each grain's position is `hash(lineId, i)`: never re-randomised per frame.

## 3. Colour logic

- **Kolam is one colour**: warm flour white on a darker ground; value contrast is the drawing. At most one accent, such as a red-ochre band on the step.
- **Rangoli**: 5–8 saturated powders (magenta, saffron, turmeric, leaf green, ultramarine, white, black), flat; shading only as stepped bands of neighbouring powders; every region bounded by a line.
- **The ground is never saturated**: earth or stone neutrals.
- **Light tells the hour**: dawn is a warm low sun with long grain shadows; festival night is lamp pools in which colours deepen.
- Example (kolam): wet ground `#4a3a2e`, dry `#6d5a48`, flour `#f1ece0`, accent `#a8442a`.
- Example (rangoli): `#d6246e`, `#f28c1b`, `#f6c90e`, `#2e9e4f`, `#1f4fb4`, white `#f7f3ea` on stone `#8a8378`.

## 4. Type & subtitles

- **Titles can be poured**: letter centrelines (hand-authored polylines or the medial axis of a glyph) traced in powder, revealed in stroke order.
- **Subtitles** are quiet and screen-space: lower third with a soft dark ground halo, flour-white Cormorant Garamond 34–40 px or Hind 30–36 px; Hindi in Hind or Tiro Devanagari Hindi; Tamil in Hind Madurai, only for real text checked by a reader. Never boxed, never perspective-distorted.
- Hold ≥ max(1.8 s, speech + 0.6 s); two lines max.

## 5. Motion quality

- **24 fps on ones**: the tip moves at a hand's pace (3–6 dot spacings per second), slowing into turns, quicker on diagonals; a short stop at each re-pinch (every 1.5–3 s) leaves a heap.
- **Dots first**, tapped in a rhythmic order (row by row or centre out), each a small puff.
- **Many hands** (four arms growing at once) is a liberty to use sparingly; the base grammar is one hand.
- **Fills pour** as a radial bloom inside the region (0.6–1.5 s).
- Easing `eio` along the path; no bounce, no overshoot.
- Never moving: laid powder (except wind, feet, rain), the ground, the grid. Light shifts slowly with the hour.

## 6. Camera grammar

Mostly overhead: the ground is the page. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Locked overhead | the pattern's logic | a rule; an algorithm; a calendar |
| Rise from the tip to the whole design | gesture becoming system | small acts adding up; a network; a community |
| Low raking angle across the grains | material, the hour | dawn; fragility; texture |
| Track down a street of doorsteps | many hands, one practice | a neighbourhood; a survey; variation |
| Follow the tip | attention, a path | a route; a thought; a delivery |
| Overhead rotation about the centre | symmetry, cycles | seasons; balance; a repeating task |
| Tilt up from design to doorway | threshold, welcome | a home; an arrival; a beginning |

Framing: designs centred or aligned to the step; never crop a loop at a "complete" reveal; keep ≥ 8 % ground margin. Transitions: a broom sweeps the old design away; a water sprinkle darkens the ground for the next; feet walk through; wind scatters; a rotation match-cut between two symmetric designs. Forbidden: kaleidoscope mirroring of the image, dissolves.

## 7. Sound palette

- **Dawn street**: crows and birds, a broom's swish (shaped noise per stroke), water splash, a bucket clank, glass bangles (bright inharmonic partials, `hand_chimes`), a far bicycle bell.
- **Powder foley**: a dry hiss as grains fall (noise band-passed 3–8 kHz, density following the pour rate), a finger-rub tick at each re-pinch, a faint patter on the ground.
- **Music, quiet**: a plucked line (`pluck('shamisen')` with low buzz, or `koto`), `flute` with breath noise, a tanpura-recipe drone, a soft barrel-drum pulse built like the tabla recipe; the shehnai recipe only for festival colour.
- **Techniques, as options**: the line's turns drive a pitch contour; dot taps on a pulse; on completion, silence with birds only.
- **Voice**: soft, close, morning register; music ducked ~8 dB; −14 LUFS.

## 8. Native moves

- **One line around every dot.** A single loop threads the whole grid and closes. *Fits content like:* a delivery route; a network reaching every house; an algorithm explained.
- **Grid before line.** Dots are tapped first; the line answers them. *Fits content like:* a plan before action; a seating chart; stars before constellations.
- **Swept away, drawn again.** *Fits content like:* a daily routine; impermanence; a reset after failure.
- **Ants and feet.** Grains carried off by ants, scattered by footsteps (rice flour is also food for small creatures). *Fits content like:* sharing; an ecosystem; the wear of daily life.
- **Colour pour.** Regions fill one by one. *Fits content like:* a festival; a budget being allocated; results coming in by region.
- **A street of thresholds.** Every doorstep a variation on one grammar. *Fits content like:* a census; a community; a design system.

## 9. Pitfalls of the medium

- Lines touching or crossing dots → mirror-curve generation; check a minimum clearance of 0.35 × spacing.
- Vector-crisp lines → granules, heaps, scatter, relief light.
- Flickering grains → seeded positions, baked finished lines.
- Broken symmetry → build a quadrant and reflect; add hand irregularity (≤ 2 %) after.
- A plotter's pace → hand speed, slowing on turns, pauses.
- Flat overheads → raking light, ground texture, a lamp or petal for scale.
- **Living, auspicious practice**: kolam and rangoli are drawn daily and at festivals in homes and temples, and some designs belong to specific rites. Don't use ritual designs or sacred symbols as decoration, and don't present the film as handmade powder work; credit the practitioners (mostly the women who draw them every day) and consult them for commercial work.

## 10. Engine

No demo engine yet (draft). A first demo should build:

- `grid.js`: lattices (`square`, `diamond`, `interleaved`).
- `kolam.js`: `mirrorCurve(grid, mirrors)` → loops; `singleLoop(grid, seed)`; `symmetrize(quadrant, order)`; `smooth(loop, r)`.
- `powder.js`: `deposit(path, p, width, seed)` into accumulation textures; heaps at pauses; wind, feet, rain masks.
- `ground.js` (wet/dry, broom marks), `comp.js` (height → normal → raking light), `fill.js` (pour, petals, lamps), `mix.py`.

Start from: `styles/one-line/demo/geom.js` (`buildPath`, `posAt`, `headAt`: progress along a path); `styles/crayon-book/demo/gl.js` (`makeComp`, a material compositor pattern); `styles/crayon-book/demo/crayon.js` (`dab`, `fill`); `styles/engraving/demo/engine/burin.js` (`resample`, `normals`, `inPoly`); `styles/paper-popup/demo/cutmesh.js` (`particles` for falling grains); `core/lib.js` (`hash`, `mulberry`, `eio`); `core/audio/sfx.py` (`noise`, `bp`, `env_exp`), `core/audio/pluck.py`.

## 11. Variation space

You decide the subject, kolam or rangoli (or both), the grid, how many hands, the hour, the opening, the ending and the camera.

- Structures: **seven dawns** (one threshold, a new kolam each day answering the last); **one loop, one town** (the line leaves the step and threads a whole neighbourhood map); **grid to festival** (a white kolam slowly becomes a rangoli as colour pours in).
- Openings: **a broom** sweeping in close-up; **a single dot** tapped into wet earth; **water** thrown in a dark arc.
- Endings: **the first footsteps** of the day cross it; **rain** softens the lines into the ground; **lamps** lit around the finished design.

---

Status: **draft** — no demo film yet. Before this is used as a library style it needs a demo film, `DEMO.md`, stills and the checks in the Lemo-Opuscar `MAINTAINING.md` ("Gates").
