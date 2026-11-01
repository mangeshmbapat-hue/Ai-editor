# Expressionist Set — Style Prompt

> A 1920s nightmare built in a studio: crooked painted flats with light and shadow brushed onto the walls, streets that lean and narrow to a point, pale-faced performers gliding along the set's diagonals, all on a tinted silent-film print.
> References (grammar only): Robert Wiene's *The Cabinet of Dr. Caligari* (1920; sets painted by Hermann Warm, Walter Reimann and Walter Röhrig) for painted light, slanted flats and jagged windows; Paul Wegener's *The Golem* (1920; architecture by Hans Poelzig) for organic, leaning houses; Arthur Robison's *Warning Shadows* (1923) for shadows that act on their own; Die Brücke woodcuts (Ernst Ludwig Kirchner, Erich Heckel) for angular cutting and distorted perspective; period tinting and toning of release prints. Never reproduce a specific set, character, make-up, intertitle or phrase, and never name them in the film.

## 1. Essence, and what it is not

- **Painted light**: highlights, shadows and beams are painted on the flats as hard-edged shapes; the studio light itself is flat. A real cast shadow is rare and meaningful.
- **Crooked architecture**: no right angles; walls lean, windows are jagged trapezoids, streets narrow to impossible vanishing points, stairs twist.
- **A shallow stage**: layered flats and a painted backdrop; performers move along the set's diagonals and edges.
- **Stylised performers**: white faces with dark-ringed eyes, dark costumes, angular poses held like sculpture.
- **A tinted silent print**: monochrome image tinted per scene (amber, blue, green, rose), jagged intertitles, iris shots.

Not Silent Film (an engraved-illustration film shown in a picture house with curtains and a pianist; here the camera is inside the painted set), not Woodcut (a printed block, not a stage), not Shadow Puppetry (no backlit screen), not film noir (no real hard key light or wet streets: light here is paint).

## 2. Materials & rendering

- **Flats**: Canvas 2D sprites or three.js planes with unlit `MeshBasicMaterial` (light is painted, so nothing is lit by the renderer); 3–6 layers in shallow depth with slight parallax; a floor painted with radiating stripes that exaggerate perspective.
- **Paint model**: flats painted at load with bold brush ribbons in 4–6 grey values, hard-edged light patches (zigzags, wedges, spirals), streaks radiating from doors and windows, drybrush texture and canvas weave. Cached; nothing repaints unless the story bends the set.
- **Built-in distortion**: flats are skewed quadrilaterals with several inconsistent vanishing points; a low-frequency warp field bends verticals 3–8°, fixed per set.
- **Performers**: cut-out rigs (or simple toon 3D) with chalk-white faces, a painted hard shadow band across the face, dark-ringed eyes, spread fingers; edges slightly soft, as if photographed.
- **Shadow layer**: a performer's shadow is a separate silhouette sprite projected along a painted light direction; it can stretch, lag, lead or act alone.
- **Print**: monochrome conversion → tint (multiply highlights by the tint) and optional toning (shift the shadows) → grain, flicker, gate weave, sparse scratches → 4:3 gate with rounded corners → iris masks (circle, oval, slit).
- **Cadence**: performers sampled on irregular, seeded holds (1–2 frames) and slightly fast, like a hand-cranked camera; the set never judders.

## 3. Colour logic

- The paint is **monochrome**, 5–7 grey steps. Colour comes only from **tinting the print**, one tint per scene: amber for lamplight interiors, blue for night, green for the uncanny, rose for passion or fire; sepia toning optional.
- Painted white is the brightest value; nothing glows or blooms.
- Faces are the second brightest; costumes the darkest; painted darks form arrows toward the subject.
- Never: full colour, coloured light sources, smooth lighting gradients (only the tint wash is smooth).
- Examples: amber `#e8b860` over ink `#1d140c`; night blue `#4f7fb8` over `#0c1220`; uncanny green `#7fa36a` over `#121a10`.

## 4. Type & subtitles

- **Intertitles**: a black card with a jagged painted border; hand-lettered angular capitals built from Anton or IM Fell English glyph outlines (opentype.js) with per-glyph shear (±8°), knife-cut edge notches and stepped baselines; cream on black, tinted with the scene.
- Devanagari intertitles: rasterise Rozha One with canvas `fillText`, then apply the same shear and edge cuts to the bitmap, keeping the headline stroke continuous.
- **Words painted on the set** use the same jagged hand.
- **Subtitles** (when there is speech): small intertitle-style plates inside the gate, IM Fell English 36–42 px; Devanagari in Tiro Devanagari Hindi; they flicker and tint with the print. Hold ≥ max(1.8 s, speech + 0.6 s). Intertitles carry narration; subtitles carry speech.

## 5. Motion quality

- 24 fps output with an 18–20 fps feel for performers (irregular seeded holds, slight speed-up); the camera is mostly locked.
- **The somnambulist glide**: slow movement along a diagonal, then a sudden angular jerk; poses held 1–2 s like sculpture.
- Shadows may move independently of their owners.
- Appear: iris-in; stepping out of a painted shadow; a door opening onto a painted wedge of light. Disappear: iris-out; dissolving into painted dark.
- The set is fixed unless the nightmare bends it (warp breathing ≤ 2 %).
- Print effects run every frame: flicker, weave, occasional scratches.

## 6. Camera grammar

A locked studio camera before a painted stage. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Locked frontal tableau of the set | a stage that is also a trap | a room; a street; a seat of power |
| Iris in or out on a face or object | attention, old-cinema emphasis | a clue; a reveal; a scene change |
| Slow push along a narrowing street | dread, inevitability | a pursuit; a walk home; a summons |
| Low angle at a towering crooked wall | menace, authority | an official; an institution; a tower |
| High angle down a twisting stair | vertigo | a descent; a fall; panic |
| A shadow on the wall, its owner off-screen | threat displaced | an approach; a crime; a secret |
| Two figures in profile on a diagonal | confrontation | an interrogation; a bargain; a farewell |
| Slit iris | partial knowledge | eavesdropping; surveillance; a peephole |

Framing: compose along the set's diagonals with performers at their converging point; keep the 4:3 gate. Transitions: iris, fade through black, a tint change on a cut, an intertitle; no modern wipes or crossfades between tints.

## 7. Sound palette

- **Silent-cinema accompaniment**: organ, organ_soft and organ_pedal, piano, solo violin and violins_trem, cellos, contrabass, harmonium (accordion), timpani rolls, gong, glass for a glass-harmonica shimmer; dissonant clusters and chromatic slides; a sine-wave theremin-like voice with portamento and vibrato for the uncanny.
- A small pit ensemble (piano, violin, organ) is the default; a slow low drone may replace it for a modern take.
- Foley, sparse: footsteps on a wooden stage, creaking flats, hinges, wind, a clock; screams stay in the image.
- Optional narrator as a fairground barker, through a period chain (band-pass ~300 Hz–3.5 kHz, crackle).
- Bed: projector hum and gate clatter. Silence: the music stops, only the projector remains.
- Mix: voice ducks music ~8 dB; −14 LUFS.

## 8. Native moves

- **Painted light moves.** A painted wedge of light slides like a puppet to find someone. *Fits content like:* an interrogation lamp; a lighthouse sweep; a spotlight on a liar.
- **The shadow acts alone.** A shadow reaches, lags or leaves its owner. *Fits content like:* a guilty conscience; a rumour; a stalker of habits.
- **The narrowing street.** Walls lean in as a figure walks deeper. *Fits content like:* debt; a deadline; a bureaucratic maze.
- **Iris on the clue.** The frame closes to one object. *Fits content like:* a key; a signature; a missing button.
- **Tint as feeling.** The same set shifts from amber to green on a cut. *Fits content like:* trust turning to fear; a dream; a fever.
- **The breathing set.** The warp field swells and the architecture leans further. *Fits content like:* panic; a hangover; a building that remembers.

## 9. Pitfalls of the medium

- **Real lighting creeping in** (Lambert shading, cast shadows from renderer lights) → unlit materials; paint every light.
- **Wrong rather than designed perspective** → distort along chosen diagonals; keep the floor readable.
- **Murky frames** → painted whites, faces bright, a tint that is not too saturated.
- **Copying the classic films** (their characters, make-up, sets or phrases) → invent everything; borrow only the grammar.
- **Horror cliché** → one uncanny element per scene; restraint is scarier.
- **Print damage drowning the picture** → low damage strength; faces always readable.
- **Modern smooth motion** → irregular cadence, held poses, sudden angular moves.

## 10. Engine

No demo engine yet (draft). A first demo should build:
- `flats.js`: `flat(quad, paintFn, seed)` skewed flats, painted light patches, brush ribbons, floor stripes.
- `warp.js`: low-frequency warp field for the set layer.
- `actor.js`: cut-out rig, face shadow band, `cadence(t, seed)` irregular holds.
- `shadow.js`: independent shadow silhouettes along a painted light direction.
- `print.js`: tint and tone per scene, iris masks; `cards.js`: jagged intertitles.
- Start from `styles/silent-film/demo/engine/film.js` (`FilmPost`: grain, flicker, weave, scratches, sepia; `damage`), `styles/silent-film/demo/engine/cards.js` (intertitles, iris, 4:3 gate), `styles/rubber-hose/demo/film.js` (rounded gate), `styles/watercolor/demo/engine.js` (stroke ribbons for brushwork), `styles/papercut-red/demo/rig.js` (jointed cut-out rig), `core/lib.js`; music via `core/audio/sampler.py`, voice via `core/tts/tts.py`.

## 11. Variation space

The agent decides the set (a town, an office, a house, a fair), the tints per scene, how much the set bends, the shadow's role, and whether anyone speaks.

- Structures: **a walk through one crooked town** (each street a deeper level of the nightmare); **a frame story** (a narrator at a fair introduces a tale that later turns on him); **a single room, five tints** (the same set seen through five states of mind).
- Openings: **an iris opening** on one painted eye in a wall; **an intertitle** whose letters cut themselves out of black; **a shadow arriving** before its owner.
- Endings: **iris closing** on one small object; **the set straightening** into right angles and ordinary light; **the shadow staying** after its owner has left.

---

Status: **draft** — no demo film yet. Before this is used as a library style it needs a demo film, `DEMO.md`, stills and the checks in the Lemo-Opuscar `MAINTAINING.md` ("Gates").
