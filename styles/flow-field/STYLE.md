# Flow-field Generative — Style Prompt

> Images drawn by code: thousands of lines follow an invisible vector field, and the picture is wherever they bunch, part or swirl. Change the field and the whole image flows into the next one.
> References (grammar only): 1960s–70s pen-plotter computer art (one pen, one seed, the drawing as a procedure); scientific flow visualisation (streamlines, line-integral convolution, wind and ocean-current maps); evenly-spaced streamline placement and curl noise from computer graphics. Copy no artist's outputs, series or signature parameters, and never name them in the film.

## 1. Essence, and what it is not

- **Lines, not shapes**: every mark is a polyline integrated through a field; no fills or outlines.
- **Form is the field**: a subject exists only as how the flow bends (attractors, vortices, a hidden shape's contours, a data field); density and direction carry it.
- **Order with noise**: many near-parallel lines under one rule; individuality comes from seeds.
- **One substrate per film**: luminous lines on a dark screen, or ink plotted on paper.
- **Visible process**: lines grow, the field drifts, the seed can be on screen.

Not One-line Drawing (one hand line that is the character; here thousands of machine lines), not Data Storytelling (no chart paper or axes; data may drive the field, never plotted), not Circuit Board (no right angles), not a screensaver (the field is about the subject).

## 2. Materials & rendering

- **Field** `F(x, y, t)` → unit vector. Base: angle `2π·turns·noise(x·f, y·f, t·k)` from 2–3 octaves of `vnoise`, or **curl noise** (gradient of a scalar potential rotated 90°: divergence-free, so lines never pile into sinks). Modifiers are summed as vectors, never as angles: attractor `(p − x)/|p − x|^a`, vortex (the same rotated 90°), uniform wind, **shape guide** `perp(∇sdf)·exp(−|sdf|/w)` from the signed distance field of a hidden glyph or silhouette, **data field** (a gridded wind or current, bilinear). Normalise last.
- **Integration**: RK4, fixed step 0.5–2 px, maximum length L, stop at the edge or when speed < ε.
- **Placement**: evenly spaced streamlines (Jobard–Lefer: seeds at d_sep beside existing lines, stop within d_test ≈ 0.5·d_sep of another, hash grid), or Poisson-disc seeds with radius ∝ 1/density from a luminance map.
- **Living flow**: particles with seeded birth time and position, life ≤ 3 s; each frame integrates trails from birth (no accumulation buffer), so any frame renders alone. 5k–60k particles as instanced WebGL quads.
- **Screen substrate**: lines 0.75–2 px, additive on near-black at 0.04–0.25 opacity, so density becomes brightness; a slight bloom only where densest; 2× supersampling.
- **Paper substrate**: cream paper with fibres; a pen of constant core width (1.4–3 px) with `multiply`, slight pooling at line ends, rare skips; pen-up travel never drawn.
- Finished plots are cached as layers; only lines in progress are recomputed, each under its own seed.

## 3. Colour logic

- The background is the neutral (near-black or paper); lines carry all the colour.
- 1–3 hues, or one ramp mapped to a single quantity: direction, speed, curl, distance from the subject, or line age. Paper mode quantises to 3–5 inks (one pen each); screen mode may be continuous.
- Highest density = lightest on screen, darkest on paper; never fill a region solid.
- One accent for the lines that matter: the streamlines through the subject, or a single tracer.
- Never a full rainbow by angle (it reads as default software).
- Example screen: ground `#07080c`, lines `#9fd8ff` → `#f2f6ff`, accent `#ff7a3d`. Example paper: `#f1ece1`, inks `#1f2a44`, `#b23a2e`, `#3b6e5a`.

## 4. Type & subtitles

- **Titles are made of the field**: text rasterised to an SDF guides lines along the glyph contours, or seeds lines only inside it, so a word forms out of flow and dissolves back. Source faces: Space Grotesk 700, Inter 800 or Rubik Mono One, 160–300 px.
- **Colophon**: IBM Plex Mono or Space Mono, 16–22 px, in a corner margin like a plot's label: `seed 41 · n 12 000 · curl`.
- **Subtitles**: Space Grotesk 500 or Inter, 34–40 px, bottom-centre, in the line colour at 90 % (screen) or ink (paper), on a soft background-coloured halo so no line crosses the words; two lines max. Devanagari: Mukta or Noto Sans Devanagari 500. Hold ≥ max(1.8 s, speech + 0.6 s).

## 5. Motion quality

- 24 fps on ones, continuous; nothing boils.
- The field drifts slowly: a line's shape changes ≤ 2–5 % per second unless turbulence is the point.
- Lines appear by growing from their seeds along arc length (`eo`), in an order that builds structure: the subject's contours first, the fill after.
- Field changes are vector blends over 1–3 s (`eio`): the image flows into the next.
- Particles fade in over 0.3 s after birth and out before death; nothing pops.
- Paper mode: the pen moves at a believable feed; ink exists only behind it.
- Never moves: substrate, colophon.

## 6. Camera grammar

A flat world seen from above; the camera mostly lets the lines move. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Locked frame, field evolving | a system with its own weather | a market; a mood; a season |
| Slow drift with the mean flow | being carried | a migration; a river; a commute |
| Push into a vortex core | the centre that pulls everything | a decision; a city centre; a storm |
| Pull back from texture to the whole image | the many make one | a crowd into a face; currents into a coast; data into a pattern |
| Locked sheet, the pen drawing | patient construction | a portrait; a route map; a record of a process |
| Reroll cut: same frame, new seed | siblings; chance | editions; variation; "no two alike" |

Framing: 20–40 % negative space; the subject in the central 70 %; the colophon in a margin. Transitions: a field morph (preferred), a reroll hard cut, lines retracting to their seeds and regrowing, a new sheet in paper mode; no dissolves between two line images (doubled density reads as mud).

## 7. Sound palette

- **Generative synthesis** (numpy): soft sine pads; granular clouds whose density follows line density and whose pitch follows field angle, quantised to a pentatonic or whole-tone set; noise beds shaped by turbulence.
- **Pitched accents**: marimba, glass, vibraphone, harp, kalimba (`pluck.py`), a felt piano for a theme; contrabass or organ_pedal drones under vortex cores.
- **Plotter foley** (paper mode): stepper whine pitched by head speed (a square wave through a resonant band-pass, 300–1200 Hz), pen-down tick and pen-up clack (`sfx.click`), felt tip on paper (fine band-passed noise ∝ speed).
- **Screen mode** has no literal foley: the grain cloud is the lines' sound; a soft `sfx.whoosh` marks a morph.
- **Silence**: the field frozen over one sustained tone, then motion resumes.
- **Voice**: calm, curious, few words. Music ducked ~6 dB, −14 LUFS.

## 8. Native moves

A menu: use the ones your story needs.

- **The field finds the shape.** Random flow is weighted toward a shape guide until the subject emerges, then released. *Fits content like:* a word forming from wind; a portrait emerging from a crowd; a coastline appearing out of currents.
- **Attractor arrival.** A point appears and every line bends toward it. *Fits content like:* a city drawing commuters at nine; a gravity explainer; a team converging on a goal.
- **Laminar to turbulent.** Raise frequency and octaves; parallel lines break into eddies. *Fits content like:* stress rising; weather building; a traffic jam forming.
- **Wind made visible.** A real gridded dataset drives the field. *Fits content like:* the monsoon's arrival; ocean currents carrying plastic; air around a building.
- **Plotted on paper.** A pen head draws the lines one by one. *Fits content like:* a portrait as a gift; a map of a year's runs; a slow ritual of making.
- **Tracer.** One accent particle is followed through the whole field. *Fits content like:* a single drop in a river; a letter through a postal network; one commuter's day.

## 9. Pitfalls of the medium

- **Angle interpolation seams** at 0/2π whip lines around → blend unit vectors.
- **Clumps and holes** where lines converge → curl noise or evenly spaced streamlines with d_test.
- **Grey mush** from too many lines → cap density, keep negative space, lower opacity.
- **Accumulation buffers** (fading the previous frame) break determinism and parallel rendering → recompute trails from birth.
- **Shimmer after encoding** on 1 px lines → supersample, minimum width ~1.2 px.
- **Pretty wallpaper** → drive the field by the subject or the data.
- **Undefined direction** on an SDF's medial axis → fade the guide weight where |∇sdf| is small.
- **Slow frames** with 60k particles in JS → integrate in a vertex shader; compute static streamlines once.

## 10. Engine

No demo engine yet (draft). A first demo should build:

- `field.js`: `noiseAngle(f, turns, oct)`, `curl(f)`, `attractor(p, a)`, `vortex(p)`, `guide(sdf, w)`, `dataField(grid)`, `blend(fields, weights)`, `sample(x, y, t)`.
- `sdf.js`: rasterise text or a silhouette with `fillText`, two-pass Euclidean distance transform, gradient.
- `stream.js`: `rk4(F, p, h, L)`, `evenlySpaced(F, dsep, dtest, seed)`, `particles(n, seed, life)`, `trailAt(i, t)`.
- `lines.js`: instanced additive segment renderer, paper pen with pooling, progress reveal.
- `plotter.js`: greedy path ordering, pen-up travel, head sprite, feed rate, sound-event export.

Start from `core/lib.js` (`vnoise`, `mulberry`, `eio`), `styles/one-line/demo/ink.js` (pen pressure, fuzzy edge, pooling: paper mode), `styles/transit-map/demo/gl.js` (a 2D ink layer printed on procedural paper), `styles/watercolor/demo/engine.js` (`withSeed` for marks built in `render(t)`), `styles/microgame/demo/glpass.js`, `core/audio/pluck.py`, `core/audio/sfx.py`.

## 11. Variation space

You decide the substrate, the field's ingredients, what drives it (a shape, a dataset, a story value), the density, the palette within the colour logic, and whether seeds are shown.

- Structures: **one field, one day** (a locked field driven by a measured day of wind, traffic or heartbeat); **a series of rerolls** (each section a sibling seed; the differences are the point); **shape to shape** (the field morphs through a chain of hidden guides, each image dissolving into flow and forming the next).
- Openings: **a single line** growing until others branch beside it; **pure noise** slowly aligning; **a blank sheet** and a pen lowering.
- Endings: **every line retracting** to its seed, leaving dots; **the field stilling** to parallel calm; **the finished plot** alone with its colophon.

---

Status: **draft** — no demo film yet. Before this is used as a library style it needs a demo film, `DEMO.md`, stills and the checks in the Lemo-Opuscar `MAINTAINING.md` ("Gates").
