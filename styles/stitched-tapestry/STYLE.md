# Stitched Tapestry — Style Prompt

> Wool embroidery on a long strip of unbleached linen: flat figures outlined in stem stitch and filled with couched wool, one continuous story read left to right, sewn capital captions above the action, creature-filled borders above and below.
> References (grammar only): the eleventh-century Anglo-Norman embroidery kept at Bayeux (continuous frieze, trees as scene dividers, captions above the action, legs coloured for contrast, commentary in the borders); medieval English and Norse crewelwork (laid-and-couched fills, stem-stitch contours); community narrative embroideries. Take the frieze grammar and the two stitches; never copy a scene, figure, border or inscription, and never name them in the film.

## 1. Essence, and what it is not

- **Bare linen is the ground and the light.** Only figures, buildings, captions and border motifs are stitched; sky and air are unworked cloth.
- **Two stitches make everything**: a stem-stitch contour (a twisted rope of overlapping stitches) and a **laid-and-couched fill** (parallel wool floats tied down by spaced crossbars). No shading: a second wool is the only modelling.
- **One frieze, read left to right**: a central band about two thirds of the strip height, narrow borders behind stitched rules. Time passes along the strip; a tree, column or doorway marks a new scene.
- **Captions are sewn** in wool capitals above the figures they name.
- **Colour separates, it does not describe**: far legs differ from near legs, hair can be blue.

Not Watercolor Brush (no wash, no painted depth) and not Printed Long Take (no 3D world, no cut lines: the strip is flat cloth and the camera only slides). Not Woodcut Print (no ink, no carved tone). Not a counted-grid textile: stitches follow the form. Not a loom tapestry: the picture is laid onto a finished cloth.

## 2. Materials & rendering

- **Linen**: a seamless 2048² plain-weave tile: two sinusoidal thread directions, per-thread width noise ±15 %, slubs, a warm unbleached base, soft stains (fbm ±4 %). Along the strip, a world-anchored random tile offset per span plus one large stain field hides the repeat. Weave height → normal map, lit in one WebGL pass by a raking key from the upper left.
- **Stitch**: a short wool capsule (3–6 mm at strip scale) drawn as a twisted ribbon: dark core, lighter flanks, alpha hairs along the edge (fuzz), a 1–2 px shadow down-right. Width 2.4–3.2 px at reference zoom, ±12 %.
- **Stem stitch**: resample the contour at equal arc length (step = 0.6 × stitch); each stitch spans two steps, overlaps the last by half and tilts ~15° off the path. The tilt makes the rope.
- **Laid-and-couched fill**: clip to the region; lay floats at a region angle (one thread apart, small linen gaps allowed); cross with bars every 6–9 mm, each tied by tiny couching stitches every 4–6 mm. The fill lies under its contour.
- **Figures** sit on a jointed 2D rig but are **re-stitched per drawing in cloth space**: a limb rotates, its threads do not.
- Cache each finished shape as a 2× sprite; stitch live only what is being sewn. Every jitter is `hash(region, i)`.

## 3. Colour logic

- **Linen plus 6–9 wools**, plant-dyed in feeling (warm, slightly greyed): madder reds, weld yellows, woad blues, two or three greens, a buff, a blue-black. Nothing brighter than the yellow, nothing whiter than the linen.
- **Value order**: contours darkest, fills mid, linen lightest. The band is fuller and darker than the borders (2–3 wools).
- One **accent wool** is reserved for one thing that recurs along the strip: a banner, an object, a person.
- Never coloured: sky, wide water (three or four wavy stem lines), the linen.
- Example: linen `#e4d6b8`, terracotta `#a44c32`, buff `#c9a874`, sage `#7f8c5a`, deep green `#3f5a3c`, slate blue `#4d6178`, blue-black `#283040`, accent gold `#d9a531`.

## 4. Type & subtitles

- **Captions are stitched**: **Cinzel** or **Uncial Antiqua** capitals rasterised to a mask, filled with horizontal laid wool, outlined in stem stitch, 48–80 px cap height, words separated by stitched dots, sewn at 6–10 letters/s.
- **Subtitles** sit off the cloth, on the wall or roller below the strip: **EB Garamond** 34–42 px in warm off-white, two lines at most; Devanagari in **Tiro Devanagari Hindi** at the same visual size. Hold ≥ max(1.8 s, speech + 0.6 s).
- Small labels (a date, a place) are stitched words in a border, ≥ 28 px cap height.

## 5. Motion quality

- 24 fps. **Camera on ones; figures on twos**, re-stitched each drawing with a light **thread boil** (stitch seed per drawing, ±0.8 px per stitch end).
- Strong poses held 6–12 drawings (point, ride, carry, fall), 2–4-drawing changes. Motion is processional: walking, riding, rowing, hauling.
- **Appearing = being sewn**: contour behind a travelling needle, floats row by row, then couching; a figure in 1–2 s, a building in 3–4 s.
- **Disappearing = unpicking**: stitches pull out in reverse order, leaving needle holes that fade in a second.
- Wind and water: a few stitch lines shift one drawing at a time, never a smooth wobble.
- Never moves: the linen, the border rules, finished captions.

## 6. Camera grammar

A strip camera: mostly a lateral slide with the strip filling the frame height. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Steady lateral slide | time flowing; one event causing the next | a voyage; a campaign; a working day |
| Locked frame between two dividers | one scene held for reading | a meeting; a bargain; a vow |
| Push-in to thread scale | the hand that made it | a face; a tool; a sewn name |
| Pull-back until the strip runs off both sides | the scale of the account | a long history; a migration; a supply chain |
| Slide that halts on a border creature | a comment from the margin | irony; a proverb; an omen |
| Tilt from border to frieze | margin and story in dialogue | cause and consequence; work and reward |
| Slide that outruns the stitching | the story still being made | news; an unfinished project; an open future |

Framing: the band fills 55–75 % of the frame height; captions stay in frame; borders may crop. Transitions: a tree or column as the wipe line, a continuous slide, unpicking to bare linen, the cloth folding; no crossfades, no cut through a figure.

## 7. Sound palette

- **Music**: recorder, flute, harp (`pluck('harp')` short, as a lyre), bagpipe drone, frame drum, hand chimes; a hurdy-gurdy is a violas drone plus oboe through a buzzy band-pass. Modal lines over one drone carry long slides.
- **Foley from the cloth**: needle through linen (filtered tick + low thump), wool drawn through (150–400 ms rising band-passed rasp), scissors, the roller creaking, a cloth flap.
- **Story sounds are small**, remembered: hooves as frame-drum taps, sea as noise swells, axes as woodblock.
- **Silence**: only the needle; one long pull of thread is a full stop.
- **Voice**: a chronicler, plain past tense, short lines. Music ducked ~8 dB under voice; −14 LUFS.

## 8. Native moves

- **Sewing-in.** A figure appears contour first, then fill, behind a travelling needle. *Fits content like:* a team assembling; a building raised; the ingredients of a dish.
- **The continuous strip.** Moments laid side by side with dividers, the camera never cutting. *Fits content like:* a supply chain; goods travelling to market; the stages of a trial.
- **Margin commentary.** Border creatures mirror or mock the main action. *Fits content like:* a fable's moral; a market reacting; an unplanned side effect.
- **The repeated figure.** One person sewn again and again, a little changed each time. *Fits content like:* a career; a plant's growth; ageing.
- **Unpicking.** A passage pulled out, leaving needle holes, and sewn differently. *Fits content like:* a revised plan; a corrected record; an alternative history.
- **Thread close-up.** Push until fibres and couching ties read. *Fits content like:* craft and labour; a signature; a detail that is evidence.

## 9. Pitfalls of the medium

- **Shaded fills read as digital painting** → no gradient inside a stitched area; two wools and a contour.
- **Threads rotating with a rigged limb look like stickers** → re-stitch in cloth space every drawing.
- **Boil on ones shimmers** → boil on twos, small amplitude.
- **Small captions turn to fuzz** → ≥ 48 px cap height, short words.
- **A tiled linen shows its repeat on a long slide** → world-anchored offsets and one large stain field.
- **Too many wools turn the frieze into a cartoon** → ≤ 9 in the band, ≤ 3 in borders.
- **Copying a historical scene, or passing the film off as a real embroidery** → invent the scenes; credit it as code-made; for museum or archive work consult textile conservators or embroiderers and credit them.

## 10. Engine

No demo engine yet (draft). A first demo should build:
- `linen.js`: weave tile, slubs, stain field, height → normal; `linen(seed, w, h)`, `spanOffset(x)`.
- `stitch.js`: `stem(path, {len, tilt, wool})`, `laid(region, {angle, gap, couch})`, `knot(p)`; stitch lists kept in sewing order so `drawStitches(ctx, list, u)` sews or unpicks to any fraction `u`; 2× sprite cache.
- `frieze.js`: strip coordinates, dividers, border motif generator, captions stitched from a text mask.
- `rig.js`: flat jointed figures re-stitched on twos; `light.js`: one WebGL raking-light pass over linen and wool height.

Start from `core/lib.js` (`mulberry`, `hash`, `vnoise`, `seg`, easing), `styles/watercolor/demo/engine.js` (width-profiled ribbons, partial drawing, sprite cache, `withSeed`), `styles/papercut-red/demo/rig.js` (affine jointed pieces), `styles/crayon-book/demo/gl.js` (Canvas layers → WebGL compositor with a surface height), `styles/engraving/demo/engine/burin.js` (marks kept in making order). Music: `core/audio/sampler.py`.

## 11. Variation space

You decide what the strip records, who speaks, the wools, the borders' role, whether the stitching is live or finished, the slide speed and the dividers.

- Structures: **a ledger strip** (one scene per day of work while a border counts); **two strips braided** (parallel lives joined at one shared scene); **a commission** (the strip is sewn as the story is told and catches up with the present).
- Openings: **a rolled bundle** unrolled across a table; **a needle on blank linen** making the first stitch; **a thread close-up** pulled back to the frieze.
- Endings: **a stitch left hanging**, needle still threaded; **the strip rolled and tied**; **blank linen ahead** as the camera slides past the last scene.

---

Status: **draft** — no demo film yet. Before this is used as a library style it needs a demo film, `DEMO.md`, stills and the checks in the Lemo-Opuscar `MAINTAINING.md` ("Gates").
