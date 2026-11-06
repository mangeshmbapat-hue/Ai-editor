# Warli — Style Prompt

> Warli wall painting in motion: figures of a circle and two triangles, dabbed in white rice paste on a mud wall, hundreds of them working at once until they join hands in one turning spiral.
> References (grammar only): the Warli painting of the Warli Adivasi community of the Sahyadri foothills of Maharashtra (around Dahanu and Jawhar), traditionally painted by women in rice paste with a chewed bamboo stick on mud-plastered walls, for marriages and the harvest. Take the circle-triangle-line vocabulary, the crowded everyday scenes and the spiral dance around the tarpa player; never copy a specific painting or painter, and never name them in the film.

## 1. Essence, and what it is not

- **One white on one earth.** Opaque grainy white on a mud-brown or red-ochre wall; nothing else.
- **Three shapes build everything**: circles (sun, moon, heads), triangles (bodies, mountains, trees, roofs), lines (limbs, ploughs, ropes, ladders). A person is a circle head over two triangles that meet at the waist, with single-line arms and legs.
- **The whole community at once.** Dozens to hundreds of small figures (2–6 % of frame height), each doing its own task, scattered across the wall with no horizon and no ground shadow.
- **The circle of dance.** Figures hold hands in rings and spirals around a musician at the centre; the spiral is the style's signature shape.
- **Handmade, not geometric.** Triangles are lopsided, circles dented, lines frayed at the end; no two figures alike.

Not Pictogram Motion (no grid, no brand system, no bold type; figures are paste dabs on mud, not round-capped bars, and their crowd is a village, not an icon set), not Chalkboard (no writing, no lesson board, no wipe), not Red Paper-cut (painted on a wall, not cut), not Madhubani (no outlines, no hatching, no colour).

## 2. Materials & rendering

- **Wall**: mud-and-dung plaster: earth base, low-frequency blotches (±5 %), straw fibres, grit, hand-smoothing arcs, hairline cracks; seeded, cached, world-anchored. Fresh plaster is a darker damp band that lightens behind a wiping edge.
- **Paste dab** (`dab(shape)`): fill white, multiply alpha by a grain texture (speckle + clotted spots, 75–100 % coverage), erode the edge with 1–2 px value noise; a darker copy 1 px down-right at 15 % makes the paste sit proud.
- **Stick stroke**: a chewed bamboo stick: 2–5 px at 1080p, a landing blob, slight taper, 2–4 bristle tracks splitting in the last 15 % (dry paste).
- **Figure kit**: head circle; upper triangle point-down (shoulders), lower triangle point-up (hips), meeting at the waist pivot; arms and legs as two-segment lines with one bend; a knot of hair, a pot, a bundle or a tool as one extra shape. Animals from the same kit (triangle or rectangle bodies, line legs, a curve of horns). Trees: a trunk line with branching lines and leaf ticks or dots; huts: a triangle roof over a square.
- **Variation per figure** (seeded): triangle ratio ±15 %, tilt ±6°, head ±10 %, limbs ±8 %, 1–3 px vertex jitter; each figure pre-rendered per pose into a sprite atlas.
- **Crowd**: agents with seeded task schedules (plough, carry, pound, fish, climb, dance), Poisson-disc placed with 1.5× body clearance, z-order by y for overlap only. Everything is a function of t; no light, no lens effects.

## 3. Colour logic

- **One colour of paint (white) and one ground.** Choose the ground per film: mud brown, red ochre, or a dark night-wall; a second ground may arrive only as a new wall.
- White is never pure: a warm off-white with grain; thinner paste (60–75 % coverage) for things far away or fading.
- **No accent hue.** Emphasis comes from size, isolation, density and motion: one figure alone in a cleared space is the "accent".
- Nothing is shaded, outlined in another colour, or lit.
- Example ground pairs: mud `#7a4a2c` + paste `#f1ebdf`; red ochre `#a2462b` + `#f4eee4`; night `#3a2a22` + `#e9e2d4`.

## 4. Type & subtitles

- Words are **painted on the wall in paste**: text to a mask, then through `dab` (grain, eroded edge, slight relief). No boxes, no plates.
- **Kalam** for subtitles (36–44 px Latin and Devanagari), **Baloo 2** (bold) for titles (70–120 px), both rough-edged by the paste pass. Hindi and Marathi subtitles are supported by both.
- Subtitles sit low on a cleared band of wall, ≤ 2 lines, appear in a quick paste dab and fade into the plaster. Hold each ≥ max(1.8 s, speech + 0.6 s).
- Numbers may be shown as **counted figures** (ten people for ten) beside the digits.

## 5. Motion quality

- **Figures on twos** (12 fps), wall and camera on ones (24 fps). Work cycles are 4–6 drawings (hoe, pestle, a walk where the triangles rock ±8° about the waist).
- **Group timing**: neighbours share a cycle with small phase offsets (5–15 %), so a field of workers ripples rather than marches in sync.
- **Painting-in**: head dab, upper triangle, lower triangle, four limb strokes in ~0.5 s; a crowd paints in by a sweep (left to right, or outward). Exits: walk off, or the paste thins into the plaster.
- Easing: linear within cycles, `eio` for placements, `ss` for camera.
- Never moves: the wall, the sun and moon unless they mark time, and the dancers' shared centre.

## 6. Camera grammar

A wall seen square on; distance is the only lens.

| Move | What it expresses | Can serve |
|---|---|---|
| Locked full wall, crowd busy everywhere | a whole community at once | a village economy; a day's work; a festival |
| Slow lateral pan along the wall | life in sequence | seasons; a supply chain; a route |
| Push into one small figure doing one task | one person's part | a single job; a witness; a newcomer |
| Pull back from one figure to hundreds | the one among many | a census; a movement; scale |
| Overhead hold on the spiral as it turns | togetherness, a cycle | a celebration; a cooperative; repetition |
| Tilt from the sun over trees to the field | the order of nature | weather; a harvest; a calendar |
| Locked frame, figures added one by one | counting | quantities; a queue; a team forming |

Framing: even a close-up holds a figure at most a third of the frame height; the paste grain is the detail. Transitions: fresh plaster wiped over and a new scene painted; a pan to an unpainted stretch; the spiral unwinding into a line that leads on. Forbidden: crossfades, perspective, blur, grading shifts.

## 7. Sound palette

- **The tarpa** leads: a gourd trumpet with a droning, reedy, nasal voice. Approximate with low `clarinet` + `bassoon` through a 700 Hz–2 kHz formant and light saturation, or numpy odd-harmonic reed synthesis; short, circling, repeated phrases.
- **Drums and bells**: a deep two-headed drum (`frame_drum` + `gran_cassa`), a sharp stick drum (`log_drum`, `woodblock`), ankle bells (`sleighbells`, soft `nepal_bells`). Never sample or imitate a recorded community song.
- **Foley**: paste dab (wet tap + brush rustle), plaster wipe (noise sweep), clay pots, wooden pestles, hoes in earth, bullock bells, birds, rain on thatch. **Ambience**: hillside wind, distant voices, night crickets.
- **Silence**: the wall alone, a single dab sound inside it.
- **Voice**: a calm community narrator, plural "we"; Hindi or Marathi narration fits; music ducked ~8 dB under voice; −14 LUFS.

## 8. Native moves

- **The spiral.** Hand-holding figures on an Archimedean spiral (`r = a + bθ`) step in a shared cycle while the ring turns around a centre musician; it can wind in or unwind into a line. *Fits content like:* a team coming together; a network effect; a cycle of the year.
- **The busy wall.** Many looping tasks at once; the camera picks one, then shows all. *Fits content like:* how a market works; a hospital shift; a factory floor.
- **Counted people.** Quantities shown as figures painted one by one, in rows. *Fits content like:* votes; a population change; how many hands make a meal.
- **The waist hinge.** The two triangles rock about one pivot; the same hinge makes walking, bowing, lifting and dancing. *Fits content like:* labour; a greeting; exhaustion.
- **Paste returns to plaster.** Figures thin and fade into the wall. *Fits content like:* migration; memory; a vanishing trade.
- **Sun and moon as clock.** Circles cross the top of the wall to mark time while work below changes. *Fits content like:* a day; a season; a long wait.

## 9. Pitfalls of the medium

- Clean vector triangles read as icons → paste grain, eroded edges, lopsided shapes.
- Copy-pasted crowds → seeded proportions, phase offsets, varied tasks.
- Figures too large → keep them small; detail is the crowd, not the figure.
- Colour creeping in → white on one ground only; emphasis by isolation.
- A perfect geometric spiral reads as hypnosis or a galaxy → joined hands, stepping legs, small radial wobble.
- Ground lines, horizon and shadows add false perspective → none; overlap by y only.
- **Sacred motifs as decoration.** The square *chauk* painted for marriages, with its deity figures, is ritual: never use it as ornament, a logo frame or a product badge. Do not present a code-made film as authentic Warli painting; for commercial work, credit or consult Warli artists.

## 10. Engine

No demo engine yet (draft). A first demo should build:
- `wall.js`: `plaster(seed, earth)`, `wipe(t, edge)`, cached at 1.5× frame.
- `paste.js`: `dab(path, {grain, erosion, relief, seed})`, `stick(pts, {w, splitAt})`, `pasteText(str, font, px)`.
- `figure.js`: `figure({h, ratio, tilt, hair, prop, seed})`, `pose(name, phase)` for walk, hoe, pound, carry, climb, dance; sprite atlas per pose.
- `crowd.js`: `scatter(region, n, clearance, seed)`, task schedules, `spiral(n, a, b, ω, t)`, `rowCount(n, t)`.

Start from `styles/papercut-red/demo/rig.js` (`solveRig`), `styles/shadow-puppet/demo/houyi.js` (jointed rig), `styles/crayon-book/demo/crayon.js` (`dab`, `ribbon`, `handCircle`), `core/lib.js`, `core/render/`, `core/audio/sampler.py`, `core/audio/sfx.py`.

## 11. Variation space

You decide the ground, the community's tasks, what the spiral means, the opening, the ending, the camera path and the pacing.

- Structures: **one long wall** (a pan that walks through seasons, each stretch a chapter); **the gathering** (scattered workers converge, task by task, into one dance); **counting** (a question answered by painting people one by one until the number is visible).
- Openings: **fresh plaster** wiped across an empty wall, then the first dab; **the sun circle alone**, the world painted beneath it; **mid-dance**, the spiral already turning, pulling back to the busy village.
- Endings: **the spiral unwinds** into a line walking off the wall; **night**: the moon rises and figures thin into the plaster; **one figure left**, small in a wide cleared wall.

---

Status: **draft** — no demo film yet. Before this is used as a library style it needs a demo film, `DEMO.md`, stills and the checks in the Lemo-Opuscar `MAINTAINING.md` ("Gates").
