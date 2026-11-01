# Pichwai — Style Prompt

> Painted temple hangings from Nathdwara in motion: a large cloth of deep indigo, black or green, filled edge to edge with rows of cows, lotus ponds, trees and night skies in fine opaque colour, with gold and silver that wake when a lamp passes; one hanging is lowered over another as the season turns.
> References (grammar only): the *pichwai* of Nathdwara in Rajasthan, large painted cloths hung behind the image of the deity in the temples of the Pushtimarg tradition and changed with the festivals and seasons, painted by the town's hereditary painters; their lotus ponds, cows, groves, moonlit nights and monsoon skies. Take the deep grounds, repetition, symmetry, seasonal change and metallic accents; never copy a specific hanging or the deity's image, and never name them in the film.

## 1. Essence, and what it is not

- **Deep ground, bright detail.** A dark dyed cloth (indigo, black, bottle green, deep red) carries small, finely painted motifs in light colours and gold.
- **Repetition with life.** Rows of near-identical cows, lotus pads, flowers, trees or figures, each slightly different in pose and marking.
- **Symmetry around a central axis**: the centre is reserved; motifs balance left and right.
- **Seasons rule the picture**: the same place repainted for spring, monsoon, autumn moon, winter; each hanging is one season or festival.
- **Gold and silver** are real metal in the paint, dull in shadow, glinting in a moving light.

Not Art Deco (no geometry, airbrush or engraved gold lines; gold is pigment on organic forms, and symmetry is calm, not mechanical), not Madhubani (no double outlines or hatched ground; the ground is deep and quiet), not Ukiyo-e (no woodblock or paper; opaque paint on cloth), not Stained Glass (front-lit; no lead, no transmitted light).

## 2. Materials & rendering

- **Cloth**: fine cotton dyed deep: plain-weave texture (2–3 % value), slight uneven dye, a faint vertical hang (sag at the bottom rod, gentle folds as low-frequency displacement). Cached, world-anchored; large format, often wider than tall.
- **Motifs as instances**: each motif (cow, lotus pad, lotus flower, banana tree, mango tree, peacock, star, cloud) is drawn once per variant (3–6 variants) as a vector sprite; placement grids add seeded micro-variation: ±4° rotation, ±6 % scale, pose variant, marking variant, ±2 px offset.
- **Pond tiling**: overlapping round pads on a staggered hex grid with rim lines and radial veins, flowers between them, fish and ducks sparse; the water itself barely visible between pads.
- **Fine line**: 0.8–1.5 px white or gold lines for petal veins, hair, ornaments; dotted borders of white points.
- **Metal**: gold and silver areas carry a micro-normal from noise; shade with a warm specular lobe from a moving lamp (`spec = max(0, n·h)^24`), base colour dull ochre-brown when unlit, bright when lit. Everything else is matte.
- **Hanging swap**: a new cloth on a rod lowers from the top over the old (cloth stiffness simulated as a damped vertical wave), or rises to reveal.
- Everything is a pure function of t under fixed seeds; finished cloths cache as layers.

## 3. Colour logic

- **One deep ground per hanging**; motifs in 4–6 light or mid colours (cow white, lotus pink, leaf green, sky blue, red accent) plus gold and silver.
- **Value order**: ground darkest, foliage mid, cows and flowers light, metal brightest only when lit.
- **Season sets the palette**: monsoon = dark grey-blue ground, green, white egrets; autumn moon = indigo with white and silver only; spring = deep red or green with pink and yellow.
- No gradients except the sky band at the top and lit metal; no cast shadows.
- Example (monsoon): ground `#1f2b3a`, leaf `#3e7a4e`, lotus `#e7a6b6`, cow `#f2ece0`, red `#b23a2c`, gold `#c9a14a`. Example (moon night): ground `#14204a`, white `#f3f0e8`, silver `#c3c7cf`.

## 4. Type & subtitles

- Text sits in the **lower border band** of the hanging, in cream or gold on the deep ground, no box.
- Latin: **Cormorant Garamond** semibold (36–44 px) for subtitles, **Playfair Display** for titles (70–110 px) in gold with a fine dotted underline. Devanagari: **Tiro Devanagari Hindi** or **Noto Serif Devanagari**. Hindi subtitles are supported.
- Titles may catch the lamp like the gold in the cloth. Subtitles fade in 0.3 s. Hold each ≥ max(1.8 s, speech + 0.6 s).

## 5. Motion quality

- **24 fps**, calm. Motif loops on twos: cows step and turn heads, tails swish, birds lift and settle, lotus heads sway (rotation ±2°).
- **Rows move as rows**: a procession of cows advances with each animal 1/8 of a step behind the one before; a breeze crosses a pond as a travelling wave of pad tilts.
- **Blooming waves**: flowers open in a front that crosses the pond (`ss` per flower, 0.6 s each).
- **The lamp**: a warm point light drifts slowly across the cloth (eased, with a slight flicker); metal glints follow it.
- Hanging changes are slow (2–4 s), with the cloth's settle wave.
- Never moves: the central axis, the borders, the ground.

## 6. Camera grammar

A hanging in a quiet room, square to the camera; the eye travels over it like a devotee's slow gaze.

| Move | What it expresses | Can serve |
|---|---|---|
| Locked full hanging, symmetric | order and calm | a ceremony; a mission statement; a season |
| Slow vertical tilt from sky band to pond | the world in layers | a day; an ecosystem; heaven to earth |
| Lateral glide along a row of cows | repetition, community | a herd; a workforce; a queue |
| Push into one motif among many | the one in the many | a single customer; a newborn calf; a choice |
| Lamp sweep, camera still | value revealed | a reveal; a luxury object; something precious noticed |
| Hanging lowered over hanging | time turns | seasons; versions; a festival calendar |
| Pull back to the hanging on a plain wall | the picture as an object | a heritage piece; a collection; an ending |

Framing: the central axis on frame centre in wides; motifs never cropped mid-row in held frames; at least one border visible except in deep pushes. Transitions: a new hanging lowers; the lamp leaves and the cloth sinks into darkness; the colour drains to the moon-night palette. Forbidden: perspective moves, depth of field, crossfades between unrelated hangings.

## 7. Sound palette

- **Instruments as options**: bamboo flute (`flute`, breathy, long phrases), a drone (`pluck('shamisen', …)`, long t60, buzz, as tanpura), a deep barrel drum (synthesised tabla model, lower), small bells (`nepal_bells`, `hand_chimes`), cattle bells (`cowbell` dampened and pitched down, layered with `nepal_bells`), harmonium (`accordion`). Never imitate temple ritual music or a specific devotional song.
- **Foley by subject**: cows lowing (synthesised, soft), hooves on earth, water and frogs in the pond, peacock call once, monsoon rain and thunder, wind in mango leaves, cloth on a rod.
- **Glints** get a high, quiet shimmer (`glass`, `glockenspiel` very soft).
- **Silence**: night; crickets only.
- **Voice**: gentle, reverent, unhurried; Hindi narration fits. Music ducked ~8 dB under voice; −14 LUFS.

## 8. Native moves

- **Rows with life.** A row of near-identical figures, each with its own small difference. *Fits content like:* a team of individuals; a product line; a village's households.
- **Seasonal swap.** A new hanging lowers over the old, same layout, new season. *Fits content like:* quarterly results; a year in a garden; versions of a plan.
- **Bloom wave.** Lotuses open in a front across the pond. *Fits content like:* a rollout spreading; spring arriving; ideas catching on.
- **The lamp finds the gold.** A light drifts and metal answers. *Fits content like:* hidden value; a jewellery piece; a memory that shines.
- **Moon night.** All colour drains to white and silver on indigo. *Fits content like:* stillness; a ceremony at night; a dream.
- **Mirror balance.** Left and right halves answer each other around the reserved centre. *Fits content like:* two partners; balance of a budget; giving and receiving.

## 9. Pitfalls of the medium

- Copy-paste repetition reads as digital wallpaper → variants plus seeded micro-variation.
- Gold painted as flat yellow → metal with micro-normals and a moving light.
- Too bright a ground → the ground is deep and dark; brightness belongs to motifs.
- Perspective or shading on cows and trees → flat forms; scale by row, not by depth.
- Busy colour → 4–6 motif colours plus metal.
- Lamp everywhere → one slow light, metal only.
- **The reserved centre and sacred imagery.** Pichwai are devotional hangings made for a deity's shrine: never put a product, logo or person in the central place, never draw the deity casually, and use the lotus-and-cow world with respect, not as decoration. Do not present a code-made film as an authentic pichwai; for commercial work, credit or consult Nathdwara painters.

## 10. Engine

No demo engine yet (draft). A first demo should build:
- `cloth.js`: `dyedCloth(seed, hue)`, `hang(t)` (sag and settle wave), `lowerOver(a, b, p)`.
- `motifs.js`: cow, pad, flower, trees, peacock, cloud, star as vector sprites with variants; `instanceGrid(region, motif, variance, seed)`, `row(motif, n, phaseLag)`.
- `metal.js`: `metalMask`, micro-normals, `lampSpec(lamp, t)`.
- `hanging.js`: borders, sky band, pond tiling, symmetry, season palettes, subtitles, `render(t)`.

Start from `styles/art-deco/demo/engine/deco.js` (`goldGrad`, `goldFlat`, `sparkle`, `glow`), `styles/art-deco/demo/engine/bulbs.js` (staged lighting), `styles/ukiyoe/demo/print.js` (`fibers`, `fillPath`, `kasumi`), `styles/shadow-puppet/demo/gl.js` (lamp field, flicker), `core/lib.js`, `core/render/`, `core/audio/sampler.py`, `core/audio/pluck.py`.

## 11. Variation space

You decide the seasons, the motifs, which ground colours, where the light goes, the opening, the ending, the camera path and the pacing; the centre stays reserved.

- Structures: **the year in hangings** (one hanging per season, each lowered over the last); **one pond, one day** (dawn to moon night on a single cloth); **the procession** (a row of cows crossing the cloth, each step a new place in the story).
- Openings: **darkness and one glint** as the lamp arrives; **an empty dyed cloth** on which the first row of motifs is painted; **a hanging rising** to reveal another behind it.
- Endings: **moon night**, all white and silver; **the lamp moves on**, gold sinking back to brown; **the hanging rolled** and laid with the others.

---

Status: **draft** — no demo film yet. Before this is used as a library style it needs a demo film, `DEMO.md`, stills and the checks in the Lemo-Opuscar `MAINTAINING.md` ("Gates").
