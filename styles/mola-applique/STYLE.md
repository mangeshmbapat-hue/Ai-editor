# Mola Appliqué — Style Prompt

> Reverse appliqué brought to life: layers of bright cotton stacked and cut through, the cut edges turned under and hemmed with tiny stitches, so every shape is a channel revealing the colour beneath and every figure is outlined again and again in parallel bands.
> References (grammar only): the molas sewn by Guna (Kuna) women of Guna Yala, Panama, and of Colombia, for reverse appliqué, nested channels, filler slits and the paired front-and-back blouse panels; general appliqué and hand-hemming practice for fold and stitch behaviour. Never reproduce a specific mola or a traditional ceremonial design, and never name them in the film.

## 1. Essence, and what it is not

- **Stacked cloth**: 2–5 layers of solid cotton; a strong top colour (often red, orange or black) cut through to the colours below.
- **Shapes are channels**: narrow bands cut along a contour, so each figure is ringed by parallel lines of alternating revealed colour.
- **Turned edges and stitches**: every cut edge is folded under into a soft, slightly puffy rim held by tiny stitches; no raw cut, no printed line.
- **No empty ground**: background spaces fill with short slits, small triangles, dots and zigzags, plus small inserted patches of extra colours.
- **Flat, bold, symmetric figures**: animals, plants, people and labyrinth geometry.

Not Papercut Red (cloth, not paper; cuts reveal *different colours* below, edges are folded and stitched), not Paper Lantern (no backlight, no deep box: layers are millimetres apart and front-lit), not Silkscreen Poster (no printed inks; colour comes through cuts), not the sibling draft Yarn Painting (no strands; folded cloth bands).

## 2. Materials & rendering

- **Layers**: one full-frame canvas per cloth layer, each a solid cotton texture (noise-warped weave, thread slubs, slight per-thread colour variation, fibre speckle), plus a mask of what remains after cutting. A pixel shows the topmost layer whose mask is on.
- **Cut model**: a cut is a closed path removed from a layer's mask (and everything above it). A **channel** is the band between two offsets of a centreline (±d/2); cutting a contour channel through layer k reveals layer k+1 as a coloured line. Nested channels cut to alternating depths give the echo outlines.
- **Channel width d** is a fixed rule per panel (about 1.2–2 % of panel height; ≥ 6 px on screen).
- **Folded rim** along every mask edge, 2–4 px: light on the side facing the key, dark on the other (normal from the mask gradient); a contact shadow on the revealed layer (offset 1–2 px, blur 2–3 px, multiply ~30 %); edges wobble ±0.5 px because a hand folded them.
- **Stitches**: short dashes (1–1.5 × 2–3 px) every 6–10 px along edges, in a thread a shade darker than the top layer, half hidden; visible embroidery (running or chain stitch) only as deliberate detail.
- **Inserts**: patches of extra colour placed under a cut window (a local change of the revealed layer).
- **Fillers**: Poisson-disk placed slits (tapered lozenges), triangles and dots in leftover space, oriented to the nearest contour.
- **Drape** (optional): a WebGL pass with low-frequency displacement and normals for the cloth's softness, a breeze ripple, or the panel sewn onto a blouse.
- Masks are built once at init under a fixed seed; a cut in progress is mask erosion along its path at progress p.

## 3. Colour logic

- **3–6 cloth colours per panel**, the top layer dominant; revealed bands contrast strongly; inserts add 2–4 bright colours in small areas.
- **Every visible colour is a layer or a declared insert.** Nothing appears from nowhere.
- **Alternate light and dark** in nested channels so shapes read; black often serves as the line-like channel between brights.
- **No gradients, no prints** (one printed-cloth insert at most, as a deliberate accent).
- **Thread nearly invisible** except deliberate embroidery.
- Example: top `#c8102e`, second `#111111`, third `#f28c00`; inserts `#2a9d8f`, `#f6d32d`, `#6a3fb5`, `#e94e9a`.
- Example (cool): top `#1b1f5f`; layers `#f5f0e6`, `#d7263d`; inserts `#2ec4b6`, `#ffbf00`.

## 4. Type & subtitles

- **Words can be cut as channels**: bold rounded faces (Baloo 2, Righteous, Bungee; Devanagari in Baloo 2) with turned edges; minimum stroke 3 × channel width; short titles only.
- **Subtitles on a sewn label**: a narrow cloth band at the bottom with a turned edge and visible stitches, Baloo 2 SemiBold or Righteous 34–42 px in the band's contrasting cloth colour, matte; Hindi in Baloo 2 or Hind. Hold ≥ max(1.8 s, speech + 0.6 s).
- Never invent text in the Guna language.

## 5. Motion quality

- **24 fps**. Cloth is opaque and flat; motion comes from making it: **cuts** (scissors run along a path, the window opens, the folded rim follows 3–6 frames later, then a run of stitches), **lifts** (a layer peels back from a corner with soft drape to show a whole lower layer), **slides** (an insert slides under a window).
- **Figures** move as stacked mask groups on twos, cut-out style.
- **Channel breath**: nested channels swap their reveal order inward or outward, a native pulse.
- Cloth breathes only with slow, small drape.
- Never: brush strokes, transparency between layers, raw edges.

## 6. Camera grammar

A camera over a sewing table, close enough to see stitches. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Locked flat-lay panel | composition, symmetry | an emblem; a map; an ecosystem |
| Macro along a channel and its stitches | handwork, time | patience; craft; repair |
| Slow push into nested channels | depth through layers | a hierarchy; history; the sea floor |
| Raking light across folded rims | relief, touch | a reveal; morning; texture |
| Pan between front and back panels | two versions | before and after; two families; a debate |
| Layer peel | what lies beneath | a secret; archaeology; a hidden system |
| The panel worn, moving on a body | it is alive | identity; daily life; a festival |

Framing: show the panel's border channel in wides; fill everything; keep channels ≥ 6 px on screen. Transitions: a slit opens and widens to the next scene's colour; a layer peels away; a stitch run closes a scene; the blouse turns from front to back. Forbidden: dissolves, digital glitch.

## 7. Sound palette

- **Foley**: scissors (`sfx.click` and `clack` with a metallic ring), cloth tear (filtered noise burst), needle pull-through (a quick rising whisper of thread), thimble tap, folding and rustle.
- **Music**: panpipe-like `flute` and `recorder` with breath noise, two pipes alternating notes (hocket); rattles (`shaker`); a soft `frame_drum`; `marimba` for small plucked figures.
- **Ambience**: an island: small waves, palm wind, a paddle's splash.
- **Techniques, as options**: hocketing parts that interlock like nested channels; each cut lands on a pulse.
- **Silence**: the sea only.
- **Voice**: warm, calm; music ducked ~8 dB; −14 LUFS.

## 8. Native moves

- **Cut to reveal.** A slit opens and the colour beneath becomes the subject. *Fits content like:* the pipes under a city; the inside of a body; a secret coming out.
- **Echo outlines.** Nested channels around a shape pulse. *Fits content like:* sound waves; influence spreading; ripples on water.
- **Layer peel.** The whole top cloth lifts to show another world. *Fits content like:* geological strata; history under a town; a company's structure.
- **Filler swarm.** Slits and triangles fill empty space like a shoal. *Fits content like:* a crowd; fish; rain.
- **Paired panels.** Front and back tell two sides of one subject. *Fits content like:* two perspectives; past and present; a question and its answer.
- **Stitched closure.** A run of stitches seals an edge. *Fits content like:* an agreement; a wound healing; a repair.

## 9. Pitfalls of the medium

- Flat vector look → weave texture, folded rims, contact shadows, stitches, wobble.
- Irregular channel widths → offsets from a centreline at a fixed width.
- Colours with no layer behind them → keep a layer stack and an insert list per panel.
- Raw cut edges → always fold and stitch.
- Empty background → fillers.
- Weave moiré and stitch aliasing on moves → mipmapped, pre-filtered textures; minimum stitch size.
- **Living identity garment**: molas are worn by Guna women as part of their identity and are an important livelihood. Don't copy traditional or ceremonial designs, don't use sacred motifs as decoration, and don't present the film as authentic Guna work; credit Guna mola makers, and commission or consult them for commercial work.

## 10. Engine

No demo engine yet (draft). A first demo should build:

- `cloth.js`: `weave(colour, seed, scale)` textures.
- `stack.js`: layer masks; `cut(path, fromLayer, toLayer)`; `channel(centreline, width, depth)`; inserts; visible-colour resolve.
- `rim.js`: fold shading from mask gradients, contact shadows, `stitches(edge, spacing)`.
- `filler.js`: Poisson slits, triangles, dots oriented to contours.
- `scissors.js` (progressive erosion with fold delay), `drape.js` (WebGL displacement, wind), `mix.py`.

Start from: `styles/papercut-red/demo/paper.js` (`cut`, `cutLine`, `cutTaper`, `inset`, `paperShadow`, `holesOf`) for cut logic and shadows; `styles/engraving/demo/engine/burin.js` (`offsetRing`, `resample`, `inPoly`) for channels; `styles/silkscreen-poster/demo/engine/silk.js` (`makeTextures`, `ringPath`, `unionPath`); `core/three/post.js` for drape lighting; `core/lib.js` (`hash`, `vnoise`); `core/audio/sfx.py` (`click`, `clack`), `core/audio/sampler.py`.

## 11. Variation space

You decide the subject, the layer stack, channel width, how much is cut on screen, the opening, the ending and the camera.

- Structures: **two panels in dialogue** (front and back answer each other); **a labyrinth** (one channel leads the eye through a maze to the centre); **the sewing table** (layers basted, cut, folded and stitched into a garment).
- Openings: **a stack of plain cloth** being basted; **a single slit** opening in red; **a stitch** pulled tight in macro.
- Endings: **the last filler slit** is cut; **the panel is sewn into a blouse** and walks away; **the top layer peels off entirely**, leaving only the colour beneath.

---

Status: **draft** — no demo film yet. Before this is used as a library style it needs a demo film, `DEMO.md`, stills and the checks in the Lemo-Opuscar `MAINTAINING.md` ("Gates").
