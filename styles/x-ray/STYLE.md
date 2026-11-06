# X-ray — Style Prompt

> Projection radiography: rays from a point source pass through things and darken a film, so bone and metal glow white, air goes black, and every grey is how much matter a ray crossed. The films hang on a cool lightbox, or the view runs live as noisy fluoroscopy or a scanner's line.
> References (grammar only): film radiography on a viewbox (negative convention, lead markers, collimation); industrial radiography (a machine's insides as stacked silhouettes); museum X-rays of paintings (a hidden layer); baggage line-scanners (an image built row by row). Use no real patient images or scans of anyone, no device interface, logo or font, and never name them in the film.

## 1. Essence, and what it is not

- **Density, not outline**: overlaps add, so parts stack into lighter shapes; hollow forms (tubes, shells, cortical bone) are brightest where the ray grazes their walls.
- **The negative convention**: matter white, air black; outside the collimated field the film is clear, blue-white on the lightbox.
- **A point source's physics**: magnification and penumbra, the heel gradient, scatter veil, quantum mottle.
- **Clinical calm**: cool, quiet, backlit; the subject is examined, never sensationalised.
- **Everything is synthetic**: procedural skeletons and mechanisms, never a real person's or patient's image.

Not Archive Light Table (no real archive objects; a simulated radiograph of what is inside), not Exploded Teardown (nothing comes apart; the inside is seen through the outside), not Shadow Puppetry (colour through hide; here colourless attenuation through volume), not a Halloween skeleton.

## 2. Materials & rendering

- **Beer–Lambert per pixel**: `I = I0(x,y)·exp(−Σ μ_m(kV)·L_m)`, `L_m` = path length through material m. Build `L_m` in three.js: closed meshes into a float target, additive blending, depth test and culling off, front faces add −depth, back faces +depth; one RGBA32F channel per group (soft tissue, cortex, marrow, metal).
- **kV is a dial**: low kV shows soft tissue; high kV burns it out, leaving bone and metal. Mid-kV μ ratios, for example: soft tissue 1, bone 2.5–3, steel 15+, lead opaque.
- **Point source**: perspective camera at the focal spot; objects nearer the tube magnify; penumbra ∝ focal spot × object-to-film / source-to-object distance, per group.
- **Film response**: exposure → density via an H&D curve (toe, gamma 2.5–3.5, shoulder), base + fog ≈ 0.2 D, brightness = lightbox × 10^(−D). Scatter veil: 10–25 % of a wide blur added back. Mottle ∝ √exposure, seeded per film or pulse. Heel: ±10–15 % along the tube axis.
- **Collimation** with sharp blades; lead letters (`L`, `R`, `01`) pure white. **Hollow forms**: bones as lathe/tube shells (dense cortex, lighter medulla, noise trabeculae); machines from cylinders, extruded gears, helical springs.
- **Display modes**, one per shot: *viewbox* (fluorescent panel with two tube streaks, diffuser, clips, film curl, faint scuffs); *fluoroscopy* (circular intensifier field, pincushion, 7.5 or 15 pulses/s, recursive lag `0.6·prev + 0.4·new` leaving ghost trails, baked from a fixed window of earlier pulses so frames render alone); *line-scan* (rows build as the object rides a belt).

## 3. Colour logic

- Monochrome on a cool blue-grey base; the lightbox a cool white. Value order: metal > markers > cortical edge > bone > soft tissue > air.
- **One accent**: grease-pencil marks (wax yellow or red) circling and numbering on the film surface; they never take mottle or blur.
- **Scanner variant**: dual-energy colour by material (organic orange, mixed green, metal blue), the only time hue encodes matter; never mixed with film mode in one shot. Never tint bones or glow green.
- Example film: air `#05070a`, tissue `#4a5560`, bone `#c9d3d9`, metal `#f4f8fa`, panel `#e6eef2`, wax `#e8c22a`. Example scanner: `#e88a2a` organic, `#5fbf4a` mixed, `#3c6fd6` metal on `#f2f2ee`.

## 4. Type & subtitles

- On the film: lead markers in Oswald 600 or Bebas Neue as opaque shapes, 40–90 px; an ID block with fictional data only (`SPECIMEN 07 · 60 kV`) in IBM Plex Mono or VT323, 18–26 px; never a real name, patient number or hospital.
- Grease-pencil notes: Caveat or Permanent Marker, 36–60 px, in the accent, written on.
- **Subtitles** on the lightbox's frosted strip below the films: Inter or IBM Plex Sans 500, 34–40 px, dark slate (white with outline on dark views). Devanagari: Noto Sans Devanagari or Hind 500. Hold ≥ max(1.8 s, speech + 0.6 s).
- Titles: lead letters exposed on a cassette, coming up white as the film develops.

## 5. Motion quality

- 24 fps. Films do not move; the camera, hands and light do.
- A new radiograph **develops**: after an exposure flash, density rises over 0.8–2 s (ease-out), thin parts last.
- Fluoroscopy steps at its pulse rate with lag trails; mottle reseeds per pulse. Line-scan builds at constant belt speed, never eased.
- Subjects move mechanically (hinges, escapements, rigid bones on joints); never morph a bone. kV eases over ~1 s; viewbox tubes flicker 2–3 times on switch-on.
- Never moves: the collimated field, markers, the viewbox frame.

## 6. Camera grammar

An examiner's camera: close, steady, travelling over the inside of something. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Wide on a viewbox wall of films | comparison; a case file | growth over time; before and after a repair; a series |
| Slow pan along a long film | following a structure | a spine; a fish; a pipeline weld |
| Push in to a grease-pencil circle | the one thing that matters | a crack; a coin inside a toy; a hidden screw |
| Locked fluoroscopy of a mechanism | how it works inside | a synthetic knee bending; a watch escapement; a valve |
| Line-scan pass on a belt | inventory; surprise | a suitcase; a gift box; a parade of tools |
| kV sweep on a locked frame | layers peeled by energy | a painting's underdrawing; fruit to seed; wall to wiring |
| Sweep bar over an ordinary render | what lies under the surface | a product; an animal; a building |

Framing: the subject fills 60–85 % of the collimated field; markers in a corner; the frosted strip stays clear for subtitles. Transitions: a film slid out and another in, the viewbox off/on, a flash then development, a sweep bar; no dissolves between films (they add density wrongly).

## 7. Sound palette

- **The room**: the anode spin-up (a swept sine rising over 1.5–3 s), the exposure beep, a contactor clunk; fluorescent hum with start-up ticks; sheet-film wobble (band-passed `sfx.brown`), clip snaps; belt rumble for a scanner.
- **Music**: clinical and clear: vibraphone_bowed, glass, harp harmonics, sparse high piano, a numpy drone or organ_soft; `sfx.heartbeat` once at most, never looped.
- **Foley**: mechanisms tick and click (woodblock, claves, `sfx.click`); bones never crack.
- **Silence**: only the hum while a film is studied.
- **Voice**: a quiet examiner or curator, plain and exact, numbers spelled out; never a diagnosis. Music ducked ~6 dB; −14 LUFS.

## 8. Native moves

A menu: use the ones your story needs.

- **See-through sweep.** A bar crosses an ordinary render and leaves the radiograph behind it. *Fits content like:* the inside of a toy robot; a wrapped gift; the frame of a guitar.
- **Exposure develops.** Flash, then densities rise from blank film. *Fits content like:* a fossil inside a rock; a letter inside an envelope; a seed inside a fruit.
- **kV peel.** Raising the energy strips soft layers until the dense core remains. *Fits content like:* the sketch under a painting; steel in a concrete beam; a bird's bones under feathers.
- **Live fluoroscopy.** A grey, noisy, lagging view of something moving inside. *Fits content like:* a hinge; a synthetic snake swallowing an egg; a clock escapement.
- **Line-scan reveal.** Objects ride through a slit; the picture builds row by row. *Fits content like:* a life in one bag; a loaf with a ring baked in; a factory line with one faulty part.
- **Grease-pencil case.** Wax marks number findings across a wall of films. *Fits content like:* a quality check; a mystery's clues; a conservator's notes.

## 9. Pitfalls of the medium

- **Alpha-blended ghosts** instead of attenuation → Beer–Lambert on accumulated thickness.
- **Solid bones** look plastic → shells with cortex and medulla.
- **Convention flipping** mid-film → pick negative or positive and hold it. **Too clean** → mottle, scatter, heel, penumbra, at levels that keep the subject readable.
- **Real medical imagery or claims** → never use real patient scans or anyone's X-ray; subjects are synthetic, labelled illustrative; no diagnoses or pathology as fact; check bone counts and joint order against an anatomy reference.
- **Horror cliché** (dancing skeletons, green glow) → clinical cool.
- **Mirrored markers** → decide the viewing side and keep every marker and ID block consistent with it.

## 10. Engine

No demo engine yet (draft). A first demo should build:

- `thick.js`: thickness accumulation per material group into RGBA32F (ShaderMaterial writing ±view depth, `AdditiveBlending`, `DoubleSide`).
- `atten.js`: `mu(kV)` table, Beer–Lambert, heel, penumbra by group depth, scatter veil, `mottle(seed, pulse)`.
- `film.js`: H&D LUT (`toe, gamma, shoulder, baseFog`), base tint, collimator, markers, ID block.
- `viewbox.js`: panel, tube flicker, clips, film curl, grease-pencil layer.
- `fluoro.js`, `linescan.js`: pulse stepping, baked lag; row build, dual-energy colour.
- `bones.js`: `boneShell(profile, cortex, medulla)`, gears, springs.

Start from `styles/shadow-puppet/demo/gl.js` (transmittance tonemapped under light: the 2D cousin of attenuation), `styles/archive-lighttable/demo/film.js` (backlit objects on a light table, marks on a 2D canvas above), `styles/teardown/demo/src/parts.js` (lofted mechanical parts), `core/three/post.js` (composer only), `core/lib.js`, `core/audio/sfx.py`, `core/audio/sampler.py`.

## 11. Variation space

You decide the subjects, display modes, kV logic, whether a grease pencil narrates, and whether the ordinary view appears.

- Structures: **an inventory** (one belt; a life told by the objects that pass); **inside one machine** (a single object studied in three projections and live, part by part); **a growth series** (the same synthetic subject at intervals, films added to the wall).
- Openings: **a dark room**, the viewbox flickering on under a blank film; **an ordinary object** crossed by the sweep bar; **the anode whine over black**, a flash, a film developing.
- Endings: **the viewbox switched off**, films turning to dark sheets; **the kV raised** until one metal piece remains; **the last film filed** under a wax number.

---

Status: **draft** — no demo film yet. Before this is used as a library style it needs a demo film, `DEMO.md`, stills and the checks in the Lemo-Opuscar `MAINTAINING.md` ("Gates").
