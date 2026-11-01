# Synthwave — Style Prompt

> A neon night drive into a retro-future: a glowing grid floor races toward a low horizon and a huge striped sun, wireframe mountains glow against a violet sky, and chrome-and-neon lettering pulses with an analog synth beat.
> References (grammar only): 1980s neon sign craft and airbrushed album and poster art (gradient skies, chrome type with a horizon line, star glints); early computer-graphics grid landscapes of the late 1970s and 80s; the 2010s retro-synth revival in music and cover art (the grid, the sliced sun, the night drive). Never copy a film title logo, a car silhouette or brand, an album cover or a melody, and never name them in the film.

## 1. Essence, and what it is not

- **The grid**: a perspective neon lattice plane scrolling toward the horizon at a constant speed locked to the music.
- **The sliced sun**: a huge disc on the horizon, gradient yellow → orange → magenta, cut by horizontal gaps that widen toward its base.
- **Night sky**: deep indigo → violet → magenta at the horizon, a star field, wireframe mountains with glowing edges and dark fills.
- **Chrome and neon type**: a metal-gradient bevelled title with a hard horizon line, plus a glowing handwritten neon script.
- **Everything glows and pumps**: lines are emissive, bloom breathes with the kick drum, the frame drives forward.

Not Vaporwave (pastel daylight, slowed irony, busts and windows), not 80s Cel Anime (hand-painted characters and cels), not Sci-fi Hologram HUD (scanned data objects and panels), not a vector arcade display (no filled sun or gradients there; beams only), not Low-poly Isometric Island (perspective night, not an orthographic model).

## 2. Materials & rendering

- **Grid** (three.js plane shader): anti-aliased lines from `fwidth`, constant screen width ~2 px with a white core and a coloured glow, line opacity fading with distance into a horizon haze band; UV scroll = `t × speed`, speed derived from the tempo (one row per beat or half beat).
- **Sun**: a camera-facing disc shader: vertical gradient, stripe mask whose gap height grows linearly toward the bottom and scrolls down slowly; an outer glow sprite.
- **Sky**: gradient + seeded star points (twinkle by `vnoise`), a faint magenta haze strip at the horizon line.
- **Mountains and objects**: low-poly meshes with dark fills (`#120424`-ish) and emissive edges (barycentric-coordinate edge shader or `EdgesGeometry` lines), so they read as glowing wireframes that occlude the sun correctly.
- **Chrome lettering** (Canvas 2D, cached per title): fill with a vertical gradient (pale sky blue top → white horizon line at ~52 % → deep brown-orange below), 2 px white inner bevel, dark violet outline, hard drop extrusion of 6–12 px; a 4-point star glint and a sweep of light pass across.
- **Neon script**: glyph outlines stroked twice: wide blurred coloured pass + thin white core; slight tube flicker.
- **Post**: bloom from `core/three/post.js` on the emissive layer only; optional light CRT pass (`core/post/crt.js`, scanlines ≤ 0.15). Everything a function of `t`.

## 3. Colour logic

- **Night base** in indigo and violet; nothing is lighter than the neon cores.
- **Two neon primaries**: magenta and cyan, for lines and type; **the sun is the one warm mass**.
- **White only in neon cores and chrome glints.**
- **Accent**: one tertiary (electric yellow or orange) reserved for the most important line or word.
- Never daylight, never green-dominant, never earth tones; shadows are deep violet, not black.
- Example: sky `#0d0221` → `#3b0a5c` → `#c2185b`, grid `#ff2bd6`, edges `#2de2e6`, sun `#ffd319` → `#ff901f` → `#ff2975`.

## 4. Type & subtitles

- **Titles**: chrome style on Audiowide, Orbitron or Righteous, 120–220 px, slightly italicised by a shear transform.
- **Neon script**: Pacifico or Kaushan Script, 80–140 px, magenta or cyan tube with a white core.
- **Multi-line neon display**: Monoton for single words, 90–160 px.
- **Subtitles**: Rajdhani 600 or Teko 500, 36–46 px, white with a soft magenta glow and a thin dark outline, low in frame above the grid. Hold each ≥ max(1.8 s, speech + 0.6 s).
- **Devanagari**: Rajdhani and Teko both carry Devanagari, so subtitles stay in the same family; titles can use Teko 600 in chrome.
- Small labels (distance, time, a counter) in Share Tech Mono or Teko, 20–26 px, cyan.

## 5. Motion quality

- 24 fps on ones; constant-speed travel (linear) is the genre's motion; camera arrivals ease out (`eo`).
- **Pump**: bloom and emissive intensity +6–10 % on each kick, decaying in ~150 ms; the grid can flash outward from the centre on accents.
- Objects arrive from the horizon along the grid and pass under the camera; wireframes build edge by edge, then fill dark.
- The sun sinks very slowly; stripes widen as it sinks.
- **Never moves**: the horizon line and the sun's x position; titles never wobble.

## 6. Camera grammar

A low, forward-driving camera with occasional lifts. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Low forward dolly over the grid | An endless drive, momentum | a commute; a long project; a road trip |
| Tracking beside a moving object | Speed, companionship | a race; a delivery; a migration |
| Crane up from the grid to the sun | Ambition, arrival | a goal; a sunrise of an idea; a finale moment |
| Banked turn (roll 5–10°) on a curve | Excitement, a turn in fate | a decision; a detour; a chase |
| Locked symmetric frame, sun centred | Iconic stillness | a title; a statement; a product |
| Rear view, horizon receding | Leaving, looking back | nostalgia; the past year; departure |
| Fly-through of neon rings or a tunnel | Acceleration, focus | a launch; a countdown; a breakthrough |
| Top-down over the grid | The map of the journey | a route; a plan; a city layout |

Framing: horizon at or slightly below centre, the sun on the vertical axis, type above the horizon. Transitions: horizon flash to white bloom, cut on the snare, light-speed streaks, the grid folding up into a wall, CRT power-off; no soft dissolves.

## 7. Sound palette

- **Analog-style synthesis in numpy**: detuned saw pads with slow filter sweeps, arpeggiated square or saw bass on sixteenth notes, a polysynth lead, FM bells; gated-reverb snare (snare sample + big reverb cut by a gate), drum machine kick and claps from the drum_kit and claps samples.
- **Lead colours**: alto or tenor saxophone for one lyrical solo, electric guitar for one power moment, never both.
- **Foley**: engine hum (filtered saw following RPM), whooshes of passing lights with Doppler shift, neon buzz (mains hum + harmonics), laser zaps (fast downward pitch sweeps).
- **Technique**: sidechain the pads to the kick; double the arpeggio speed instead of changing tempo to accelerate.
- **Silence**: engine idle and neon buzz only.
- **Voice**: a cool night-radio DJ, close and warm; or a vocoded line (simple channel vocoder). Music ducked ~6 dB; −14 LUFS.

## 8. Native moves

- **Endless drive.** The grid scrolls; markers and objects pass at constant speed. *Fits content like:* a commute; a year of milestones; a long-distance call.
- **Sunset slices.** The striped sun sinks, gaps widening. *Fits content like:* the end of an era; a countdown; the last hour of a shift.
- **Chrome title shine.** A light sweep and a star glint cross a chrome word. *Fits content like:* a launch; a chapter name; a record score.
- **Wireframe build.** A skyline or object draws edge by edge, then fills dark. *Fits content like:* a city plan; a product; a stadium.
- **Grid pulse.** Lines flash outward from a point on the beat. *Fits content like:* a broadcast; a heartbeat; news spreading.
- **Rear-view mirror.** A framed view of the road behind, the past shrinking. *Fits content like:* nostalgia; leaving home; a career looked back on.

## 9. Pitfalls of the medium

- **Grid moiré at the horizon** → `fwidth` anti-aliasing, distance fade, render 2× and downsample.
- **Bloom washes the frame** → bloom only the emissive layer, with a threshold.
- **Borrowed icons** (famous car silhouettes, film title logos) → invent vehicles and lettering or show none.
- **Gradient banding** in the sky and sun → float targets plus dither.
- **Thin magenta and red lines smear after encoding** (4:2:0 chroma) → lines ≥ 2 px with a white core; test the encoded file.
- **Monotony of constant scroll** → change camera height, speed and framing per section; allow stops.
- **Grid speed off the beat** → derive scroll speed from the tempo.
- **Text glow halos** → render subtitles after bloom.

## 10. Engine

No demo engine yet (draft). A first demo should build:

- `grid.js`: plane shader, `scroll(t, rowsPerBeat)`, horizon haze, pulse.
- `sun.js`: sliced-disc shader (`gapGrow`, `scroll`, `sink`).
- `sky.js`: gradient, seeded stars, haze strip.
- `wire.js`: dark-fill meshes with emissive edges; build-by-edge progress.
- `chrome.js`: chrome and neon lettering to cached canvases; shine and glint.
- `synth.py`: saw, square, FM voices, gated reverb, sidechain.

Start from `core/three/post.js` (bloom, grade), `core/post/crt.js`, `styles/cel-anime-80s/demo/bg.js` (neon tube colour + emissive pair), `styles/hologram-hud/demo/engine/holo.js` (wireframe projection), `styles/lowpoly-island/demo/post.js` (sky blend), `core/lib.js`. Drums and sax from `core/audio/sampler.py` (drum_kit, claps, snare, alto_sax, electric_guitar).

## 11. Variation space

The agent decides what travels the grid, the landmarks, the sun's height, the neon pair, the title words, the pacing and the camera path.

- Structures: **a night drive in chapters** (each landmark a chapter title in chrome); **a countdown to midnight** (the sun sinks as numbers fall); **a race between two lights** (two trails on parallel lanes, cut between them).
- Openings: **a single grid line** draws to the horizon in the dark; **a chrome title** catches a glint before anything else exists; **an engine starts** on black and the grid lights up row by row.
- Endings: **the sun sets** and only the grid remains; **crane up into the stars** until the grid is a thin line; **the CRT powers off** to a dot.

---

Status: **draft** — no demo film yet. Before this is used as a library style it needs a demo film, `DEMO.md`, stills and the checks in the Lemo-Opuscar `MAINTAINING.md` ("Gates").
