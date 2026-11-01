# Pointillism — Style Prompt

> A picture built from separate dabs of pure, unmixed colour that blend only in the viewer's eye: up close a field of dots, at a distance a calm, luminous scene in bright outdoor light.
> References (grammar only): Georges Seurat (1880s) for equal-sized dabs, the stillness of figures and contrast halos along every edge; Paul Signac (1890s–1900s) for larger, mosaic-like dabs and saturated complementary pairs; Michel-Eugène Chevreul's law of simultaneous contrast for which colours sit side by side; the dotted painted borders some divisionist canvases carried. Never reproduce a specific painting's composition or figures.

## 1. Essence, and what it is not

- **Dabs of pure colour, all about one size**, on a white ground, never blended on the canvas: mixtures exist only optically.
- **Every area holds 3–5 pigments**: local colour, a warm light, a reflected colour, and its complement in the shadows.
- **Halos at edges**: along a light–dark boundary the light side brightens and the dark side darkens.
- **Stillness**: figures in profile or frontal, simplified into geometric silhouettes; motion is slow and measured.
- **Distance is the image**: far away the colour mixes; close up the picture dissolves into abstract dots, and the camera can travel between the two.

Not Impasto (no knife planes or ridges), not Risograph or Halftone Dossier (print dots on a screen that vary in size; here dabs are placed by hand, one size, varying in colour), not Watercolor (no translucent washes), and not a "pointillise" photo filter: each dab is a pure pigment chosen by optical mixing, not the sampled colour of a photograph.

## 2. Materials & rendering

- **Ground**: white primed canvas with a fine weave, showing in the gaps between dabs (5–15 % uncovered).
- **Dab**: a short rounded mark 6–12 px at 1080p (one size per film, ±15 % jitter), aspect 1.2–1.6, oriented by a slow direction field or by area (horizontal for water, vertical for grass), opaque, with an optional tiny ridge highlight.
- **Renderer**: WebGL2 instanced quads with an SDF dab shape; per instance: position, size, angle, pigment index, seed. 50 k–400 k dabs per frame.
- **Colour field**: the scene is first rendered as flat shapes (Canvas 2D or a three.js render target) at low resolution: that is the target colour per pixel, never shown.
- **Optical decomposition**: a fixed set of 10–14 pigments. A 32³ LUT maps each target colour to its top 4 pigments and weights so that their average **in linear RGB** matches the target, biased toward complements in shadow and warm pigments in light. Each dab picks one pigment by comparing its seeded hash with the cumulative weights: deterministic and stable while its target is stable.
- **Anchoring**: background dabs are scattered once (Poisson disc) in world space; moving figures carry their own dabs in object space. A dab never re-randomises its position from frame to frame.
- **Dab scale**: within a shot the dab set is fixed to the world; between shots it is regenerated so on-screen size stays in range. Only a deliberate push-in lets dabs grow.
- **Halos**: an edge mask from the colour field's luminance gradient shifts pigment choice within ~2 dabs of an edge.
- **Shimmer**: water and sky dabs re-pick their pigment on twos with 5–10 % probability; everything else holds.
- Optional painted border: a band of dabs complementary to the adjacent picture edge.

## 3. Colour logic

- **Pigments, not mixtures**: 10–14 pure, saturated hues plus white. No black: darks are deep blue, violet and red-brown dabs together.
- High key, compressed values: sunlight scenes; the darkest value is a mid-dark.
- Each area = local colour + warm light + reflected colour + complement in shadow.
- A pure vermilion is reserved for small focal points (a parasol, a sail, a scarf).
- Never: grey dabs, black outlines, gradients inside a dab, mixing in sRGB.
- Example pigment set: white `#f4f1e8`, yellow `#f6d34a`, orange `#f29a3a`, vermilion `#e0483a`, rose `#c94f8a`, violet `#7a4fb3`, ultramarine `#2f4fb0`, cobalt `#3d8fd1`, viridian `#2fa58a`, emerald `#7cbf4a`, ochre `#b9873f`.
- Example twilight shift: drop yellow and orange to a third of their weight, add violet and cobalt.

## 4. Type & subtitles

- **Titles are painted in dabs**: letters as a mask filled with dabs, ≥ 160 px so they read; Cormorant Garamond or Playfair Display for the period, Limelight for a poster flavour.
- **Subtitles are clean, not dotted**: Cormorant Garamond SemiBold italic 38–44 px, deep ultramarine-violet over a soft pale halo, bottom centre; Devanagari in Tiro Devanagari Hindi. Hold ≥ max(1.8 s, speech + 0.6 s).
- No HUD, no labels; if a number is needed it is spoken or painted in dabs.

## 5. Motion quality

- 24 fps. Carried dabs move on ones with their objects; shimmer updates on twos.
- Slow and measured: figures glide or stand; a walk is a slow translation with a tiny bob; easing `ss` and `eio` with long durations.
- **Painting-in**: dabs appear in passes (local colour, then complements, then halos).
- **Dab migration**: to change scene, each dab travels to a target position in the next image and takes its pigment there; since both images are made of the same dabs, it is a morph without a dissolve.
- Exits: dabs lift off and scatter, or fall back to bare canvas.
- Never moves: the canvas weave, the border, the sun (unless the day itself is the subject).

## 6. Camera grammar

A painter's distance that can change. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Locked wide tableau | calm, the whole scene at once | a park; a beach; a market at rest |
| Very slow lateral pan | a promenade | a riverbank; a street; a procession |
| Push-in until the image dissolves into dabs | how it is made; meaning slipping | a memory; analysis; a closer look at data |
| Pull back from dabs to image | understanding emerging | a reveal; a summary; a resolution |
| Locked view, light changing | light as the subject | a day; a season; ageing |
| Profile tableau with figures crossing | the ritual of daily life | a routine; a queue; a parade |
| Coarse-to-fine dabs on a locked frame | attention sharpening | a decision; an arrival; recognition |

Framing: horizontal compositions, horizon on a third, verticals of trees and figures as rhythm; a figure is ≥ 60 dabs tall; no extreme close-up unless the dissolve is the point. Transitions: dab migration, painting-in, pigment-swap dissolve (each dab switches when its own hashed threshold passes); never an optical crossfade of two frames.

## 7. Sound palette

- **Musical pointillism**: a melody split note by note across instruments (harp, flute, piccolo, clarinet, oboe_stac, violins_pizz, glockenspiel, vibraphone, marimba), short notes in an airy texture over long bowed tones (violas, cellos).
- **A sound made of dots**: granular clouds of short sampled grains, seeded, with density following the picture's activity.
- Foley: quiet brush taps for painting-in; water lapping, oars, birds, distant voices, wind in poplars.
- Silence: the dabs freeze, only ambience remains.
- Voice: calm, unhurried narrator. Music ducked ~8 dB under voice; −14 LUFS.

## 8. Native moves

- **Dissolve into dots.** A push-in turns a face or object into abstract colour. *Fits content like:* how a screen makes colour; a memory losing detail; a crowd as individuals.
- **Emerge from dots.** Scattered dabs settle and a picture appears. *Fits content like:* a census becoming a portrait; a mosaic of donors; a team forming.
- **Light swap.** On a locked view every dab re-picks its pigment as the hour changes. *Fits content like:* a day at a harbour; climate seasons; a mood shift.
- **Dab migration.** One image morphs into the next by moving its dabs. *Fits content like:* a caterpillar to a butterfly; a village to a town; a sketch to a product.
- **Mixture as quantity.** The ratio of two pigments in an area encodes a measured value. *Fits content like:* air quality across a city; ripeness of fruit; a vote share.
- **Halo of light.** A figure glows by its edge contrast alone. *Fits content like:* a hero singled out in a crowd; a lit window at dusk; the one person who notices.

## 9. Pitfalls of the medium

- **Swimming dots** → anchor dabs to world or object; shimmer only on twos at low probability.
- **Muddy colour** → average in linear RGB, a small pigment set, no grey dabs.
- **Photo-filter look** → pure pigments, an orientation field, halos, simplified forms, no outlines.
- **Unreadable faces and hands** at dab size → simplify forms, keep figures large, prefer profiles.
- **Regular-grid patterning** → Poisson disc with jitter, never a lattice.
- **Compression smear** → dabs ≥ 6 px; encode at a high quality setting in `core/render/mux.sh` and check the file at 100 %.

## 10. Engine

No demo engine yet (draft). A first demo should build:
- `dabs.js`: instanced WebGL2 renderer `makeDabs(gl, max)`, per-instance buffers, SDF dab shader, canvas weave ground.
- `field.js`: renders the hidden colour field (Canvas 2D shapes or a three.js render target).
- `pigment.js`: pigment set, `buildLUT(pigments, {shadowBias, lightBias})`, `pick(seed, weights)`.
- `scatter.js`: Poisson-disc sets in world and object space, per-shot regeneration.
- `halo.js`, `migrate.js`: edge mask; dab correspondence between two images (sort by position and pigment, then pair).
- Start from `styles/impasto/demo/engine/impasto.js` (instanced stroke renderer with a per-stroke layout), `styles/crayon-book/demo/gl.js` (paper-tooth compositor), `styles/risograph/demo/riso.js` (dot shading and paper); `core/lib.js` (`mulberry`, `hash`, `vnoise`, easing); music via `core/audio/sampler.py`.

## 11. Variation space

The agent decides the place, the pigment set, the dab size, whether the border is painted, the time of day and how often the camera breaks the image into dots.

- Structures: **one place through one day** (a locked view whose pigments change hour by hour); **near and far** (each section alternates a dissolve into dots with a pull back to a new place); **a portrait gallery** (profile figures, each emerging from dabs and saying one line).
- Openings: **bare canvas** that fills pass by pass; **an extreme close-up of dabs** pulled back into a riverbank; **a single vermilion dab** that becomes a parasol.
- Endings: **the dabs scatter** back to bare canvas; **a pull back** until the painting, with its dotted border, is a small rectangle; **dusk** until only blue and violet dabs remain.

---

Status: **draft** — no demo film yet. Before this is used as a library style it needs a demo film, `DEMO.md`, stills and the checks in the Lemo-Opuscar `MAINTAINING.md` ("Gates").
