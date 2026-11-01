# Felt Stop-motion — Style Prompt

> Needle-felted wool characters on a set of felt sheets and wool roving, shot with a macro lens a pose at a time: soft fuzzy silhouettes, bead eyes, matte saturated wool, and a halo of fibres that shifts with every frame.
> References (grammar only): the craft of needle felting (wool roving compacted with barbed needles into dense, slightly lumpy forms); 1960s–80s European children's television stop-motion with fabric and wool puppets on miniature sets, shot on twos; macro tabletop photography (shallow focus, warm practical light). Never copy a series' characters, sets or music, and never name them in the film.

## 1. Essence, and what it is not

- **Fuzzy, matte forms.** Round, chubby wool bodies with a halo of stray fibres; light scatters into them; no specular highlight anywhere except the eyes.
- **Bead or embroidered faces**: two glossy bead eyes (the only shiny things), stitched or felted mouths swapped by replacement.
- **A felt world**: flat cut felt sheets with soft edges, wool roving clouds, yarn streams, felt flowers; mixed fibre colours (heathered).
- **Stop-motion truth**: poses on twos, fibre halo changing every drawing, tiny exposure flicker, slight pose wobble.
- **Macro scale**: a real tabletop at centimetre scale, shallow depth of field, warm lamp light.

Not Brick Toy (rigid glossy plastic, studs), not claymation (clay smears and shows fingerprints, has a slight sheen; felt is dry, fibrous and never smears), not Knitted World (no stitch grid; felt is matted fibre), not Tilt-Shift Miniature (not real places faked small).

## 2. Materials & rendering

- **three.js in real units** (metres): puppets 4–10 cm tall, sets 0.3–1 m wide, so HDRI, shadows and depth of field behave like a macro shot.
- **Puppet bodies**: soft primitives (spheres, capsules, ellipsoids) blended into lumpy forms, with low-frequency surface noise (±3–6 % radius) so nothing is perfectly round.
- **Wool shading**: `MeshPhysicalMaterial` roughness 1, `sheen` 0.6–1 with a lighter sheen colour (velvety rim), wrap lighting for scattering; albedo with fibre-streak noise mixing 2–3 wool colours.
- **Fuzz**: shell texturing (16–32 shells, fibre density noise in surface UV, alpha tapering outward, total length 0.5–2 mm at puppet scale) plus a few thousand instanced stray fibres along the silhouette (thin curved ribbons). Fibre noise is anchored to the surface; its seed changes per drawing for boil.
- **Felt sheets**: flat slabs 2–3 mm thick, normal map from dense fibre noise, slightly ragged cut edges; roving as soft volumetric clumps (shells on noise blobs).
- **Eyes**: small glossy beads with clearcoat and a tiny window highlight; embroidered details as thread textures.
- **Light**: a key softbox (RectAreaLight), a warm practical, a bounce; HDRI low. Post from `core/three/post.js`: DOF focused on the eyes, GTAO for soft contact, low bloom, warm grade.
- **Stop-motion pass**: character transforms quantised to twos; per-frame exposure flicker ±0.5–1 % (seeded); shells reseeded per drawing.
- Render at 2× and downsample (shells alias).

## 3. Colour logic

- **Wool dyes**: soft but saturated, never neon; 5–6 hues per set plus **undyed wool** (cream, grey, brown) as the neutral.
- No pure black (charcoal wool) and no pure white (cream); fibre mixing gives every colour a heathered flicker.
- Puppets one step brighter and more saturated than the set; backgrounds lighter and cooler with depth.
- **One accent** for the hero or for feeling (a red scarf, a yellow flower).
- Example: meadow `#8fae5b`, sky felt `#a9c7d8`, undyed `#e9dfcb`, bark `#7a5a3e`, hero `#d8613c`, eyes `#141414`.
- Example (night): ground `#2f3a52`, moon `#f0e2b0`, roving cloud `#8c93a8`, lantern accent `#f2a23a`.

## 4. Type & subtitles

- **Titles are felt objects**: letters cut from felt sheets (rounded Baloo 2 or Shrikhand outlines extruded 3 mm) or felted from roving, laid on the set and lit with it. Devanagari titles in Baloo 2.
- **Subtitles**: Baloo 2 32–40 px in cream with a soft dark shadow, lower third, no box; Baloo 2 also covers Devanagari. Two lines max.
- Hold each subtitle ≥ max(1.8 s, speech + 0.6 s).

## 5. Motion quality

- **24 fps output, puppets on twos.** The camera moves on twos too (a stepped motion-control rig), unless a shot chooses a smooth glide on ones for the whole film.
- Wool has soft mass: small anticipation, gentle overshoot on a spring (`spring` with low stiffness), no smear frames, no squash beyond ~5 %.
- **Fibre boil** on every drawing keeps still puppets alive; a held pose still breathes (a 1–2 % chest scale cycle).
- Walks are hops or waddles with a body bob; replacement mouths and eyelids swap on twos.
- **Appear** by felting in (loose roving gathers and compacts) or hopping in; **disappear** by puffing out into roving or walking off.
- **Never moves**: the felt ground and set pieces unless touched; the lamp.

## 6. Camera grammar

A tabletop camera at puppet height. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Low eye-level medium on a puppet | Being with the character | a conversation; a worry; a small victory |
| Stepped dolly along a felt landscape | A small journey | a walk to school; a delivery; a migration |
| Rack focus between two puppets | Attention shifting | a reply; a surprise; a choice |
| Top-down onto the felt set | The map of a little world | a village; a game; a plan |
| Push to close-up on bead eyes | Feeling | fear; love; recognition |
| Pull back to show set edges and the real table | It is a made world | a bedtime frame; a "the end"; a making-of |
| Locked wide with weather moving | Time on the set | snow falling; seasons; a storm |

Framing: puppets fill ≥ 1/3 of frame height in dialogue; keep eyes in focus. Transitions: a felt sheet sliding over the lens, a roving cloud passing close and soft, a cut on action; no crossfades or digital wipes.

## 7. Sound palette

- **Cosy acoustic**: `ukulele`, `glockenspiel`, `kalimba`, a music box via `pluck('music_box', …)`, `clarinet`, `bassoon` (comic), `violins_pizz`, `accordion`, `recorder`, `vibraphone`, soft `marimba`.
- **Foley muffled by wool**: footsteps as low-passed soft thuds, wool rub as brushed noise, felt flaps, tiny bead clicks, a puff of roving (a breathy noise burst), springs and pops for comic beats from `core/audio/sfx.py`.
- **Ambience**: miniature nature (birds, a brook, wind) kept small and close; room tone for interiors.
- **Silence**: room tone and one small sound (a bead click, a breath).
- **Voice**: warm, gentle; character voices short and simple; music ducked ~8 dB under voice; final −14 LUFS.

## 8. Native moves

- **Felting in.** A cloud of loose roving gathers, compacts and becomes a creature or object. *Fits content like:* an idea taking shape; a new member joining a team; a seed growing into a plant.
- **Puff out.** A shocked or vanishing character bursts into loose roving. *Fits content like:* a surprise; a burst bubble of hope; something forgotten.
- **Living stillness.** A held puppet keeps breathing through fibre boil. *Fits content like:* waiting at a station; listening to a story; grief.
- **Felt-sheet world.** Layered flat felt hills and skies slide like theatre flats. *Fits content like:* a journey over hills; a weather change; day into night.
- **Yarn water.** A river or rain of yarn strands in stepped motion. *Fits content like:* a stream; a waterfall; a downpour.
- **Real-table reveal.** The camera finds the edge of the felt and the real room beyond. *Fits content like:* a bedtime story ending; a craft explainer; a world that is small.

## 9. Pitfalls of the medium

- Smooth CG plush look → shells plus halo fibres, stepped twos, exposure flicker, lumpy forms.
- Fur too long reads as an animal pelt → felt fibres are short and matted (0.5–2 mm at scale).
- Shiny wool → roughness 1, sheen only; only bead eyes reflect.
- Shell aliasing and sorting artefacts → 2× supersampling, alpha-to-coverage.
- Fibres swimming on camera moves → noise in surface UV, not screen space.
- Boil so strong it buzzes → small amplitude; fewer stray fibres on faces.
- Wrong scale (sharp backgrounds) → real units and a macro aperture so depth of field is shallow.

## 10. Engine

No demo engine yet (draft). A first demo should build:
- `wool.js`: shell fuzz material (`shells(mesh, {n, length, density, drawing})`), stray-fibre instancing, sheen and wrap settings.
- `felt.js`: felt sheet and roving materials; cut-edge geometry.
- `puppet.js`: blended soft bodies, bead eyes, replacement mouths and lids, simple IK for hops and waddles.
- `stop.js`: time quantisation to twos (`drawingAt(t)`), seeded exposure flicker, stepped camera paths.
- Start the set, real-unit scale, HDRI and RectAreaLight softboxes, and the stepped-character / smooth-camera logic from `styles/brick-toy/demo/set.js` and `bricks.js`; DOF, GTAO, bloom and grade from `core/three/post.js`; macro tricks from `styles/tilt-shift/demo/post.js`.
- `mix.py`: foley via `core/audio/sfx.py`, music via `core/audio/sampler.py` / `core/audio/pluck.py`, voice via `core/tts/tts.py`. Seeds and easing from `core/lib.js` (`mulberry`, `spring`, `seg`).

## 11. Variation space

You decide the characters, the set, the wool palette and accent, whether the camera steps or glides, how much fibre boil, the opening and the ending.

- Structures: **a small errand** (one character crosses a felt landscape, each stop a new texture); **a season cycle on one hill** (the same set re-dressed in four wools); **a felt workshop** (an object is felted, used and unfelted back to roving).
- Openings: **a heap of loose roving** that gathers into the hero; **a top-down felt map** the camera descends into; **a bead eye opening** in extreme close-up.
- Endings: **the hero puffs back** into roving that drifts out of frame; **the camera pulls back** past the set edge to the dark room; **snow of wool fibres** settling over a still scene.

---

Status: **draft** — no demo film yet. Before this is used as a library style it needs a demo film, `DEMO.md`, stills and the checks in the Lemo-Opuscar `MAINTAINING.md` ("Gates").
