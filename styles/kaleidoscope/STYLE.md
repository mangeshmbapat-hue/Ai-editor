# Kaleidoscope — Style Prompt

> A view down a mirrored tube: loose pieces of coloured glass in a backlit cell are multiplied by mirrors into a perfectly symmetric pattern that re-forms every time the cell turns and the pieces tumble.
> References (grammar only): the 19th-century two- and three-mirror kaleidoscope and its object cells (loose glass, beads, oil-filled cells); the teleidoscope (a lens that folds the outside world); dihedral and wallpaper-group symmetry from mathematics (how many mirrors, at which angles). Copy no maker's design, pattern or packaging, and never name them in the film.

## 1. Essence, and what it is not

- **Real mirror symmetry**: two mirrors at 180°/N give N-fold dihedral symmetry (60° → 6, 45° → 8, 30° → 12); three mirrors give an endless triangular tiling. All symmetry comes from folding one wedge, never from copied sprites.
- **Transmitted coloured glass**: pieces glow from a frosted diffuser behind them, overlaps darken, edges catch thin highlights.
- **A physical cell**: pieces tumble under gravity as the cell turns, sticking and then sliding in avalanches; nothing morphs.
- **The eyepiece**: a circular field in black; farther reflections slightly darker and greener (mirror losses).
- **Two rotations**: turning the cell changes the pattern; turning the tube spins it rigidly.

Not Stained Glass (no lead lines, no picture, no stone hall), not Paper-cut Lightbox (no cut paper scenes), not Memphis Diorama (no 3D toy objects), not a vector "mandala generator" (no physical cell, no attenuation, no eyepiece).

## 2. Materials & rendering

- **Object cell**: a square render target (1024–2048 px) holding a frosted diffuser (warm white with low-frequency density noise) and 20–80 pieces: rounded chips, rods, beads, faceted jewels, a twist of wire, a pressed leaf. Each is drawn with `multiply` into a white transmittance canvas (colour = dye), with a darker rim where the glass is thicker (1.5–3 px), an inner highlight arc (`screen`, 30–60 %) and a few bubbles. Clear pieces act as lenses: offset the background inside them.
- **Tumbling**: a fixed-step 2D rigid-body pre-simulation at 240 Hz (seeded): circle and convex colliders inside a circular drum, gravity rotating with the cell angle, restitution 0.1–0.2, friction 0.4–0.6, so pieces stick and then avalanche. An oil-filled cell adds heavy damping and slow drift. Bake per-frame transforms to JSON; `render(t)` only reads them.
- **Fold shader** (WebGL): polar coordinates about the tube axis; two-mirror fold `θ' = mod(θ − φ_tube, 2α)`, `if θ' > α: θ' = 2α − θ'`; reflection count `k = floor((θ − φ_tube)/α)`; sample the cell at `(r, θ' + φ_cell)`. Three-mirror: reflect the point across the triangle's edges until it lies inside, counting reflections. Loss `R^k` (R 0.88–0.94) with a faint green-grey tint and slight blur per bounce. Thin dark seams (0.5–1 px) along the mirror joins and a 0.1–0.3° misalignment, for honesty.
- **Eyepiece**: a circular aperture 70–90 % of frame height, soft edge, black outside, a faint ring of the tube's inner wall; a dust speck, if any, in screen space, never folded.
- **Exterior** (when the camera leaves the eyepiece): a three.js brass or card tube in a small studio. Supersample the fold 2×; average 3–5 sub-frames in fast spins.

## 3. Colour logic

- 4–6 dye hues plus clear glass; the neutrals are the diffuser's warm white and the black around the eyepiece.
- All colour is transmitted: nothing is brighter than the diffuser; overlaps get darker, never whiter.
- Jewel tones of varied value (a dark ruby, a mid amber, a pale aqua) so the pattern still reads in greyscale.
- One accent piece (gold foil, or a clear prism whose highlight sparkles), once per set.
- Never: smooth digital gradients across the field, glow on everything, neon.
- Example jewel set: ruby `#9c1b2e`, amber `#e09a2b`, emerald `#1f7a4f`, cobalt `#2546a8`, aqua `#7fd1d0`, diffuser `#fbf3e4`.

## 4. Type & subtitles

- **No text inside the folded field**: a mirrored letter cannot be read. Words live in the black surround or in shots of the unfolded cell.
- Titles: one upright line under the circle in Cormorant Garamond 500 or Poiret One, 60–110 px, warm white; or a word built from glass pieces in the cell, shown unfolded through the side of the cell before the mirrors take it.
- **Subtitles**: in the black below the circle, Cormorant Garamond 500 italic or Inter 400, 34–40 px, warm white at 85 %, no box. Devanagari: Tiro Devanagari Hindi or Noto Serif Devanagari. Hold ≥ max(1.8 s, speech + 0.6 s).

## 5. Motion quality

- 24 fps, continuous. Tube spin ≤ 20–30°/s (faster strobes); the cell turns in eased strokes like a hand on a ring (30–90° in 1–2 s, `eio`), with pauses.
- Pieces stick, then a cluster slides and tumbles in 0.3–0.8 s and settles with small bounces. An oil cell drifts and rotates slowly.
- The fold is fixed per shot; changing the fold count is a declared, openly digital move.
- Appear: a piece dropped into the cell from the rim. Disappear: it slides out of the visible wedge.
- Never moves: the eyepiece circle, the surround, any text.

## 6. Camera grammar

One round window and what turns behind it. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Locked eyepiece, cell turning | change from the same pieces | a shifting mood; a new idea; seasons |
| Tube spin, pattern rotating rigidly | contemplation; a cycle | waiting; a daily routine; time passing |
| Slow push toward the centre | going deeper | focus; a memory; meditation |
| Pull back from eyepiece to tube and hand | the inner world was small | a child's toy; a gift; a sense of scale |
| Through the side of the cell, unfolded | the plain pieces behind the wonder | how it works; humble ingredients; behind the scenes |
| Fold count change, 3 → 6 → 12 | complexity growing | a community; scaling up; multiplication |
| Teleidoscope on an outside scene | the world as pattern | a street crossing; a garden; a crowd |

Framing: the circle centred; nothing important at the exact centre, where every reflection meets. Transitions: a tumble, the eyepiece iris closing and opening, a spin blur, a cut on an avalanche; no crossfades between two folded patterns (they blur to mud), no digital wipes.

## 7. Sound palette

- **Glass in the cell**: clouds of tiny clicks timed to the simulation's contacts (3–10 ms noise bursts band-passed 3–8 kHz with short inharmonic resonances), a soft slide hiss, and for the tube a faint friction squeak (a band-passed sawtooth slowly swept).
- **Music**: crystalline: glass, glockenspiel (low-passed for a celesta colour), hand_chimes, vibraphone, harp, music_box and kalimba (`pluck.py`), over a cello or organ_soft drone.
- **Techniques, as options**: mirror forms (palindromic phrases; a melody answered by its inversion in another voice); a motif repeated N times for N-fold symmetry; an avalanche landing as a flurry of grace-note clicks.
- **Ambience and silence**: a quiet room, a clock, rain on a window; at rest, room tone only.
- **Voice**: intimate and wondering, close-miked. Music ducked 6–8 dB; −14 LUFS.

## 8. Native moves

A menu: use the ones your story needs.

- **The turn.** The cell rotates; nothing, then everything re-forms. *Fits content like:* a new view of the same facts; a dish from the same ingredients; a team reshuffled.
- **The avalanche.** At a tipping angle a cluster slides; the pattern breaks and resolves. *Fits content like:* a market shock; a sudden memory; a decision finally made.
- **Drop a piece.** A new piece falls in and appears N times at once. *Fits content like:* a newcomer changing a group; one new ingredient; a rumour multiplied.
- **Behind the mirrors.** Cut to the plain cell: a few modest pieces. *Fits content like:* how a festival is really made; the reality behind a brand; a family's ordinary keepsakes.
- **Teleidoscope.** The outside world, folded. *Fits content like:* a city junction as a star; a flower bed; a dance floor.
- **Out of the eyepiece.** Pull back to the tube in a hand or on a table. *Fits content like:* a grandparent's toy; a gift; the end of a dream.

## 9. Pitfalls of the medium

- **Text in the fold** is mirrored → keep text outside the field.
- **Seams and cracks** at wedge edges from filtering → mirrored-coordinate sampling, clamped LOD, supersampling; draw one deliberate seam line instead.
- **Flat vector look** → transmittance, rims, overlaps, per-bounce losses, the eyepiece.
- **Strobing** on fast spins and fine detail after encoding → speed limit, sub-frame blur, no 1 px high-contrast detail.
- **Monotony** of an endless mandala → pace with stillness, tumbles and behind-the-mirror cuts; make the cell's contents the story's own objects.
- **Sacred patterns as decoration**: folds resemble mandalas, rangoli and rose windows → do not present them as religious diagrams, do not drop sacred signs into the cell as ornaments, do not call the film a mandala.
- **Physics in render order** → bake the tumble.

## 10. Engine

No demo engine yet (draft). A first demo should build:

- `cell.js`: piece generators (`chip`, `rod`, `bead`, `jewel`, `leaf`), transmittance render with rims and highlights, `renderCell(frame)`.
- `tumble.js`: fixed-step rigid bodies in a drum, rotating gravity, `bake(seed, cellAngle)` to per-frame transforms.
- `fold.js`: WebGL pass with `fold2(N)`, `fold3()`, loss `R`, tint, seams, misalignment, supersampling.
- `eyepiece.js`, `scope3d.js`: aperture, inner ring, text surround; the exterior tube.

Start from `styles/stained-glass/demo/glass.js` (glass pieces and transmittance textures; drop the lead), `styles/shadow-puppet/demo/gl.js` (transmittance × light × tonemap), `styles/microgame/demo/glpass.js` (WebGL pass helper), `styles/glass-product/demo/studio.js` (exterior shots), `core/lib.js`, `core/audio/sampler.py`, `core/audio/pluck.py`.

## 11. Variation space

You decide the cell's contents (ideally the story's own objects), the mirror system, the colour set, the turning rhythm, and whether the outside world appears.

- Structures: **one cell, many turns** (each section a new configuration of the same pieces); **adding pieces** (one fragment at first, another dropped in each chapter); **inside and outside** (the folded view alternating with the plain world the pieces came from).
- Openings: **black, and the eyepiece iris opening**; **the empty cell**, one piece dropped in; **the unfolded cell** seen from the side before the mirrors take it.
- Endings: **out of the eyepiece** to a hand setting the tube down; **every piece sliding to the bottom**, leaving the clear diffuser; **the fold count falling** to one wedge of plain pieces.

---

Status: **draft** — no demo film yet. Before this is used as a library style it needs a demo film, `DEMO.md`, stills and the checks in the Lemo-Opuscar `MAINTAINING.md` ("Gates").
