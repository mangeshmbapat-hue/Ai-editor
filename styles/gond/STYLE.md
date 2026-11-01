# Gond — Style Prompt

> Gond painting in motion: big flat silhouettes of trees, animals and birds in bright colour on a plain ground, each body zoned and filled with rows of dots, dashes and scales that follow the form and can flow like sap.
> References (grammar only): the painting of the Pardhan Gond community of Madhya Pradesh (notably around Patangarh in Dindori district), which grew from Gond wall and floor decoration into paintings on paper and canvas from the 1980s, with its forest cosmology and each painter's own filling pattern. Take the zoned bodies, the pattern-as-skin and the plain ground; never copy a specific painting or a named painter's signature pattern, and never name them in the film.

## 1. Essence, and what it is not

- **Big flat silhouettes** with a clean dark or coloured outline: a tree with roots, a deer, a fish, a peacock, a snake. One to five large forms per frame; the ground around them is plain.
- **Bodies are zoned.** Curved guide lines divide each body into bands that follow its shape (neck, flank, leg, branch).
- **Pattern is the skin.** Each zone has a base colour and one filling pattern in a contrasting colour: dot rows, dash rows, fish scales, seed teardrops, combed lines, chevrons. Pattern elements line up along the flow of the form.
- **Bright and decisive**: saturated flat colour, no shading, no light.
- **Animals and trees are kin**: a deer's antlers can be branches, a tree's roots can be snakes; forms merge.

Not Madhubani (no double outline, the ground stays plain, pattern flows with the form instead of hatching every gap), not Copperplate Engraving (lines decorate, they do not model light), not Risograph or Silkscreen Poster (no print registration, no halftone, no ink layering), not pointillism (dots never mix colours optically; they are drawn marks in rows).

## 2. Materials & rendering

- **Ground**: paper or canvas, plain cream, white or one flat colour (deep blue, black, ochre); a faint canvas weave or paper grain, cached and world-anchored.
- **Silhouette**: each form is a closed Bézier shape filled flat, outlined with a 3–6 px line (black or a dark hue) with ±5 % width noise. Shapes are authored in local coordinates.
- **Zoning**: guide curves as contour offsets (bands stepping inward) or streamlines of a flow field from the shape's spine split the body into 3–9 zones, each edged with a thin line.
- **Pattern elements** are drawn marks, never tiles: `dots` (2–6 px, irregular), `dashes`, `scales`, `seeds` (teardrops), `comb`, `chevrons`, placed along streamlines at 1.6–2.2× their size, oriented to the flow, ±10 % size and ±8° jitter (seeded).
- **Signature set**: a film chooses 3–5 pattern elements as its own vocabulary and uses them consistently, the way each painter has a recognisable fill.
- **Order**: fill → outline → guides → patterns row by row. Finished forms are cached as sprites; animated forms keep marks in spine coordinates. Pattern **phase** along each streamline makes marks travel. Everything is a pure function of t under fixed seeds.

## 3. Colour logic

- **Ground is one plain value**; forms carry all colour. Never pattern the ground.
- Each zone = **base hue + pattern hue** with strong contrast (yellow dots on red, white dashes on blue, black scales on orange).
- 5–8 saturated hues per film, plus black and white; neighbouring zones never share a base hue.
- No gradients, shading, glow or transparency. Night is a dark ground, not darker forms.
- One hue may be reserved for the living force the film is about (all sap, all water, all breath).
- Example: ground `#f4ede0`, outline `#1b1b1b`, red `#d2352b`, yellow `#f2c230`, blue `#2f6db5`, green `#3b9a4a`, orange `#ec7a24`, pink `#e75b8f`. Example night: ground `#141c3a` with the same hues and white marks.

## 4. Type & subtitles

- Words stand on the plain ground like a small painted form: **Baloo 2** (600–800) for titles (70–120 px), letter bodies filled with one dot or dash pattern in a second colour; **Mukta** or **Hind** for subtitles (36–44 px).
- Devanagari: Baloo 2 for titles, Mukta or Hind for subtitles; Hindi subtitles are supported.
- Subtitles: centred low on the ground, dark on light grounds or white on dark, no box; a thin flat outline (2 px) of the ground colour where they cross a form. Fade in 0.2 s. Hold each ≥ max(1.8 s, speech + 0.6 s).

## 5. Motion quality

- **24 fps** for camera and pattern flow; body animation on twos (12 fps).
- **Pattern flow is the main motion**: phase advances along streamlines (0.2–1 element per second), so a trunk seems to carry sap, a fish to breathe, a river to run. It never jitters.
- Bodies move as flat rigs: a neck bends, a wing pivots, a tree sways about its root (skew 0.4–1°); pattern follows the bend.
- **Growth**: a tree grows branch by branch (each branch a silhouette scaling out from its joint with `eo`), then its zones fill row by row.
- **Transformation**: one silhouette morphs into another along matched contour points (a root into a snake, a branch into an antler) while patterns re-flow.
- Appear: fill pops (0.15 s), outline draws, patterns fill; disappear: patterns drain, silhouette fades. Never moves: the ground; no shake, no parallax.

## 6. Camera grammar

A painted sheet: the camera moves over it flat, and the forms carry the action.

| Move | What it expresses | Can serve |
|---|---|---|
| Locked frame on one great form | presence, a world-tree | an ecosystem; an institution; a family |
| Slow push into one zone of pattern | the texture of life | cells; a crowd; a material |
| Pan along a long form (a snake, a river, a root) | connection, continuity | a supply line; a migration; a lineage |
| Tilt from roots to crown | depth to height | growth; history to now; underground to sky |
| Pull back from pattern to the animal it is | the small makes the large | a community; data into meaning |
| Cut on a shape match (antler to branch) | kinship between things | analogy; inheritance; cause and effect |
| Locked frame, forms growing in | building up | a project; a season; a city plan |

Framing: one hero form fills 50–80 % of the frame with plain ground around it; never crop through a head. Transitions: a shape match; patterns draining and refilling as the next form; a pan along a connecting root. Forbidden: dissolves, depth of field, perspective, motion blur.

## 7. Sound palette

- **Instruments as options**: a bowed fiddle voice in the bardic manner (`erhu` pitched down, a nasal formant, slides), barrel drums (`frame_drum`, `conga` low tones, the synthesised tabla model detuned rounder), bamboo flute (`flute`, `recorder`), plucked drone (`pluck('shamisen', …)` with buzz), rattles (`shaker`) and small bells. Never imitate a recorded song of the community.
- **Pattern sounds**: a row filling = one soft `kalimba` or `marimba` note; flowing patterns get a low shimmer pad (filtered noise + sine cluster).
- **Foley**: synthesised birds, hooves on leaves, wind in branches, water, insects.
- **Silence**: patterns stop flowing, only the forest bed or nothing.
- **Voice**: a storyteller's warmth, unhurried; Hindi narration fits. Music ducked ~8 dB under voice; −14 LUFS.

## 8. Native moves

- **Pattern flow.** Marks travel along streamlines inside a form. *Fits content like:* water through a city; money through an economy; blood in a body.
- **Zone by zone.** A form fills one zone at a time, each zone a chapter or a part. *Fits content like:* the parts of an engine; the stages of a life; departments of a company.
- **Kinship morph.** One form grows into another along matched contours. *Fits content like:* a seed into a tree into a house; a problem into its solution; an ancestor into a descendant.
- **The world-tree.** One great tree carries every subject on its branches, in its roots and in its birds. *Fits content like:* a family history; an organisation chart; a food web.
- **Pattern swap.** Same silhouette, new filling pattern, new meaning. *Fits content like:* healthy vs sick; day vs night; before vs after.
- **Ground flip.** The plain ground changes from cream to night while every form stays. *Fits content like:* a day's end; a mood turning; a hidden side revealed.

## 9. Pitfalls of the medium

- Patterns pasted as bitmap tiles read as wallpaper → place each mark along streamlines with jitter.
- Patterns that ignore the form → orient to the flow field; zones follow anatomy.
- Patterned ground reads as Madhubani → keep the ground plain.
- Too many small forms → few large ones; pattern is the detail.
- Pattern flow too fast reads as a loading spinner → ≤ 1 element per second.
- Shading or highlights creep in → flat only; volume comes from zone curves.
- **Sacred motifs and signatures.** Gond paintings carry the community's deities and cosmology, and many painters treat their filling pattern as a personal signature: do not use deities as decoration, and do not copy a known painter's pattern. Do not present a code-made film as authentic Gond painting; for commercial work, credit or consult Gond artists.

## 10. Engine

No demo engine yet (draft). A first demo should build:
- `form.js`: `form(beziers, {outline, seed})`, `spine(form)`, `bend(form, t)`, `morph(a, b, p)` (matched contour sampling).
- `zones.js`: `contourBands(form, n)`, `flowField(form)`, `streamlines(zone, spacing)`.
- `marks.js`: `dots`, `dashes`, `scales`, `seeds`, `comb`, `chevrons` placed along streamlines with `phase`, `jitter`, `seed`; `signature(set)`.
- `sheet.js`: grounds, sprite cache, subtitles, `render(t)`.

Start from `styles/engraving/demo/engine/burin.js` (`resample`, `normals`, `offsetRing`, `hatchAlong`, `contourHatch`, `stipple`), `styles/woodcut/demo/engine/hatch.js` (direction fields `dirContour`, `dirRadial`), `styles/one-line/demo/geom.js` (path sampling), `core/lib.js` (`mulberry`, `vnoise`, `eo`, `eio`), `core/render/`, `core/audio/sampler.py`, `core/audio/pluck.py`.

## 11. Variation space

You decide the forms, the signature pattern set, the ground, what flows and what stays still, the opening, the ending, the camera path and the pacing.

- Structures: **one tree, many lives** (the camera visits each branch and root); **a chain of morphs** (each form becomes the next, a story told by transformation); **two grounds** (the same forms by day and by night, patterns changing meaning).
- Openings: **one mark**, a single dot that becomes a row, a zone, an animal; **a plain ground** with one silhouette filling flat before any pattern; **mid-flow**, a close-up of flowing dashes pulled back to reveal the river.
- Endings: **patterns stop flowing**, the forest at rest; **everything returns to the tree**; **the ground turns night** and only the white marks remain.

---

Status: **draft** — no demo film yet. Before this is used as a library style it needs a demo film, `DEMO.md`, stills and the checks in the Lemo-Opuscar `MAINTAINING.md` ("Gates").
