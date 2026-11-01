# Wooden Toy — Style Prompt

> A world of lathe-turned and fretsaw-cut wooden toys under a warm lamp: peg people, pull-along animals and stacking rings in glossy lacquer over visible grain, moving only the way wooden toys can.
> References (grammar only): Erzgebirge (Ore Mountains, Saxony) turned toys and the ring-turning technique (Reifendrehen), for lathe profiles and painted villages; Channapatna lacquered toys (Karnataka, India) for lac colour applied on the lathe and rounded forms; kokeshi of the Tōhoku region (Japan) for a turned body with painted face and lathe-ring decoration; nursery pull-along and push-puppet toys for mechanisms. Never reproduce a specific workshop's design, mark or figure, and never name them in the film.

## 1. Essence, and what it is not

- **Everything is turned or cut wood**: solids of revolution (bead, cove, cylinder, sphere, cone) and flat fretsaw profiles with rounded edges; nothing is sculpted or soft.
- **Grain shows through the finish**: lacquer and stain are thin; end grain shows rings, side grain shows stripes; edges are worn to bare wood.
- **Toy mechanics, not animation**: wheels roll, pegs hop, rings stack, dowel joints pivot, strings pull, push-puppets collapse; nothing bends.
- **A real miniature under real light**: a warm practical lamp, a tabletop or floorboards, macro depth of field, soft contact shadows.
- **Faces are painted dots**: two eyes, a mark, perhaps cheeks; character comes from shape, tilt and timing.

Not Brick Toy (no plastic, no studs, no building system), not Paper Pop-up (solid wood, no cards or hinges), not a clay film (nothing squashes), not Tilt-shift (a real miniature, not a real place made to look small).

## 2. Materials & rendering

- **Geometry** (three.js, units in mm): `LatheGeometry` from a 2D profile (Catmull-Rom of 8–20 points, ≥ 48 radial segments); fretsaw pieces as `ExtrudeGeometry` with bevel (size 1–2 mm, 3 segments); wheels, axles and dowels from cylinders.
- **Wood is a solid texture**, not a UV map: in the shader, annual rings = `fract(k·dist(p, treeAxis) + warp(p))`, with a tree axis per piece set by seed (offset and tilted), so end grain shows ring arcs and side grain long stripes; latewood darker; species presets (beech: pale pink, fine; maple: near white; walnut: dark, wide; a pale ivory-wood for lacquer toys). Object space: the grain moves with the piece.
- **Finishes** on `MeshPhysicalMaterial`: oiled (roughness ~0.5, grain fully visible); lacquer (clearcoat 1, clearcoat roughness 0.05–0.15, grain multiplied into the colour at 15–30 %); **lathe lac bands** (rings of colour with slightly uneven edges, very glossy); opaque brush paint with faint brush marks.
- **Wear**: an edge mask (bevel distance or a precomputed curvature attribute) reveals bare wood on rims, corners and wheel treads; seeded per piece.
- **Painted details**: faces, flowers and stripes as decals drawn once into a `CanvasTexture` per piece, with imperfect brush edges.
- **Set and light**: a wooden table or floor in an HDRI room, one warm key lamp, soft fill, contact shadows; macro depth of field from `core/three/post.js`.
- **Hand placement**: every animated piece gets per-drawing jitter (±0.2 mm, ±0.3°) seeded by drawing index: the trace of a hand that moved it.

## 3. Colour logic

- **Wood is the neutral**: one light species plus at most one dark accent wood.
- Lacquer: 4–6 saturated, slightly warm colours (red, yellow, green, blue, orange), one colour per region, no gradients; black and white only for faces and dots.
- The hero toy owns one lacquer colour that no other toy uses.
- Light is warm (about 3000–3800 K); shadows warm-neutral; no coloured gels unless a window or lamp in the story motivates them.
- Toys sit in the mid-to-light values; the background is darker and soft, or the reverse for a white nursery.
- Never tint the grain in unnatural hues; stain only.
- Example: beech `#d9b98f`, walnut `#6b4a33`, lac red `#c8352e`, lac yellow `#e9b730`, lac green `#2f8a4f`, lac blue `#2a5ea8`, face black `#1d1a18`.

## 4. Type & subtitles

- **Titles** are objects: letters on chamfered alphabet blocks or fretsaw-cut letters standing on the table; Rubik Mono One or Bungee for blocks, Baloo 2 ExtraBold for friendly cut letters (Latin and Devanagari). Chapter titles may be pyrography (letters burned into a board: dark, slightly blurred edge).
- **Subtitles**: warm cream text with a soft dark halo, Baloo 2 Medium 38–44 px (Latin and Devanagari), bottom centre, never animated.
- Hold ≥ max(1.8 s, speech + 0.6 s).

## 5. Motion quality

- 24 fps; **toys on twos** with hand-placement jitter; **camera on ones** (motion-control smooth).
- **Mechanics decide motion**: rolling rotation = distance / radius exactly; a peg hop is a parabola with a click landing and a damped rock about its base edge; dropped rings bounce 1–2 mm; round-bottomed wobble toys rock with damped oscillation; a push-puppet goes limp at its joints and snaps back taut.
- No squash, no bending: jointed figures pivot at pins only.
- Appear: dropped in from above by an unseen hand and settling, rolled in, or turned out of a blank on the lathe. Disappear: knocked over, rolled out, lifted out of frame.
- Never moves: the table, the lamp (unless switched as a story event), painted faces.

## 6. Camera grammar

A macro camera on a tabletop. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Low macro at table level, shallow focus | the toy is life-size to us | a journey; a meeting; a parade |
| Overhead on the table | the play mat as a map | a route; a game; a gathering |
| Slow dolly along a row of toys | a collection, a procession | a family; a queue; a catalogue |
| Rack focus from one toy to the next | attention moving | a choice; a discovery; a reply |
| Locked medium on a mechanism | how it works | a process; cause and effect |
| Orbit around one turned figure | craft and volume | a hero; a gift; a heritage piece |
| Pull back to the scale of the room | it was play | a reveal; waking up; the game ends |

Framing: 50–100 mm equivalent at toy scale; focus on the painted eyes; horizon low. Transitions: a toy rolling across the lens, a focus pull to blur and back, a hand-placed board sliding in; no digital wipes or crossfades.

## 7. Sound palette

- Wooden and small: marimba, xylophone, woodblock, log_drum, claves, glockenspiel, music_box and kalimba (`core/audio/pluck.py`), ukulele, recorder, harp; a toy piano = high piano register with short decay layered with glockenspiel.
- **Foley by material**: wood on wood = short modal knocks (woodblock or claves pitched by piece size); wheels on boards = low rumble plus one tick per revolution tied to wheel angle; lacquer clicks brighter than oiled wood; stacking rings = rising clacks; lathe hum, chisel scrape and falling shavings; a squeak of string through a hole.
- Ambience: a quiet room, a clock, a radiator tick.
- Silence: everything stops; a single wobble toy rocks to rest.
- Voice: a warm, close storyteller. Music ducked ~8 dB under voice; −14 LUFS.

## 8. Native moves

- **Turned into being.** A blank spins on the lathe; the chisel finds a figure in a spray of shavings. *Fits content like:* a product being made; a child growing up; an idea taking shape.
- **Ring-slice reveal.** A turned ring is sliced like bread and every slice is an animal profile. *Fits content like:* a census of a species; a team introduced; a menu of choices.
- **Pull-along parade.** Toys on a string follow a leader with clacking wheels. *Fits content like:* a supply chain; a school trip; a festival procession.
- **Push-puppet collapse.** A figure goes limp and stands up again. *Fits content like:* exhaustion and recovery; a joke landing; a power cut.
- **Stack and topple.** Rings or blocks rise piece by piece, then fall. *Fits content like:* savings growing; a deadline crisis; a city skyline.
- **Nesting reveal.** A turned doll opens to show a smaller one, again and again. *Fits content like:* generations of a family; layers of a problem; a company's history.

## 9. Pitfalls of the medium

- **Plastic look** (uniform gloss, no grain) → solid grain under the lacquer, edge wear, varied clearcoat roughness.
- **Sliding wheels** → derive rotation from distance travelled.
- **Stretched grain** on turned pieces → solid texture in object space, never UV-mapped stripes.
- **Bending or squashing** → rigid pieces and pins only.
- **Too perfect** → placement jitter, imperfect decals, dust.
- **Scale confusion** → keep focus distance and depth of field consistent with millimetre-scale toys.
- **Living traditions as decoration** → Channapatna, Erzgebirge and kokeshi are living crafts with named makers: credit the tradition, never present the film as authentic handmade craft or as a workshop's product, keep religious or festival figures out of decoration, and consult or commission artisans of the tradition for commercial work.

## 10. Engine

No demo engine yet (draft). A first demo should build:
- `lathe.js`: `turn(profile, {seg, species, finish, seed})`, `ringSlice(ringProfile, n)`, shavings as curled ribbons.
- `fret.js`: `cut(shape2D, thickness, bevel)` for flat toys and letters.
- `wood.js`: grain injected into `MeshPhysicalMaterial` via `onBeforeCompile`: `{species, axis, ringK, warp, seed}`.
- `finish.js`: lac bands, decals, edge-wear mask.
- `toyrig.js`: wheel constraints, pins, hop arcs, wobble damping, push-puppet chains, placement jitter.
- `set.js`, `post.js`: start from `styles/brick-toy/demo/set.js` (HDRI desk set, lamp), `styles/brick-toy/demo/bricks.js` (material factory, geometry cache), `core/three/post.js` (depth of field, GTAO, grade) and the macro tuning in `styles/tilt-shift/demo/post.js`.
- `core/lib.js` (`spring`, `mulberry`); music via `core/audio/sampler.py` and `core/audio/pluck.py` (music_box, kalimba); foley via `core/audio/sfx.py`.

## 11. Variation space

The agent decides the toy family, the woods and lacquers, the room, the scale of the world, the mechanisms that carry the story and the voice.

- Structures: **a workshop day** (each toy is turned, finished and joins the others); **a tabletop road trip** (one pull-along toy crosses books, cups and floorboards); **a stacking story** (each chapter adds a ring, and the tower is the plot).
- Openings: **a log end** with its rings in close-up, pulling out to the lathe; **a hand-placed first toy** dropped into an empty frame; **the toy box lid opening** and light falling on painted faces.
- Endings: **everything back in the box**, the lid closing; **the lamp switched off**, one lacquer glint left; **one last wobble** settling to stillness.

---

Status: **draft** — no demo film yet. Before this is used as a library style it needs a demo film, `DEMO.md`, stills and the checks in the Lemo-Opuscar `MAINTAINING.md` ("Gates").
