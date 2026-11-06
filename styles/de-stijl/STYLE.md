# De Stijl — Style Prompt

> Neo-plastic composition in motion: thick black lines on a white ground divide the frame into rectangles, a few filled with red, yellow or blue, and the whole grid rebalances as lines slide and planes trade colour.
> References (grammar only): Piet Mondrian's neo-plastic paintings of the 1920s–30s for asymmetric balance, line weight and the restriction to verticals, horizontals and primaries; his late New York works (1942–44) for lines broken into small coloured blocks with a syncopated pulse; Theo van Doesburg's counter-compositions for the 45° variant; Bart van der Leck for figures reduced to coloured bars; Gerrit Rietveld's Schröder House (1924) for planes and lines separated in space. Never reproduce a specific painting, piece of furniture or building, and never name them in the film.

## 1. Essence, and what it is not

- **Only orthogonals and rectangles**: verticals, horizontals, no curves; no diagonals except in a declared 45° counter-composition film.
- **Primaries and non-colours**: red, yellow, blue; black lines; white and light-grey planes.
- **Asymmetric equilibrium**: a large white plane balanced by a small saturated block; never symmetric; balance itself is the drama.
- **An infinite grid seen through a window**: lines run off the frame edge or stop short of it.
- **Rearrangement is the motion**: lines slide along their own axis, planes change colour, rectangles split and merge.

Not Bauhaus (no circles or triangles, no construction lines, no mechanical figures), not Swiss Motion Graphics (no typographic grid with one signal colour; here lines and colour planes are the content), not Transit Map (lines carry no routes or stations), not Memphis Diorama (no pastels, patterns or diorama).

## 2. Materials & rendering

- **Data model**: lines `{axis: 'h'|'v', pos, from, to, w}`; cells are the faces of their arrangement, each with a colour. Positions are functions of t; cells are recomputed every frame (cheap), filled first, lines drawn on top.
- **Line weight**: 1.2–3 % of frame height, constant within a shot; lines may differ in weight from one another, deliberately.
- **Surface, one per film**: *flat* (crisp vector, 2× supersampled); *painted* (subtle brush direction per cell, horizontal or vertical, by a light normal map; slightly warm off-white; line edges with ±0.3 px hand variation; optional fine craquelure for an aged canvas).
- **Boogie mode**: lines become chains of small squares (a yellow line carrying red, blue and grey blocks) that travel along the line.
- **Space mode** (three.js): planes as thin slabs and lines as square-section bars floating apart in 3D; matte paint, one soft key light, hard shadows, orthographic or long-lens camera.
- **Rebalancing solver**: when a block is added or removed, solve for line positions that bring the colour-weighted centroid back near a target and keep area ratios within bounds; animate to the solution.
- Small data, fully deterministic; no textures beyond the chosen surface.

## 3. Colour logic

- **Red, yellow, blue, black, white, grey. Nothing else.**
- Coloured cells cover ≤ 25 % of the frame; white and grey ≥ 60 %.
- Weight: blue is the heavy dark, yellow the light, red the loud; balance a big yellow with a small blue.
- A small red or blue square may be reserved as the protagonist.
- Never: other hues, gradients, shadows in 2D modes, coloured lines (except in boogie mode, where lines turn yellow).
- Example: white `#f3f1ea`, grey `#d9d6cf`, red `#d22b26`, yellow `#f4cc1f`, blue `#1d3f97`, black `#121212`.
- Example boogie: lines `#f2c81e`, blocks `#cf2a24`, `#2348a6`, `#bdb9b0` on `#f3f1ea`.

## 4. Type & subtitles

- Text is set strictly horizontal or vertical inside cells, flush against lines.
- Faces: Space Grotesk or Inter for text; Rubik Mono One or Bungee for blocky display; Devanagari in Hind (its geometric strokes sit well in rectangles) or Mukta.
- **Titles are built from the grid**: letters made of rectangles on a 5×7 cell grid using the same line system, so a title is a composition.
- **Subtitles** live in a white cell at the bottom bounded by a black line, part of the composition: Space Grotesk Medium 36–42 px, Hind Medium for Devanagari, black on white. Hold ≥ max(1.8 s, speech + 0.6 s).

## 5. Motion quality

- 24 fps on ones. Motion is sliding along an axis; nothing rotates except the whole canvas in a 45° lozenge turn.
- Easing: `eio` for rebalancing slides (0.4–1.2 s); a colour change floods the cell along its long axis in 3–6 frames.
- A line grows from a junction to the next line or the frame edge; it retracts to merge two cells.
- Boogie mode: blocks hop along lines on subdivisions of the beat, in syncopated patterns, never all at once.
- Settled compositions hold still; restlessness kills balance.
- Never moves: the frame edge, line weights within a shot.

## 6. Camera grammar

A frontal view of a picture plane that can open in depth. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Locked composition, lines sliding | rebalancing, negotiation | a decision; a budget; a household |
| Push into one cell that becomes a new composition | recursion, scale | a detail; a room in a building; a smaller world |
| Pull back: the composition is part of a larger grid | context | a city; an organisation; a system |
| Lateral pan along an endless grid | continuity | a street; a timeline; a journey |
| Lozenge turn (canvas rotates 45°) | a new perspective | a shift; a twist; a surprise |
| Lift into space (planes separate in 3D) | structure revealed | architecture; an interior; a plan becoming a building |
| Boogie traffic (blocks run along lines) | city rhythm | traffic; a market; a party |

Framing: never centre the main block; balance large empty white against small colour; keep a line 10–30 % in from each edge. Transitions: a line sweeping across with the next composition behind it, a cell flood, a recursion zoom, the lozenge turn; no crossfades, no diagonal or organic wipes.

## 7. Sound palette

- **Stillness**: sparse piano or upright, vibraphone, glockenspiel; clean intervals and real silence between phrases.
- **Boogie**: a rolling left-hand piano bass (piano, upright, honky_tonk), walking jazz_bass or contrabass_pizz, brushed snare, hihat, trumpet_mute, clarinet, tenor_sax. The rhythm drives the blocks.
- Foley: plane slides (soft wooden glide), line snaps (woodblock click), colour floods (a brush swish), joinery clicks in space mode.
- Silence: a composition rebalances in silence and clicks into place.
- Voice: calm and measured. Music ducked ~8 dB under voice; −14 LUFS.

## 8. Native moves

- **Rebalancing.** A new block arrives and the lines slide until the whole is in balance again. *Fits content like:* a new baby in a family; a hire in a team; a city adding a park.
- **Line extension.** A black line grows and splits a plane in two. *Fits content like:* a border drawn; a decision dividing a group; a road through a field.
- **Recursive cell.** One cell opens into a whole composition of its own. *Fits content like:* a building's floors; an organisation chart; a zoom from country to street.
- **Boogie traffic.** Small blocks pulse along yellow lines. *Fits content like:* rush hour; packets in a network; dancers in a hall.
- **Figure as bars.** A person, animal or object reduced to a few coloured rectangles. *Fits content like:* a cyclist; a cow in a field; a chair being designed.
- **Lift into space.** Planes and lines pull apart into an elementary 3D structure. *Fits content like:* a house plan; a piece of furniture assembled; a stage set.

## 9. Pitfalls of the medium

- **Clip-art pastiche** → each shot a new composition that carries meaning through motion; never a famous painting.
- **Symmetry** → run the balance solver toward an off-centre target.
- **Too much colour** → coloured cells ≤ 25 %.
- **Thin or inconsistent lines** → weight from frame height, constant within a shot.
- **Diagonals sneaking in** through camera roll or perspective → only the declared lozenge; long lens in space mode.
- **Shimmering edges** on slow slides → 2× supersampling; snap to whole pixels at rest.
- **Protected designs** → invent furniture and buildings from the line system.

## 10. Engine

No demo engine yet (draft). A first demo should build:
- `grid.js`: lines model, `cells(lines, bounds)` → rectangles, `layout(t)` from keyframed line positions.
- `balance.js`: `rebalance(cells, {target, minArea, maxColour})` → new line positions.
- `paint.js`: flat and painted surfaces, line edges, colour flood.
- `boogie.js`: blocks travelling along lines on beat subdivisions.
- `space.js`: three.js slabs and bars, long-lens camera, lift animation.
- `letters.js`: block letters from the grid.
- Start from `styles/swiss-motion/demo/ease.js` (precise ease, `snap`, `steps`, `track`), `styles/transit-map/demo/net.js` (a line network on a constrained grid), `styles/memphis-diorama/demo/memphis.js` (flat-colour three.js world), `core/three/post.js`, `core/lib.js` (`monotone`, `track`, `seg`); music via `core/audio/sampler.py`.

## 11. Variation space

The agent decides the surface, the modes used (still, boogie, space), what the protagonist block stands for and how the balance tips.

- Structures: **a negotiation** (each new block forces a rebalance until one does not fit); **zoom of scale** (a recursive descent from a city grid to a single room); **a day of traffic** (stillness at dawn, boogie at rush hour, stillness at night).
- Openings: **one black line** crossing an empty white frame; **a single red square** alone, the grid growing around it; **the lozenge** turning upright into a square composition.
- Endings: **perfect balance** held in silence; **lines retracting** until one white plane remains; **lift into space** and orbit to show it was a house all along.

---

Status: **draft** — no demo film yet. Before this is used as a library style it needs a demo film, `DEMO.md`, stills and the checks in the Lemo-Opuscar `MAINTAINING.md` ("Gates").
