# Kathputli Marionette — Style Prompt

> Rajasthani string-puppet theatre: carved wooden heads with huge painted eyes, bright cloth bodies trimmed with gold ribbon and mirrors, hanging and dancing on strings in a small arched booth while a dholak keeps the beat and a squeaking reed gives them voices.
> References (grammar only): the kathputli tradition of Rajasthan's Bhat puppeteer families for the carved, often legless figures, the improvised booth with its arched backdrop, the few strings held directly in the fingers and the reed voice (boli); village-fair entertainment for the repertoire of types (dancer, horse-rider, juggler, snake charmer). Never reproduce a specific family's puppets, play or song, and never name them in the film.

## 1. Essence, and what it is not

- **A small arched stage**: a printed or painted backdrop of scalloped arches and windows, a valance above where the strings vanish into darkness, a cloth floor.
- **Carved, painted heads**: large almond eyes with heavy black lines, arched brows, moustaches, red lips, turbans or veils; glossy lacquer; one expression forever.
- **Cloth bodies, often legless**: long flared skirts or robes in bright cotton edged with gold ribbon (gota) and mirror-work; stuffed cloth arms; small wooden hands.
- **Visible strings**: few, taut, catching the light, rising straight out of frame. Puppets hang, sway, hop and land.
- **Fair-ground types**: the dancer who spins, the horse-rider, the juggler, the snake charmer, a king and his court.

Not Shadow Puppetry (no screen, no backlight, no rods from below: these are 3D, front-lit and hang from above), not Paper Pop-up (carved wood and cloth on a stage, not folded card), not Brick Toy (handmade, soft, lacquered, governed by gravity), not 3D character animation (no walk cycles, no facial animation: strings and gravity do the acting).

## 2. Materials & rendering

- **three.js stage**: booth frame, backdrop texture (arches, borders, block-print pattern), folded valance, side cloths, floor cloth. Light: warm front key (lamp or bulb), soft fill, a back rim; soft shadow maps throw the puppets onto the backdrop: the shadow is a second actor.
- **Head**: a lathe or sculpted low-poly form with smooth normals; painted-face decal (eye lines, brows, lips, cheek dots) under a lacquer clearcoat; visible wood grain at the neck, small chips.
- **Body**: padded torso, 2–3-segment cloth arms on hinges, the skirt as a ring of position-based particles whose radius flares with spin (r = r0 + k·ω²), with noise wrinkles; turban or veil; pompoms and tassels as spring chains.
- **Strings**: distance constraints from control points (the puppeteer's fingers) to the head, back and hands; drawn as thin cylinders with a ≥ 1 px screen-width floor and a specular glint; they always disappear above the valance.
- **Simulation**: position-based dynamics at 240 Hz, driven by keyframed finger paths, pre-simulated into a frame cache (seeded, deterministic). Gravity, damping, hem-to-floor contact.
- **Costume detail**: gota as metallic strips with a woven pattern; mirror pieces as instanced discs with jittered normals that glint as puppets turn; ghungroo bells at the hem.
- **Post** (`core/three/post.js`): shallow DOF (backdrop slightly soft), GTAO in folds, bloom only on mirrors and the lamp, a warm grade, light vignette.

## 3. Colour logic

- **Costumes in Rajasthani textile colour**: vermilion, saffron, turmeric, magenta, emerald, indigo; 4–6 hues per scene, each puppet two (body + skirt) plus gold.
- **Faces in a limited palette**: a flat warm skin, black eye lines, red lips; high contrast for distance.
- **The backdrop is one deep ground** (maroon or indigo) with lighter arches, darker than the puppets so they pop; true black only in the void above.
- **Gold is reserved** for trim and crowns; mirrors give white glints only.
- **Light is warm**: a night show is a lamp pool; a daytime fair is flatter and dustier.
- Example (stage): backdrop `#6b1420`, arches `#d9a441`, floor `#3b2a1e`. Dancer: skirt `#e01f3d`, bodice `#f2b705`, gota `#d4af37`. Rider: turban `#f26a1b`, robe `#1f5fa8`.

## 4. Type & subtitles

- **Subtitles on a painted board** hung from the booth's lower front (cloth banner or wooden board with a printed border), Baloo 2 SemiBold or Mukta 34–42 px for Latin and Devanagari, off-white on the board colour; the banner sways slightly with the stage. Hold ≥ max(1.8 s, speech + 0.6 s).
- **Titles**: painted on the top arch, or on a placard a puppet carries in on its strings (it bobs, then exits). Yatra One or Rozha One for short Devanagari titles.
- Puppets never lip-sync: a speaking puppet bobs its head on accents, and its words appear in the subtitle.

## 5. Motion quality

- **24 fps on ones**, physics-driven. Finger paths are keyframed with `eio` and `spring`; the puppet's motion is their consequence: hop, sway, bounce, drag, never smooth intent.
- **Signature moves**: the dancer's spin (skirt flares to a disc), the bow (forward pitch), the rider's gallop (horse and rider one piece, rhythmic up-down), the juggler's throw, the floating hop (lift, glide, soft hem thump), two puppets clashing.
- **Settle**: every move ends in a 0.5–1.5 s damped sway.
- **Landings on the dholak beat.**
- Never moving: the booth (except the banner), the faces. Attitude comes from head angle and body tilt.

## 6. Camera grammar

A spectator at a fair, sometimes slipping backstage. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Front row: whole booth, heads in foreground | this is a show | a fable; a lesson; an announcement |
| Medium on one puppet, strings rising | a role and its controller | an individual; a job; dependency |
| Tilt up the strings to the hands | the controller revealed | power; a manager; fate |
| Floor-level low angle | the puppet as giant | pride; a hero; a child's view |
| Close on painted eyes | fixed face meets the moment | irony; humour; a stare |
| Behind the backdrop | the craft | a making-of; the truth behind |
| Locked wide through a dance | rhythm, repetition | a routine; a cycle; a celebration |
| Whip pan with a hop | energy | an escape; a race; a chase |

Framing: when a puppet is the subject its strings are in frame; the stage floor line is visible in wides; audience heads give scale. Transitions: the valance drops; a puppet crosses the lens; the lamp dims; the backdrop cloth is swapped. Forbidden: digital wipes, crossfades between unrelated scenes.

## 7. Sound palette

- **Dholak**: two-headed hand drum: bass head with upward glide (bayan-like low membrane), treble slap and ring (darbuka attack + `frame_drum`), a fast looping pattern with fills.
- **Around it**: ghungroo and small cymbals (`sleighbells`, `nepal_bells`), harmonium (`accordion`), wooden clappers (`claves`, castanets from `world_perc`), a bowed drone (`erhu` or low `cellos` through a nasal formant).
- **The boli**: the reed squeak, synthesised: a sawtooth at 900–1800 Hz through a narrow resonant band-pass, fast pitch contours following the rhythm of the line, gated into syllables; pair it with a narrator who speaks the meaning.
- **Foley**: wooden head knock, hem thump on the cloth floor, string creak and twang (a high, short `pluck`), bells on every landing, skirt swish on spins; a fair outside (children laughing, claps, vendors' bells).
- **Silence**: the dholak stops and a puppet hangs mid-air; only a string creak.
- **Mix**: dholak forward, narrator clear (music ducked ~8 dB), boli at speech level but band-limited; −14 LUFS.

## 8. Native moves

- **Strings to the sky.** Tilt from a puppet up its strings to the hands. *Fits content like:* a worker and a boss; algorithms steering users; fate.
- **The spin.** The dancer turns and her skirt opens into a disc. *Fits content like:* a celebration; a whirlwind week; dizziness.
- **The hop.** A puppet floats across the stage in one arc. *Fits content like:* travel; a jump in time; skipping a step.
- **Slack strings.** The strings go loose and the puppet folds to the floor. *Fits content like:* burnout; a power cut; sudden freedom.
- **The shadow on the backdrop.** It grows, lags or acts alone. *Fits content like:* a fear; a dream; a hidden self.
- **The tangle.** Two puppets' strings cross. *Fits content like:* a conflict; a partnership; red tape.
- **Backstage.** The puppeteer behind the arches. *Fits content like:* a making-of; a supply chain; the people behind a service.

## 9. Pitfalls of the medium

- Puppets moving like game characters → physics: hang, sway, hop; no leg cycles.
- Strings flickering or vanishing → ≥ 1 px width, antialiasing, a glint; keep them in frame.
- Simulation jitter or explosions → fixed-step pre-simulation, enough constraint iterations, damping, caching.
- Plastic heads → painted wood under clearcoat, grain, chips.
- Strobing mirror glints → seeded normals, a bloom threshold, slight temporal smoothing.
- A cardboard-box stage → printed backdrop texture, valance folds, a warm light pool.
- **Living tradition**: kathputli is a hereditary craft of puppeteer communities who still perform and struggle for a livelihood. Don't caricature performers or present the film as a recorded traditional show; keep deity figures out of decoration; credit the tradition, and commission or consult puppeteers for commercial work.

## 10. Engine

No demo engine yet (draft). A first demo should build:

- `booth.js`: frame, backdrop texture, valance, side cloths, lights.
- `puppet.js`: `head(spec)` (lathe, features, face decal, turban or veil), torso, arms, `skirt(ringN, flareK)`.
- `strings.js`: position-based solver, `presim(controls, hz = 240)` → frame cache, string drawing.
- `controls.js`: keyframed finger paths per beat; `costume.js`: gota, mirror instancing, bells.
- `mix.py`: dholak and boli synthesis.

Start from: `styles/brick-toy/demo/set.js` (`buildSet`: three.js set and lights); `core/three/post.js` (`makePost`: DOF, GTAO, bloom, grade); `styles/paper-popup/demo/cutmesh.js` (`thread` for strings, `particles` for dust); `styles/shadow-puppet/demo/houyi.js` (`ik`, `solve` for reaches) and `styles/shadow-puppet/demo/stage.js` (frame and audience heads); `core/lib.js` (`spring`, `mulberry`); `core/audio/sampler.py`, `core/audio/sfx.py`.

## 11. Variation space

You decide the story, the cast of types, whether we go backstage, the stage colours, the opening, the ending and the camera.

- Structures: **a fair's programme** (act after act, each puppet one idea); **one puppet's day** (it wakes on its nail, works, rests); **who pulls the strings** (front and backstage alternate).
- Openings: **puppets hanging on a nail**, lifeless, until a hand takes them; **the dholak alone** in the dark, then the lamp; **audience heads** settling as the cloth lifts.
- Endings: **puppets laid in a trunk**; **strings slack**, the puppet sitting on the floor; **the booth folded away** at dusk.

---

Status: **draft** — no demo film yet. Before this is used as a library style it needs a demo film, `DEMO.md`, stills and the checks in the Lemo-Opuscar `MAINTAINING.md` ("Gates").
