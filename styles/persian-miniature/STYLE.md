# Persian Miniature — Style Prompt

> Persian manuscript painting brought to life: a jewel-coloured world seen from several heights at once (gardens and pools laid flat from above, pavilions in elevation, small elegant figures on rising planes) inside ruled gold margins with panels of text.
> References (grammar only): Persianate painting of the Timurid and Safavid workshops (Herat, Tabriz, Isfahan; 15th–17th c.) for tilted, stacked space, patterned surfaces, spongy rocks and gold skies; the illuminated manuscript page (rulings, text panels, illuminated headpieces, gold-flecked margins) for the frame. Never copy a specific painting, an illustrated scene from a named poem or a manuscript layout, and never name them in the film.

## 1. Essence, and what it is not

- **Many viewpoints at once**: the ground tilts up to fill the picture; pools, carpets and garden beds are seen from directly above; walls and pavilions in elevation; no single vanishing point, no cast shadows.
- **Every surface patterned**: tiles, carpets, textiles, arabesque panels, flowering trees, all at a fine scale.
- **Jewel pigments and metal**: lapis blue, malachite green, vermilion, white, gold skies and rulings, silver water (often tarnished dark).
- **Small, slender figures** with round faces, in groups and elegant gestures; size follows the story, not optics.
- **The page frame**: ruled margins and text panels that cut into the picture; a tree or a rock may break out over the rulings into the margin.

Not Ukiyo-e (no woodblock, no bokashi, no single-view space; painted with gold and pattern), not Isometric Picture Book (no true isometric, no modern flat colour: viewpoints are mixed and every surface patterned), not the sibling draft Mughal Miniature (which leans toward modelled portraits and recorded events; here space is lyrical, flat and stacked).

## 2. Materials & rendering

- **Folio** (cached): burnished cream paper (fine fibres, faint sheen); margins of tinted paper with gold flecks (instanced flakes that glint); ruling bands in gold, blue, red and black around the picture; text panels as ruled cells.
- **Paint**: opaque flat body colour with slight brush granularity (1–2 % noise), fine dark outlines (0.7–1.5 px at 1080p), interior detail as fine lines. Patterns are motif generators (arabesque spirals, hexagon and star tiles, carpet borders, floral sprays) clipped into regions.
- **Space is planes**: ground polygons stacked up the page (higher = farther), each flat; buildings as frontal elevations; carpets and pools top-down; occlusion by stacking order only.
- **Landscape kit**: spongy rocks of layered lobes with pale edges; tall dark cypresses; blossoming fruit trees (blossom dots); plane trees with hand-shaped leaves; a stream as a silver ribbon with curling ripples.
- **Figures** are cut-out sprites with pivots (head, arms, sleeves, a held cup or book), built once.
- **Gold**: a 2D metallic term (a sheen gradient keyed to camera position plus grain) so gold moves with the camera; **silver** is a dark tarnished grey with a faint sheen.
- **No light direction** in the painting: no shading, no cast shadows; only metal reacts to the camera.
- Each plane is cached at 1.5× for push-ins; patterns are pre-rendered and mip-filtered. Everything is a pure function of `t`.

## 3. Colour logic

- **5–7 pure pigments + gold + paper**; flat, saturated, high-key except lapis and tarnished silver.
- **Each figure's garment is one colour** with its pattern in a second; neighbouring figures differ in hue.
- **Gold is reserved** for skies, crowns, rulings and illumination; never for ground.
- **Value order**: garments most saturated; grounds pale (soft greens, ochres, lilac, rose); skies gold or deep lapis with star dots. No atmospheric perspective, no gradients.
- Example: lapis `#1f3f9a`, turquoise `#2aa6a0`, malachite `#3f8f4a`, vermilion `#d8402b`, saffron `#e9b23a`, rose `#e8a0a8`, lilac ground `#c9b6d8`, paper `#f2e6c9`, gold `#c9a23f`, tarnished silver `#3b3f44`.

## 4. Type & subtitles

- **Subtitles live in a text panel**: a gold-ruled cartouche in the lower margin, cream or lapis ground, Cormorant Garamond or EB Garamond Italic 32–40 px in dark ink or gold; Hindi in Tiro Devanagari Hindi or Noto Serif Devanagari. The ruling draws on, then the text appears. Hold ≥ max(1.8 s, speech + 0.6 s).
- **Titles** sit in an illuminated headpiece (gold and lapis arabesque), Cormorant Garamond SC or Playfair Display.
- **Persian script** (Noto Nastaliq Urdu or Amiri) only for real, reviewed text. Never pseudo-script, never religious verses as ornament.

## 5. Motion quality

- **24 fps**; figures **on twos** as cut-out puppets: gestures (a finger raised to the lips in wonder), head turns, a horse's prance, a cup offered; small, graceful amplitudes and long holds.
- **Environment life**: stepped ripples on silver water, birds in 2-frame cycles, falling blossom dots, banners and tassels swaying.
- **Planes unfold**: a plane can rise from top-down to upright elevation like a page standing up: the medium's native transformation.
- Parallax between planes stays small (≤ 2–4 % of frame) so the page stays a page. Gold glints shift with the camera.
- Never moving: rulings, text panels once revealed, the folio.

## 6. Camera grammar

The camera reads a book: it climbs the page, glides over gardens and turns folios. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Whole folio, margins visible | the book, order | a poem; a chapter; a map |
| Rise up the stacked planes | farther is higher | a road to a palace; a mountain pass; a day's travel |
| Top-down glide over beds and pool | the order of a garden | a design; abundance; a plan |
| Push into a pavilion window | inner life | a conversation; a secret; study |
| Lateral track along a procession | many with one purpose | a caravan; a festival; a court |
| Pull back from a detail to the folio | context | a revelation; a summary |
| Page turn | a new chapter | a new episode; a new day |

Framing: margins in wides; figures small (6–14 % of frame height in wides), groups rising diagonally up the page; text panels never cover faces. Transitions: page turns, a gold ruling drawing a new frame, a plane unfolding. Forbidden: lens blur and depth of field (there is no optical space), crossfades, cast shadows.

## 7. Sound palette

- **Persian classical families, approximated**: long-necked lutes (`pluck('shamisen')` with low buzz, or `pipa`, with glides for microtonal inflections), hammered dulcimer (a bright, short `pluck('koto')` excitation in fast double strikes, or `dan_tranh_trem`), spike fiddle (`erhu`: slides, nasal), reed flute (`flute` with heavy breath noise and slow vibrato), goblet drum (darbuka doom/tak), frame drum (`frame_drum` + `tambourine` jingles).
- **Modal colour**: non-tempered inflections by pitch bend; never a known composition.
- **Foley**: fountain (filtered noise + drips), synthesised birdsong (sine sweeps), wind in cypresses, silk rustle, hooves on stone, page turns, the crackle of gold leaf.
- **Silence**: the fountain alone.
- **Voice**: a poetic narrator, measured, light hall reverb; music ducked ~8 dB; −14 LUFS.

## 8. Native moves

- **The page unfolds.** A plane rises from plan to elevation. *Fits content like:* a building being designed; a city plan becoming a street; a memory taking shape.
- **Climb the planes.** Travel up the page is travel into distance. *Fits content like:* a journey's stages; a social ladder; a mountain crossing.
- **Breaking the frame.** A tree or figure grows over the ruling into the margin. *Fits content like:* an idea outgrowing its limits; an escape; growth.
- **Pattern spreads.** Tiles and carpets fill surface after surface. *Fits content like:* a house prepared for guests; a garden's design; a trade network.
- **Text and image answer.** A panel of words appears; the picture responds. *Fits content like:* a poem; a recipe; a lesson.
- **Gold to lapis.** The sky turns from gold to night blue with star dots. *Fits content like:* a day ending; a change of mood; years passing.

## 9. Pitfalls of the medium

- One-point perspective creeping in → plan each scene as stacked planes, elevations and top-down carpets.
- Shading and cast shadows → remove; volume comes from pattern and overlap.
- Figures too large (portrait feel) → small groups; the setting carries the scene.
- Pattern moiré on moves → render at 1.5–2× and mip-filter; avoid fine pattern on fast pans.
- Gold painted as yellow → metallic sheen that moves with the camera, gold flecks.
- Fake script → only real, verified text, otherwise Latin or Devanagari panels.
- **Respect**: much of this tradition illustrated poetry and history, but some manuscripts carry religious subjects. Don't use religious figures, verses or sacred calligraphy as ornament, avoid orientalist fantasy, and don't present the film as an authentic manuscript painting; credit the tradition, and consult or commission living miniature painters for commercial work.

## 10. Engine

No demo engine yet (draft). A first demo should build:

- `folio.js`: paper, gold-fleck margins, rulings, text panels, headpiece.
- `planes.js`: stacked layout; `unfold(plane, p)` from plan to elevation.
- `pattern.js`: `clipPattern(region, motif, scale)` with tile, carpet and arabesque motifs.
- `flora.js` (cypress, blossom tree, plane tree, flowers), `rocks.js` (lobed rocks), `figure.js` (pivot rigs).
- `gold.js` (sheen keyed to camera, flakes), `mix.py`.

Start from: `styles/ukiyoe/demo/print.js` (`fillPath`, `line`, `poly`, `cartouche`); `styles/art-deco/demo/engine/deco.js` (`goldGrad`, `goldFlat`, `sparkle`, `rules`) for gold and rulings; `styles/papercut-red/demo/rig.js` (`put`, `solveRig`) for cut-out figures; `styles/stained-glass/demo/glass.js` (`voronoi`, `seedsIn`) for blossoms and rock lobes; `styles/silkscreen-poster/demo/engine/silk.js` (`polyPath`, `ringPath`); `core/lib.js`; `core/render/still.mjs`; `core/audio/pluck.py`, `core/audio/sampler.py`.

## 11. Variation space

You decide the subject, the number of folios, the plane layout, the palette within the rules, the opening, the ending and the camera.

- Structures: **a book of seasons** (one garden over four folios); **a caravan** (one procession continuing across many pages); **a city from above** (planes unfold street by street).
- Openings: **a closed binding** opening to the first folio; **a gold sky**, the camera descending plane by plane; **a single text panel** whose words become the picture.
- Endings: **the page turns to a blank folio**; **the sky turns lapis** and lamps light in a pavilion; **pull back** to the open book on a cushion.

---

Status: **draft** — no demo film yet. Before this is used as a library style it needs a demo film, `DEMO.md`, stills and the checks in the Lemo-Opuscar `MAINTAINING.md` ("Gates").
