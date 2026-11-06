# Kerala Mural — Style Prompt

> Wall painting from Kerala brought to life: long-eyed figures with swelling outlines in five earth pigments on lime plaster, rounded by deeper tones of the same hue and seen by oil-lamp light.
> References (grammar only): the mural tradition of Kerala's temples and palaces (c. 16th–19th c., and its living revival in Kerala's mural schools) for the five-colour (panchavarna) palette, sketch-then-outline method, same-hue modelling and gapless panels; Kathakali make-up for colour as character and acting with the eyes. Never copy a specific mural, deity image or composition, and never name them in the film.

## 1. Essence, and what it is not

- **A warm lime-plaster wall** under everything: matte, uneven, cracked, smoke-darkened above.
- **Five pigments only**: red ochre, yellow ochre, green, lime white, lamp black (a rare blue as a sixth).
- **Modelled, not flat**: each form is rounded by deeper tones of its own hue toward its contour, so bodies swell like fruit; no directional light, no cast shadow.
- **The outline is the drawing**: a black or red-brown line that swells on curves and thins at tips, laid last over a yellow-ochre sketch.
- **Long eyes, full panels**: eyes reaching toward the ear, arched brows, tall crowns, heavy ornament; every gap filled with foliage, flowers, birds and animals inside painted borders.

Not Ukiyo-e (no printed blocks, no paper, no bokashi skies), not Stained Glass (light falls on the wall; nothing transmits, no lead lines), not the sibling drafts Pattachitra or Kalamkari (cloth grounds, flat fills, no same-hue modelling), and not vector art with a plaster texture on top: the rounded volume and the eye are the style.

## 2. Materials & rendering

- **Wall** (cached at init, 1.5× frame): warm lime base, trowel undulation (two noise octaves, also a normal map), seeded branching hairline cracks, salt blooms, flaked patches, soot above lamps. All damage is a world-anchored mask.
- **Layer order per figure**: plaster → yellow-ochre sketch (1–1.5 px, ~60 %) → pigment fills (multiply over the plaster grain at ~90 %, edges ragged ±0.6 px) → same-hue modelling → lime-white highlights (eyes, teeth, pearls) → final outline.
- **Modelling**, the signature: a cached distance field from each region's boundary drives a darkening ramp, darkest at the contour, quantised to 3–4 steps with step edges blurred 4–8 px: layered pigment, not airbrush.
- **Outline**: a tapered Catmull-Rom ribbon, 1.5–5 px at 1080p, ±12 % width noise; thick outside, fine on fingers and folds.
- **Ornament** from path generators (beads, petal crowns, collars, leaf sprays); **figures** are per-part sprites with pivots, built once under a fixed seed.
- **Lamp light** multiplies the wall: one or two warm radial lobes, a few % flicker from 5–8 Hz value noise, relief from the plaster normal map; beyond the lamp the wall falls to deep umber, never black. Everything is a pure function of `t`.

## 3. Colour logic

- **Five pigments and their deeper tones.** No purple, pink, cyan or neon; no gradient crosses between hues.
- **Plaster is the light**; pure white only as small lime highlights.
- **Colour is character**: as with Kathakali make-up, the murals are often described as giving serene, noble figures green, proud or passionate ones red and gold-yellow, fierce ones dark tones. Fix one role per colour for the film; change a figure's colour only when its change of nature is the point.
- **Value order**: outline → deep contour tone → body hues → plaster. Background foliage is less saturated so figures stay forward.
- **Yellow ochre is the gold**; metallic only for a few raised dots on crowns.
- Example: red ochre `#a8411f`, yellow ochre `#d6a03c`, green `#3f6a3c`, lime `#efe5cd`, black `#1c1712`, rare blue `#2f4a7a`. Example (faded wall): `#b06a48`, `#c9a666`, `#6f8a66`, `#e4d8bd`, `#3a2e26`.

## 4. Type & subtitles

- **Subtitles are painted on the wall**: a band in the panel's lower border (red-ochre ground, yellow-ochre double rule), text in lime white or yellow ochre. Latin in Cormorant Garamond 600 or EB Garamond, 30–40 px; Hindi in Tiro Devanagari Hindi or Noto Serif Devanagari; Malayalam in Noto Serif Malayalam, only for real text checked by a reader.
- Letters take the plaster grain and lamp light; keep ≥ 4.5 : 1 contrast. Reveal with a left-to-right brush clip (0.3–0.5 s); leave by fading to plaster.
- **Titles**: inscriptions in the top border, sketched in ochre, then filled; never glowing.
- Two lines max. Hold ≥ max(1.8 s, speech + 0.6 s). Split Devanagari by grapheme cluster for per-letter reveals.

## 5. Motion quality

- **24 fps**; figures **on twos**, parts rotating about pivots in small amplitudes (head ±6°, neck slide, hand swaps); camera and lamp on ones.
- **Painting-in is the main motion**: sketch → fill → modelling → outline, about 20 / 30 / 30 / 20 % of a figure's progress.
- **The eyes act**: the iris slides inside the long eye on ones, brows lift, lids narrow; the rest of the face stays still.
- Poses are held; changes are short (0.3–0.6 s, `eio`) and land in a hold. No walk cycles.
- Always alive: lamp flicker. Never moving: wall, borders, outline widths. Things arrive by being painted, leave by fading to plaster.

## 6. Camera grammar

The camera is a visitor with a lamp moving along a painted wall. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Lateral travel along the wall | a sequence read in order | a journey; a lineage; a working day |
| Locked camera, lamp carried across | discovery in darkness | a secret; a memory; a night scene |
| Tilt from base border to crown | stature, hierarchy | a ruler; a tall tree; growing up |
| Close on the eyes | inner feeling | a decision; a lie; affection |
| Locked panel, figures painted in | composition as meaning | a family; an assembly; a recipe |
| Raking glide over cracked plaster | the wall's age | time passing; loss; restoration |
| Pan across a border into the next panel | a chapter turn | a new day; a new place |
| Pull back to pillars and lamp | the story becomes a place | a summary; a return to the present |

Framing: figures fill their panel, heads in the top third, borders visible in wides. Transitions: lamp dims and rises on the next panel; a border band slides across; fade to plaster. Forbidden: dissolves, digital wipes, zoom blur.

## 7. Sound palette

- **Kerala percussion, approximated**: chenda (stick drum: `snare2` + `toms` over a low `frame_drum`), maddalam (hand barrel drum: darbuka + low `frame_drum`), idakka (hourglass drum: synthesised membrane, ±4-semitone squeezed glides), elathalam (small cymbals: short `clash` + `nepal_bells`).
- **Winds and drone**: a curved horn (`horn`/`trombone`, upward glide); a double reed (shehnai recipe); a tanpura-recipe drone; quiet `flute`.
- **Techniques, as options**: build intensity by dividing the beat in stages, not by changing tempo; one idakka glide on a glance; a hard stop before a reveal.
- **Foley**: dry brush on plaster (noise 2–6 kHz), wick pop, bare feet on stone, a falling plaster flake, crows outside, monsoon rain on a tiled roof.
- **Silence**: only the flame's soft roar; at most one idakka note inside it.
- **Voice**: calm, resonant storyteller, stone-corridor reverb (~0.8 s); music ducked ~8 dB under voice; −14 LUFS. Never imitate temple ritual music.

## 8. Native moves

- **Outline-first painting.** Ochre sketch, fills, modelling, then the swelling outline. *Fits content like:* a craftsman making a tool; a city planned, then built; a family tree growing.
- **The eyes speak.** Iris glides and brow lifts carry the line. *Fits content like:* a negotiation; a teacher's look; a child's first surprise.
- **Lamp reveal.** The wall exists only where the lamp lights it. *Fits content like:* an archive; a forgotten history; a mystery.
- **Fill the gaps.** Bare plaster fills with leaves, birds and animals. *Fits content like:* a forest regrowing; a market at dawn; a crowded festival.
- **Colour as nature.** A figure's skin colour turns as its nature turns. *Fits content like:* a calm worker turning angry; a rival becoming an ally; illness and recovery.
- **Loss and restoration.** Pigment fades and flakes over decades in seconds, then is repainted. *Fits content like:* heritage conservation; memory lost and recalled; a town's revival.

## 9. Pitfalls of the medium

- Flat fills read as clip art → same-hue modelling from the contour, plaster grain under every fill.
- Uniform outlines look like vector strokes → tapered ribbons, thick outside, fine inside.
- Generic almond eyes → elongate toward the ear, heavy upper lid, visible white, small high iris.
- Extra hues creep in → five pigments only; run a palette check on stills.
- Even lamp light kills depth → radial falloff to umber. Swimming cracks → bake them into the wall.
- **Sacred source**: most Kerala murals are devotional and many are in active temples. Don't use deity images, sacred symbols or ritual objects as ornament; paint people, animals, plants and work. Don't present the film as authentic mural work; credit the tradition and, for commercial work, consult or commission Kerala mural artists.

## 10. Engine

No demo engine yet (draft). A first demo should build:

- `plaster.js`: `makeWall(w, h, seed)` → albedo, normal, age mask; `crackWalk(seed, branches)`; `wallLight(lamps, t)`.
- `mural.js`: regions with pigment roles; `paintStage(region, p)`; `modelTone(region, hue, steps, width)` from a cached distance field; `outline(path, wMin, wMax)`.
- `ornament.js` (beads, crowns, leaf sprays, borders), `figure.js` (pivots, `eye(irisX, lid, brow)`), `mix.py`.

Start from: `core/lib.js` (`mulberry`, `vnoise`, `eio`, `seg`); `styles/ukiyoe/demo/print.js` (`fbm`, `wob`, `line`, `fillPath`, `cartouche`); `styles/watercolor/demo/engine.js` (`mk`/`drawS` ribbons, `sprite`, `withSeed`); `styles/papercut-red/demo/rig.js` (`solveRig`); `styles/shadow-puppet/demo/gl.js` (`makeGL`, a light × surface compositor to adapt as lamp × wall); `core/render/still.mjs`, `core/audio/sampler.py`, `core/audio/sfx.py`.

## 11. Variation space

You decide the subject, the panel layout, the colour roles, the lamps, how much figures move, the opening, the ending and the camera path.

- Structures: **a corridor of panels** (each one stage of a craft); **one wall, many lamps** (each lamp reveals a different group); **a portrait gallery** (figures whose colours state their roles, each speaking in turn).
- Openings: **bare plaster** receiving the first ochre line; **a dark corridor** where one wick is lit; **a crack in old plaster** followed into a painted world.
- Endings: **the lamp is put out**; **the panel ages a century** in seconds and is left so; **a pull back to a doorway** where daylight bleaches the wall.

---

Status: **draft** — no demo film yet. Before this is used as a library style it needs a demo film, `DEMO.md`, stills and the checks in the Lemo-Opuscar `MAINTAINING.md` ("Gates").
