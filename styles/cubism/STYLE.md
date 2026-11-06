# Cubism — Style Prompt

> One subject seen from several sides at once and broken into overlapping planes: shards of muted ochre, grey and green, each holding a different view, with lines that start and stop and letters pasted in like newsprint.
> References (grammar only): Analytic Cubism (Pablo Picasso and Georges Braque, c. 1909–12) for faceting, passage between planes and a near-monochrome palette; Synthetic Cubism and papier collé (Braque, Picasso, Juan Gris, 1912–14) for flat cut planes, imitation wood grain, stencilled letters and pasted paper; Paul Cézanne's late still lifes for tilted tables and shifting viewpoints; Fernand Léger's *Ballet mécanique* (1924) for a cubist film's repetition and fragmented objects. Never reproduce a specific painting or its figures, and never use a real newspaper masthead or label.

## 1. Essence, and what it is not

- **Simultaneity**: one subject drawn from 2–5 viewpoints in the same frame: a profile nose with a frontal eye; a table seen from above, a bottle from the side.
- **Facets, not shapes**: the image is planes with straight or gently curved edges, each with its own light-to-dark ramp, unrelated to a single light source.
- **Passage**: plane edges break off so one plane flows into the next.
- **Two modes, one per film**: *Analytic* (small facets, brushed hatching, earth tones) or *Synthetic* (large flat cut planes, textures, pasted paper, a few brighter colours).
- **Everyday subjects made strange**: tables, glasses, bottles, instruments, pipes, newspapers, fruit, portraits, cafés.

Not Stained Glass (opaque planes, no lead, no transmitted light), not a kaleidoscope (no mirror symmetry), not a Voronoi or shatter filter over a render (facets follow the subject's planes and viewpoints), not 60s Spy Titles (no silhouettes on flat colour), not Impasto (no knife ridges).

## 2. Materials & rendering

- **Hidden 3D**: a three.js scene of simple models (lathe bottles, box tables, a sphere-and-cylinder head) rendered from K = 2–5 cameras into render targets holding tone (Lambert luminance), normal and object ID.
- **Facet partition**: a planar arrangement of lines (dominant verticals and horizontals, 30–60° diagonals taken from the subject's contours in the depth and normal buffers, a few free cuts, occasional arcs for shoulders and sound holes) split into polygons. Cached per shot; regenerated only on a "turn".
- **Viewpoint assignment**: each facet samples one camera, by design (face region → profile or front) or by seeded hash weighted toward the main view.
- **Facet shading**: a linear ramp across each facet from a light edge to a dark edge, mixed ~50 % with the sampled tone; neighbours alternate light-against-dark at shared edges.
- **Lines**: facet edges as charcoal-like brush lines 1.5–4 px, drawn for only part of their length (passage), darker where planes overlap.
- **Analytic surface**: short directional brush hatches along each ramp in 3–5 tones, canvas weave under thin paint.
- **Synthetic surface**: flat fills plus textures: comb-drawn imitation wood grain, invented newsprint (columns of nonsense text), wallpaper patterns, sand grain, stippled dots. Pasted pieces sit on their own layer with a thin paper shadow, slightly misaligned, cut or torn edges.
- Deterministic: every texture, line break and hatch from seeded noise; the world never moves on its own.

## 3. Colour logic

- **Analytic**: 1–2 hues plus neutrals (ochre, umber, grey-green, slate, bone white, near-black); value carries everything; no accent.
- **Synthetic**: 4–6 flat colours including one or two brighter notes (a blue, a red), plus brown, black and white textures; one accent colour reserved for the subject's key object.
- Value contrast lives at facet edges: a light plane against a dark neighbour.
- Never: saturated gradients, glossy highlights, naturalistic skin colour, pure white backgrounds.
- Example Analytic: `#c9b48a` ochre, `#8a7a5a` umber, `#5f6b5c` grey-green, `#3b3a36` dark, `#e8e0cc` bone.
- Example Synthetic: `#2f4a7a` blue, `#b8423a` red, `#d8c9a0` paper, `#7a5a3a` wood grain, `#1e1e1e` black.

## 4. Type & subtitles

- **Letters are part of the picture**: stencilled fragments (Allerta Stencil, or bridges cut into Oswald), newsprint serif (EB Garamond), typed scraps (Special Elite); rotated, partly covered by facets, showing 3–6 letters of a word.
- Devanagari fragments: bridges cut into Mukta Bold glyphs, keeping the headline stroke readable.
- **Titles** assembled from pasted letters of mixed sources, ≥ 120 px.
- **Subtitles** are printed on a strip of newsprint-coloured paper pasted at the bottom (rotation ≤ 1°, thin paper shadow): EB Garamond 36–42 px near-black; Devanagari in Tiro Devanagari Hindi. Subtitles are never fragmented or covered. Hold ≥ max(1.8 s, speech + 0.6 s).

## 5. Motion quality

- 24 fps. The painting itself is still; change comes in stepped events.
- **The turn**: an object "rotates" by facets switching to the next viewpoint one after another in a ripple, each switch a 2–4 frame slide or flip.
- A gesture shows as two positions coexisting (an arm in two places) rather than a movement between them.
- Facet geometry may drift ±1–3 % over several seconds to keep the canvas alive; otherwise it holds.
- Appear: facets are brushed in (Analytic) or arrive as pasted paper and press flat (Synthetic). Disappear: facets fall away or are covered by a new pasted plane.
- Never moves: the frame edges; the tilted tabletop that serves as the stage.

## 6. Camera grammar

The camera hardly moves; the viewpoints do. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Locked frontal tableau | contemplation of the whole | a still life; a portrait; a café table |
| Facet turn (subject turns, camera does not) | seeing every side | an argument; a personality; an object explained |
| Push into one facet that opens onto another view | entering a viewpoint | a memory; a character's view; a detail |
| Viewpoint count rising, 2 → 5 | complexity growing | confusion; a crowd; a debate |
| Viewpoint count falling to 1 | clarity | an agreement; a solution; a pause |
| Lateral slide of the facet grid | passing time or travel | a street; a train window; a day |
| Pasted fragment slapped on | a fact from outside | a headline; a ticket; a letter |

Framing: centre-weighted pyramidal or oval composition, the subject filling 60–80 %, edges dissolving into faint facets. Transitions: facet-by-facet re-assignment to the next scene, a pasted plane covering the frame, a plane sliding over; no crossfades.

## 7. Sound palette

- Café and studio instruments: nylon or acoustic guitar (`core/audio/pluck.py`), a mandolin-like tremolo (banjo pluck, short decay), clarinet, accordion, violin, piano, contrabass_pizz; light percussion.
- **One motif, several sides**: the same short phrase played by different instruments at once with offsets, cut into cells and re-ordered, canon-like; the ensemble stays small.
- Foley: glass clink, cork, pipe tap, a guitar body knock, paper being pasted and smoothed, scissors, café room tone.
- Silence: all instruments stop; one plucked string.
- Voice: two or more voices describing the same thing from different sides, overlapping slightly, dry. Music ducked ~8 dB under voice; −14 LUFS.

## 8. Native moves

- **Several sides at once.** Profile and front, top and side share one image. *Fits content like:* a person seen by family and colleagues; a product's every feature; a city from street and roof.
- **The turn without a camera.** Facets ripple to the next view. *Fits content like:* a sculpture explained; a chair designed; a story told from another witness.
- **Tilted table.** The surface tips up so everything on it can be read. *Fits content like:* a recipe's ingredients; a desk's clutter; a game board.
- **Pasted fact.** A fragment of printed matter enters the painting. *Fits content like:* a date; a price; a train ticket.
- **Looking longer.** A familiar object splits into more and more facets, then recomposes. *Fits content like:* overthinking; scientific analysis; a memory examined.
- **Passage.** Two objects merge through shared planes. *Fits content like:* a musician and the instrument; a city and its river; two friends' viewpoints.

## 9. Pitfalls of the medium

- **Random shatter look** → derive cut lines from the subject's contours plus a dominant grid.
- **Unreadable subject** → keep 2–3 anchors intact (an eye, a bottle neck, a sound hole).
- **Too many viewpoints** → at most 5, most facets from the main view.
- **Real brands in collage** → generated nonsense text, invented names, no logos.
- **Clean digital lines** → broken, varied-width brush lines and hatching.
- **Too much colour in Analytic mode** → earth tones and value only.
- **Restless canvas** → facets change only on events; drift stays tiny.

## 10. Engine

No demo engine yet (draft). A first demo should build:
- `views.js`: three.js scene rendered from K cameras into tone, normal and ID targets.
- `facets.js`: `buildFacets(lines, bounds)` → polygons; `assignViews(facets, rule, seed)`; `turn(facets, fromView, toView, t)`.
- `paint.js`: facet ramps, directional hatches, broken edges, canvas weave.
- `collage.js`: wood-grain comb, newsprint generator, stencil bridges, pasted pieces with paper shadows.
- Start from `styles/stained-glass/demo/glass.js` (polygon pieces, `voronoi`, `seedsIn`, `softPoly` — swap lead cames for broken brush edges), `styles/woodcut/demo/engine/hatch.js` (hatching that follows a tone field), `styles/papercut-red/demo/paper.js` and `styles/spy-titles/demo/glyph.js` (cut pieces, paper shadows, letters as paths), `core/three/post.js` (render targets), `core/lib.js`; music via `core/audio/sampler.py` and `core/audio/pluck.py`.

## 11. Variation space

The agent decides the subject, Analytic or Synthetic mode, the number of viewpoints, which objects stay readable, and what is pasted in.

- Structures: **one object, five sides** (each section adds a viewpoint until the object is fully known); **a conversation at a table** (each speaker's turn re-assigns facets to their view); **a day in a café** (the facet grid slides as time passes, pasted fragments marking the hours).
- Openings: **a single realistic view** that cracks into its first facet; **a pasted scrap of text** around which the painting grows; **a blank tilted tabletop** onto which objects arrive from different sides.
- Endings: **the viewpoints collapse to one** and the object is simply itself; **a final pasted plane** covers all but one facet; **the facets recompose** into a different object than the one we started with.

---

Status: **draft** — no demo film yet. Before this is used as a library style it needs a demo film, `DEMO.md`, stills and the checks in the Lemo-Opuscar `MAINTAINING.md` ("Gates").
