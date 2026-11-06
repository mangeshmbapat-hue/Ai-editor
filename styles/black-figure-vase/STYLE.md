# Black-figure Vase — Style Prompt

> A turning clay vessel whose painted frieze is the film: glossy black silhouettes on orange terracotta, detail scratched through the black to the clay, touches of added red and white; the vase turns on its wheel and the story comes round its belly.
> References (grammar only): Corinthian and Attic black-figure pottery of the seventh and sixth centuries BCE (silhouette with incised detail, added purple-red and white, animal friezes, ornament bands: meander, tongues, palmette-and-lotus, rays at the foot); the potter's wheel and three-stage firing for how the surface comes to be. Never copy a known vase's scene, figures, inscriptions or signatures, and never name them in the film.

## 1. Essence, and what it is not

- **Two values carry everything**: the semi-gloss black of the slip and the warm orange of fired clay. Figures are black; clay is ground.
- **Detail is incised, not painted**: thin scratched lines through the black reveal clay (anatomy, folds, feathers, hair). No dark line ever sits on the black.
- **Added colour is sparse**: a dull purple-red and a chalky white laid over the black (beards, fillets, shield rims, a category of figure), nothing else.
- **The picture is curved**: it lives on a body of revolution; figures foreshorten toward the vessel's edges and a highlight slides over the gloss as it turns.
- **Bands organise the world**: one figure zone between ornament friezes; figures in profile on a ground line, eye drawn frontal.

Not Shadow Puppetry (nothing is transmitted; the silhouette is opaque paint lit from the front). Not Red Paper-cut (no cut holes; detail is scratched). Not Copperplate Engraving (incision is contour only, never hatched tone). Not red-figure (figures reserved in clay on a black ground) and not a glazed modern ceramic (no glassy coat, no brushwork shading).

## 2. Materials & rendering

- **Vessel**: three.js `LatheGeometry` from a profile curve (32–64 points, 256 radial segments): amphora, hydria, cup, flask or an invented shape; rim thickness modelled, handles as tubes. The profile itself can animate (a pot being thrown).
- **Decoration canvas** in surface coordinates: u = angle, v = **arc length along the profile** (not height, or necks and shoulders stretch). Up to 8192 × 2048, redrawn only when a drawing changes. Layers: clay albedo → slip mask (black) → incisions (`destination-out` on the slip, 1–2 px, ragged, with a pale burr) → added red and white (over slip only).
- **Material**: `MeshPhysicalMaterial`; slip roughness ~0.25 with clearcoat ~0.3 (semi-lustre, never mirror); clay roughness ~0.7 with burnish streaks running round the pot; a height map so incisions hold a sliver of shadow; wear on high points.
- **Slip edges** are never vector-perfect: 0.5–1 px value-noise wobble, heavier black at stroke ends, thin spots where clay speckles through.
- **Light**: key softbox upper left, cool rim behind, dark backdrop so the vessel's outline reads; GTAO and depth of field from `core/three/post.js`.
- **Flat mode**: the decoration canvas shown unrolled as a strip, for reading a whole frieze.
- **Figures**: 2D profile rigs drawn into the canvas per drawing; incisions regenerate from each part's contour and interior lines. All jitter seeded per part.

## 3. Colour logic

- **Clay + black + two added colours.** No fifth hue, no painted gradients; only light, wear and the curve change value.
- Clay is the light, black the subject. The figure zone keeps ≥ 40 % clay so silhouettes separate; ornament bands may be mostly black.
- **Added red** for the one thing that carries meaning (a cloak, a wound, a target); **added white** for a second category of figure or small details (teeth, dots, sails).
- The world around (room, plinth, wall) stays dark and desaturated: the clay is the warmest thing on screen.
- Example: clay `#c8743c`, black slip `#1d1612`, added red `#7a2a22`, added white `#e8dcc4`, room `#2a2420`.

## 4. Type & subtitles

- **On the vase**, words are painted inscriptions: short names in small separated letters in black beside a figure, following its contour, sometimes running right to left; **GFS Didot** or **Noto Serif** (Greek coverage) at 22–34 px on the canvas. Invented names only; never a real potter's or painter's signature.
- **Subtitles** live in the room, not on the clay: **Cinzel** (wide tracking) or **Cormorant Garamond** 34–42 px, warm white on the dark backdrop under the vessel, two lines at most; Devanagari in **Noto Serif Devanagari**. Hold ≥ max(1.8 s, speech + 0.6 s).
- Titles: a band of inscription that turns into view, or letters incised through a black field.

## 5. Motion quality

- **Wheel and camera on ones** (24 fps): constant angular speed or eased spin-ups. **Figures on twos**, redrawn silhouettes painted round the pot.
- **Rotation is the time axis**: the next scene comes round; story time ≈ angle. Typical 6–20°/s; one turn for a whole account.
- **Strobe animation**: figures repeated at equal angles appear to move when each drawing is shown at the same front angle (one frame per step): the pot as a zoetrope.
- Profile acting only: stride, run (the archaic bent-knee run for speed), fight, carry, dance. A figure turns round by being redrawn facing the other way, never in 3/4.
- Appearing: slip brushed in, silhouette filling, then incisions scratched contour first. Disappearing: the vase turns away, or wear flakes slip back to clay.
- Never moves: ground lines, ornament bands.

## 6. Camera grammar

A studio camera around one object. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Locked camera, vase turning | the story coming round; a cycle | a fable; seasons; a process with stages |
| Orbit around a still vase | studying an object | a museum piece; evidence; a gift |
| Push into the frieze until the curve flattens | entering the picture | a face; a moment of choice; a detail |
| Macro along an incised line | craft; precision | a wound; a map line; a sign of ownership |
| Pull back to a shelf of vessels | many stories, one culture | a collection; an archive; a comparison |
| Unroll to a flat strip | reading the whole account | a timeline; a summary; a map |
| Strobe-locked spin | figures alive in a loop | a dance; labour; a repeated action |

Framing: the figure zone faces camera; the vessel's outline stays inside frame in wide shots; text only in the room or painted. Transitions: rotation, a turn to another vessel, unroll and roll, a kiln-glow fade; no crossfades between unrelated images.

## 7. Sound palette

- **Instruments**: plucked lyre (`pluck('harp')` short, or a dry `pluck('koto')`), a double reed (two oboes, one held as a drone, saturated), frame drum, small bells (`nepal_bells`, `triangle`), handclaps; modal lines over a drone.
- **Foley from clay**: the wheel's slow periodic rumble and creak, slip brushed on (soft noise), incision (short high scratch), a knuckle tap on fired clay (dull pitched tok with inharmonic partials), kiln roar, shards.
- **Ambience**: a quiet gallery or a workshop yard.
- **Silence**: the wheel stops; one scratch.
- **Voice**: a measured storyteller. Music ducked ~8 dB under voice; −14 LUFS.

## 8. Native moves

- **The turning frieze.** The vessel rotates and the next episode comes round. *Fits content like:* a year of farm work; a recipe's stages; a relay of messengers.
- **The pot as zoetrope.** Repeated figures at equal angles become a loop under the strobe. *Fits content like:* a runner's stride; a hammer at an anvil; a bird in flight.
- **Kiln reveal.** The firing shown as states: all orange, all black (reduction), then clay returns to orange while the slip stays black. *Fits content like:* a hidden pattern emerging; a test result; a photograph developing.
- **Scratch to detail.** A black blob gains eyes, muscles and folds as incisions are cut. *Fits content like:* a sketch becoming a plan; a suspect described; a character introduced.
- **Shards reassembled.** The vase breaks or is found broken; fragments rejoin with gaps. *Fits content like:* a lost record; a reconstruction; memory.
- **Unroll.** The cylinder flattens into a strip to read the whole sequence. *Fits content like:* a timeline; a summary; a family tree.

## 9. Pitfalls of the medium

- **Shading inside the black** reads as vector art → flat slip; value comes from gloss and curve.
- **Too many or too thick incisions** turn it into engraving → 1–2 px, contours and key interior lines only.
- **3/4 views and overlaps in depth** break the archaic grammar → profile figures, frontal eye, side by side.
- **A seam at angle 0** → wrap the canvas and draw across the seam twice.
- **Stretched necks and shoulders** → v = profile arc length.
- **Strobe aliasing** → lock the frame rate to the figure spacing, or keep speeds clear of it.
- **Mirror gloss** looks like modern glazed ware → semi-lustre slip, matte clay.
- **Passing it off as a genuine antiquity** (fake museum labels, accession numbers, real signatures) → present it as code-made; invent names; consult archaeologists for educational work.

## 10. Engine

No demo engine yet (draft). A first demo should build:
- `vase.js`: profile → `LatheGeometry`, handles, arc-length UVs, material maps (slip/clay roughness, wear, incision height).
- `slip.js`: 2D painting into the surface canvas: `silhouette(part)`, `incise(path, w)`, `added(part, 'red'|'white')`, `wear(seed, amount)`, ornament band generators (`meander`, `tongues`, `rays`).
- `figures.js`: profile rigs with poses on twos; `wheel.js`: rotation, strobe lock, firing states.

Start from `core/three/post.js` (GTAO, DOF, grade), `styles/brick-toy/demo/set.js` (studio set, softboxes, HDRI), `styles/brick-toy/demo/bricks.js` (roughness maps with fingerprints and wear), `styles/engraving/demo/engine/burin.js` (lines kept in cutting order for live incision), `styles/shadow-puppet/demo/houyi.js` (profile jointed rig with IK), `core/lib.js`.

## 11. Variation space

You decide the vessel's shape (or several), what the bands hold, whether the pot is new, worn or broken, the added-colour rule, the room and the turning speed.

- Structures: **one turn, one cycle** (a full rotation equals a year, a day or a life); **a shelf in dialogue** (two vessels answer each other scene by scene); **the making** (thrown, painted, fired; the frieze tells its own commission).
- Openings: **a lump of clay** on a spinning wheel; **an incised eye** in macro, pulled back to the figure; **a shard** in the dark, turned in a hand.
- Endings: **the vase stops** with one figure facing us; **the kiln door closes** on the glow; **the strip rolls back** into the cylinder.

---

Status: **draft** — no demo film yet. Before this is used as a library style it needs a demo film, `DEMO.md`, stills and the checks in the Lemo-Opuscar `MAINTAINING.md` ("Gates").
