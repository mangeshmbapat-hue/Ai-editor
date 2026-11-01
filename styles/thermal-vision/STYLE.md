# Thermal Vision — Style Prompt

> A long-wave infrared camera's view: the picture is a map of surface temperature shown through a false-colour palette, with a scale bar, a spot meter and the camera's own machinery (auto-ranging, shutter freezes, sensor noise) in plain sight. Heat stays where things have been and fades by physics.
> References (grammar only): building-inspection thermography (scale bar, spot meter, isotherm alarm); night wildlife films shot in thermal (warm bodies on cold ground); industrial condition monitoring (a hot bearing over time). Copy no maker's interface, logo, palette name or typeface, and never name them in the film.

## 1. Essence, and what it is not

- **Colour is temperature.** Every pixel is one palette lookup of apparent temperature; nothing else makes hue.
- **A low, soft sensor**: 320×240 or 640×480 class, a germanium lens, noise, faint column stripes.
- **The instrument is on screen**: scale bar, spot meter and reading, palette and emissivity labels; every number comes from the simulation.
- **Heat has memory**: a handprint on a wall, footsteps, a seat just left; traces bloom, spread and fade.
- **Auto-ranging is a character**: a hot thing enters and the world sinks toward cold.

Not Sci-fi Hologram HUD (no invented glowing chrome; the overlay is a plain instrument), not LiDAR Survey or Satellite Briefing (a simulated heat field, not survey data or photographs), not a "heat filter" over a colour render (hue never comes from albedo).

## 2. Materials & rendering

- **Render temperature, then colour.** The scene (a Float32 grid in 2D, or three.js meshes with a ShaderMaterial into a `HalfFloatType` target) outputs °C: `T_app = ε·T_surf + (1 − ε)·T_refl`, `T_refl` being what the surface mirrors (clear night sky −20…−40 °C, a ceiling, the operator). Skin ε 0.98, paint/wood/brick 0.90–0.95, water 0.96, glass 0.92 but **opaque**, polished metal 0.05–0.1 (a mirror). People are generic procedural figures with no faces or likeness; never footage or scans of real people.
- **Heat events in closed form**, so any frame renders alone: a contact print is a seeded mask that cools and spreads, `ΔT(t) = ΔT0·e^(−(t−t0)/τ)·σ0²/σ(t)²`, `σ(t)² = σ0² + 2D(t − t0)`. Footsteps and handprints are lists of stamps; breath and steam are curl-noise particles integrated from birth; hot air is a value-noise shimmer.
- **Sensor pass** (WebGL): downsample to sensor size, optics blur (σ ≈ 0.6 px), temporal noise (NETD ≈ 0.05 °C, reseeded per sensor frame), drifting column offsets, local-contrast enhancement leaving a thin dark halo round hot edges. Upscale bilinear: soft, not pixel art.
- **AGC**: span = 1st–99th percentile of a 64-bin histogram, smoothed (rise τ ≈ 0.4 s, fall ≈ 1.2 s) with hysteresis. Smoothing has history, so **bake `span[frame]` in a pre-pass**. A shot may lock the span; hot things then clip.
- **Shutter (NUC)**: every 40–120 s, or for a held breath, the image freezes 0.25–0.5 s with a click. Sensor rate 30 Hz, or 8.7 Hz for an export-class camera. The HUD is drawn after the sensor pass, sharp, in screen space.

## 3. Colour logic

- One palette per shot, monotonic in value from cold to hot. A palette change is a visible event (the HUD label ticks), never a grade.
- Ironbow by default (black → indigo → magenta → orange → yellow → white); white-hot or black-hot for sober scenes; rainbow only when tiny differences matter.
- **Isotherm** is the only extra hue: one saturated colour flooding a temperature band, reserved for the reading that matters. Never colour an object by hand: change its temperature or the span.
- 256-entry interpolated LUT plus ordered dither, so slow gradients do not band.
- Example ironbow: `#000000 #1d0b5a #5c0f8b #a62a8a #e0532d #f59d1f #fde66a #ffffff`. Example arctic: `#06102e #1b3f8b #3f8fd2 #c99a3a #f6e3a0`, isotherm `#3dff7a`.

## 4. Type & subtitles

- HUD: IBM Plex Mono or Share Tech Mono, 20–28 px, tabular digits, one decimal and a unit (`31.4 °C`); tags pinned to things (`Sp1 47.2`, `Bx1 max 63.0`) with 1 px leaders.
- **Subtitles**: Inter or IBM Plex Sans 500, 34–40 px, white with a 2 px black outline, no box, bottom-centre, clear of the scale bar; two lines max. Devanagari: Noto Sans Devanagari 500, same outline. Hold ≥ max(1.8 s, speech + 0.6 s).
- **Titles are heat**: a word written by a warm finger on a cold surface, or a wire bent into letters that warms through the palette (Space Grotesk 700 or Oswald paths, 120–220 px).

## 5. Motion quality

- 24 fps output; the picture steps at the sensor rate; heat physics is continuous; the HUD ticks at 2–4 Hz.
- Heat never pops: it rises over 0.2–1 s and leaves by exponential cooling; compress with time-lapse, never fake τ.
- AGC breathing is the "lighting" motion: eased, never per frame.
- Handheld = low drift (0.3–1 Hz, ±0.5°); tripod = dead still; drone = smooth. No flares or bokeh shapes in LWIR.
- Never moves: the HUD, the scale bar, the palette within a locked span.

## 6. Camera grammar

An instrument's camera: it searches, measures and waits. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Locked tripod, time-lapse cooling | heat leaving as time passes | a meal going cold; a street after sunset; an engine at rest |
| Slow pan, spot meter riding a surface | inspection; one anomaly | a hidden pipe; roof heat loss; a row of solar panels |
| Handheld search with AGC re-ranging | looking for warmth in the dark | a lost pet; a nest in a hedge; a hot server rack |
| Aerial nadir pass | a pattern seen from above | a herd count; a heating main; a leaking pipeline |
| Push in on a rolling reading | one number decides | a bearing; a kettle near boiling; a battery cell |
| Visible ↔ thermal split line | what looks fine and what is not | a house; a circuit board; a quiet forest |
| Isotherm threshold sweep | where the heat really is | a fault; a fire front; a hive's core |

Framing: subject ≥ 1/4 of the frame; the right ~10 % belongs to the scale bar; the spot meter sits on the subject, never on an edge. Transitions: hard cut, a shutter freeze as the cut point, a palette switch, the visible/thermal wipe; no dissolves between heat maps (the AGC cannot be in two places).

## 7. Sound palette

- **The camera**: shutter click (`sfx.click` pitched down + band-passed noise), a tick on palette change, a two-tone beep when an isotherm trips; a cooled camera's Stirling cooler as a steady ~50 Hz buzz.
- **Music**: cold and sparse: numpy sine drones with slow beating, noise beds, vibraphone_bowed, glass, harp harmonics, contrabass. Warmth arrives as timbre (cellos or tenor_sax_nv), not volume. Option: sonify the spot meter (1 °C ≈ a semitone).
- **Foley by what is warm or cold**: breath, steam hiss, an engine ticking as it cools (seeded clicks, lengthening gaps), steps on frozen ground; night beds of wind and crickets.
- **Silence**: a still, cooling frame, room tone, one shutter click.
- **Voice**: a calm field operator or naturalist, numbers spoken as words. Music ducked ~6 dB; −14 LUFS.

## 8. Native moves

A menu: use the ones your story needs.

- **The heat trace.** Something leaves; its warm print stays, spreads and fades. *Fits content like:* a chair just vacated; paw prints across a frozen yard; a door handle that tells who passed.
- **AGC re-range.** A hot thing enters and the world sinks to black; when it leaves, detail rises back. *Fits content like:* a match in a cold room; a kettle switched on; the sun clearing a ridge.
- **Isotherm flood.** A band floods in one colour; raising the threshold shrinks it to the source. *Fits content like:* an overloaded socket; a leaking pipe under a floor; a compost heap's core.
- **Glass is a mirror.** A window shows only the operator's warm reflection. *Fits content like:* a house keeping secrets; a shop window at night; a look at oneself.
- **Thermal crossover.** At dawn or dusk subject and background match and the image goes flat, then returns inverted. *Fits content like:* a change of shift; a day's turning points; two rivals becoming alike.
- **Cooling clock.** A locked time-lapse where cooling is the clock. *Fits content like:* bread leaving the oven; a car park after rush hour; a forest after a storm.

## 9. Pitfalls of the medium

- **Colouring the scene instead of its temperature** breaks every AGC change → render a float temperature target; colour only in the LUT pass.
- **Photographic sharpness** reads as a filter → sensor downsample, blur, noise, stripes.
- **Seeing through walls or glass** → surfaces only; hidden things show through their effect on a surface (pipes as stripes).
- **Shiny metal glowing hot** → low ε that mirrors the room; a strip of tape (ε 0.95) for a true reading.
- **AGC pumping every frame** → percentile span with time constants and hysteresis, baked, or a locked span.
- **Surveillance and targeting looks** (crosshairs on people, gunsight reticles, fever screening) → synthetic figures only, no faces or identities; meter things and animals; never present output as a real measurement of a person.

## 10. Engine

No demo engine yet (draft). A first demo should build:

- `heat.js`: materials `{T, eps}`, `apparent(T, eps, Trefl)`, temperature render, `stamp(x, y, mask, t0, dT, tau, sigma0)`, `plume(seed, t)`.
- `sensor.js`: `sensorFrame(t, hz)`, `downsample(res)`, `noise(netd, seed)`, `fpn(seed, t)`, `nuc(times)`.
- `palette.js`: 256×1 LUTs, `bakeSpan(frames)` with plateau equalisation, `isotherm(lo, hi, hue)`.
- `hud.js`: spot meter, boxes, scale bar, rolling readouts.

Start from `core/lib.js` (`mulberry`, `vnoise`, `ss`), `styles/microgame/demo/glpass.js` (WebGL pass helper), `styles/pixel-rpg/demo/px.js` (palettes as lookup swaps), `styles/hologram-hud/demo/engine/hud.js` (leaders, rolling numbers; recolour white), `core/render/video.mjs`, `core/audio/sfx.py`, `core/audio/sampler.py`.

## 11. Variation space

You decide the subject, the palette and whether it changes, the sensor rate, whether readings are spoken, and whether a visible counterpart appears.

- Structures: **a night survey** (an operator walks a site; each anomaly a stop with a reading); **one place through a day** (a locked view, dawn crossover to night); **a relay of warmth** (heat passed from hand to cup to table to cat, each print fading as the next forms).
- Openings: **a black frame that is really cold** until one warm breath appears; **a shutter click on a frozen image** that starts to move; **the visible picture** with a split line sliding across.
- Endings: **the last trace fading** into the room; **thermal crossover**, the image going flat at dusk; **a window** holding only the operator's warm reflection.

---

Status: **draft** — no demo film yet. Before this is used as a library style it needs a demo film, `DEMO.md`, stills and the checks in the Lemo-Opuscar `MAINTAINING.md` ("Gates").
