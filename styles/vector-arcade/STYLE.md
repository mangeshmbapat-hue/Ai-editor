# Vector Arcade — Style Prompt

> Glowing lines on pure black from an early-1980s vector arcade monitor: ships, rocks, tanks and tunnels drawn as bright wireframe outlines by a beam that jumps between objects, with segmented score digits, dot-spray explosions and cellophane-tinted bands of colour.
> References (grammar only): 1979–1983 XY-monitor arcade cabinets (beam-drawn wireframes, intensity levels, bright vertices, colour overlays laid over monochrome tubes, later three-gun colour vector displays); public-domain stroke fonts of the 1960s; early wireframe flight and tank simulators. Never copy a real game's title, ship, enemy shapes, screens, sounds or cabinet art, and never name them in the film.

## 1. Essence, and what it is not

- **Lines only**: every object is a polyline of light on black; no fills, no raster, no gradients. Vertices glow brighter where the beam settles.
- **A blanked beam**: the beam switches off between objects, so shapes float separately (unlike a scope trace).
- **Arcade grammar**: a playfield, segmented score digits at the top, life icons, screen wrap-around, thrust flames that flicker, explosions as sprays of dots and drifting segments.
- **Simple 3D**: perspective wireframes (terrain lines, tunnels seen down their axis, boxy vehicles) with brightness falling with distance.
- **Colour, if any, is limited**: a white-blue beam under fixed cellophane bands, or a few saturated primaries from a colour vector tube.

Not an oscilloscope (one continuous unblanked trace driven by audio in a lab; here a game display with separate objects), not 16-bit Pixel RPG or Microgame Frenzy (raster pixels), not Sci-fi Hologram HUD (data panels and cyan holograms), not Synthwave (filled sun, gradients, chrome), not ASCII / CRT Terminal (characters on a grid).

## 2. Materials & rendering

- **Display list** per frame, like the hardware: `move` (beam blanked), `line(x, y, intensity)`, `dot`; coordinates on a 1024 × 1024 DAC grid, 8–16 intensity steps, a vector budget per frame (overloads dim and flicker).
- **Beam splat** (WebGL2, additive float target): each vector as an analytic Gaussian line (core σ ≈ 1–1.4 px at 1080p), brightness = intensity × (1 / beam speed); an extra dot at every vertex and endpoint (settling); dots are zero-length vectors and very bright.
- **Refresh and persistence**: the game refreshes at 40–60 Hz; each output frame integrates its refreshes plus the previous 1–2 frames at decaying weight, computed from `t`, never by feedback.
- **Deflection**: slight overshoot at sharp corners, ±0.3 px DAC noise.
- **3D**: perspective wireframes, optional hidden-line removal; distance lowers intensity.
- **Overlays**: colour bands are screen-space multiplies fixed to the glass; objects change colour as they cross them.
- **Glass**: black, faint reflection, soft bloom (`core/three/post.js`); no scanlines or shadow mask.
- **Determinism**: scripted play (not interactive): positions are closed-form or fixed-step simulations from seeded initial conditions; explosion debris is seeded per event.

## 3. Colour logic

- **Black is the screen**, never grey; light comes only from the beam.
- **Monochrome mode**: one cool white beam (`#e8f4ff` core, blue-white bloom); colour only from fixed overlay bands.
- **Colour-vector mode**: at most four saturated primaries (red, green, blue, yellow; cyan and magenta as mixes), each assigned a role (player, enemy, terrain, score). Choose one mode per film.
- **Intensity carries meaning**: player and score at full; distant terrain at a third; debris fading.
- Never fills, never gradients, never white areas larger than a dot.

## 4. Type & subtitles

- **All text is vectors**: a segmented stroke font on a 4 × 6 grid (hand-built), or a public-domain Hershey-style simplex; digits with leading zeros for scores.
- **Titles**: the stroke font scaled to 100–200 px cap height with doubled strokes for weight; or an OFL face's outlines (Orbitron or Michroma, converted to paths) stroked, never filled.
- **Labels**: score, lives, level, high-score initials in the stroke font at 24–36 px cap height, top of the playfield.
- **Subtitles**: the stroke font at 30–40 px cap height in a band at the bottom, full intensity, letter-spaced 0.3 em, inside the glass. Hold each ≥ max(1.8 s, speech + 0.6 s).
- **Devanagari**: outline paths of Rajdhani or Teko glyphs, stroked by the beam at ≥ 44 px, shirorekha as one bright continuous line; or Rajdhani 600 as clean glowing text if legibility suffers.

## 5. Motion quality

- **Arcade physics, not motion-design easing**: inertia and thrust, friction, constant-speed drift, screen wrap. No `back` or spring curves.
- Rotation may step in 16–32 fixed angles (a hardware feel) or turn smoothly; choose one per film.
- Output 30 or 60 fps when the delivery allows; at 24 fps the refresh integration gives the motion its trails.
- Appear: vectors draw on in a few frames, or a dot expands into a shape (hyperspace in). Disappear: explode into a dot spray and spinning, drifting line segments that fade over ~1 s.
- Thrust flames flicker on alternate refreshes; shots are bright dots with short trails.
- **Never moves**: overlay bands and the score area.

## 6. Camera grammar

The screen is the camera; the world moves inside it. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Locked playfield with wrap-around | A closed world with rules | a routine; a market; a cycle |
| First-person wireframe view with crosshair and radar | Searching, threat from all sides | exploration; a hunt for an answer; a city at night |
| Dive down a wireframe tube | Acceleration, focus | a deep dive; a pipeline; a countdown |
| Display-list zoom (everything scales from a point) | Approach, importance | a detail; a new level; a target |
| Deflection shake on impact | Shock | a crash; bad news; a loss |
| Attract mode (the machine plays itself) | Demonstration | a tutorial; a ranking; a recap |
| Pull back from the glass to a dark cabinet | It is a game | a making-of; a memory of playing; a frame story |

Framing: score on top, subtitles at the bottom; objects 3–10 % of screen height with space around them. Transitions: blank screen for 4–12 frames, hyperspace collapse, starfield streak, a level card; no dissolves or wipes. A cabinet, if shown, carries no brand, title or real artwork.

## 7. Sound palette

- **Discrete-circuit sound effects** in numpy: explosions as white noise through a decaying low-pass, thrust as rumbling low-passed noise, shots as fast downward pitch sweeps, enemy warbles as frequency-modulated squares, beeps as short squares.
- **A pulse instead of music during play**: a two-note bass thump that speeds up as tension rises; melody only in attract and interstitial moments as simple square-wave tunes.
- **Foley of the cabinet**: button clicks, a synthesised coin clink, hum, a high-voltage crackle at power-on.
- **Voice**: early speech-synthesis character for short callouts (TTS through a narrow band-pass, 8 kHz resample, bit-crush, monotone); the narrator otherwise warm and dry. Effects ducked ~6 dB under voice; −14 LUFS; near-mono mix.
- **Silence**: the blank screen and the hum.

## 8. Native moves

- **Explode into segments.** An object's lines break apart and drift, spinning. *Fits content like:* a plan failing; a breakup; a product taken apart.
- **Wrap-around.** An object leaves one edge and returns at the opposite one. *Fits content like:* a cycle; a commute; history repeating.
- **Overlay crossing.** An object changes colour as it passes into a tinted band. *Fits content like:* crossing a border; entering a danger zone; a status change.
- **Periscope radar.** A first-person wireframe view with a sweeping radar. *Fits content like:* searching; navigating a city plan; looking for a lost thing.
- **Tube dive.** A flight down a geometric tunnel, segments rushing past. *Fits content like:* a deep dive; data through a network; time travel.
- **Attract mode.** The machine plays a demo and shows a high-score table. *Fits content like:* a ranking; a tutorial; credits.
- **Hyperspace.** Collapse to a dot, reappear elsewhere. *Fits content like:* teleporting; a sudden move abroad; a job change.

## 9. Pitfalls of the medium

- **Thin lines with no glow** look like a drawing app → Gaussian beam, bloom, bright vertices.
- **Fills creep in** → never fill; shade only by line density and intensity.
- **Too many vectors** → keep scenes sparse; respect a vector budget.
- **Copying real games** → invent silhouettes, sounds and titles; no famous rock shapes or ship outlines.
- **Motion-design easing** → arcade physics and stepped rotation.
- **Thin lines destroyed by encoding** → line core ≥ 1.5 px at 1080p with glow; avoid thin pure-blue lines; high bitrate.
- **Photosensitive explosions** → no full-screen flashes; limit bright pulses to ≤ 3 per second.
- **Judder at 24 fps** → refresh integration or a higher frame rate.

## 10. Engine

No demo engine yet (draft). A first demo should build:

- `dlist.js`: display list (`move`, `line`, `dot`), DAC quantisation, intensity steps, vector budget.
- `beamgl.js`: WebGL2 Gaussian segment splats, vertex dots, refresh integration and short persistence, overlay bands, glass, bloom.
- `vfont.js`: segmented stroke font, digits, title outlines from OFL fonts via path conversion.
- `game.js`: scripted physics, wrap, seeded explosions into segments, attract-mode scripts.
- `wire3d.js`: perspective wireframes, depth intensity, radar sweep.
- `sfx.py`: noise explosions, sweeps, warbles, the accelerating pulse.

Start from `styles/hologram-hud/demo/engine/holo.js` (wireframe projection), `styles/ascii-crt/demo/crt.js` (monochrome glass and power on/off; without raster), `styles/microgame/demo/glpass.js` (pass helper), `core/three/post.js` (bloom), `core/lib.js` (`mulberry`, `hash`). Sound effects from numpy in the manner of `core/audio/sfx.py`.

## 11. Variation space

The agent decides the objects, the colour mode and overlays, the game's rules, what the score counts, the frame rate, the pacing and how often the cabinet is seen.

- Structures: **levels as chapters** (each level a new rule, the score counting the film's subject); **an attract-mode documentary** (the machine demonstrates, a voice explains); **one long tube dive** with stations along the way.
- Openings: **power-on** from a dot to a bright playfield; **a high-score table** whose top entry is the film's subject; **a single ship** drifting in silence before the first pulse.
- Endings: **the last object explodes** into segments that settle as the final word; **a new high score** entered letter by letter; **the screen blanks** and the cabinet hum remains.

---

Status: **draft** — no demo film yet. Before this is used as a library style it needs a demo film, `DEMO.md`, stills and the checks in the Lemo-Opuscar `MAINTAINING.md` ("Gates").
