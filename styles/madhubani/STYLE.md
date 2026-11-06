# Madhubani — Style Prompt

> Mithila painting that draws itself: every form is a double ink outline laid by a bamboo nib, then every gap is packed with hatching, dots and flat earth colour until no bare ground is left.
> References (grammar only): Mithila (Madhubani) painting of the Mithila region of Bihar and the Nepal Terai, painted mostly by women on the mud walls of the home for weddings and festivals, and on paper since the 1960s; its two best-known manners, *Bharni* (flat filled colour) and *Kachni* (fine line and hatching). Take the double line, the filled ground, the bordered panel and the motif logic; never copy a specific painting or painter, and never name them in the film.

## 1. Essence, and what it is not

- **The double outline.** Every form is two near-parallel ink lines 3–8 px apart; the channel between them is bare, a second colour, or tiny ticks. A single outline reads as unfinished.
- **No bare ground.** Inside and around every figure the space is packed: hatching, cross-hatch, chevrons, dot rows, small leaves, scales.
- **Every picture is a bordered panel.** One to three pattern bands (zigzag, chained loops, creeper, triangles) enclose the composition.
- **A small symbolic cast**: paired fish, peacocks, parrots, turtles, a sun and moon with faces, lotus, bamboo, the tree. Bodies are flat; a human face is in profile with one large frontal almond eye.
- **Pattern is the shading.** Distance, mass and mood come from fill density and direction, never from light.

Not Gond (Gond fills a flat body with one flowing dot-and-dash texture on a plain ground; Madhubani fills the ground too and doubles every line), not Warli (no white stick figures on mud), not Woodcut Print or Copperplate Engraving (hatching is ornament and rhythm, not tone modelling light), not Crayon Picture Book (no wax tooth, no child logic).

## 2. Materials & rendering

- **Ground**: handmade paper (warm fibres, deckle edge) or a mud-washed wall (ochre blotches ±6 %, grit, cracks); seeded, cached, world-anchored, never animated.
- **The nib**: each line is a polyline at near-constant width (1.6–3 px at 1080p) with ±10 % width noise, an ink pool at the start (a 1.3× dot) and a dry tail, advancing at writing speed (600–900 px/s) so drawing order shows.
- **Double line**: offset the centre ring by ±d/2 and draw each offset as its own nib stroke with an independent wobble seed; closed rings overlap 2–4 px where they meet.
- **Fills** are clipped to a region (body, channel or ground): `hatch` (spacing 3–6 px), `crossHatch`, `chevron`, `dotRows`, `scales`, `leafTiles`, `concentric` (rings stepping inward). Every fill line is a nib stroke, not a bitmap. *Bharni* colour is poured flat with ±4 % mottling, stopping 1–2 px short of the ink; the ink is re-drawn over it.
- **Ground fill**: a Poisson-disc scatter of small motifs (four-petal flowers, leaves, dots) with collision against figures; the remainder is hatched. Coverage test: no bare disc wider than 3 % of frame height.
- **Cache** finished figures as sprites; only a figure being drawn is drawn stroke by stroke from a list built once under a fixed seed (`mulberry`): every frame is a pure function of t.
- **No scene light**: paper texture multiplied over everything, at most a faint warm vignette in screen space.

## 3. Colour logic

- **One manner per film.** *Kachni*: ink plus one red on cream, colour only in channels and accents. *Bharni*: 4–6 saturated flower-and-earth hues in flat fields.
- **Black is the structure**: colour never meets colour without a line between.
- **Flat and opaque**: no gradients, shading or highlights. Darker means a hatch laid over the hue.
- Neutral ground is cream or mud ochre; the brightest value is a bare channel.
- One hue may be reserved for the film's key motif and never used elsewhere.
- Example (Bharni): ground `#efe2c2`, ink `#1d1712`, vermilion `#c8321e`, turmeric `#e5a823`, leaf `#3f7d3a`, indigo `#2b4a8c`, pink `#df6a8a`. Example (Kachni): `#f1e6cc`, `#1a1410`, `#b52a1c`.

## 4. Type & subtitles

- Subtitles live in a **lower border band** of the panel (~1/9 of the frame tall, double-ruled), ink on ground colour, never a box.
- **Kalam** for subtitles (34–42 px) and small labels beside motifs (24–30 px); **Yatra One** for titles (64–110 px). Devanagari: Kalam for subtitles, Yatra One or **Tiro Devanagari Hindi** for titles; Hindi subtitles sit in the same band.
- Titles take the double line: text to mask, trace the outline, nib it twice, tick the channel.
- Subtitles write in left to right (~0.4 s), leave by fading into the band. Hold each ≥ max(1.8 s, speech + 0.6 s).

## 5. Motion quality

- **Drawing-in is the main motion**: outline one, outline two, channel, body fill, then the ground around. A figure takes 1–3 s; a crowd draws in parallel with staggered starts. Pen and camera on ones (24 fps).
- **Figures move flat, on twos**: translate, pivot, swap a pose. A fish swims by a travelling sine along its spine; its hatching lives in spine coordinates and bends with it.
- Finished figures **do not boil**; a 2-frame tremor only while the nib draws.
- Appear by being drawn; disappear by being hatched over into the ground, or under a wash of ground colour.
- Easing `eio`; `back` only for a motif landing. Never moves: border, ground, paper.

## 6. Camera grammar

A panel on a wall or a sheet on the floor: the camera stays square to it.

| Move | What it expresses | Can serve |
|---|---|---|
| Locked full panel inside its border | a whole symbolic order at once | a household; a blessing; a cycle of the year |
| Slow push into one motif | closeness to one symbol | a gift; a single choice; a name |
| Lateral track along a wall of panels | scenes in a row | steps of a process; a family history; a market lane |
| Pull back from a fill to its figure | pattern becomes meaning | a field that is a crowd; a texture that is a fish |
| Close follow of the nib | making as content | a lesson; patience; a craft |
| Tilt down a tall panel (sky, tree, pond) | the world in layers | an ecology; a day; floors of a house |
| Cut between bordered panels | chapter breaks | chapters; options side by side; before and after |

Framing: silhouettes read first; symmetry is welcome; a border edge stays in frame except in a deep push. Transitions: a border draws around the next scene; ground fill swallows the old one; a lateral move. Forbidden: dissolves, zoom blur, lens flare, perspective moves.

## 7. Sound palette

- **Instruments**: a dholak-like drum (the synthesised tabla model, rounder and lower), jhal cymbals (`nepal_bells`, a choked `crash`), harmonium (`accordion`), bamboo flute (`flute`), a drone (`pluck('shamisen', …)`, long t60, high buzz). Never imitate a specific ritual or wedding song; write an original melody or use hum and drone.
- **Foley**: nib scratch per stroke (band-passed noise, length = stroke length), a soft dab per fill, paper rustle, water plops, synthesised bird chirps, wind in bamboo.
- **Ambience**: a courtyard (distant cattle bells, sparrows), monsoon rain on tiles. **Silence**: the nib lifted, paper room tone only; cut beds hard.
- **Voice**: warm and close, short lines; Hindi narration via `core/tts/tts.py` works. Music ducked ~8 dB under voice; −14 LUFS.

## 8. Native moves

- **Horror vacui fill.** Gaps fill with motifs and hatching until nothing is bare, all driven by one progress value. *Fits content like:* a city growing dense; a calendar getting booked; a field after sowing.
- **Two lines, two voices.** The two outlines of one form are drawn at different moments or in two colours; the channel carries the message. *Fits content like:* a partnership; a border between two places; a bilingual word.
- **Density as feeling.** A figure re-hatched tighter, looser or at a new angle. *Fits content like:* a fever; drought spreading; a crowd's mood turning.
- **Mirrored pair.** Two motifs face each other across an axis and act in mirror. *Fits content like:* two teams; a negotiation; twins.
- **Border as clock.** The border draws itself one segment per unit of time. *Fits content like:* a countdown; months of a project; a year of savings.
- **Swallowed by pattern.** The ground's pattern grows over a figure until it is gone. *Fits content like:* forgetting; a species lost; a village under flood water.

## 9. Pitfalls of the medium

- Single outlines read as colouring-book art → always double, independent wobble.
- Bare gaps read as clip art → coverage test on every held frame.
- Hatching that curves with form and darkens to one side reads as engraving → fixed angle per region, even spacing.
- Gradients, shadows, glows → forbidden; darker means a hatch.
- Mechanically perfect lines → width noise, ink pools, overlaps where rings close.
- Motif soup → small cast; ground motifs at least 4× smaller than figures.
- **Sacred motifs as decoration.** The *kohbar* wedding painting, deities and their emblems carry ritual meaning: never use them as ornament, for a product or in jest. Do not present a code-made film as authentic handmade Mithila painting; for commercial work, credit or consult Mithila artists.

## 10. Engine

No demo engine yet (draft). A first demo should build:
- `nib.js`: `nibStroke(pts, {w, wobble, pool, seed})`, `doubleLine(ring, d, seedA, seedB)`, `strokeProgress(list, p)`.
- `fill.js`: `hatch`, `crossHatch`, `chevron`, `dotRows`, `scales`, `concentric`, `scatterMotifs(region, motifs, rMin, seed)`, `coverage(mask)`.
- `motifs.js`: fish, peacock, parrot, sun, moon, lotus, bamboo, tree as local rings with fill recipes; `spineBend(fig, t)`.
- `panel.js`: grounds, `border(rect, bands)`, sprite cache, subtitle band, `render(t)`.

Start from `styles/one-line/demo/geom.js` and `demo/ink.js` (path sampling, ink line), `styles/woodcut/demo/engine/hatch.js` (`hatch`, `lines`), `styles/engraving/demo/engine/burin.js` (`offsetRing`, `inPoly`, `subtract`), `core/lib.js`, `core/render/`, `core/audio/sampler.py`, `core/audio/pluck.py`.

## 11. Variation space

You decide the manner, the motif cast, what the ground fill means, the border bands, the opening, the ending, the camera path and the pacing.

- Structures: **one wall, many panels** (a lateral walk, each panel a chapter); **one panel that fills** (a single composition grows denser as the story accumulates); **a pair** (two mirrored halves as call and answer, joined at the end in one border).
- Openings: **a bare wall being washed** before the first line; **one motif already finished**, the camera pulling back as the rest is drawn; **the border first**, an empty frame waiting.
- Endings: **the last gap filled**; **the nib lifted mid-hatch**, one area left bare on purpose; **pattern swallows all** but one small motif.

---

Status: **draft** — no demo film yet. Before this is used as a library style it needs a demo film, `DEMO.md`, stills and the checks in the Lemo-Opuscar `MAINTAINING.md` ("Gates").
