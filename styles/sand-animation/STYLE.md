# Sand Animation — Style Prompt

> Dark sand on a backlit glass table, filmed from above: light is wherever the sand has been pushed away, and a fingertip, the edge of a palm or a falling trickle turns one picture into the next without a cut.
> References (grammar only): live sand-art performance on a lightbox (each image becomes the next in front of the audience); 1970s under-camera sand shorts of the National Film Board of Canada era (sand moved between exposures, figures dissolving into landscape). Never copy a performance's images, sequences or music, and never name them in the film.

## 1. Essence, and what it is not

- **One plate of light, one material.** A glowing glass plate; everything on it is sand. Thin sand glows amber, thick sand is opaque near-black: tone is sand *depth* and nothing else.
- **Drawing by removal.** A line of light is a channel ploughed by a fingertip, with a soft raised berm on both sides. Light areas are swept clear, never painted on.
- **No cuts.** The next picture is made from the sand of the last: a sweep's berm becomes the next contour, a moon is pushed into an eye, a crowd is swept into a wave.
- **Grain at every edge.** Where sand thins it breaks into single visible grains; masses have soft, slightly ragged contours, never vector-clean.
- **Hands or no hands.** Performance mode shows the artist's hands as silhouettes; under-camera mode never does. Pick one per film.

Not Shadow Puppetry (no puppets or cloth: a heap of material, not cut pieces), not Chinese Ink Wash (no brush or paper; tone is the depth of a heap that can be pushed back), not Paper-cut Lightbox (one plane of glass, no stacked sheets), not chalk or charcoal (nothing is drawn on; it is uncovered).

## 2. Materials & rendering

- **Height field.** The world is a sand depth map `h(x,y)` anchored to the glass (~960×540 cells for 1080p) in WebGL2 float ping-pong textures.
- **Tools are mass-conserving stamps along paths**: `carve` (fingertip, radius ≈ 1/80–1/50 of frame width) removes sand inside a moving disc and redeposits it in a ring 1.3–2 r out, biased ahead of the motion (bulldozer model); `sweep` (palm edge, a long capsule) moves a whole band; `pour` (trickle from a fist) adds a seeded Gaussian; `press` makes a round hole with a rim; `scratch` (fingernail) cuts a 1–2 cell hairline; `flick` throws seeded grains that land and add to `h`.
- **Relaxation**: 2–4 angle-of-repose iterations after each tool step round berms and turn stamps into heaps.
- **Light**: `L = lightbox(x,y) · gel(x,y) · exp(−σ·h)`, with σ chosen so 4–6 density bands read between bare glass and opaque. The lightbox is warm white (~3200 K) with a broad hotspot falling 8–15 % toward the corners.
- **Grain**: a world-anchored hash field. Where `h` is thin, a pixel is either a grain or glass, with probability from `h`: thin sand is dithered by grains, never translucent grey. Berm crests get a faint cool glint (≤ 5 %).
- **Hands** (performance mode): a jointed 2D silhouette, slightly soft (closer to the lens), a warm rim on the fingertips from below; outside the transmission model.
- **Determinism**: the simulation is path-dependent: bake it sequentially at a fixed step with checkpoints every 12–24 frames; `render(t)` seeks the nearest and replays seeded tool events.

## 3. Colour logic

- **Monochrome by transmission**: one light colour and its absence. Mid-tones are thin sand glowing warm; shadows are deep warm umber, never neutral grey or blue.
- Bare glass is the only near-white; nothing is brighter than the lightbox.
- **One optional accent, a gel** under part of the glass. It colours light, never sand. Reserve it for one recurring meaning; at most two gels per film.
- Value order: a light figure in dark ground, or a dark mass against light; never a 50/50 grey frame.
- Example: lightbox `#f6e3bf`, thin sand `#c9925a`, mid `#6e4a2c`, opaque `#1e140c`, gel `#d2452c`.
- Example (cool night): lightbox `#dfe6e4`, sand `#2a2622`, gel `#3d7fb8`.

## 4. Type & subtitles

- **Titles are carved with a fingertip**: a centreline (hand-authored, or a thinned glyph of Kalam or Caveat; Kalam or Yatra One for Devanagari) ploughed progressively, berms included; letters ≥ 1/10 of frame height.
- **Subtitles** are light, not sand: EB Garamond or Cormorant Garamond 34–42 px in the lightbox colour at ~90 %, a soft dark halo, no box, on the darkest band of the plate. Devanagari: Tiro Devanagari Hindi or Noto Serif Devanagari at the same visual size. Two lines max, 0.2 s fades; they are never swept.
- Hold each subtitle ≥ max(1.8 s, speech + 0.6 s).

## 5. Motion quality

- **24 fps.** Performance mode changes on ones at human speeds: fast sweeps (0.2–0.4 s across the frame, ease-out), slow detail strokes. Under-camera mode changes on twos, and grain reseeds per drawing (≤ 1 cell boil on thin edges).
- **Structure before detail**: masses (sweep, pour), contours (carve), then details (press, scratch).
- **Appear** uncovered or poured in; **disappear** swept, buried or blown.
- A figure moves by being redrawn: carve the new pose, sweep the old one into ground.
- **Never moves**: the glass, the lightbox hotspot, the overhead axis (except as a deliberate move). Grain never swims.

## 6. Camera grammar

The camera hangs over a table; most of a film is one locked overhead frame. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Locked overhead, whole plate | The performance: every change is seen | a metamorphosis; a list of places; a life in stages |
| Slow push into one region | Leaning in while detail is carved | a face; a window; a single lamp |
| Drift following the fingertip | Being carried by the act of drawing | a route; a river traced; a letter written |
| Pull back past the plate edge to table and artist | The world is a heap on glass | a frame story; a telling that ends; "it was only sand" |
| Roll of 90–180° on the locked plate | Up becomes down, a horizon becomes a wall | a fall; a dream; the other side |
| Low oblique view across the heaps | Relief: sand as landscape | a dune; a ruin; an aerial memory |

Framing: the picture stays in the central 80 % of the plate, with a band for subtitles. Transitions: sweep, pour-over, a palm over the lens, the lightbox dimming; never a crossfade, a hard cut between unrelated pictures or a digital wipe.

## 7. Sound palette

- **Intimate and acoustic**: piano, `cellos` or `violin`, `harp`, `guitar_nylon`, `hang`, `kalimba`, `vibraphone_bowed`, `glass`, a soft `frame_drum`; a numpy drone (detuned sines + filtered noise) for desert or night; tanpura colour from `pluck('shamisen', …)` with long t60 and high buzz.
- **The sand is the foley**: a granular hiss whose level follows the swept volume per frame (band-passed noise 1.5–7 kHz with sparse click grains for coarse sand); pours = low granular rumble plus hiss; a press = a soft tap on glass; a flick = a short spray; a palm on glass = a muffled slap. Build them from exported tool events.
- **Silence** is a lifted hand: music out, a hiss tail fading, at most one sound inside.
- **Voice**: a close, quiet storyteller, few lines; music ducked ~8 dB under voice; final −14 LUFS.

## 8. Native moves

- **Sweep metamorphosis.** A palm edge crosses the picture; its berm lands where the next picture's key line must be. *Fits content like:* a coastline becoming a face; a field turning into a crowd; a map becoming a family tree.
- **Line of light.** One fingertip channel draws a figure out of dark sand in a single stroke. *Fits content like:* a route home; a signature; a pulse line.
- **Pour of night.** A trickle buries the light areas and builds new masses. *Fits content like:* dusk over a town; a flood rising; forgetting.
- **Press of lamps.** Fingertip holes in dark sand become windows, stars or eyes. *Fits content like:* a village lighting up; a count of homes; a sky of names.
- **Breath scatter.** A gust breaks a figure into grains that resettle as another. *Fits content like:* a seed head; a rumour spreading; a monument eroding.
- **The giant hand.** The artist's hand looms over the world. *Fits content like:* fate; a parent over a childhood memory; a maker and the thing made.

## 9. Pitfalls of the medium

- Lines without berms look like an eraser on a picture → every carve redeposits sand; relax after each tool.
- Smooth gradients read as airbrush → thin sand is grain dither, not translucent grey.
- A path-dependent simulation breaks parallel rendering and seeking → sequential bake with checkpoints; every path and spray seeded.
- Detail sand cannot hold → minimum feature ≈ one fingertip (nail scratches excepted); simplify silhouettes.
- Flat grey frames with no silhouette → each picture mostly dark with a light figure, or mostly light with a dark one.
- Hands hiding the picture → enter, act, leave; never during a spoken line.
- Grain swimming on camera moves → grain belongs to the glass, not the screen.

## 10. Engine

No demo engine yet (draft). A first demo should build:
- `sand.js`: the height field and tools (`carve(path, r, depth)`, `sweep(capsule, dir)`, `pour(x, y, rate, spread)`, `press(x, y, r)`, `scratch(path)`, `flick(x, y, dir, n)`, `relax(iters, repose)`), seeded with `mulberry` and shaped with `vnoise` / `ss` / `eo` from `core/lib.js`.
- `bake.mjs`: sequential tool timeline, checkpoints, `stateAt(t)`, swept volume per frame as sound events.
- `light.js`: WebGL2 compositor (`lightbox · gel · exp(−σh)`, grain dither, crest glints); start from the transmission compositor in `styles/shadow-puppet/demo/gl.js`.
- `hand.js`: silhouette hand rig; jointed pieces after `styles/papercut-red/demo/rig.js`.
- `glyph.js`: centreline titles (thinned glyph masks → carve paths).
- `foley.py`: hiss, pour and taps from `core/render/events.mjs` output via `core/audio/sfx.py` (`bp`, `noise`, `thump`); music from `core/audio/sampler.py` / `pluck.py`; voice `core/tts/tts.py`.
Render with `core/render/video.mjs`, `srt.py`, `mux.sh`.

## 11. Variation space

You decide the subject, the mode (performance or under-camera), the sand and lightbox colours, whether a gel appears, the opening, the ending and the pace of metamorphoses.

- Structures: **one continuous transformation** (a single plate becomes ten pictures in one locked take); **a house across decades** (each sweep moves to the next room and generation); **call and answer** (two hands draw from opposite edges of the plate and meet in the middle).
- Openings: **a full plate of dark sand** with one fingertip hole of light; **an empty lightbox** and a trickle from above; **the artist's hands resting** on the glass edge before the first touch.
- Endings: **swept clean** to bare light; **the lightbox switched off**, the last picture a dark heap in room light; **one breath** that leaves a single figure standing.

---

Status: **draft** — no demo film yet. Before this is used as a library style it needs a demo film, `DEMO.md`, stills and the checks in the Lemo-Opuscar `MAINTAINING.md` ("Gates").
