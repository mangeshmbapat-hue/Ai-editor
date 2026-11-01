# Kalighat Pat — Style Prompt

> Bazaar watercolours from 19th-century Calcutta in motion: a large figure on blank paper, its outline laid in one sweeping, swelling brushstroke, its volume shaded softly just inside the edge, its colours few and bold, its wit sharp.
> References (grammar only): Kalighat painting, made in the 19th century by *patua* painters who settled near the Kalighat temple in Calcutta and sold quick, inexpensive pictures on mill-made paper to pilgrims and townspeople: deities, scenes from epics, and lively satire of city types and scandals of the day. Take the single sweeping contour, the shading along the edge, the blank ground and the satirical eye; never copy a specific picture, and never name it in the film.

## 1. Essence, and what it is not

- **One stroke, one contour.** Each form is outlined by a single fast brushstroke that swells and thins (thin at the start, full on the curve, flicked off at the end).
- **Shading along the edge.** A soft darker wash runs just inside each contour and fades toward the middle: round, plump volume without a light source.
- **Blank paper.** No setting; at most one prop (a stool, a fish, an umbrella). The figure fills most of the sheet.
- **Few bold colours** in flat areas, black hair as a solid mass, silvery highlights on jewellery.
- **A point of view**: sharp-eyed portraits of types, foibles and pretensions; dignity for the devotional, wit for the worldly.

Not One-line Drawing (that is a thin line that never lifts; here each form has its own swelling brush contour, colour and edge shading), not Ink Wash (no landscape, no ink tones as atmosphere; figures and colour lead), not Watercolor Brush (no specimen notes, no painted scenery, no flying-white bristles), not 1930s Rubber Hose (no film gate, no music-driven bounce; caricature is drawn, not animated rubber).

## 2. Materials & rendering

- **Paper**: smooth, thin, cream mill-made paper; faint fibres, light foxing spots, a slight cockle (low-frequency displacement) where wet colour sat; deckle-free trimmed edges; occasionally a string hole at the top. Cached, world-anchored.
- **The contour stroke**: a Catmull-Rom spine with a pressure profile (start 25 %, peak 100 % at 30–60 % of length, end flick 10 %), max width 6–14 px at 1080p scaled by figure size, a wet edge (slightly darker rim), and a dry-brush break in the last 10 % (2–3 bristle gaps). One stroke per contour; long contours may be two strokes that meet on a curve.
- **Edge shading**: compute a distance field inside each shape mask; paint a translucent wash of a darker shade of the fill in a band 10–25 % of the local width, falloff `ss`, edge-darkened by 5 %. Multiply onto the flat fill.
- **Flat colour**: watercolour-flat with mild granulation (fine noise ±3 %) and occasional overrun 1–2 px past the contour.
- **Hair**: a solid black mass painted with a few broad strokes, with bristle edges where it meets skin.
- **Silver**: jewellery and trims in a metallic grey with a soft sheen term from a slow moving light; nothing else shines.
- Finished figures cache as sprites; strokes being painted are drawn by progress. Everything is a pure function of t under fixed seeds.

## 3. Colour logic

- **Paper is the ground and the white**; no background colour, ever.
- **4–6 hues per sheet**: black (hair, contours), one red, one yellow or ochre, one blue or green, a skin tone or two, and silver.
- **Shading is the same hue, darker**, only in the band along the edge; no cast shadows.
- Contours are dark (black or a deep brown) on all forms; colour may run slightly past them, never fall short.
- Silver is reserved for ornament and status (jewellery, buttons, a watch chain); one silver accent per sheet.
- Example: paper `#efe4cc`, contour `#1c1714`, red `#b8352a`, ochre `#d79a32`, indigo `#2e4f86`, green `#4f7d4b`, skin `#e2b48a`, silver `#a9adb3`.

## 4. Type & subtitles

- Captions are **written on the sheet's bottom margin** by brush or pen, like a stall seller's note; subtitles follow the same rule: dark ink on the paper, no box.
- Latin: **IM Fell English** (34–42 px) for subtitles, **Playfair Display** italic for titles (70–110 px). Bengali: **Tiro Bangla** or **Noto Serif Bengali**; Devanagari: **Tiro Devanagari Hindi**. Hindi subtitles are supported.
- Words appear by a fast left-to-right brush reveal (0.3–0.5 s). Hold each subtitle ≥ max(1.8 s, speech + 0.6 s).

## 5. Motion quality

- **Pose to pose by redrawing**: a figure holds a pose; to move, a fresh contour sweeps the new pose in 0.4–0.8 s while the old pose fades with the wash (an animated drawing, not a puppet). Between redraws, holds of 1–3 s.
- Small acting inside a hold on threes (8 fps): an eye glance, a raised finger, a fan or a fish tail flick, each a 2–3 drawing swap.
- **Stroke speed** is the brush's: fast, confident, eased out at the flick (`eo`); shading wash follows 0.2 s later with `ss`.
- Comic timing: hold, glance, hold, reveal. A satirical reveal is the prop drawn last.
- Camera on ones (24 fps). Never moves: the paper. Nothing slides around the sheet; figures do not walk across blank space, they are redrawn in a new place.

## 6. Camera grammar

A sheet on a table or hung on a string at a stall; the camera looks straight at it.

| Move | What it expresses | Can serve |
|---|---|---|
| Locked sheet, figure redrawn pose to pose | character through gesture | a portrait; a habit; a confession |
| Slow push to the face and eye | the look that judges | irony; a decision; doubt |
| Pan along sheets pegged on a string | a gallery of types | a cast of characters; options; a city's people |
| Diptych, two sheets side by side | comparison | before and after; two rivals; promise vs reality |
| Cut to the prop drawn last | the punchline | the hidden motive; the real cost; a twist |
| Pull back from one sheet to the stall | the picture as a thing sold | a market; mass production; a souvenir |
| Tilt from head to feet | the whole person, judged | status; dress; a reveal of shoes or a weapon |

Framing: one figure fills 70–85 % of the sheet height; generous blank paper on the side the figure faces. Transitions: a new sheet laid over the old; the brush sweeping a new contour across the frame; a sheet lifted off the string. Forbidden: painted backgrounds, dissolves, depth of field, perspective scenery.

## 7. Sound palette

- **Instruments as options**: a one-string plucked drone with glides in the Bengal folk manner (`pluck('shamisen', …)` single string, bend), a barrel drum (the synthesised tabla model, lower and woody, like a khol), small hand cymbals (`nepal_bells`, `claves` for dry ticks), harmonium (`accordion`); for satire, a brassy street band (`clarinet`, `trumpet`, `tuba_stac`, `snare`). Never imitate a known song.
- **Foley by material**: brush swish on thin paper (short, bright), wet wash (soft hiss), paper lifted and pegged, a string creak, coins at a stall, a crowd murmur, a cat, a fish slap, an umbrella snapping open.
- **Silence**: hold on a glance with nothing but paper room tone; the next brush sweep breaks it.
- **Voice**: a dry, amused narrator, short lines; Hindi or Bengali narration fits. Music ducked ~8 dB under voice; −14 LUFS.

## 8. Native moves

- **The one-stroke reveal.** A whole figure arrives in a few sweeps. *Fits content like:* a profile of a person; a product's silhouette; a new character entering.
- **Redraw as change.** The same figure redrawn in a new pose or role. *Fits content like:* a promotion; a change of heart; a habit forming.
- **The prop last.** The telling object is painted after the figure, flipping its meaning. *Fits content like:* a hidden cost; a conflict of interest; a secret hobby.
- **Gallery on a string.** Sheets of types pegged in a row. *Fits content like:* customer personas; a team; the cast of a debate.
- **Edge shading swells.** The band of shade widens or narrows to make a figure heavier or lighter. *Fits content like:* pride; burden; a body getting stronger.
- **Silver glint.** A slow light catches only the silver. *Fits content like:* wealth; vanity; one valuable detail.

## 9. Pitfalls of the medium

- Sketchy contours of many short strokes → one sweeping stroke per contour.
- Full gradient shading → only the band along the edge.
- Backgrounds creep in → blank paper; one prop at most.
- Uniform line width reads as vector → pressure profile, wet rim, dry flick.
- Figures sliding across the sheet like puppets → redraw in place.
- Satire that targets a community, caste, religion or a real private person → aim at behaviour and types, never at groups or identifiable people.
- **Sacred images as decoration.** Many Kalighat pictures are devotional images of deities: do not use them as ornament or in jest. Do not present a code-made film as an authentic Kalighat painting; for commercial work, credit or consult patua artists.

## 10. Engine

No demo engine yet (draft). A first demo should build:
- `brush.js`: `sweep(spine, {pressure, wMax, wetRim, dryBreak, seed})`, `strokeProgress(p)`.
- `shade.js`: `distanceField(mask)`, `edgeBand(mask, frac, colour)`, `flatFill(mask, colour, granulation)`.
- `figure.js`: figures as lists of contours, fills and hair masses per pose; `redraw(poseA, poseB, p)`; small 2–3 drawing swaps.
- `sheet.js`: paper, cockle, foxing, string and pegs, silver sheen, caption margin, `render(t)`.

Start from `styles/ink-wash/demo/ink.js` (`mk`, `draw`, `blot`: pressure-driven brush), `styles/watercolor/demo/engine.js` (`mk`, `drawS`, washes, `withSeed`), `styles/silent-film/demo/engine/redraw.js` (redrawn frames), `core/lib.js` (`mulberry`, `vnoise`, `eo`, `ss`), `core/render/`, `core/audio/sampler.py`, `core/audio/pluck.py`, `core/audio/sfx.py`.

## 11. Variation space

You decide the cast of types, the props, the colour set, whether the tone is devotional, tender or satirical, the opening, the ending, the camera path and the pacing.

- Structures: **a gallery** (one sheet per type, pegged in a row); **one figure, many redraws** (a life told by poses); **the pair** (two figures on one sheet, their relation redrawn scene by scene).
- Openings: **a blank sheet** and the first sweep of a contour; **a stall at the start of a day**, sheets being pegged; **a close-up of the eye** being painted, pulling back to the figure.
- Endings: **the prop revealed**; **the sheet sold**, folded and carried away; **the string full**, every type side by side.

---

Status: **draft** — no demo film yet. Before this is used as a library style it needs a demo film, `DEMO.md`, stills and the checks in the Lemo-Opuscar `MAINTAINING.md` ("Gates").
