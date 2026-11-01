# Blue Tiles (Delft / Azulejo) — Style Prompt

> Cobalt brushed onto white tin glaze across a wall of square tiles: each tile a small painted vignette or one fragment of a larger panel, the glaze milky and crazed, the blue pooling where the brush paused, the window light breaking from tile to tile.
> References (grammar only): Dutch tin-glazed tiles of the 17th–18th centuries (one motif in a roundel, corner ornaments that join where four tiles meet, trades, ships, games, landscapes; pounced outlines; manganese as a second colour); Portuguese azulejo panels of the 18th century (one large blue-and-white scene spanning many tiles inside a painted frame); Chinese blue-and-white porcelain as the source of the cobalt idiom. Never copy a known tile series, panel, factory mark or painter's mark.

## 1. Essence, and what it is not

- **One pigment on white glaze**: cobalt in three to five strengths, from a pale wash to a near-violet line. The glaze is the light.
- **A grid of slightly imperfect squares**: grout lines, tiles a little out of plane, each catching the window reflection at its own angle.
- **The brush cannot be corrected**: raw glaze drinks the paint, so strokes have loaded starts, pooled ends and darker crossings; outlines first, then washes, then dots.
- **Two scales of picture**: a single motif per tile (a wall of vignettes) or one panel painted across many tiles, with joints that never quite align.

Not Chinese Ink Wash (pigment on glaze, not ink on absorbent paper; no grey tones, no bleeding wet edges). Not Watercolor Brush (no paper, one hue). Not Stained Glass (opaque and reflective, no lead, no transmitted colour). Not a blue duotone filter over a drawing: every mark is a brush stroke in cobalt.

## 2. Materials & rendering

- **Tile body**: a 1024² texture per tile from an atlas of variants: milky white glaze (slightly cool or slightly cream, per batch), glaze thickness noise (thicker toward edges → a faint blue-green tint), pinholes, occasional crazing (sparse Voronoi crack lines), chipped corners showing buff earthenware.
- **Cobalt model**: paint into a density canvas D per tile; colour = glaze × exp(−k·D·a), with absorption a stronger in red and green than in blue (Beer–Lambert), so low density gives sky blue and high density a deep violet-blue. Overlaps add density: crossings darken by themselves.
- **Brush**: bristle strokes (a ribbon plus 5–12 bristle tracks) with a loaded start (+40 % density), a body that thins along the stroke, a pooled end; a fine liner brush for outlines and a broad soft brush for washes. Dots and stippling for foliage and sea.
- **Firing**: before firing, cobalt reads as a dull grey-black on a chalky matte glaze; after firing, a 1.5–3 px blur of D into the glaze, the blue saturates, and a clearcoat-like gloss appears. Firing is a state that can animate.
- **Wall** (three.js or a 2D normal-mapped pass): each tile a slightly convex plane (bevelled edges), offset ±0.5 mm and rotated ±0.3°, set in grout 2–4 mm wide (off-white or grey, matte, rough). Glaze clearcoat 1, roughness ~0.12; a window or softbox environment so a specular patch slides across the tiles in steps. `core/three/post.js` for AO in the grout and DOF.
- **Panel mode**: a large picture cut into tile canvases, each painted separately: lines break at joints by 1–3 px, washes shift slightly in strength from tile to tile.
- **Pounce**: a dotted charcoal outline from a pricked pattern, gone after firing.

## 3. Colour logic

- **Cobalt on white, nothing else** by default: 3–5 strengths of one blue plus the glaze, the grout and the room.
- At most **one second pigment**: a manganese purple or an antimony-like yellow, reserved for frames, borders or one recurring accent object.
- **Value order**: outlines darkest, mid washes for form, paper-white glaze for light; skies mostly unpainted with a few horizontal strokes.
- The room stays neutral; warmth comes from window light on the glaze, not the paint.
- Example: glaze `#f3f1ea`, wash `#9db8d9`, mid `#4f78b3`, line `#1f3a7a`, deep `#18215a`, grout `#d8d2c4`, optional manganese `#5e3a5e`.

## 4. Type & subtitles

- **Painted lettering** belongs on the tiles: a cartouche or a row of border tiles, letters brushed in cobalt from **IM Fell English** or **Playfair Display** italic shapes (rasterise, then paint with the brush model so strokes pool), 36–60 px.
- **Subtitles**: a quiet band below the wall in **IM Fell English** or **EB Garamond** 34–42 px, deep cobalt on a glaze-white strip with a thin blue rule, two lines at most; Devanagari in **Tiro Devanagari Hindi**. Hold ≥ max(1.8 s, speech + 0.6 s).
- Small labels: a number or name in a tile's corner, ≥ 24 px.

## 5. Motion quality

- 24 fps. **Camera and light on ones; painted figures on twos or threes**: a tile vignette animates as a few repainted drawings, like a flip of tiles.
- **Painting-in** is the main motion: pounce dots → liner outline → washes → dots, each stroke at brush speed; a tile paints in 2–4 s, a panel tile by tile.
- **Tiles change one at a time**: a whole wall changes by a wave of individual tiles flipping, sliding or being replaced, never by a global crossfade.
- **Window light** drifts slowly across the glaze; reflections jump at tile edges.
- Never moves: the grout grid, finished tiles not in use, the frame border.

## 6. Camera grammar

A wall camera that respects the grid. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Locked wall of vignettes, one tile alive at a time | many small moments, a catalogue | trades of a town; a day's hours; a family album |
| Push into one tile until the glaze fills the frame | a single memory | a ship leaving; a child's game; a lost object |
| Lateral track along a long panel | a continuous scene | a harbour; a battle of ideas; a procession |
| Raking light across the tiles | the wall as a place, time of day | dawn in a kitchen; an old house; decay |
| Pull back from a tile to a whole room of walls | scale, a culture of images | a station; a tiled hall; a city |
| Tile drops out to reveal the next scene | a hidden layer | a secret; a memory under a memory; repair |

Framing: grout lines are horizontal and vertical on screen unless the camera rakes on purpose; text never crosses a joint mid-word. Transitions: a tile flip, a tile falling out, a glaze reflection wipe, a grid of tiles turning in a wave; no crossfades, no free-floating images off the grid.

## 7. Sound palette

- **Instruments**: harpsichord, recorder, lute or guitar (`guitar_nylon`, `pluck('nylon_guitar')`), viols as `cellos`/`violas` played soft, bells and carillon (`tubular_bells`, `glockenspiel`, `hand_chimes`); a bright plucked line (`pluck('acoustic_guitar')` with tremolo) for azulejo moods.
- **Foley from ceramic**: a fingertip tap on glaze (a short high "tink", inharmonic), tiles clicking in a stack, a trowel in mortar, a tile prised out (grit + crack), a brush on raw glaze (very dry soft whisper), the kiln's roar.
- **Ambience**: a canal or harbour through a window, a kitchen, rain on glass.
- **Silence**: room tone and one tile tap.
- **Voice**: a warm, domestic narrator. Music ducked ~8 dB under voice; −14 LUFS.

## 8. Native moves

- **The wall of vignettes.** Every tile holds its own small scene; one comes alive at a time. *Fits content like:* the trades of a street; twelve months; the members of a team.
- **Panel assembled.** A big picture builds tile by tile, gaps in the grid filling. *Fits content like:* a city plan; a puzzle being solved; a community project.
- **Joint mismatch.** The panel's lines break at the joints, showing separate hands. *Fits content like:* collaboration; a story told by many; a repaired history.
- **Grey to blue.** A dull grey painting turns to bright cobalt in the kiln. *Fits content like:* an idea becoming real; a print developing; a result revealed.
- **The missing tile.** One tile falls out, revealing mortar or a different scene. *Fits content like:* a gap in a record; a secret; something stolen.
- **Corner joins.** Quarter motifs on four tiles meet to make one ornament. *Fits content like:* four people meeting; a merger; a crossroads.

## 9. Pitfalls of the medium

- **Flat digital blue** reads as a duotone filter → density model with pooled ends and darker crossings, several strengths.
- **A perfect grid** looks like a texture, not a wall → per-tile offset, tilt and glaze variation; reflections that jump.
- **Continuous lines across joints** betray a single image → paint panel tiles separately, break lines at joints.
- **Too much second colour** loses the idiom → one extra pigment at most, reserved.
- **Animation too fluid** dissolves the ceramic feel → repaint on twos or threes; change walls tile by tile.
- **Religious panels and factory marks as decoration** → many historic panels are devotional and many marks belong to living manufacturers; invent secular subjects and never imitate a mark.
- **Presenting it as genuine antique or handmade tiles** → credit it as code-made; consult tile painters for commercial or heritage work.

## 10. Engine

No demo engine yet (draft). A first demo should build:
- `tile.js`: glaze texture atlas, crazing, chips, bevel normal; `tile(seed, batch)`.
- `cobalt.js`: density canvas per tile, `stroke(path, brush)`, `dot(p, r)`, Beer–Lambert colour, `fire(u)` from grey raw state to fired blue with softening.
- `wall.js`: grid with grout, per-tile offset and tilt, panel slicing, tile flips and drop-outs.
- `pounce.js`: dotted transfer outlines; `light.js`: window environment and moving reflection.

Start from `styles/ink-wash/demo/ink.js` (bristle stroke engine, `mk`, `draw`, `drawSeq`), `styles/watercolor/demo/engine.js` (width profiles, partial strokes, sprite cache), `styles/stained-glass/demo/glass.js` (piece grid and `voronoi` for crazing), `styles/brick-toy/demo/set.js` (softbox and HDRI studio light for glossy surfaces), `core/three/post.js`, `core/lib.js`.

## 11. Variation space

You decide vignette wall or panel (or both), the number of tiles, the glaze age, whether a second pigment exists, the room and window, and whether we see the painting or only the fired wall.

- Structures: **a calendar wall** (one tile per month, the year read across the grid); **the restoration** (a damaged panel completed tile by tile); **a street of trades** (each tile a shop, the camera walking the wall like a street).
- Openings: **a bare biscuit tile** receiving the pounce; **window light** sliding over an old kitchen wall; **one tile in macro**, pulled back to the room.
- Endings: **the last tile set into the gap**; **night**, the glaze reflecting one lamp; **the kiln door opening** on a stack of fresh blue.

---

Status: **draft** — no demo film yet. Before this is used as a library style it needs a demo film, `DEMO.md`, stills and the checks in the Lemo-Opuscar `MAINTAINING.md` ("Gates").
