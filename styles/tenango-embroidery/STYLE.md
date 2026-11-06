# Tenango Embroidery — Style Prompt

> Dense satin-stitched animals, birds and flowers on plain white cotton: flat silhouettes filled with glossy parallel threads whose direction changes from part to part, often a single colour per cloth or per creature, arranged edge to edge in a crowded, symmetrical field.
> References (grammar only): the embroidery of Otomí (Hñähñu) communities around Tenango de Doria and San Nicolás in Hidalgo, Mexico (designs drawn on manta cotton by specialist drawers, then filled in satin stitch by embroiderers; deer, birds, roosters, rabbits, plants and people at work, mirrored pairs, no outlines). Credit the communities; never copy a specific piece or a named artisan's design, and never name them in the film.

## 1. Essence, and what it is not

- **White cotton and thread only**: the cloth is the ground; every figure is solid embroidery with crisp edges.
- **Satin stitch fills**: parallel, tightly packed threads; **direction changes by part** (body diagonal, wing across, tail along), so one colour shows several values as the sheen turns.
- **Silhouettes with reserved details**: no outlines; an eye, a feather split or a leaf vein is a narrow gap where the cloth shows.
- **Crowded, balanced fields**: animals and plants fill the cloth with small even gaps, often mirrored left and right, stacked without a ground line.
- **One colour per cloth or per creature**: monochrome (red, blue, black, purple) or a field where each creature has its own colour.

Not Red Paper-cut (thread with sheen and stitch direction, not cut paper; details are gaps, not cut lace). Not Pictogram Motion (figures are lively, folkloric and stitched, not information icons). Not Stitched Tapestry (no outlines, no couched wool, no narrative frieze or captions) and not Cross-stitch (no grid, no X stitches).

## 2. Materials & rendering

- **Manta cloth**: a plain-weave white cotton tile with soft weave relief, slight creases, a faint warm cast; normal map lit from the upper left.
- **Design**: each motif is a set of closed parts (body, neck, wing, tail, legs, petals) with a **stitch angle per part**; gaps between parts are 2–4 px of cloth. Drawn first as a pale blue or pencil line on the cloth (the drawer's design), which the stitching covers.
- **Satin fill**: for each part, scan lines at its angle, spacing ≈ thread width (2–3 px at reference scale); each scan segment inside the part is one thread from edge to edge. Spans longer than ~10 mm are split into staggered shorter stitches (long-and-short) so floats never sag.
- **Thread**: a capsule ribbon with an **anisotropic highlight** (Kajiya–Kay style): brightness depends on the angle between thread direction and light, so parts at different angles read as different tones of one colour. Slight fuzz at ends, a 1 px raised shadow on the cloth beside the edges.
- **Edges**: thread ends form a slightly ragged, raised boundary (±0.6 px), never a vector line.
- **Compositing**: render threads as height + tangent + colour buffers; light in one WebGL pass (sheen from tangent, shadow from height). Cache finished motifs as textures; stitch live only the one being made.
- **Rig**: animals are parts on a 2D jointed rig; when a part rotates, its stitch angle stays fixed to the part (embroidery is on the cloth of the creature), but the light response changes, so movement makes the sheen shift.
- Everything seeded per motif and part.

## 3. Colour logic

- **White cloth + 1 thread colour** for the purest look; **or** one colour per creature from a set of 6–10 saturated threads, never two colours inside one small creature.
- The sheen does the modelling: value differences come from stitch direction, not from extra shades.
- Monochrome films: the single colour is everything; emphasis comes from density and size, not an accent.
- Multicolour films: one colour is the **accent** reserved for one recurring creature or thing.
- Never: gradients, outlines in a second colour, coloured backgrounds, shadows painted on the cloth.
- Examples: red `#c0272d` on `#f6f3ec`; field — magenta `#c2246e`, orange `#e86a1c`, yellow `#efbe1f`, green `#2f9a4a`, turquoise `#1a9ab0`, blue `#2a4ea5`, purple `#6b3b98`, black `#1c1b1f`.

## 4. Type & subtitles

- **Titles are embroidered**: **Hind** Bold or **Baloo 2** ExtraBold letters rasterised to parts, each letter stitched in satin at a fixed angle (vertical strokes vertical, bowls along the curve), 80–140 px, in the film's thread colour.
- **Subtitles**: on a plain cotton band below the field, **Hind** Medium 36–44 px in the darkest thread colour, two lines at most. Hind also sets Devanagari, so Hindi subtitles keep the same face. Hold ≥ max(1.8 s, speech + 0.6 s).
- Labels: short stitched words, ≥ 48 px; embroidery cannot hold small type.

## 5. Motion quality

- 24 fps. **Camera on ones; creatures on twos**, pose to pose with short hops, pecks, turns of the head; wings in 3–4 drawings.
- **Stitching-in**: a part fills thread by thread along its angle (a needle travelling back and forth), parts in order body → limbs → details; a bird takes 2–3 s, a full field much longer, so use 4–16× for crowds.
- **Sheen motion**: a slow light sweep (or a slight cloth tilt) makes every part flash at its own angle; a living cloth even when nothing moves.
- **Mirroring**: a motif and its mirror move in mirror phase.
- **Disappearing**: unpicked threads lift out, leaving the pale design line on the cloth.
- Never moves: the cloth (except a deliberate tilt), the design layout once full.

## 6. Camera grammar

A flat-cloth camera with light that moves. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Locked full cloth, creatures active | abundance; an ecosystem | a forest; a market; a festival day |
| Push into one creature until threads fill the frame | the single life inside the crowd | a portrait; a newborn; a lost animal |
| Slow pan across a crowded field | a world without a horizon | a migration; a garden; a village |
| Light sweep across a held frame | the cloth breathing | dawn; time passing; attention |
| Tilt of the cloth itself | the object in the hand | a gift; an heirloom; a sale |
| Pull back to a pair of mirrored cloths | balance; partnership | a couple; two communities; dialogue |
| Macro on a reserved eye gap | the detail that gives life | a gaze; a decision; a recognition |

Framing: creatures never cropped mid-body in a held frame; gaps between creatures stay even; text only in bands. Transitions: a creature stitching in to cover the frame, a light flare off the threads, unpicking to bare cloth, a fold of the cloth; no crossfades.

## 7. Sound palette

- **Instruments**: string-band timbres (`guitar_nylon` strums, `violin`, sampler `harp` or `pluck('harp')`), `marimba`, small percussion (`shaker`, `claves`), a wooden flute colour (`recorder`). Do not imitate a specific regional music; consult musicians of the region for films about it.
- **Foley from the work**: needle through cotton (soft tick), thread drawn (short silky zip, pitch rising), scissors, a hoop tightening, cloth shaken out, a hand smoothing threads.
- **Story sounds** from the creatures, small and clear: birdsong, a rooster, rustling leaves, water.
- **Silence**: only the thread pulling through.
- **Voice**: warm, close, unhurried. Music ducked ~8 dB under voice; −14 LUFS.

## 8. Native moves

- **Stitching-in.** A creature fills thread by thread, part by part. *Fits content like:* a birth; an idea forming; a product assembled.
- **Sheen turn.** Light crosses the cloth and each part flashes at its own angle. *Fits content like:* morning; a mood change; a hidden pattern revealed.
- **The crowded field.** Creatures added one by one until no gap remains. *Fits content like:* biodiversity; a growing community; a city filling up.
- **Mirror pair.** A motif and its reflection act in mirror phase. *Fits content like:* twins; a debate; a call and response.
- **One colour, many creatures.** A monochrome field where only shape and stitch angle separate beings. *Fits content like:* equality; a single species' many roles; a uniform crowd with individuals.
- **The design line.** The drawer's pale line on cloth before stitching, then covered. *Fits content like:* a plan; a prophecy; a sketch becoming real.

## 9. Pitfalls of the medium

- **Flat colour fills** look like vector clip art → thread scan lines with anisotropic sheen per part.
- **One stitch angle for a whole creature** loses the modelling → a different angle per part.
- **Outlines** break the idiom → none; reserved gaps for detail.
- **Long floats** look slack → split spans over ~10 mm.
- **Sparse fields** feel empty → fill the cloth with even gaps.
- **Smooth tweened motion** turns it into a cartoon → pose to pose on twos.
- **Copying Tenango designs or presenting the film as handmade** → these designs belong to Otomí communities, and uncredited commercial copies have been publicly objected to; invent motifs, credit the tradition, and work with Tenango artisans for commercial use.

## 10. Engine

No demo engine yet (draft). A first demo should build:
- `motif.js`: creatures and plants as parts with stitch angles and reserved gaps; mirrored placement; `field(seed, motifs, gap)`.
- `satin.js`: scan-line fill per part, span splitting, stitch order for `stitchIn(part, u)` and `unpick(part, u)`, ragged edge ends.
- `thread.js`: height/tangent/colour buffers and a WebGL pass with anisotropic sheen and raised shadow; `manta.js`: cloth tile, creases, design line.
- `rig.js`: parts on a 2D rig with stitch angles fixed to parts.

Start from `styles/engraving/demo/engine/burin.js` (`contourHatch`, `resample`, ordered line making for stitch scans), `styles/papercut-red/demo/paper.js` (pieces pre-rendered to textures and placed), `styles/papercut-red/demo/rig.js` (affine jointed parts), `styles/crayon-book/demo/gl.js` (Canvas layers → WebGL lighting compositor), `core/lib.js`.

## 11. Variation space

You decide monochrome or multicolour, the creature vocabulary the film invents, how crowded, mirrored or not, whether stitching is seen live, and how the light moves.

- Structures: **one cloth filling** (a single field completed creature by creature); **a season in four cloths** (the same layout re-stitched in four colours); **the drawer and the stitcher** (design lines appear first, threads follow, the two stories meeting).
- Openings: **a needle and one thread** on bare manta; **a finished cloth** caught in raking light; **a single eye gap** in macro, pulled back to the creature.
- Endings: **the last gap filled**; **the cloth folded** and the sheen vanishing; **one creature left as a design line**, unstitched.

---

Status: **draft** — no demo film yet. Before this is used as a library style it needs a demo film, `DEMO.md`, stills and the checks in the Lemo-Opuscar `MAINTAINING.md` ("Gates").
