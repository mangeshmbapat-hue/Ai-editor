# Yarn Painting — Style Prompt

> Pictures made of coiled thread: coloured yarn pressed strand by strand into a wax-covered board, each shape outlined and then filled with lines that echo its contour or spiral from its centre, so the whole image has the ridged, glowing texture of wool.
> References (grammar only): the yarn paintings (nierika) of the Wixárika (Huichol) people of the Sierra Madre Occidental, Mexico, for the outline-then-echo fill, the contrasting outline strand and saturated colour; coiling and couching in textile craft for how a strand behaves. Never reproduce Wixárika sacred symbols or specific works, and never name them in the film.

## 1. Essence, and what it is not

- **Everything is yarn**: no painted area anywhere; every pixel belongs to a twisted strand lying beside the next, ridged and slightly fuzzy, with wax showing in tiny gaps.
- **Outline, then echo**: each shape is first ringed by a strand of a contrasting colour, then filled inward with lines parallel to its contour, or by a spiral; the background is filled the same way around the figures.
- **Saturated contrast**: hot pink, orange, turquoise, yellow, green, purple, black; neighbours always differ.
- **Flat and frontal**: figures in profile or front view, no perspective, no painted shading; light only rakes the strands and gives each a sheen.
- **Direction is expressive**: the way the strands run (radiating, rippling, spiralling) carries energy and flow.

Not One-line (no ink; many fixed-width strands fill areas), not Crayon Book (no paper tooth, no wax resist: here wax is glue under thread), not Stained Glass (nothing transmits; the outline is a coloured strand, not lead), not a "fluffy" texture over vector art: the fill direction is designed.

## 2. Materials & rendering

- **Board**: wood under a layer of beeswax (amber, semi-glossy, fingerprinted), visible only in gaps and at the edges.
- **Strand width w** is the film's pixel: 6–12 px at 1080p, fixed per scene.
- **Strand renderer**: contact shadow (offset 0.15 w, blur 0.3 w, multiply) → base colour body → ply twist (diagonal stripes at 35–50° to the path, period ≈ 0.9 w, alternating light and dark from a phase along and across the path) → raking sheen (lighter on the side whose normal faces the light) → fuzz (a few short seeded hairs at 20–40 % alpha).
- **Fill generator**: region polygon → successive inward offsets at spacing w → either concentric closed rings or one spiral (link each ring to the next at a seam); narrow parts (limbs, stems) become single strands along the medial axis; leftover slivers get short squiggles. Background: outward offsets from the figures clipped to the frame, or straight rows, radial rays or rings around a centre.
- **Order**: outline strands first, then fills from the outline inward; a final "pressed" pass closes gaps slightly.
- **Relief light**: strands write a height map (rounded profile); a WebGL pass lights it with a moving raking light, so light sweeps can reveal texture.
- Finished regions are cached as sprites; only the strand being laid is live. Paths are built once under a fixed seed; texture phase is tied to arc length, so it never swims.

## 3. Colour logic

- **6–10 saturated yarn colours**; each region one colour; outlines contrast in hue *and* value with both sides.
- **No gradients**: tone changes only by switching yarn in bands of echo lines.
- **One strong background colour** (or banded rings) that contrasts with every figure; a dark outline yarn around figures for legibility.
- **Wax amber is the only neutral** and never forms an area.
- **Light**: one warm raking key; satin sheen, never metallic.
- Example: magenta `#e0218a`, orange `#ff7a00`, yellow `#ffd400`, turquoise `#00a6a6`, green `#3fb535`, cobalt `#1f3fbf`, black `#141414`, wax `#c8902e`.
- Example (cool): `#2b2d9c`, `#00b7c2`, `#f5f5f0`, `#ff3b6b`, `#ffd166`.

## 4. Type & subtitles

- **Short titles in yarn** (≤ 3 words): outlines from Baloo 2, Righteous or Bungee (Devanagari from Baloo 2) turned into an outline strand plus echo fill; minimum stroke 3 w.
- **Subtitles stay clean text**: Baloo 2 SemiBold or Righteous 34–42 px (Hindi in Baloo 2), off-white with a dark outline (~12 % of x-height), on a lower strip of solid dark strands like a woven band. Hold ≥ max(1.8 s, speech + 0.6 s).
- Never set long text in yarn.

## 5. Motion quality

- **24 fps**; laying is the main motion: the strand grows along its path at a hand's pace (8–20 w per second), on ones, the tip pressed with a slight bulge; fills cascade ring by ring.
- **Unravel and re-coil**: strands lift from their end and travel into new paths (arc-length-matched path morphs): the native transformation.
- **Figures move as whole cut-outs on twos**, their yarn texture moving with them.
- **Echo lines can ripple**: a slow phase wave along background rings, sparingly, for energy.
- **Light sweeps** change the sheen.
- Never: texture sliding along a strand, boiling outlines, half-transparent yarn.

## 6. Camera grammar

A camera over a board on a table, close enough to feel the wool. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Locked frontal board | the whole composition | an emblem; a summary; a map |
| Macro on the strand tip being pressed | craft, slowness | patience; care; repair |
| Raking-light sweep, camera locked | texture and hidden lines | a discovery; time of day; a secret pattern |
| Spiral push-in to a centre | going inward | a heart; a core idea; a seed |
| Lateral travel along a long board | sequence | a river's course; a migration; a process |
| Pull back from one strand to the whole | one thread among many | a community; a contribution; an ecosystem |

Framing: centred, symmetric compositions are native; figures fully outlined; the background fills to the edge. Transitions: unravel (strands peel into the next scene's paths); a spiral wipe (one strand coils over the frame); the board rotates. Forbidden: dissolves, digital wipes.

## 7. Sound palette

- **Material foley**: yarn drawn through fingers (soft friction noise band-passed 1–4 kHz, one burst per arm pull), a thumb pressing into wax (short sine sweep + noise), scissors snip, warm wax crackle, board taps.
- **Music**: a small bright fiddle (`violin`, high register, short bowed phrases), a small strummed guitar (`guitar_nylon` or `ukulele`), rattles (`shaker`), a soft `frame_drum`, `flute`; dry and acoustic. No chant, no imitation of ceremonial song.
- **Techniques, as options**: short melodic cells that loop like echo lines; one layer added as each ring fills.
- **Ambience**: an open-air workshop in the hills: wind, birds.
- **Silence**: only fibre friction.
- **Voice**: warm, measured; music ducked ~8 dB; −14 LUFS.

## 8. Native moves

- **Outline, then echo.** A boundary is set, then filled ring by ring. *Fits content like:* a park planned and planted; the organs of a body; the phases of a project.
- **Spiral from the centre.** *Fits content like:* an idea spreading; a whirlpool; a growing city.
- **Unravel and re-coil.** One picture's yarn becomes the next. *Fits content like:* recycling; one trade becoming another; a life change.
- **Radiant background.** Echo rings pulse outward from the subject. *Fits content like:* sound; influence; heat.
- **One strand through everything.** A single colour runs across figures, joining them. *Fits content like:* a supply chain; a family line; a river.
- **Raking-light reveal.** *Fits content like:* hidden water; a secret path; morning arriving.

## 9. Pitfalls of the medium

- Smooth fills with noise → real strands: twist stripes, gaps, fixed width.
- Yarn grows huge on zoom-ins → keep w within 6–14 px on screen; regenerate fills at the new scale or limit zoom.
- Offset failures (self-intersections, slivers) → robust polygon offsetting, simplify first, squiggle the slivers.
- Texture swimming in motion → stripe phase tied to arc length.
- Neighbours with weak contrast → automatic contrast check between adjacent regions.
- Laying everything in real time is slow to watch → batch rings or accelerate; reserve real-time laying for hero shapes.
- **Sacred source**: Wixárika yarn paintings grew from ceremonial offerings and carry sacred imagery (deer, maize, peyote, ancestors, deities). Don't use these as decoration or branding; work with secular subjects in the grammar. Don't present the film as Wixárika work; credit the tradition, and commission or consult Wixárika artists for commercial work.

## 10. Engine

No demo engine yet (draft). A first demo should build:

- `yarn.js`: `strand(path, w, colour, light, seed)` with shadow, twist, sheen, fuzz; sprite cache.
- `coil.js`: `echoFill(poly, w)` → rings or `spiral`; `medialStrand(poly)`; `squiggle(sliver)`; background `rays`, `rows`, `rings`.
- `board.js` (wax and wood, height map), `light.js` (WebGL raking light over strand heights).
- `unravel.js`: arc-length matched path morphs. `mix.py`.

Start from: `styles/engraving/demo/engine/burin.js` (`offsetRing`, `resample`, `normals`, `inPoly`, `contourHatch`) for echo rings; `styles/one-line/demo/geom.js` (`buildPath`, `posAt`, `headAt`) for laying progress; `styles/crayon-book/demo/crayon.js` (`line`, `fill`) and `styles/crayon-book/demo/gl.js` (`makeComp`) for textured marks and a compositor; `styles/watercolor/demo/engine.js` (bristle tracks, for fuzz); `styles/silkscreen-poster/demo/engine/silk.js` (`unionPath`, `ringPath`); `core/lib.js`; `core/audio/sampler.py`, `core/audio/sfx.py`.

## 11. Variation space

You decide the subject, the strand width, fill direction per region, the palette within the rules, the opening, the ending and the camera.

- Structures: **one board in reading order** (centre figure, rings outward, background last); **a triptych** (three boards joined by one strand colour); **a chain of transformations** (each shape unravels into the next).
- Openings: **a ball of yarn rolls in** and its strand starts the first outline; **raking light over bare wax** with a thumbprint; **a finished spiral**, the camera pulling out.
- Endings: **the last gap is filled**; **the board unravels** back into a ball; **the light leaves**, only outline strands keep their sheen.

---

Status: **draft** — no demo film yet. Before this is used as a library style it needs a demo film, `DEMO.md`, stills and the checks in the Lemo-Opuscar `MAINTAINING.md` ("Gates").
