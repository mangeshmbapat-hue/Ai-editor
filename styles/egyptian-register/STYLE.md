# Egyptian Registers — Style Prompt

> Painted and carved wall scenes in the manner of ancient Egyptian tomb chapels: figures in composite profile standing on horizontal ground lines, stacked in registers, labelled by columns of signs, flat ochres and blues on plaster or limestone; the story is read band by band.
> References (grammar only): Old to New Kingdom Egyptian wall painting and relief (registers, hierarchical scale, composite view, the squared proportion grid, raised and sunken relief, colour conventions); tomb-chapel scenes of daily work (fields, workshops, boats, markets) for how labour is laid out in rows. Never copy a known scene, ruler, deity or text, and never name them in the film.

## 1. Essence, and what it is not

- **Registers**: the wall is cut into horizontal bands, each with its own ground line. A band is a place, a step or a moment.
- **Composite view**: head in profile with a frontal eye, shoulders frontal, hips turned, legs and feet in profile.
- **Size is importance**: the main figure may span two or three registers; workers are small. Groups are rows of one outline repeated with small offsets.
- **Text is part of the picture**: columns or rows of signs face the same way as the figure they belong to and fill the air beside it.
- **Flat colour inside a dark contour**: no cast shadow, no perspective; a pool is a rectangle seen from above with trees laid flat around it.

Not Pictogram Motion (no modern icons or information grid; these figures have dress, gesture and craft). Not Shadow Puppetry (opaque painted plaster, nothing lit through). Not Red Paper-cut (no cut holes, no paper). Not a pastiche of pyramids and mummies: the grammar is daily work.

## 2. Materials & rendering

- **Ground**: whitewashed or ochre-washed plaster over mud (mottled, hairline cracks, losses) or fine limestone (pale, faint bedding, chisel marks). One pre-rendered texture and height map per wall.
- **Painting order** (also the reveal order): a red-ochre sketch, corrected in black; flat fills; a final dark contour. Brush edges wobble 0.5–1 px; fills are two passes at ±3 % so they are not digital-flat.
- **Proportion grid**: standing figures are built on a squared grid (the classical canon puts 18 squares from soles to hairline). The grid is a real layer that can be drawn in red for a making sequence.
- **Relief modes** from the same figure mask: painted flat; **raised** (background lowered); **sunken** (figure cut in, contour as a deep chamfer that holds a shadow). Mask → distance field → height profile → normal map, lit by a key that can travel (sun across a wall, a lamp in a corridor).
- **Figures**: 2D jointed rigs built on the grid, poses chosen from a canonical set (stride, carry, hoe, row, pour, offer, sit); head always profile, eye always frontal.
- **Wear** is a per-film decision: losses where plaster has fallen, faded blue, soot. Seeded and fixed to the wall.
- World-anchored on the wall plane; the camera pans, tilts and zooms over it.

## 3. Colour logic

- **5–7 pigment colours, flat**: red ochre, yellow ochre, a blue, a green, black, white, on the ground colour.
- **Conventions as grammar**: skin by category of figure (darker red-brown and pale yellow ochre were traditional conventions for men and women); water is blue with black zigzags; plants green; metal and grain yellow. A film may define its own categories but keeps one colour per category throughout.
- **Blue and green are precious**: the brightest blue is reserved for one meaningful thing (the river, the sky band, a key object).
- Never: gradients, cast shadows, rim light on painted figures (light exists only in relief mode).
- Example: plaster `#e6d7b8`, red ochre `#a9472c`, yellow ochre `#d1a24a`, blue `#2f6f9a`, green `#4f8a6a`, black `#1e1a16`, white `#f2ece0`.

## 4. Type & subtitles

- **Signs are real writing.** Either use correct, checked sign groups (**Noto Sans Egyptian Hieroglyphs**, reviewed by a specialist), or leave the label columns to the film's own language. Never pseudo-hieroglyphs that pretend to be text.
- **Labels in the film's language** sit in painted columns or short horizontal bands beside the figure, black or blue on the ground, **Cormorant SC** or **Cinzel** at 28–40 px, written in after the figure is painted.
- **Subtitles**: a bottom register reserved as a text band (ground colour, ruled above and below in black), **Cormorant Garamond** 600 at 36–44 px in black, two lines at most; Devanagari in **Tiro Devanagari Hindi**. Hold ≥ max(1.8 s, speech + 0.6 s).
- Titles: large painted signs or letters in a framed panel; in relief mode, cut in sunken relief and lit across.

## 5. Motion quality

- 24 fps; **figures on twos, pose to pose**: the composite view only reads in canonical poses, so transitions are short (2–4 drawings) and poses hold.
- **Labour loops**: hoeing, rowing, threshing, carrying, pouring as 4–8-drawing cycles repeated along a row with phase offsets, so a register moves like a machine.
- **Appearing**: painted in (red sketch on the grid → fills → black contour), or carved (the chamfer of a sunken relief catches light as it is cut).
- **Light** is the main non-figure motion: a raking key crossing relief marks the passing of a day.
- Never moves: ground lines, register borders, text once written.

## 6. Camera grammar

The wall is the world; the camera reads it. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Lateral pan along one register | a process step by step | a harvest; a production line; a voyage |
| Tilt through the registers | one level to the next | social layers; floors of a building; stages of a system |
| Locked wall, every register working | simultaneity | a town at work; an ecosystem; a workshop |
| Push into one small figure | the individual in the row | a worker's story; a witness; a mistake |
| Raking-light sweep on relief | time passing on stone | a day; centuries; a memorial |
| Pull back to the whole wall | the system at once | a summary; an inventory; an account |
| Grid reveal over a figure | how it is constructed | a standard; design rules; measurement |

Framing: ground lines stay parallel to the frame; label columns stay with their figure. Transitions: a register border as the wipe line, a tilt to the next band, a lamp moving into darkness; no crossfades, no perspective tricks.

## 7. Sound palette

- **Instruments**: harp (sampler `harp` or `pluck('harp')`), flute, a double reed (oboe, saturated), clappers (`claves`, `woodblock`), frame drum, a jingling rattle (`tambourine` jingles, `sleighbells`, `shaker`), handclaps, a held drone. Nothing claims to be reconstructed ancient music.
- **Foley from the wall and the work**: chisel on limestone (sharp tick + grit), brush on plaster, stone dust, footsteps in a stone corridor, reeds rustling, oars and water, grain poured, cattle, a counting voice.
- **Ambience**: a cool stone room, wind outside.
- **Silence**: the tick of one chisel stroke, or a lamp flame.
- **Voice**: a scribe's register: lists, measures, names, numbers. Music ducked ~8 dB under voice; −14 LUFS.

## 8. Native moves

- **Registers as parallel tracks.** Several bands run at once, each a different place or role. *Fits content like:* a supply chain; a hospital shift; the departments of a company.
- **Size as rank.** One figure scaled across registers while the rows work beneath. *Fits content like:* a deadline over a team; a river feeding many fields; a market price ruling small traders.
- **Built on the grid.** A red squared grid appears and a figure is drawn onto it square by square. *Fits content like:* a design standard; a measured plan; how proportions are taught.
- **Labour loop.** One cycle repeated along a row with offsets, a machine made of people. *Fits content like:* a bakery; a shipyard; a data pipeline.
- **The tally column.** A label column fills with signs or numbers as goods pass. *Fits content like:* an inventory; a census; a harvest ledger.
- **Light across relief.** A low sun sweeps carved figures that appear and vanish with the shadow. *Fits content like:* a day's work; a memorial; centuries passing.

## 9. Pitfalls of the medium

- **Pseudo-hieroglyphs as decoration** → real, checked sign groups or the film's own language in the columns.
- **Deities, funerary formulas and royal signs (cartouches, crowns) as ornament** → keep to daily-life grammar; they belong to a religion and to Egyptian heritage.
- **Wrong composite view** (shoulders in profile, eye in profile) reads as a modern cartoon → frontal shoulders and eye, profile head and legs.
- **Shading, perspective or overlap in depth** → flat fills, ground lines, figures side by side.
- **Free in-betweens** make figures wobble out of the canon → pose to pose, short transitions.
- **Too much wear** hides the story → losses only away from faces, hands and labels.
- **Passing it off as an authentic ancient wall** → present it as a code-made reconstruction; consult Egyptologists for educational films.

## 10. Engine

No demo engine yet (draft). A first demo should build:
- `wall.js`: plaster or limestone texture, cracks, losses, height map; `wall(seed, kind, age)`.
- `canon.js`: grid-based figure construction, composite-view parts, the canonical pose set, `figure(spec, pose, gridUnit)`.
- `register.js`: bands, ground lines, layout, labour loops with phase offsets, label columns.
- `relief.js`: mask → distance field → height → normal, lit by a moving key in a WebGL pass.

Start from `styles/papercut-red/demo/rig.js` (affine jointed pieces), `styles/papercut-red/demo/paper.js` (pieces pre-rendered to textures and placed by transform), `styles/stained-glass/demo/glass.js` (smooth polygons, `softPoly`), `styles/shadow-puppet/demo/gl.js` (a light field × surface compositor to adapt for raking light), `styles/ukiyoe/demo/print.js` (flat colour fields, `fbm`, textures), `core/lib.js`.

## 11. Variation space

You decide what the registers mean (places, roles, times), the scale of importance, plaster or stone, painted or carved, the wear, the light and whether text is real signs or the film's language.

- Structures: **one object's life** (from raw material in the bottom band to its use at the top); **a day in rows** (each register an hour, read top to bottom); **the census** (a wall that fills with figures and tallies as a count is taken).
- Openings: **a red grid** on blank plaster; **a lamp** entering a dark corridor; **one small worker** in close-up, pulled back to the whole wall.
- Endings: **the last register left unpainted**, the sketch line still red; **the sun leaves the relief**; **a plaster loss** spreading until only one figure remains.

---

Status: **draft** — no demo film yet. Before this is used as a library style it needs a demo film, `DEMO.md`, stills and the checks in the Lemo-Opuscar `MAINTAINING.md` ("Gates").
