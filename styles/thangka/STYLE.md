# Thangka — Style Prompt

> Himalayan scroll painting brought to life for secular subjects: a gessoed cotton canvas built up from a charcoal proportion grid, dense mineral colours shaded in soft same-hue gradations, gold line on everything precious, cloud scrolls and blue-green hills, the whole picture mounted in silk brocade.
> References (grammar only): thangka painting of Tibet, Nepal (including the Newar painters of the Kathmandu Valley), Bhutan and the wider Himalaya for the measured grid, hierarchical composition, mineral palette, gold line, gradation shading, cloud and landscape conventions and the brocade mount. Never depict or adapt Buddhist deities, teachers, deity mandalas, mantras or sacred syllables, never copy a specific thangka, and never name them in the film.

## 1. Essence, and what it is not

- **A measured centre**: the composition grows from a grid; one central subject, large and frontal, with smaller subjects arranged symmetrically around it in registers or a ring (scale is rank).
- **Mineral colour**: dense, matte, opaque blues, greens, reds, yellows, white and black laid flat, then shaded by fine same-hue gradations toward edges.
- **Gold line**: outlines and ornament in gold over colour, burnished in places so it catches the light.
- **Landscape conventions**: rounded blue-green hills with banded shading, lakes with curling waves, multi-banded cloud scrolls, flowers and jewels in the foreground, deep blue sky lightening to the horizon.
- **The mount**: silk brocade borders with narrow red and yellow inner strips, a lower panel, wooden dowels, a thin veil that can lift.

Not Stained Glass (nothing transmits, no lead: matte mineral paint and gold line), not Ukiyo-e (painted, not printed; symmetric hierarchy and gold), not the sibling draft Persian Miniature (no stacked garden planes: a symmetric centre with registers), and not a mandala generator.

## 2. Materials & rendering

- **Ground** (cached): cotton weave under chalk-and-glue gesso, polished smooth (weave faint in thin areas), a soft sheen.
- **Grid layer**: charcoal construction lines (centre axis, diagonals, circles, proportion units) in a dry, grainy line (1–1.5 px, ~50 %), drawn first and covered later.
- **Paint**: ink underdrawing (fine, even) → flat opaque fills with slight granularity → **gradation shading**: a distance-from-edge ramp in the region's own hue, rendered through a fine blue-noise stipple (1–2 px) so it reads as patient brushwork, not a digital gradient.
- **Lines**: final ink lines (dark red-brown or black), then **gold**: ochre-gold strokes with a sheen term keyed to camera position, grain, and burnished points that sparkle as the camera moves.
- **Cloud scrolls**: rows of lobes ending in spiral curls, filled in 2–4 colour bands shaded from the outline inward, gold-outlined.
- **Hills and water**: rounded mounds with horizontal blue-green banding and lighter tops; lakes and waterfalls in curl-wave patterns; flowers and gems as small sprites.
- **Mount**: a three.js plane (or 2D with a normal map) carrying a procedural damask in gold thread on silk with soft anisotropic sheen; the veil as a thin cloth with simulated folds that lifts; dowels with metal end caps; an unroll from the top dowel.
- **Painting order** (deterministic progress): grid → sketch → background colours → land → central subject → shading → ink line → gold. Built once under a fixed seed; a pure function of `t`.

## 3. Colour logic

- **6–8 mineral pigments + gold**, opaque and dense; shading moves lighter or darker within a hue, never toward grey.
- **Deep blue sky, green hills**, vermilion and orange accents, white for clouds and highlights, ink for outlines.
- **Gold marks what is precious**: outlines of the central subject, ornaments, the brightest accents; never large flat areas.
- **The brocade mount is the frame neutral**: red and yellow inner strips, an outer silk in dark blue or a gold-patterned weave.
- **Value**: the centre carries the strongest contrast; registers step down.
- Example: azurite `#1e4fa3` / light `#6f9bd8`, malachite `#2f8a5a` / light `#8cc9a0`, cinnabar `#c0342b`, orange `#e2782a`, orpiment `#e8c33a`, white `#f2efe6`, ink `#1d1a1a`, gold `#c8a14a`; mount red `#9e1b1b`, yellow `#e3b21a`, outer `#1c2f6b`.

## 4. Type & subtitles

- Little text belongs on the painting: a narrow inscription band at its foot, or an embroidered label on the lower brocade panel.
- **Subtitles** sit on the lower brocade: Cormorant Garamond 600 or EB Garamond 32–40 px, gold-cream on dark silk with a thin gold rule; Hindi in Tiro Devanagari Hindi or Noto Serif Devanagari. Hold ≥ max(1.8 s, speech + 0.6 s).
- **Tibetan script** (Noto Serif Tibetan) only for real, reviewed secular text; never mantras or sacred syllables.
- **Titles**: gold lettering on a dark band, or woven into the brocade.

## 5. Motion quality

- **24 fps**; painting-in is the main motion, stages overlapping region by region.
- **Living details on twos**: cloud scrolls drift and curl (lobes rotate slightly, bands turn), waves loop, waterfalls shimmer, birds and animals move as cut-outs; the central subject moves least.
- **The mount moves as cloth**: the veil lifts (1.5–3 s), the scroll unrolls from the top dowel, the brocade sways a little when hung.
- Gold glints shift with the camera.
- Never moving: the centre axis, the grid geometry, the registers' positions.

## 6. Camera grammar

The camera stands before a hanging scroll and moves along its axis. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Frontal, whole scroll with brocade | presence, order | a portrait of a place; a summary; a teaching |
| Vertical tilt down the scroll | sky to ground | peaks to valley; a source to a river; generations |
| Push in to the centre | concentration | a core idea; the heart of a system |
| Rotation about the centre | cycles | seasons; the water cycle; a working year |
| Macro on gold line | precision, value | craft; something precious; a detail that matters |
| Veil lift | unveiling | a discovery; an opening; a launch |
| Scroll unroll | beginning a record | a chronicle; a map; an archive |

Framing: symmetric; the centre axis on frame centre in wides; brocade visible in wides; registers never cropped arbitrarily. Transitions: unroll and roll-up; veil lift and fall; cloud scrolls sweeping across as a wipe; painting-in from the grid. Forbidden: crossfades, glitch, lens flares.

## 7. Sound palette

- **A secular Himalayan palette**: a plucked lute (`pluck('shamisen')` with low buzz, or `pipa`), bamboo flute (`flute` with breath), soft `frame_drum`, sparing bells (`hand_chimes`, `nepal_bells`), low bowed drones (`contrabass`, `cellos`, `organ_pedal`).
- **Monastic instruments and chant belong to religious practice**: don't imitate long horns, ritual oboes, cymbal rites or chanting as background colour. If a low swell is needed, build an abstract one (`tuba` or `trombone` with a slow crescendo) that follows no ritual pattern.
- **Foley**: brush on gesso (fine scratch), charcoal on cloth, a burnishing stone (friction noise), brocade rustle, the veil's whisper, a dowel knock, mountain wind, streams, animal bells far off.
- **Silence**: high-altitude wind alone.
- **Voice**: calm, close narrator, little reverb; music ducked ~8 dB; −14 LUFS.

## 8. Native moves

- **From grid to picture.** Charcoal proportions first, then everything finds its place. *Fits content like:* architecture; a city plan; the proportions of a body.
- **Hierarchy by scale.** One large centre, smaller things around it. *Fits content like:* a keystone species; a river and its tributaries; a core product and its parts.
- **Cloud-scroll wipe.** Banded clouds roll across and change the scene. *Fits content like:* weather; time passing; a dream.
- **Veil lift / unroll.** The picture is revealed as an object. *Fits content like:* an annual event; an archive opened; a reveal.
- **Registers around the centre.** Small scenes ring the centre, read in order. *Fits content like:* the water cycle; a crop's year; the stages of a craft.
- **Gold line last.** Gold traces what matters. *Fits content like:* highlighting value; trade routes; heritage worth keeping.

## 9. Pitfalls of the medium

- Smooth digital gradients → same-hue stippled gradation.
- Gold painted as yellow → metallic sheen and burnished glints.
- Asymmetric drift → build on the grid and check symmetry.
- Generic swirl clouds → curl-ended lobes, banded colour, gold outline.
- Brocade moiré → pre-filtered damask, soft anisotropic sheen.
- Exotic cliché → no "mystic East" framing, no chant as spice.
- **Sacred objects**: thangkas are religious images used in practice, painted by trained painters to iconometric rules and consecrated. Never use deities, teachers, deity mandalas, mantras, seed syllables or ritual objects, for decoration or for products. Keep subjects secular (landscape, animals, people, science); even then, don't present the film as a thangka or as authentic work. Credit the tradition and consult practitioners and thangka painters on appropriateness, and commission them for commercial work.

## 10. Engine

No demo engine yet (draft). A first demo should build:

- `ground.js` (gessoed cotton, sheen), `grid.js` (`drawGrid(spec, p)`: axis, diagonals, circles, units).
- `paint.js`: flat fills; `shade(region, hue, dir, steps)` by distance ramp and blue-noise stipple.
- `line.js`: ink and gold lines, burnish glints.
- `cloud.js` (scroll lobes, banded fills), `land.js` (hills, lakes, waves, waterfalls, flowers).
- `mount.js` (brocade, veil, dowels, unroll), `mix.py`.

Start from: `styles/ukiyoe/demo/print.js` (`bokashi`, `kasumi`, `fillPath`, `line`) for gradations and banded clouds; `styles/ukiyoe/demo/wave.js` (`wave`, `foam`) for curling water; `styles/art-deco/demo/engine/deco.js` (`goldGrad`, `goldFlat`, `sparkle`) for gold; `styles/engraving/demo/engine/burin.js` (`stipple`) for shading; `styles/papercut-red/demo/fold.js` (`camFold`, `drawFold`) as a start for the unroll; `core/three/post.js` for the mount; `core/lib.js`; `core/audio/pluck.py`, `core/audio/sampler.py`.

## 11. Variation space

You decide the secular subject, the centre and its registers, the palette within the rules, how much of the mount is shown, the opening, the ending and the camera.

- Structures: **a valley from source to plain** (registers from glacier to fields, the river as axis); **a cycle around a centre** (seasons, water or a crop's year in a ring); **the workshop** (the picture made from grid to gold while its subject is explained).
- Openings: **the rolled scroll** untied on a table; **a charcoal axis** on blank gesso; **a cloud scroll in macro**, pulling out to the whole.
- Endings: **the veil falls** back; **the scroll is rolled up** and tied; **only the gold lines remain** as colour fades to gesso.

---

Status: **draft** — no demo film yet. Before this is used as a library style it needs a demo film, `DEMO.md`, stills and the checks in the Lemo-Opuscar `MAINTAINING.md` ("Gates").
