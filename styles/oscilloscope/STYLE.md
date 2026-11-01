# Oscilloscope Art — Style Prompt

> One green beam of light on the dark glass of an oscilloscope in XY mode, drawing every image as a single continuous path many times a second; brightness is where the beam lingers, trails are phosphor memory, and the soundtrack can be the very signal that draws the picture.
> References (grammar only): XY-mode oscilloscope music and laboratory demonstrations (a stereo signal as a picture); Lissajous figures of the 19th century (frequency ratios as shapes); early analog computer graphics on vector scopes in the 1950s–60s (rotating wireframes, single-stroke lettering). Never copy a specific oscilloscope music piece or instrument faceplate design, and never name them in the film.

## 1. Essence, and what it is not

- **One beam**: a single point of light moving continuously; every image is a path. No fills except by scribbling, no second independent colour.
- **Phosphor light**: brightness ∝ time spent (slow = bright, fast = faint); corners and turnarounds glow; persistence leaves fading trails; a soft halo blooms around bright spots.
- **Retrace lines**: the beam is never switched off, so faint lines join separate shapes; they are part of the look.
- **The instrument**: dark grey-green glass, an etched 8 × 10 graticule with minor ticks, a bezel outside the screen.
- **Sound and picture are one signal**: left channel = x, right = y. The film can be heard as it is drawn.

Not ASCII / CRT Terminal (raster characters on a grid; here no raster at all), not Sci-fi Hologram HUD (many lines, panels and data; here one trace), not a vector arcade display (blanked beam between objects, game playfield and colour overlays; here a lab instrument with one unblanked trace driven by audio), not Circuit Board.

## 2. Materials & rendering

- **Path model**: `path(t, s)` returns `(x, y)` for `s ∈ [0, 1)`, the shape at time `t`. Shapes are polylines, parametric curves (Lissajous, circles, spirals) or projected 3D wireframes ordered into one continuous route (nearest-neighbour ordering to minimise jumps).
- **Beam sampling**: the path is traversed `f` times per second (40–200 Hz); sample it at 48 kHz, i.e. 2000 points per 24 fps frame. This stream is both the picture's source and an optional stereo audio file.
- **Splatting** (WebGL2, additive float target): each segment between consecutive samples is drawn as an analytic Gaussian line (`exp(−d²/σ²)`, σ ≈ 1–1.6 px at 1080p) with energy ∝ segment duration / segment length, so slow parts glow. Bright spots get a slightly wider σ (spot blooming). Tiny deflection noise ±0.3 px.
- **Persistence without feedback**: render the last k frames' beam segments with weights `exp(−age/τ)` (τ 20–120 ms; k = ceil(4τ/frame)), so each frame is a pure function of `t`.
- **Phosphor tone map**: energy → white-green core → green → dark; wide low bloom (`core/three/post.js`).
- **Glass**: grey-green base (never pure black), phosphor grain, edge-lit graticule at 6–10 %, soft reflection, rounded mask. No scanlines, shadow mask or pixel grid.

## 3. Colour logic

- **Monochrome phosphor**: one hue. Default green (P31-like, `#3dff8a` core fading to `#0b5d2e`); alternatives: blue-white with a yellow-green afterglow (long-persistence P7-like), or white. Choose one per film.
- **Intensity is the only variable**: importance = brightness = dwell time.
- **The dark is glass**, a grey-green `#0a120d`-ish with faint graticule light, never `#000`.
- The bezel, if shown, is neutral dark grey with printed legend in off-white; it never glows.
- A second trace (dual-beam) stays the same phosphor.

## 4. Type & subtitles

- **Words are drawn by the beam** with a single-stroke vector font (a hand-built stroke set, or a public-domain Hershey-style simplex), 60–160 px cap height, written at a slower beam speed so they read brighter.
- **Bezel legend** (when the instrument is shown): Share Tech Mono or IBM Plex Mono, 14–20 px, off-white silk-screen look, invented labels (no real manufacturer marks).
- **Subtitles**: on a strip below the screen or low inside the glass, IBM Plex Mono 500 at 32–40 px in a pale phosphor tone with a soft glow, rendered as clean text (not beam-drawn) for legibility. Hold each ≥ max(1.8 s, speech + 0.6 s).
- **Devanagari**: Noto Sans Devanagari 500 in the same strip; for beam-drawn Devanagari titles, trace glyph outlines from Noto Sans Devanagari as paths, large and slow.

## 5. Motion quality

- The beam is continuous; frames at 24 or 30 fps sample the persistence. Path frequency should be an integer multiple of the frame rate to avoid strobing.
- **Morphs**: resample both paths to equal arc length, align starting points, interpolate with `eio`; a circle is the universal in-between.
- **Lissajous drift**: frequencies a hair off an integer ratio make the figure rotate slowly; locking the ratio stills it.
- Appear: drawn on (path revealed from 0 to s), or frequency and phase "tune in" from chaos to a still figure. Disappear: amplitude collapses to a bright dot that fades.
- 3D wireframes rotate smoothly inside the trace.
- **Never**: raster wipes, global opacity fades (dim by beam intensity), several independent beams at once.

## 6. Camera grammar

Two worlds: the glass (most of the film) and, rarely, the instrument in a dark room. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Locked screen, trace performs | Concentration, measurement | an explanation; a song; a portrait in one line |
| Gain zoom (the trace scales, the glass stays) | Looking closer by turning a knob | a detail; scale; magnification |
| Slow push into the glass past the graticule | Leaving the instrument for the signal | immersion; abstraction; a dream |
| Pull back to bezel, knobs and a dark lab | It is a machine | a making-of; a lesson; a reveal of the source |
| Rotation inside the trace (3D wireframe) | Volume from one line | a building; a molecule; a planet |
| Switch to sweep mode (Y over time) | From shape to time | a heartbeat; a voice; a seismograph |
| Trigger slip and relock | Losing and finding sync | confusion; a reunion; an argument resolved |

Framing: the trace fills 50–80 % of the graticule, centred, dark glass around it. Transitions: morph through a circle, collapse to a dot and redraw, drift into noise and lock, XY-to-sweep switch; no unrelated cuts, no dissolves.

## 7. Sound palette

- **The drawing signal is an instrument**: a circle is a pure sine pair, a square buzzes, a star rasps; choosing the path frequency picks the pitch, so shapes can play notes and a chord can be a knotted figure.
- **Around it**: sub-bass sines, soft noise beds, slow pads (numpy), sparse plucks (`pluck.py` kalimba, music_box), occasional bowed vibraphone.
- **Foley of the instrument**: relay clicks, knob detents, a power-on thump with high-voltage crackle, a quiet fan hum.
- **Making it listenable**: high-pass the audible copy at 20–30 Hz (off-centre shapes create DC), tame its top, limit it. The picture always comes from the clean stream, so mixing never distorts the image.
- **Silence**: the dot at rest, the fan.
- **Voice**: dry, precise lab narrator, close. Music and signal ducked ~6 dB under voice; −14 LUFS.

## 8. Native moves

- **The sound draws.** Each note reshapes the trace; a chord is a Lissajous knot. *Fits content like:* explaining harmony; a heartbeat; a voice message made visible.
- **Lissajous lock.** Two drifting frequencies settle into a still figure. *Fits content like:* two people falling into step; a negotiation; calibrating a machine.
- **One-line wireframe.** A 3D object rotating, drawn as one continuous path with its retrace lines. *Fits content like:* an architectural model; a molecule; a satellite.
- **Collapse to a dot.** The image shrinks to a bright point that fades. *Fits content like:* an ending; a star dying; a machine switching off.
- **Sweep mode.** The display turns into a scrolling waveform. *Fits content like:* vital signs; an earthquake record; a voice.
- **Beam handwriting.** The beam writes a word in a single stroke. *Fits content like:* a signature; a name; a date.
- **Phosphor memory.** Long persistence turns motion into history. *Fits content like:* orbits; a walked route; a pendulum's decay.

## 9. Pitfalls of the medium

- **Uniform line brightness** looks like a drawing app → brightness from dwell time, bright corners and endpoints.
- **Too much path** → every part gets faint (the beam has a fixed time budget): simplify, fewer bolder shapes.
- **Messy retrace lines** → order sub-paths by nearest neighbour; keep a few as texture.
- **Raster artefacts** (scanlines, pixel grids, characters) → none; it is a vector display.
- **Feedback persistence breaks parallel rendering** → compute from the last k frames.
- **Harsh or dangerous audio** (DC, piercing highs) → filter and limit the audible copy; check at low volume first.
- **Illegible beam text** → fewer strokes, larger, slower; clean subtitles separately.
- **Strobing** when path frequency and frame rate beat → integer multiples or temporal supersampling.

## 10. Engine

No demo engine yet (draft). A first demo should build:

- `paths.js`: shape library (Lissajous, polygons, spirals, stroke font), `morph(a, b, u)` by arc length, `wire3d(model, cam)` projection, `route(subpaths)` ordering.
- `beam.js`: path → 48 kHz sample stream; Gaussian segment splats weighted by dwell, in a WebGL2 additive float target.
- `phosphor.js`: weighted last-k persistence, tone map, bloom, glass, graticule, power on/off.
- `xy.py`: writes the same stream as stereo audio, builds the filtered audible copy, mixes with voice.

Start from `styles/ascii-crt/demo/crt.js` (monochrome glass, curvature, power on/off; drop characters and raster), `styles/hologram-hud/demo/engine/holo.js` (wireframe projection), `styles/microgame/demo/glpass.js` (pass helper), `core/three/post.js` (bloom), `core/lib.js`. Foley via `core/audio/sfx.py`; plucks via `core/audio/pluck.py`.

## 11. Variation space

The agent decides the shapes, the phosphor colour, whether the soundtrack drives the picture, how often the instrument is seen, the pacing and the morph chain.

- Structures: **one continuous line** that morphs through a whole story; **a lesson at the bench** (cut between the lab and the glass as each knob changes the picture); **a duet** (two signals, one per channel, finding a shared figure).
- Openings: **a dot at rest** that starts to circle; **power-on** (a bright flash line opening into the glass); **noise tuning in** to the first clear figure.
- Endings: **collapse to a dot** that fades with the fan; **the last figure locks** and holds; **the camera pulls back** to the dark lab, the trace still glowing.

---

Status: **draft** — no demo film yet. Before this is used as a library style it needs a demo film, `DEMO.md`, stills and the checks in the Lemo-Opuscar `MAINTAINING.md` ("Gates").
