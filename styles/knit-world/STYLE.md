# Knitted World — Style Prompt

> A world made of knitted and crocheted fabric: every surface is a lattice of yarn stitches, colour is a knitting chart, objects are stuffed and seamed, and a pulled strand can unravel anything row by row and knit it back up.
> References (grammar only): knitting charts (one square = one stitch, colour changes on the stitch grid); stranded colourwork such as the Fair Isle tradition of Shetland (two colours per row, small repeating bands); crochet toy-making (tight spiral rounds, stuffed forms); woollen stop-motion sets for macro tabletop light. Never copy a published pattern or a designer's chart, and never name the references in the film.

## 1. Essence, and what it is not

- **The stitch is the pixel.** Every surface shows a regular grid of V-shaped knit stitches (or purl bumps, rib, crochet rounds) at one gauge per world; colour changes snap to stitch cells.
- **Soft, stuffed volume**: puffy objects with seams, slight sag, plump edges; flat knitted panels as skies and grounds.
- **Yarn is a material**: twisted plies, a short fuzz halo, small irregularities in stitch tension, heathered colour.
- **Unravel and knit-up**: a pulled strand undoes the fabric stitch by stitch into a kinked wavy yarn; the strand can knit back into something else. This is the medium's signature.

Not Felt Stop-motion (matted fibre, no stitch structure), not cross-stitch (X stitches embroidered on woven cloth), not 16-bit Pixel RPG (screen pixels, hard edges; here every cell is a soft lit yarn loop), not Brick Toy (rigid, glossy, snapped together).

## 2. Materials & rendering

- **Stitch atlas**: pre-generated sprites per stitch type (knit V, purl bump, rib pair, cable crossing, crochet single), each with albedo-mask, height, normal and AO, two plies twisting, a fuzz fringe. Knit stitches are ~1.3× wider than tall.
- **Chart**: an indexed grid (palette indices, like a pixel buffer) that says which yarn colour and stitch type each cell holds. Pictures are designed on the chart; gradients are dithered by stitch.
- **Knit shader** (WebGL2 / three.js material): for each pixel, find its stitch cell in surface UV, sample the atlas, tint by the chart colour with per-stitch ±4 % value noise and occasional flecks of another yarn, light with the normal map. Flat panels in 2D; 3D objects with UVs aligned to stitch rows and puffy displacement.
- **Seams**: where UV islands meet, a visible seam of whipstitches; place them where a maker would sew.
- **Fuzz**: a few instanced short fibres on silhouettes and a soft halo pass; small, never hairy.
- **Yarn strand**: a tube (3D) or ribbon (2D) with ply-twist texture, kinked by the memory of loops (a sinusoid of the stitch width along its length); simulated as a Verlet rope baked at a fixed step.
- **Unravel as a pure function of `t`**: every stitch has an index in knitting order (row by row, alternating direction for flat pieces, spiral for rounds). The state is one number `N(t)`: stitches above `N` are gone, and the free strand runs from stitch `N` to the pull point with length = stitches released × yarn per stitch (~3.5 stitch widths). Knit-up runs `N` upward.
- Gauge is world-anchored: stitches scale with the object, never with the screen.

## 3. Colour logic

- **Yarn palette per film**: 6–9 colours, each heathered; an **undyed oatmeal or grey wool** is the neutral.
- **Two colours per row** in colourwork bands; solid areas use one colour. That rule keeps the chart honest.
- No anti-aliased gradients: transitions are stitch dithers or stripes.
- **One accent yarn** (a red, a mustard) for the hero, the pulled strand, or the thing that connects.
- Value: hero objects one step brighter; grounds in deeper or greyer wools.
- Example: oatmeal `#e3d7bf`, moss `#6f8a4c`, sea `#3f6f8f`, slate `#4a4f57`, mustard `#d8a43a`, accent red `#c43a33`.

## 4. Type & subtitles

- **Titles are knitted**: letters rasterised onto the stitch grid from a pixel face (Press Start 2P or VT323 at a whole number of stitches; ≥ 7 rows per letter height), knitted into a panel; or duplicate-stitched over existing fabric. Devanagari titles: Baloo 2 rasterised at ≥ 12 rows so matras survive.
- **Subtitles** are typeset, not knitted: Baloo 2 32–40 px (covers Devanagari) in cream with a soft dark shadow, lower third, no box. Two lines max.
- Hold each subtitle ≥ max(1.8 s, speech + 0.6 s).

## 5. Motion quality

- **24 fps output, puppets and props on twos** like stop-motion; the camera on twos as well unless the film chooses a smooth glide throughout.
- **Unravel and knit-up advance in whole stitches**: slow = one stitch per drawing, fast = one row per drawing; the strand follows on twos with rope sway.
- Stuffed objects move softly: small overshoot, slight sag on landing, no stretch beyond the fabric.
- **Appear** by knitting up from a cast-on edge or by a strand arriving; **disappear** by unravelling or being folded away like a scarf.
- **Never moves**: the gauge, the stitch grid on a surface (it never slides across a shape), the lamp.

## 6. Camera grammar

A macro tabletop camera in a soft room. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Follow the strand | Connection, consequence | a supply chain; a family tie; a message passed on |
| Push into stitches until loops are landscape | Scale, what things are made of | a cell; a neighbourhood; a habit |
| Pull back to a blanket or jumper | The whole is one piece | a community; a map; a year of work |
| Top-down onto a knitted map | Overview, planning | a town; a route; a garden |
| Low eye-level on stuffed characters | Being in the world | a chat; a small adventure; a shop |
| Locked frame while a piece unravels | Loss in slow time | a memory fading; budget cuts; a ruin |

Framing: stitch cells ≥ 6 px on screen at hero size; keep the pull point visible during an unravel. Transitions: knit-up wipe (rows climbing up the frame), unravel wipe, a knitted panel sliding over the lens, a cut on action; no crossfades.

## 7. Sound palette

- **Cosy and plucked**: `ukulele`, `guitar_nylon`, `harp`, `kalimba`, music box via `pluck('music_box', …)`, `glockenspiel`, `clarinet`, `bassoon`, `flute`, `accordion`, `violins_pizz`, `cellos` for warmth.
- **Foley of yarn**: needle clicks (soft wooden or small metal ticks), a strand sliding (soft friction noise), unravelling as rapid gentle pops at the rate stitches release, a cushion thump, a seam pulled tight (rubbery squeak).
- **Ambience**: fireside crackle, rain on a window, a kettle; or the world's own sounds kept soft.
- **Silence**: a held room with one click of needles.
- **Voice**: warm and unhurried; music ducked ~8 dB under voice; final −14 LUFS.

## 8. Native moves

- **Unravel.** A strand is pulled and a piece undoes row by row into wavy yarn. *Fits content like:* a memory fading; a plan falling apart; a forest cleared.
- **Knit-up.** A strand climbs into rows and becomes something new. *Fits content like:* a town rebuilt; a habit forming; a body healing.
- **Chart as picture.** A flat knitted panel changes stitch colours over time like a slow display. *Fits content like:* a map of spreading water; a scoreboard; a growing crowd.
- **Follow the thread.** One strand runs from object to object across the set. *Fits content like:* who supplies whom; a family tree; a rumour's path.
- **Dropped-stitch ladder.** A run opens down the fabric, one rung at a time. *Fits content like:* a crack in a system; a rumour spreading; a deadline slipping.
- **Cable cross.** Two strands or columns twist around each other. *Fits content like:* two lives; a partnership; DNA.

## 9. Pitfalls of the medium

- A knit texture laid over flat art reads as a filter → the stitch grid must drive colour (chart) and shading (normals), aligned to each form.
- Mixed gauges → one stitch size per world unit across all objects.
- Moiré from tiny stitches → atlas mipmaps; below ~6 px per stitch fade to heathered flat colour.
- Unravel that ignores yarn length → strand length from stitches released.
- Too much fuzz looks hairy → a short, faint halo only.
- Anti-aliased gradients in charts → stitch dithers and stripes.
- Claiming hand-made craft → say it is made in code; credit pattern designers or makers if a real chart or a craft tradition's motif is used.

## 10. Engine

No demo engine yet (draft). A first demo should build:
- `stitch.js`: atlas generator (`atlas({types, plies, fuzz})`), chart buffer (`chart(w, h, palette)`), knit shader with per-stitch noise; indexed palette, lookup swaps and Bayer dithering after `styles/pixel-rpg/demo/px.js`.
- `yarn.js`: strand tube/ribbon with ply twist, baked Verlet rope, stitch ordering, `unravel(chart, N)`, `knitUp(chart, N, target)`.
- `knit3d.js`: three.js material applying the stitch shader in UV space, puffy displacement, seams; desk, HDRI and softboxes after `styles/brick-toy/demo/set.js`; DOF, GTAO and grade from `core/three/post.js`.
- `mix.py`: needle and yarn foley via `core/audio/sfx.py`, music via `core/audio/sampler.py` / `core/audio/pluck.py`, voice via `core/tts/tts.py`.
Seeds and easing from `core/lib.js`; render with `core/render/video.mjs`, `srt.py`, `mux.sh`.

## 11. Variation space

You decide the world, the gauge, the yarn palette and accent, flat panels or 3D, what the strand means, the opening and the ending.

- Structures: **one pulled thread** (a single strand unravels a whole place, then knits it back as something else); **a jumper's year** (a garment's colour bands mark months, each band a scene); **a network** (strands link stuffed houses and every exchange tightens or loosens them).
- Openings: **a cast-on edge** and needles clicking as the first row appears; **a loose end** snagging on something; **a close-up of loops** that pulls back to a whole knitted town.
- Endings: **unravelled to a ball of yarn** rolling to rest; **bound off**, the last stitch pulled tight and cut; **a blanket folded**, the world tucked inside.

---

Status: **draft** — no demo film yet. Before this is used as a library style it needs a demo film, `DEMO.md`, stills and the checks in the Lemo-Opuscar `MAINTAINING.md` ("Gates").
