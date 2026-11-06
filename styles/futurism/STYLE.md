# Futurism — Style Prompt

> Speed and noise made visible: a moving body leaves a fan of repeated contours behind it, wedges of colour shoot along its lines of force, and the street splits open around the machine.
> References (grammar only): Giacomo Balla (1912–13) for repeated limbs and iridescent interpenetrations of light; Umberto Boccioni for lines of force and bodies that pour into space; Gino Severini for dancers fragmented into colour; Étienne-Jules Marey's chronophotography and Anton Giulio Bragaglia's photodynamism for movement as superimposed phases; Luigi Russolo's noise-intoner orchestra (1913) for the sound; Futurist "words-in-freedom" pages for type. Borrow the visual and sonic grammar only, never the movement's glorification of war or its politics, and never reproduce a specific work.

## 1. Essence, and what it is not

- **Repeated contours**: a moving thing is drawn several times along its path (4–12 phases), fanned, the latest phase strongest.
- **Lines of force**: sharp wedges, curves and spirals radiating along the direction of motion, cutting the frame into dynamic sectors.
- **Interpenetration**: the moving body and its surroundings cut into each other; the street splits around the tram; light breaks into triangles.
- **Diagonals everywhere**: the frame is sectored by obliques; a calm horizontal is rare and therefore meaningful.
- **Subjects of energy**: engines, trains, bicycles, dancers, crowds, streetlights, factories.

Not Cubism (several views of a still object; here one view of a body across time), not motion blur (blur smears continuously; here phases are discrete contours), not Kino Montage (no archive photographs, no single red on newsprint, no slogans), not City Symphony (no real footage).

## 2. Materials & rendering

- **Phase stack**: render the subject at times t − iΔ (i = 0…N−1, Δ = 1/24–1/8 s, N growing with speed). Each phase is a flat-coloured silhouette with an ink contour; value and contrast fall off with i (100 % → 25 %); phases are offset slightly perpendicular to the motion so they fan. Phases are pure functions of the subject's own animation at earlier times.
- **Lines of force**: wedges (3–40° wide) emitted from leading edges along the velocity and trailing behind, bent by the path's curvature, length proportional to speed; alternating light and dark flat fills with hard edges.
- **Sectoring**: a few strong diagonals or arcs centred on the motion split the frame; inside each sector the background is sheared along the motion by velocity × k and re-tinted one step toward the sector's colour (interpenetration).
- **Light fans**: a lamp or the sun as radiating triangles of complementary colours, nested like a prism.
- **Surface, one per film**: *divisionist dashes* (short directional strokes of pure colour following the force lines) or *hard planes* (flat cut shapes with a light paper grain).
- Canvas 2D with offscreen layers (phases, force, sectors, ground) composited per frame; WebGL only for the sector shear. The camera mostly stays still: motion lives in the subject.

## 3. Colour logic

- High key, high contrast, complementary pairs: orange/blue, red/green, yellow/violet; 5–7 hues.
- **Speed is warm, recession is cool**: reds, oranges and yellows at the leading edge; blues and violets in the trailing phases.
- Neutral: a light warm grey for daylight, a deep blue-black for night under electric light.
- Pure white is reserved for light sources and the leading phase's edge.
- Never: muddy browns (that is Cubism), pastels, soft gradients.
- Example day: ground `#f2efe8`, red `#e8442e`, orange `#f2a81d`, yellow `#f5d93a`, blue `#2c5fb8`, violet `#5a3c9a`, ink `#1c1c22`.
- Example night: ground `#141824`, lamp `#fff4c2`, rays `#f2c14e` / `#3f7fe0` / `#c8452f`.

## 4. Type & subtitles

- **Words-in-freedom**: onomatopoeia and short words in mixed sizes, weights and angles, set along lines of force and overlapping the image; Anton, Bebas Neue, Oswald, Rubik Mono One; Special Elite for small typed asides. Devanagari: Baloo 2 ExtraBold. At most three words at a time; each word is synced to its sound.
- Letters may stretch along the motion (scale-x up to 2) but never skew past legibility.
- **Subtitles are calm**: static, bottom centre, Oswald Medium 38–44 px, white with a dark keyline; Devanagari in Mukta SemiBold. Hold ≥ max(1.8 s, speech + 0.6 s). Subtitles never join the words-in-freedom.

## 5. Motion quality

- 24 fps on ones; the phase fan updates every frame.
- Easing: acceleration (`ei`) and constant velocity dominate; stops are abrupt. A slow `eio` is kept for one deliberate calm.
- **Phase count follows speed**: at rest one contour; accelerating, the fan opens; braking, it closes onto the front phase.
- Mechanical rhythms (pistons, pedals, wheels) repeat exactly and drive the phase spacing.
- Appear: entering at speed with phases already trailing. Disappear: shooting out of frame, the phases lingering ≤ 0.5 s and decaying.
- Never moves during a shot: the main sector diagonals (they are the composition) and the ground.

## 6. Camera grammar

A mostly locked camera; speed is drawn, not filmed. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Locked frame, subject crossing at speed | speed itself | a race; a commute; a delivery |
| Head-on approach, phases expanding | impact coming | a train; a deadline; a confrontation |
| Rotating fan around a pivot | rhythm, labour | a dancer; a hammer; a pedalling cyclist |
| Sector split along lines of force | worlds colliding | city and machine; noise invading calm |
| Overhead on a crossing | simultaneity | a crowd; an intersection; a market |
| Push along a light fan into its source | energy | electricity; a factory start; floodlights |
| Sudden full stop to one contour | shock, silence | an accident; an arrival; a pause |

Framing: dominant diagonals at 30–60°, the subject off-centre with lead room for its fan. Transitions: a phase wipe (the subject crosses and the next scene is revealed behind its phases), a sector split, a flash cut on a noise burst; no crossfades.

## 7. Sound palette

- **Noise intoners**, synthesised in numpy: a buzzing string or noise source through a tuned resonator with a pitch lever (glides as melody). Families: howlers (rising and falling whine), roarers (low rumble), cracklers, buzzers, gurglers, hissers, rustlers, exploders.
- Around them: piano clusters, timpani, snare, bass_drum, toms, trumpet_stac, trombone glissandi, tuba; mechanical loops (pistons = cowbell, woodblock, hihat).
- **Foley is rhythm**: engines, wheels over rail joints (one clack per joint, tied to speed), bicycle chains, presses, steam, crowds, traffic.
- Silence: a sudden total stop, all beds cut.
- Voice: declamatory and staccato, or none. Music ducked 6–8 dB under voice; one intoner family at a time; −14 LUFS.

## 8. Native moves

- **Phase fan.** A body leaves its past contours behind it. *Fits content like:* a sprinter's start; a barista's hands at rush hour; a robot arm on a line.
- **Lines of force.** Wedges shoot from the leading edge and carve the frame. *Fits content like:* a product launch; a goal; a delivery drone.
- **The world splits.** Background sectors shear around a passing machine. *Fits content like:* a metro through a city; a wave of news; a bike through traffic.
- **Light into triangles.** A lamp breaks into nested prisms of complementary colour. *Fits content like:* a street at night; a power grid switching on; a stage.
- **Noise made visible.** Each sound gets its word, its wedge and its colour. *Fits content like:* a factory tour; a construction site; a festival.
- **The fan closes.** Phases collapse onto one contour when something stops. *Fits content like:* a finish line; a moment of doubt; a train arriving.

## 9. Pitfalls of the medium

- **Video-echo look** (semi-transparent copies of a render) → flat phases with contours, fanned offset, stepped falloff.
- **Clutter** → one moving subject per shot, ≤ 12 phases, a simple ground.
- **Arbitrary lines of force** → derive them from velocity and path curvature.
- **Ideological baggage** → no glorification of war, violence or the movement's political slogans; celebrate motion, labour and machines.
- **Strobing** of fast subjects at 24 fps → let phases fill the gaps; don't move the camera at the same time.
- **Noise fatigue** → one intoner family per moment, quiet beds, silence as contrast.
- **Type clutter** → three words maximum, each tied to a sound.

## 10. Engine

No demo engine yet (draft). A first demo should build:
- `phases.js`: `drawPhases(subject, t, {n, dt, fan, falloff})` — samples the subject's own pose function at earlier times.
- `force.js`: `forceLines(path, t, {count, spread, curl, seed})` from velocity and curvature.
- `sector.js`: frame partition plus a WebGL shear-and-tint pass per sector.
- `rays.js`: prismatic light fans; `words.js`: words-in-freedom laid along curves.
- `intoners.py`: `intoner(kind, pitch_curve, dur, seed)` resonator synthesis, mixed with `core/audio/sfx.py` and `core/audio/sampler.py`.
- Start from `styles/scifi-toon/demo/toon.js` (affine stack, constant-width ink, flat fills), `styles/spy-titles/demo/glyph.js` (letters as paths), `styles/swiss-motion/demo/ease.js` and `core/lib.js` (easing, `seg`, `mulberry`); foley cues from `core/render/events.mjs`.

## 11. Variation space

The agent decides the moving subject, the surface mode (divisionist dashes or hard planes), day or night, how much the world splits, and the noise families.

- Structures: **a single journey** (one subject accelerating through several sectors of a city); **a machine and a body** (alternating a mechanical rhythm with a human one until they share one fan); **a symphony of a workplace** (each section adds a moving subject and its intoner).
- Openings: **a single still contour** that starts to multiply; **a noise first**, then its wedge; **a lamp switched on** that breaks into triangles.
- Endings: **the fan closes** onto one still contour; **the subject exits** and its phases fade from an empty sector; **every sector re-joins** into one calm horizontal.

---

Status: **draft** — no demo film yet. Before this is used as a library style it needs a demo film, `DEMO.md`, stills and the checks in the Lemo-Opuscar `MAINTAINING.md` ("Gates").
