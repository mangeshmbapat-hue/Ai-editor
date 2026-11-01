# Fauvism — Style Prompt

> A moving painting in wild, unmixed colour: broad separate brushstrokes of pure hue laid on primed canvas, coloured contour lines, violet shadows and red trees, light made from colour contrast instead of light and dark.
> References (grammar only): the Collioure summer paintings of 1905 (pure colour as sunlight, bare canvas between strokes); the same circle's river and harbour views a year later (complementary water, dashes of pure pigment); late-19th-century cloisonnism (flat areas held by coloured contours). Never copy a painting, composition or figure, and never name painters or works in the film.

## 1. Essence, and what it is not

- **Colour chosen by feeling, not by object.** A red tree, an orange sea, a green stripe down a cheek; shadows are violet, blue or viridian, never grey or black.
- **Separate strokes of one pure hue each**, broad (a flat brush 1–3 % of frame width), side by side, opaque, never blended; primed canvas peeks through the gaps and becomes the light.
- **Coloured contours** of varying weight (ultramarine, vermilion, viridian) hold simplified shapes.
- **Flattened space**: a high horizon, few planes, distance by cooler hue rather than greyed atmosphere.
- **Complementary pairs vibrate** side by side (orange/blue, red/green, yellow/violet). The tone is joy, heat, sun.

Not Impasto Oil Painting (no knife planes, no raked height field, no value-first realism: colour beats value, paint is brushed), not Watercolor Brush (opaque, never transparent), not Crayon Picture Book (no wax tooth), not Memphis Diorama (no flat vector fills or patterns), not pointillism (strokes, not dots; no optical mixing).

## 2. Materials & rendering

- **Canvas**: cached primed cotton, cream white, `sin × sin` weave warped by noise at ±4 %; it shows through every gap.
- **Colour design first**: each scene is a set of polygon regions, each assigned a hue by mood (not by the object's local colour) and a stroke direction field (along the form, across a sky, around a face).
- **Stroke** (instanced WebGL quads): flat-brush footprint, length 3–8 × width, square start, dry tail breaking into 3–6 bristle streaks, 1D-noise bristle grooves across the width, ±12 % width wobble. Regions filled to 70–90 % coverage; 5–15 % of strokes are a complement or neighbour hue ("sparks").
- **Contours**: Catmull-Rom ribbons drawn after the fill, width ±35 % with pressure, in a contrasting hue, sometimes broken.
- **Thin paint, flat light, opaque layering**: no height field or raking light; a later stroke fully covers an earlier one, no wet-in-wet mixing.
- **Caching**: stroke lists seeded by region id and baked to sprites; static regions never repaint; moving objects carry anchored strokes, re-rendered on twos. A **repaint** draws a new seeded generation over the old, stroke by stroke.
- Render 2× and downsample; everything a function of `t` (seed any stroke built per frame).

## 3. Colour logic

- **5–7 pure hues per scene** at full chroma; the cream canvas is the only neutral and the brightest light.
- **No grey, no black, no brown.** The darkest value is ultramarine, deep violet or viridian.
- **Value still separates the subject**: plan a value thumbnail, then swap hues at about the same value, so the silhouette survives a greyscale check.
- **The strongest complementary pair is reserved for the focal point** (vermilion against viridian, cadmium against violet); the rest of the frame uses neighbouring, calmer pairs.
- Warm/cool, not light/dark, models form: the lit side warm, the shadow side cool.
- Example: `#e8442a` vermilion, `#f6b42c` cadmium, `#2b6fd6` cobalt, `#6a3fb0` violet, `#1f9e6a` viridian, `#ff8fb1` rose on `#f3ecdc` canvas.

## 4. Type & subtitles

- Words are painted with the same brush: glyphs rasterised from a font, filled with strokes like any region, then given a contour in a complementary hue.
- **Titles**: Shrikhand or Abril Fatface as the skeleton, 90–180 px, filled stroke by stroke, slightly irregular.
- **Labels**: Kalam or Permanent Marker, 28–40 px, ultramarine.
- **Subtitles**: sit on a strip of bare canvas (an unpainted band with a ragged brushed edge) at the bottom, Kalam 600 or Baloo 2 600 at 36–44 px in ultramarine or deep violet; a soft cream halo when crossing paint. Hold each ≥ max(1.8 s, speech + 0.6 s).
- **Devanagari**: Kalam (it covers Devanagari) or Yatra One for titles; the shirorekha is drawn as one continuous brush stroke when titles are painted in.

## 5. Motion quality

- 24 fps; moving subjects on twos (their strokes are re-rendered), camera moves on ones over cached paint.
- **Painting-in** is the main appearance: dominant hue, then sparks, contour last (or contour first, colour flooding in). Leaving: overpainted with fresh strokes, never an opacity fade.
- Sway and gesture are stroke-group transforms (rotate a tree's stroke group about its base, `sin` sway ~1–2°).
- Easing: `eo` for strokes landing, `eio` for camera; a stroke reveals linearly, like a brush pulled.
- **Never moves**: the canvas weave and the bare gaps of static regions; no global stroke boil.

## 6. Camera grammar

A painting is a window; the camera respects the canvas. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Locked canvas, things painted in | Making, attention | a recipe; a portrait; a place being described |
| Slow pan across a wide painted panorama | Abundance, a walk | a market; a coast; a festival street |
| Push into strokes until they become abstract colour | Feeling over fact | an emotion; a taste; music |
| Pull back from an abstract field to the scene | Meaning assembling | a solution; an arrival; a memory recovered |
| Repaint on a locked frame (new hue map) | Mood changing, same place | before/after; seasons of the heart; good news |
| Interior to open window to view | Home and the world | travel; longing; a hotel morning |
| Cut on a hue match between canvases | Rhythm, kinship | a series of places; a family; products of one maker |

Framing: high horizon, big simple shapes, the focal pair near a third. Transitions: overpaint wipe (a broad brush sweeps a new hue across), hue-match cut, a fresh canvas sliding in; no photographic dissolves, no digital wipes.

## 7. Sound palette

- **Sunny and rhythmic**: accordion, nylon guitar, ukulele or strumstick strums, pizzicato strings, clarinet, flute, marimba, xylophone, tambourine, claps, cajon, shaker; a piano for quieter painting.
- **Foley of paint**: bristle swish per stroke (band-passed noise with the stroke's own envelope, pitch rising with stroke speed), a soft tap as a loaded brush lands, a canvas thump when a new canvas is set, water-jar rinse between colours.
- **The scene's own world** under it: sea, cicadas, a market. Option: each hue's repaint brings in its own instrument.
- **Silence**: the brush lifted, the room and the light; one swish ends it.
- **Voice**: warm, delighted, conversational. Music ducked ~6 dB under voice; −14 LUFS.

## 8. Native moves

- **Recolour by feeling.** The same place repainted stroke by stroke with a new hue map as the mood changes. *Fits content like:* a city before and after a result; a kitchen on an ordinary and a festival day; a product seen in three moods.
- **Complementary vibration.** The focal object sits against its complement, whose sparks pulse. *Fits content like:* the one item that matters on a shelf; a speaker in a crowd; a sale price.
- **Bare-canvas light.** Light arrives as strokes lift away and leave the cream canvas. *Fits content like:* dawn; an idea; a clearing in a forest.
- **Contour first, colour floods in.** A coloured line drawing fills with strokes in seconds. *Fits content like:* a building plan; a new face in the team; a map of a route.
- **The open window.** Interior and view in one canvas, the window as the bright centre. *Fits content like:* travel; a home office; longing.
- **Stroke dance.** Strokes lift off, move to the music and land as a new picture. *Fits content like:* a festival; a song's chorus; a crowd forming.

## 9. Pitfalls of the medium

- **Mud** from blended or semi-transparent overlaps → opaque strokes, no wet mixing, never lay complements over each other at partial alpha.
- **Rainbow chaos** → 5–7 hues per scene, one dominant per region, one focal complementary pair.
- **A swirl-filter look** (every stroke boiling) → static regions stay still; only moving objects and deliberate repaints change.
- **Illegible faces** under arbitrary hues → strong contour, warm/cool split, value separation.
- **Photo-filter strokes** sampled from an image → design regions and hues; strokes follow form.
- **Flat vector look** → keep gaps, bristle streaks, weave, contour weight variation.
- **Saturated reds smear after encoding** (4:2:0 chroma) → contours ≥ 3 px at 1080p, test the encoded file, pull pure red slightly toward orange.

## 10. Engine

No demo engine yet (draft). A first demo should build:

- `brush.js`: instanced flat-brush quads, bristle streak texture, dry tail, `stroke(path, width, hue, seed, progress)`.
- `regions.js`: scene as hue-assigned polygons with direction fields; `fill(region, coverage, sparks, seed)` → cached stroke lists.
- `contour.js`: pressure ribbons in a contrasting hue.
- `canvas.js`: primed weave, compositing, supersampling.
- `repaint.js`: hue maps per mood, repaint schedules (`order`, `duration`), overpaint wipe.

Start from `styles/impasto/demo/engine/impasto.js` (instanced stroke pipeline; drop the height field and raking light), `styles/watercolor/demo/engine.js` (width-profiled ribbons for contours, `withSeed`), `styles/crayon-book/demo/gl.js` (paper texture compositor), `core/lib.js`. Music from `core/audio/sampler.py` (accordion, guitar_nylon, violins_pizz, clarinet, marimba, tambourine); stroke swishes in `core/audio/sfx.py` style numpy synthesis.

## 11. Variation space

The agent decides the places and figures, the hue maps and when they change, the focal pairs, how much canvas stays bare, the pacing and the camera path.

- Structures: **one place, three moods** (the same canvas repainted as the feeling changes); **a sunny itinerary** (a canvas per stop, cut on hue matches); **a portrait sitting** (a face painted, repainted and finally seen in its truest colours).
- Openings: **bare canvas with one stroke** of vermilion that becomes something; **a field of pure colour** pulled back into a scene; **a coloured contour drawing** waiting to be filled.
- Endings: **the painter's last spark** of the complement lands on the focal point; **the canvas is overpainted** with a single hue, leaving one window bare; **a pull-back** shows many canvases drying side by side.

---

Status: **draft** — no demo film yet. Before this is used as a library style it needs a demo film, `DEMO.md`, stills and the checks in the Lemo-Opuscar `MAINTAINING.md` ("Gates").
