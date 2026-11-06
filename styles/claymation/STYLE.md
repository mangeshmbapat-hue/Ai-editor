# Claymation — Style Prompt

> Stop-motion with oil-based modelling clay: soft rounded characters and props sculpted by hand, fingerprints and tool marks left in, surfaces that "boil" a little every frame because a hand touched them, squash and stretch that keeps its volume, and anything able to melt into anything else.
> References (grammar only): plasticine stop-motion from the 1970s onward (characters on wire or ball-and-socket armatures, replacement mouths for speech, bead eyes, miniature sets lit like a film stage, animation on twos); clay metamorphosis shorts (one lump becoming a sequence of things); clay painted on glass for morphing transitions. Never copy a studio's characters, designs or sets, and never name them in the film.

## 1. Essence, and what it is not

- **Clay is soft, matte and handled**: thumbprints, smears, tool lines and slight lumps on every surface; colours mixed by hand, never perfectly flat.
- **Boil**: surface detail changes slightly from drawing to drawing because the animator re-touched the puppet; the silhouette stays.
- **Volume-true squash and stretch**: bodies flatten and lengthen without losing mass; impacts dent; nothing is rigid except the set.
- **Metamorphosis is native**: one form melts and re-forms into another; clay can merge, split and be re-rolled.
- **A real miniature world**: tabletop scale, practical lights, shallow depth of field, slight frame-to-frame exposure flicker, no motion blur.

Not Brick Toy (bricks are rigid, glossy and snap; clay deforms, is matte and smears). Not Paper Pop-up Book (paper folds and hinges, never squishes). Not Memphis Diorama or Low-poly Isometric Island (no clean CG surfaces, no flat-shaded facets). Not a smooth 3D cartoon with a clay texture.

## 2. Materials & rendering

- **Engine**: three.js, PBR. Clay material: `MeshPhysicalMaterial` roughness 0.55–0.7, a faint sheen (sheen 0.2–0.3, oily highlight), no clearcoat; **wrap lighting** or a small subsurface fake (lighten the terminator in `onBeforeCompile`) so edges glow softly like wax-rich clay.
- **Fingerprints**: procedural normal decals (warped concentric ridges, ~0.4 mm ridge spacing at puppet scale, 6–12 mm prints) placed by a seeded touch schedule; touches cluster on parts that moved this drawing (hands, mouth, joints).
- **Tool marks and lumps**: low-frequency displacement (1–3 mm), loop-tool grooves in the normal map, colour mottling ±4 % with mixing streaks.
- **Boil**: per drawing, re-seed a small-amplitude 3D noise displacement (0.2–0.5 mm) and shift 10–30 % of the prints; amplitude is a dial (0 = careful studio, high = rough hand-made).
- **Sculpting and morphs**: shapes as signed-distance primitives combined with smooth union (`smin`), polygonised by marching cubes per drawing for morphs and merges; heroes as fixed-topology meshes with blend shapes for faster acting.
- **Puppet**: armature skeleton (bones) skinning the clay; squash and stretch by bone scale with volume preservation (sy = s, sx = sz = 1/√s); **replacement mouths** (a set of 8–12 sculpted mouth shapes swapped, not morphed); eyes are glossy beads (white with a black pupil dot, the only shiny parts), lids pressed on.
- **Set**: miniature practical set at true scale (a 20 cm puppet), painted or clay-covered backdrops, real-looking props; key light with soft shadows, a fill, a rim; GTAO for contact darkening; physical DOF with narrow focus (macro look).
- **Camera artefacts**: exposure flicker ±1–2 % per frame, no motion blur, a faint grain.

## 3. Colour logic

- **Mixed clay colours**: saturated but slightly muddy, never pure primaries; 5–8 clay colours per film plus set colours.
- **Characters carry the saturation**; sets are a step quieter and more textured (painted card, fabric, wood).
- **Accent**: one clay colour reserved for one thing (a scarf, a fruit, a door); it may smear onto other things it touches as a story device.
- Light sets mood (warm practicals, cool daylight); no grade that flattens the clay.
- Never: glossy plastic highlights on clay, pure black or white clay, gradients painted on characters.
- Example: skin clay `#e2a07a`, sky clay `#7fb6d6`, grass `#7fae4e`, red `#c9443a`, mustard `#d8a838`, purple `#7a5a9a`, dark brown `#4a3227`.

## 4. Type & subtitles

- **Titles are sculpted**: **Baloo 2** ExtraBold or **Rubik Mono One** letters extruded (opentype paths → `ExtrudeGeometry`) with rounded bevels, clay material, prints and boil; they can be squashed, rolled or stamped into a slab.
- **Subtitles**: screen-space, **Baloo 2** SemiBold 38–46 px, warm cream with a soft dark outline at the bottom centre, two lines at most; Baloo 2 also sets Devanagari, so Hindi subtitles keep the same face. Hold ≥ max(1.8 s, speech + 0.6 s).
- Labels inside the set are scratched into clay or written on paper props. Write "clay animation" in on-screen text: "Claymation" has been used as a trademark.

## 5. Motion quality

- 24 fps; **puppets on twos** (12 drawings/s), ones for fast action or smooth hero moments; **camera moves on ones** (motion-control feel), held still most of the time.
- **Pose to pose with spacing in the poses**: no motion blur; fast moves use **smears** (a stretched or multiplied clay shape for one drawing) instead.
- **Squash and stretch with weight**: anticipation, a squash on landing, overshoot, settle over 3–6 drawings.
- **Lip-sync by replacement**: one mouth shape per phoneme group, changed on twos, held on long vowels.
- **Metamorphosis** takes 12–48 drawings: the form softens, flows into a lump or a neck, and re-forms.
- **Idle**: boil and a slight breath keep long holds alive.
- Never moves: the set (unless it is clay), the lights within a shot.

## 6. Camera grammar

A stop-motion stage camera: mostly locked, moves deliberate and slow. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Locked medium on a puppet | performance; the gag lands | a reaction; a monologue; a mistake |
| Macro close-up with shallow focus | the material, intimacy | a tear; a fingerprint; a tiny object |
| Slow motion-control dolly through the set | the world is real and small | a street; a workshop; a journey |
| Overhead on a work surface | making, assembly | a recipe; a build; a plan |
| Pull back to reveal the tabletop scale | the world's smallness | a reveal; humour; a "making-of" |
| Push into clay until it fills the frame, morph out | transformation | a dream; an idea; a new chapter |

Framing: eyes and mouth readable in dialogue; feet in frame for walks; no wide shots that shrink faces. Transitions: a clay morph, a hand-squash wipe (a slab pressed over the lens), a cut on action, a light switching; no digital crossfades.

## 7. Sound palette

- **Music**: playful acoustic ensembles: `upright` or `honky_tonk` piano, `clarinet`, `tuba_stac`, `bassoon_stac`, `pluck('banjo')`, `ukulele`, `xylophone`, `marimba`, `glockenspiel`, `accordion`; pizzicato strings (`violins_pizz`, `cellos_pizz`) for tiptoe; `woodblock`; slide-whistle glides from a pitch-bent `ocarina`.
- **Foley of clay**: squelches and soft slaps (low-passed wet noise + low thump), squishy footsteps, rolling and kneading (soft rhythmic sticky noise), stretching (a creaky rubbery band-pass), a dull "pat" for impacts; props by their own material. Ambience: a small room tone, kept low.
- **Silence**: a held pose with only a tiny squelch.
- **Voice**: character voices with clear diction, close-miked, light room. Music ducked ~8 dB under voice; −14 LUFS.

## 8. Native moves

- **Metamorphosis.** One shape melts and re-forms into another. *Fits content like:* a caterpillar to a butterfly; an idea becoming a product; a mood changing.
- **The fingerprint.** A macro reveals the maker's print on a character. *Fits content like:* identity; a handmade brand; a creator and creation.
- **Squash and stretch.** A body flattens, stretches and springs back with weight. *Fits content like:* a heavy burden; a joyful jump; a crash test.
- **Merge and split.** Two lumps press into one, or one tears into two. *Fits content like:* a partnership; cells dividing; a team splitting.
- **Replacement faces.** Mouths and brows swapped for big readable expressions. *Fits content like:* a comic dialogue; a tutorial host; a children's lesson.
- **The hand of the animator.** A real-scale hand enters to fix a puppet. *Fits content like:* a "behind the scenes"; fate intervening; a correction.

## 9. Pitfalls of the medium

- **Smooth CG clay** without boil and prints reads as plastic → prints, lumps, boil per drawing.
- **Boil too strong** makes the whole frame crawl → small amplitude, more on moving parts.
- **Motion blur** breaks stop-motion → none; use smears.
- **Shiny material** reads as candy or plastic → roughness ≥ 0.55, sheen only.
- **Morphing mouths** look like CG → replacement shapes on twos.
- **Volume loss** reads as balloons → preserve volume.
- **Copying a famous clay character or studio look** → invent designs; never imitate a studio's house style; and do not present the film as handmade stop-motion.

## 10. Engine

No demo engine yet (draft). A first demo should build:
- `clay.js`: clay material with wrap lighting and sheen, fingerprint normal decals, tool marks, colour mottling, boil by drawing index.
- `sculpt.js`: SDF primitives with `smin`, marching cubes per drawing, merge/split and morph helpers.
- `puppet.js`: armature skinning, volume-preserving squash/stretch, replacement mouth sets, bead eyes.
- `stopframe.js`: twos stepping, smears, exposure flicker, camera bump; `set.js`: miniature set, practical lights.

Start from `styles/brick-toy/demo/set.js` (tabletop set at true scale, HDRI, softboxes, shadow fitting), `styles/brick-toy/demo/bricks.js` (roughness maps with fingerprints and smudges), `styles/brick-toy/demo/actors.js` (a posable figure with pose objects), `styles/brick-toy/demo/rockets.js` (pre-simulated physics for falls), `core/three/post.js` (GTAO, DOF, grade), `core/lib.js` (`spring`, `back`, `mulberry`).

## 11. Variation space

You decide the cast, the clay palette, the set's scale and materials, how rough the boil is, whether the animator's hand appears, and how much metamorphosis the story needs.

- Structures: **one lump** (a single piece of clay plays every role in turn); **a workshop day** (characters built, tested and rebuilt on a bench); **two neighbours** (two clay households whose colours mix as they meet).
- Openings: **a block of fresh clay** squeezed by a hand; **a macro fingerprint** pulled back to a face; **a set in darkness** with one practical light switching on.
- Endings: **the puppet rolled back into a ball**; **the camera pulls out** to the studio table; **the last pose held** while the boil slowly stops.

---

Status: **draft** — no demo film yet. Before this is used as a library style it needs a demo film, `DEMO.md`, stills and the checks in the Lemo-Opuscar `MAINTAINING.md` ("Gates").
