# Cross-stitch — Style Prompt

> Pictures counted onto even-weave cloth one X at a time: every cell of the grid is either bare fabric or a two-legged cross of cotton floss, outlines are straight backstitches along the grid, and the world changes by being stitched, unpicked and restitched cell by cell.
> References (grammar only): European and American alphabet samplers of the 17th–19th centuries (border bands, alphabets, numerals, small isolated motifs, a name and a date); counted cross-stitch charts (symbol grids, colour keys, the rule that all top legs cross the same way); folk cross-stitch traditions such as Eastern European embroidered towels and Palestinian tatreez, which are living and carry regional meanings. Never copy a known chart, sampler or regional motif set, and never name them in the film.

## 1. Essence, and what it is not

- **A visible grid of holes**: the Aida or even-weave cloth shows its square mesh wherever it is not stitched.
- **The X is the pixel, with depth**: each filled cell is two diagonal floss legs, the top leg always crossing in the same direction, with thread sheen and a shadow on the cloth.
- **Backstitch outlines** run along cell edges in straight segments; French knots for eyes and dots; half and quarter stitches only where a curve truly needs them.
- **Limited thread palette**: a numbered chart of 8–24 colours; tones change in whole steps; blends are two strands of different colours in one needle.
- **Change happens by stitching**: images build, unpick and restitch cell by cell; nothing slides between cells.

Not 16-bit Pixel RPG (pixels are light; here each cell is thread with shadow, sheen and holes, and nothing scrolls sub-cell). Not Microgame Frenzy (no screen, no UI frames). Not Tenango embroidery or Stitched Tapestry (no free-form satin or wool; the count rules). Not a pixel-art image with a fabric texture laid on top.

## 2. Materials & rendering

- **Cloth**: Aida as a procedural tile: square blocks of woven threads with holes at every cell corner, a cell size of 10–24 px at reference zoom (one parameter: the count), cream or white, faint grid shading, a fold crease if the cloth was stored.
- **Cell buffer**: a `Uint16Array` of chart indices (0 = bare), the single source of truth; the chart, the stitched cloth and the back are all views of it.
- **Stitch sprite**: per colour, an atlas of 8–16 X variants (leg width 35–45 % of the cell, two or three twisted strands visible, sheen along the leg direction, slight fuzz, a soft shadow down-right). Choose the variant by `hash(x, y)`; under leg first, top leg second, all tops crossing the same way.
- **Tension jitter**: leg ends ±0.08 cell, leg width ±6 %; the top leg very slightly thicker. Never perfect, never random-looking.
- **Backstitch**: straight floss segments from hole to hole, one strand, darker colour, drawn above the crosses.
- **Specials**: French knot (a small raised dome with a spiral highlight), half stitch (one leg), blended needle (two strands of different colours twisted).
- **The back**: a separate render of the same buffer: travelling threads between cells of the same colour, knots or loop starts, thread tails, a tangle that tells the effort.
- **Hoop**: optional wooden ring (three.js or a 2D sprite) holding the cloth taut, outside the hoop creases and slack.
- Light: one key from the upper left; a WebGL pass lights cloth and thread height. Re-render only cells that change.

## 3. Colour logic

- **8–24 thread colours** chosen as a chart; each has a symbol and a number in the key. Tones step: at most three values per hue.
- **The cloth is a colour**: cream, white or a dyed ground; bare cloth is used as a value (background, highlights), never filled just to fill.
- **Backstitch** is the darkest colour or a near-black brown, reserved for outlines and text.
- **Accent**: one red (or one metallic-looking thread) reserved for the subject or the maker's mark.
- Never: anti-aliasing, gradients, a colour outside the chart.
- Example: cream Aida `#efe7d2`; floss — red `#b5262f`, deep red `#7d1a24`, green `#3f7a3a`, sage `#8fae7e`, blue `#2f4f8a`, ochre `#c99a3b`, brown `#5b3a26`, black-brown backstitch `#2a1e18`.

## 4. Type & subtitles

- **Stitched lettering** is native: alphabets drawn on the grid from bitmap faces (**Silkscreen**, **Press Start 2P**, **VT323** rasterised at one cell per pixel), or hand-charted sampler letters 7–9 cells tall.
- **Subtitles** live off the cloth: on the paper chart margin or a band below the hoop, **IBM Plex Mono** or **Space Mono** 32–40 px in the backstitch colour, two lines at most. Devanagari: **Noto Sans Devanagari** for subtitles; for stitched Hindi words, rasterise **Hind** at cell resolution and hand-fix the matras on the grid. Hold ≥ max(1.8 s, speech + 0.6 s).
- The maker's initials and a year, stitched in a corner, are a native signature.

## 5. Motion quality

- 24 fps. **Camera on ones; stitching quantised to cells.** A stitch lands as under leg then top leg (2–4 frames per cell close up; whole rows per frame when wide).
- **Stitch order is real**: rows worked left to right as half-crosses, then back as top legs; or cell by cell. Pick one per film and keep it.
- **Animation is restitching**: a character moves by unpicking cells behind and stitching cells ahead, on twos to fours; at most a few cells per step, so motion reads as stitched effort.
- **Unpicking** leaves faint holes and fibre fuzz in the cells for a moment.
- **Light sweep** and a slight hoop tilt are the only continuous motions.
- Never moves: the grid, the chart key, a finished border.

## 6. Camera grammar

A craft-table camera that can read the chart. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Locked hoop, cells filling | patience; something made by hand | a gift; a recovery; a long project |
| Macro on one X being made | the smallest unit of effort | a first step; a habit; a vote |
| Pull back from the hoop to the whole cloth | scale of the work | a lifetime; a community; a total |
| Cut to the chart and back | plan versus result | a blueprint; a budget; a recipe |
| Flip to the back of the cloth | the hidden labour and mess | behind the scenes; stress; real cost |
| Pan along a border band | repetition and order | days; generations; a list |
| Tilt of the hoop in raking light | the object, its age | an heirloom; a memory; a museum |

Framing: the grid stays axis-aligned unless the hoop is deliberately tilted; text sits on whole cells; subjects centred on whole cells. Transitions: cells filling to cover the frame, unpicking to bare cloth, turning the hoop over, a cut to the chart; no crossfades.

## 7. Sound palette

- **Instruments**: domestic and small: `pluck('music_box')`, `pluck('kalimba')`, `glockenspiel`, soft `piano`, `accordion` for a parlour, `ukulele`, `recorder`. Melodies can be quantised like the grid: short repeating patterns that add one note per row.
- **Foley from thread and cloth**: needle through Aida (soft tick at the hole), floss drawn (short silky zip; longer for long travels), the hoop screw tightening, scissors, a needle tapping the hoop, thread separating into strands (a tiny rasp), unpicking (sharp little snaps).
- **Ambience**: a room: clock, kettle, rain on a window.
- **Silence**: only the needle ticks.
- **Voice**: intimate, personal, as if read from a letter. Music ducked ~8 dB; −14 LUFS.

## 8. Native moves

- **Cell by cell.** An image completes one X at a time, row by row. *Fits content like:* savings growing; days of a recovery; a vaccine campaign counted.
- **Chart to cloth.** The symbol grid becomes thread in place. *Fits content like:* a plan executed; a code compiled; a recipe cooked.
- **The back of the work.** Turn the hoop to show tangles and travel threads. *Fits content like:* what a performance costs; hidden labour; anxiety behind calm.
- **Unpick and restitch.** Cells pulled out and replaced in a new colour. *Fits content like:* a correction; a changed mind; a rebuilt town.
- **Sampler band.** Border, alphabet, small motifs and a name and date. *Fits content like:* a family record; a school year; a résumé.
- **Count shift.** The same chart on finer or coarser cloth changes the picture's grain. *Fits content like:* zooming into data; childhood vs adulthood; resolution of memory.

## 9. Pitfalls of the medium

- **Flat pixel squares** look like a filter → X sprites with legs, sheen, shadow and visible holes.
- **Inconsistent top legs** look sloppy → all top legs cross one way (break it only on purpose).
- **Sub-cell motion** breaks the medium → move by restitching cells.
- **Too many colours** turn it into a photo mosaic → ≤ 24, stepped tones.
- **Stitching everything** hides the cloth → use bare cloth as a value.
- **Small subtitles stitched on the grid** become unreadable → subtitles off the cloth.
- **Regional and ceremonial motifs as decoration** (tatreez patterns, embroidered towel symbols) → they carry identity and ritual meaning for living communities; invent motifs, and consult or credit embroiderers of the tradition for commercial work. Do not present the film as handmade.

## 10. Engine

No demo engine yet (draft). A first demo should build:
- `chart.js`: palette key with symbols, the cell buffer, image → chart quantisation, bitmap text → cells.
- `stitch.js`: per-colour X atlas, backstitch, knots, half stitches, stitch order and `stitchTo(buffer, u)`, `unpick(cells, u)`.
- `aida.js`: cloth tile by count, holes, creases; `back.js`: the reverse-side render from the same buffer.
- `hoop.js`: hoop, cloth slack, tilt; one WebGL pass for thread height and sheen.

Start from `styles/pixel-rpg/demo/px.js` (indexed framebuffer, palette tables, Bayer dither for choosing between two threads), `styles/pixel-rpg/demo/sprites.js` (small rigged sprites at low resolution), `styles/crayon-book/demo/gl.js` (Canvas → WebGL lighting compositor), `core/three/post.js` (DOF for macro on the hoop), `core/lib.js`.

## 11. Variation space

You decide the count and cloth colour, the chart palette, whether we see the chart, the back or the hoop, the stitch order, and whether figures animate by restitching or the cloth is a still record.

- Structures: **a sampler made over years** (bands added one per year); **two hoops** (two people stitching toward the same chart in different places); **unpicking** (a finished cloth taken apart cell by cell to reveal an older picture beneath).
- Openings: **a blank hoop** and a threaded needle; **the back of a finished cloth** before turning it over; **a chart key** read colour by colour.
- Endings: **the last cell**; **initials and a year** stitched in the corner; **the hoop released** and the cloth relaxing into creases.

---

Status: **draft** — no demo film yet. Before this is used as a library style it needs a demo film, `DEMO.md`, stills and the checks in the Lemo-Opuscar `MAINTAINING.md` ("Gates").
