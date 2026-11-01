# Voxel World — Style Prompt

> A world made only of equal cubes on one grid: terrain, houses, trees, water and people are stacks of blocks, and everything that happens is a block placed, a block broken, or light, water or growth spreading to the next cell.
> References (grammar only): sandbox block-building games (a world edited one cube at a time, tick-based water and light, mining); voxel-art dioramas (one colour per cube, soft global light, a tiny world on a plinth); layer-by-layer 3D printing. Copy no game's textures, blocks, characters, creatures, interface or music, and never name them in the film.

## 1. Essence, and what it is not

- **One grid, one cube size** for the whole world (figures may use a finer sub-grid, declared once); no slopes, no curves, nothing built is ever rotated off the axes.
- **Edits are the drama**: place, break, spread, each quantised to a game tick.
- **Readable faces**: three face values per block (tops lightest) plus soft occlusion in every inside corner.
- **Textured or solid**: 16×16 pixel faces sampled nearest, or one flat colour per voxel; one look per film.
- **A small figure for scale**, built from the same blocks.

Not Brick Toy (no studs, no glossy plastic, no stop-motion of a real toy), not Low-poly Isometric Island (no facets or triangles; only axis-aligned cubes), not 16-bit Pixel RPG (3D cubes from any angle, not sprites), not Tilt-Shift Miniature (a digital world, not a photographed real place).

## 2. Materials & rendering

- **Data**: chunks of 32³ `Uint8Array` block IDs. The world at time t = base generation + an **edit log** `{tick, x, y, z, id}` applied up to `tick(t)`. Growth, fluids and light are pre-simulated at 20 ticks/s into edit logs too, so nothing depends on the previous rendered frame.
- **Generation**: `vnoise` heightmap; grass/dirt/stone by depth; caves by a 3D noise threshold; seeded tree templates and ore clusters.
- **Meshing**: greedy meshing per chunk (merge coplanar same-ID faces, cull hidden ones); rebuild only chunks touched at the current tick. **Vertex AO** per corner: `ao = s1 && s2 ? 0 : 3 − (s1 + s2 + c)` mapped to 0.55–1.0; flip each quad's diagonal toward the brighter pair to avoid streaks.
- **Textured look**: a procedural 16×16 atlas, `NearestFilter`, no linear mip blur; face shading by direction (top 1.0, N/S 0.8, E/W 0.65, bottom 0.5); block light 0–15 flooded per tick, mixed with sky light; fog in the horizon colour.
- **Voxel-art look**: one colour per voxel, a key light with soft shadows, hemisphere fill, GTAO and a little DOF from `core/three/post.js`, ACES tone mapping; the world on a plinth or a floating island.
- **Break**: an 8–10 stage crack overlay (`polygonOffset`), then 8 or 27 sub-cubes on seeded closed-form ballistic arcs with one bounce, shrinking away in 0.6–1 s.
- **Place**: scale 0 → 1.08 → 1 (`back`), or a short drop onto the seat with a puff of tiny cubes.
- **Fluids**: level-based spread (one cell per step, 7–8 levels), surface lowered by level, translucent with depth tint. **Figures**: original six-box characters with sine limb swings.

## 3. Colour logic

- 16–32 colours for the whole world in one palette table; each block type one base colour, or a texture of 3–5 shades of it. Shading comes from face direction and AO, never extra hues.
- Sky gradient and fog share one hue family; the fog colour is the horizon colour.
- Value order: tops > sides > undersides; foliage darker than grass tops; water reflects the sky.
- One accent block for what matters (a glowing ore, a beacon, a marker), emissive in the voxel-art look.
- Night is lit only by light blocks (warm) and a cool moon, never by a blue grade over everything.
- Example meadow: grass `#6fae4b`, dirt `#8a5a36`, stone `#8d8f94`, wood `#b5824c`, leaves `#3f7f3a`, water `#3c78c8`, sky `#9fd2f2`, accent `#f2c230`.

## 4. Type & subtitles

- **Titles are built**: text rasterised to the grid (one cell = one block), extruded 2–4 blocks deep and placed block by block with the place sound; raster sources Press Start 2P, Silkscreen or VT323 at 8–16 cells tall.
- **Subtitles**: VT323 or Pixelify Sans, 38–46 px, white with a hard one-"pixel" offset shadow, bottom-centre on a 50 % black plate with square corners. Devanagari: Teko or Noto Sans Devanagari 500 (Teko's squared shapes sit well with blocks). Hold ≥ max(1.8 s, speech + 0.6 s).
- In-world labels: block-built signs with pixel text, or floating VT323 name tags.

## 5. Motion quality

- **Two clocks**: the world steps on ticks (20 Hz, each event snapped to the nearest frame at 24 fps), so growth and spread visibly step; camera and figures move continuously at 24 fps.
- Building runs layer by layer (bottom-up or row by row), one block every 1–4 frames, faster once a pattern repeats.
- Blocks never slide between cells; only debris and dropped items move freely.
- Figures hop to climb one block; first person bobs.
- Appear: place pop, chunk load at the fog edge. Disappear: crack and debris, an explosion sphere, layers peeling from the top.
- Never moves: the grid, the voxel size.

## 6. Camera grammar

A diorama you can also walk in. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Slow orthographic isometric orbit | a whole small world | a village; a factory floor; a plan |
| Locked time-lapse of building | patience and labour | a house rising; a town across centuries; a bridge |
| First-person walk with head bob | being inside | a cave; a commute; a guided tour |
| Low flyover, chunks loading at the fog edge | discovery and scale | a new continent; a map revealed; a long journey |
| Cross-section: a clipping plane slices the world | what lies underneath | geology; plumbing; roots and burrows |
| Push in until single blocks fill the frame | the smallest unit | a material's texture; one brick of a big idea |
| Pull up from a figure to the whole island | the one in the many | a decision; solitude; home |

Framing: verticals stay vertical (no Dutch tilt); a followed figure ≥ 1/10 of frame height; the horizon or plinth stays readable. Transitions: a chunk-load sweep, a wall of blocks filling the screen and breaking away, a cut on a placed block, a day-night fade; no dissolves or blurred wipes.

## 7. Sound palette

- **Block foley by material** (synthesised): stone = `sfx.clack` + a 120 Hz `thump`; wood = woodblock knock; dirt = a 60 ms band-passed brown-noise crunch; sand = a soft hiss; glass = a tink then a noise-burst shatter; metal = inharmonic bell partials. Place higher than break; seeded ±5 % pitch per event so repeats never machine-gun.
- **World**: footsteps per material, water (filtered noise with bubbling blips), cave drips in long reverb, wind on heights, birds by day, crickets at night.
- **Music**: sparse ambient piano with long rests, kalimba and music_box (`pluck.py`), marimba, harp, numpy pads; or chiptune (square, triangle and noise channels in numpy) for a game-like film. Long stretches belong to the world alone.
- **Silence**: underground, only drips and room tone.
- **Voice**: a friendly, curious narrator or a builder thinking aloud. Music ducked ~6 dB; −14 LUFS.

## 8. Native moves

A menu: use the ones your story needs.

- **Block by block.** A structure assembles in visible order. *Fits content like:* a home built over a year; a cathedral across generations; a molecule assembled atom by atom.
- **Mine and reveal.** Breaking a tunnel exposes layers, ore and buried things. *Fits content like:* rock strata; an archaeological dig; the search for a lost object.
- **Cross-section.** The clipping plane shows what is inside. *Fits content like:* an ant colony; a building's floors; a city's underground.
- **Spread by ticks.** Water, light or plants travel cell to cell. *Fits content like:* a flood; irrigation reaching a field; a forest regrowing after fire.
- **Revoxelise.** The world resamples to a coarser or finer grid (octree merge and split). *Fits content like:* a memory losing detail; a zoom from planet to street; a rough draft becoming final.
- **Light block at night.** A lamp floods light level by level into darkness. *Fits content like:* first light in a cave; a village at night; an idea spreading.

## 9. Pitfalls of the medium

- **Blurry textures** → `NearestFilter`, mips by nearest or none, anisotropy off.
- **Seams, sparkle, z-fighting** on overlays → greedy chunk meshes with shared vertices; `polygonOffset` for cracks.
- **Flat, dead shading** → vertex AO with the diagonal flip plus direction shading.
- **Mixed voxel sizes** → one grid for the world, one declared sub-grid for figures.
- **Copying a famous sandbox game** (textures, blocks, creatures, hotbars, hearts, crosshairs, sounds) → all original.
- **Too many cubes** → chunked greedy meshes, frustum culling, rebuild only touched chunks.
- **Simulation in render order** breaks determinism → pre-simulate ticks into edit logs.

## 10. Engine

No demo engine yet (draft). A first demo should build:

- `grid.js`: chunk storage, `get/set`, `stateAt(tick)` from base world + edit log, ray pick.
- `gen.js`: `terrain(seed, size)`, `caves`, `tree(template, seed)`, `ores`.
- `mesh.js`: `greedy(chunk, atlas)`, vertex AO with diagonal flip, face shading, `rebuild(dirty)`.
- `atlas.js`: procedural 16×16 faces from palette shades, crack stages.
- `sim.js`: tick pre-simulation of fluids, block light (flood fill) and growth into edit logs.
- `fx.js`, `rig.js`: debris, place pop, explosion sphere; box figures.

Start from `styles/brick-toy/demo/bricks.js` (geometry cache), `styles/brick-toy/demo/set.js` (scene assembly), `styles/lowpoly-island/demo/world.js` (a world laid out in cells, pop-ins tied to notes), `styles/lowpoly-island/demo/post.js` (orthographic GTAO, depth fog, grade), `core/three/post.js` (voxel-art DOF, GTAO), `styles/pixel-rpg/demo/px.js` (palette tables), `core/lib.js`, `core/audio/sfx.py`, `core/audio/pluck.py`.

## 11. Variation space

You decide the look, world size, grid scale, the figure (or none), edit density, tick speed and palette.

- Structures: **one plot of land through time** (a locked island across seasons and generations, each era an edit log); **an expedition** (a figure crosses a generated world, each biome a chapter); **build, break, rebuild** (a structure raised, undone by a flood or a blast, raised again differently).
- Openings: **one block** placed on an empty plane; **the world loading** chunk by chunk outward from the camera; **underground darkness** until a light block is set.
- Endings: **the world revoxelising** coarser until it is a single block; **the last block** that completes the structure; **a pull-up** until the whole world sits on its plinth in the void.

---

Status: **draft** — no demo film yet. Before this is used as a library style it needs a demo film, `DEMO.md`, stills and the checks in the Lemo-Opuscar `MAINTAINING.md` ("Gates").
