# Ebru Marbling — Style Prompt

> Colours floated on a tray of thickened water: drops spread into rings, a stylus and combs drag them into veins, waves and flowers, and a sheet of paper laid on the surface lifts the whole pattern at once.
> References (grammar only): Turkish ebru (pigments with ox gall sprinkled from horsehair brushes onto a size thickened with tragacanth, drawn with an awl and combs, lifted onto paper; stone, combed, wavy, nightingale's-nest and flowered patterns), inscribed by UNESCO as Turkish intangible heritage; European marbled endpapers for combed patterns; Japanese suminagashi for floating ink rings. Never copy a known master's sheet or flower, and never name them in the film.

## 1. Essence, and what it is not

- **Colour floats**: every new drop spreads and pushes everything already on the surface outward, so earlier colours become thin rings and veins.
- **Lines are boundaries, not strokes**: the pattern is made of colour fields meeting, with fine pale halos where gall-rich colour pushed others back. No outline is ever drawn.
- **Tools pull, never paint**: an awl draws one curl, a comb drags parallel tines, a brush sprinkles; the result follows fluid rules exactly (area is preserved, nothing crosses).
- **The lift**: the pattern exists for the film twice: alive on water, then fixed on paper, slightly mirrored, with small voids where air was trapped.

Not Watercolor Brush (no pigment soaking into paper, no brush marks). Not Chinese Ink Wash (no brush gesture; ink rings only as a special case). Not a fluid simulation or a flow-field generative piece (no swirl, no vortices, no noise advection: only drops and tool strokes).

## 2. Materials & rendering

- **Operation list, not a simulation.** The surface is the composition of exact, invertible marbling maps applied in order:
  - **Drop** at centre c, radius r: every point p moves to c + (p − c)·√(1 + r²/|p − c|²). Inside the new disc is the new colour.
  - **Tine line** through point b in direction m (unit), normal n: p moves by z·m with z = α·λ / (d + λ), d = |(p − b)·n|; α = shift, λ = sharpness. A comb is several parallel tines; a back-and-forth comb is two passes.
  - **Curl** (awl circling): rotation about c by an angle that falls off with distance.
- **Rendering per pixel** (WebGL fragment shader): run the inverse maps from the newest op back to the oldest; whenever a point lands inside a drop at its own time, take that drop's colour; otherwise the tray colour. Up to a few hundred ops fit in a uniform buffer; beyond that, bake the field to a texture and continue. This is exact, resolution-free and deterministic.
- **Vector mode**: forward-map densely sampled drop boundaries for crisp hairline halos and for animating along the boundaries.
- **Halo**: a 1–2 px lighter rim on each drop's boundary (gall), stronger for early drops; colours slightly granular (pigment flecks: blue-noise speckle ±5 %).
- **Water**: a faint softbox reflection; tiny ripples only at tool contacts.
- **Paper**: laid on from one edge (a contact line sweeping across); lifted copy is mirrored, a little paler, with fibre texture, a few voids (seeded white specks) and a straight drip edge where it left the tray.
- Op times drive animation: a drop's r eases to size in 0.3–1 s; a tine's α eases along the stroke.

## 3. Colour logic

- **3–6 pigments plus the tray colour**, mineral and earthy in feeling: indigo, madder red, ochre, a green, a soot black, a white made from chalk.
- **Order is value**: the first colours become the thinnest veins, the last drops the largest fields. Plan the order: dark first for fine dark veining; light last for open fields.
- **The ground** is usually the first colour sprinkled over the whole tray, not the paper.
- **Accent**: a single bright drop added last and kept small (a flower's centre, a signal).
- Never: gradients inside a field, a colour that appears without a drop, black outlines.
- Examples: stone pattern — ochre ground `#d6b170`, indigo `#2b3d6b`, madder `#9c3a2c`, soot `#2a2622`, chalk `#efe9dc`; night — soot ground `#1d1c22`, blue `#36518a`, white `#e9e6dd`, accent red `#c4402f`.

## 4. Type & subtitles

- **Titles**: letters can be marbled: rasterise **Cormorant Garamond** or **Playfair Display** to a mask, fill it with the lifted pattern, place on cream paper with a thin dark rule; or let a drop sequence form one large initial.
- **Subtitles**: on the paper margin or a cream band below the tray, **EB Garamond** 34–42 px in soot, two lines at most; Devanagari in **Noto Serif Devanagari**. Hold ≥ max(1.8 s, speech + 0.6 s).
- Marbled sheets traditionally frame calligraphy; do not imitate Arabic calligraphy or sacred texts as decoration.

## 5. Motion quality

- 24 fps on ones, all continuous: the medium has no stepped drawing. Slow viscous easing (`eo` for spreading drops, `eio` for tool strokes).
- **Rhythm comes from drops**: each drop is an event that pushes the whole surface; sequences of drops are phrases.
- **Tool strokes** cross the tray at 100–400 px/s; combs slower; the awl curls in 1–2 s.
- **Nothing moves by itself**: between ops, the surface is still (or drifts by less than a pixel per second).
- **The lift** takes 1–2 s down and 1.5–3 s up; the tray left behind is pale and broken, then wiped.
- Never moves: the tray edges, a lifted sheet once laid to dry.

## 6. Camera grammar

A top-down studio camera over the tray, with occasional side views of hands and paper. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Locked overhead, drops landing | accumulation; one thing pushing another | growth; crowding; influence |
| Slow push into veins | detail hidden in the pattern | a microscope view; a map; a fingerprint |
| Track with a comb across the tray | order imposed on chaos | regulation; a harvest; a day's routine |
| Side view at water level as paper descends | the decisive moment | a vote; a photograph; a commitment |
| Lift and turn to the dried sheet | the record, fixed | a memory; a document; a result |
| Pull back to a wall of drying sheets | many versions, none the same | a community; variation; an archive |
| Rewind of ops (inverse maps) | undoing; tracing back to the cause | an investigation; regret; origins |

Framing: overhead shots keep the tray edge out of frame unless the film is about the tray; hands enter from one side only. Transitions: a new drop covering the frame, a comb wipe, a paper lift, a full-frame drop of tray colour; no crossfades between unrelated patterns.

## 7. Sound palette

- **Instruments**: an end-blown reed flute colour (`flute` with heavy breath noise, slow vibrato, low register), a plucked zither line (`pluck('koto')` or `pluck('harp')` with fast tremolo), a lute (`pluck('nylon_guitar')` darkened), frame drum and `world_perc` darbuka strokes, a bowed drone (`cellos`). Modal, unhurried; do not claim a specific makam.
- **Foley from water and tools**: a drop landing (soft pitched plip, pitch from drop size), sprinkled spatter (many tiny plips), a stylus sliding (thin wet hiss), a comb (soft multi-tine drag), paper laid down (a hush), paper peeled up (slow suction, drip), tray wiped with newsprint.
- **Silence**: the still tray between drops: only room tone.
- **Voice**: hushed, slow, a teacher at the tray. Music ducked ~8 dB under voice; −14 LUFS.

## 8. Native moves

- **The push.** Each new drop shoves everything outward into thinner rings. *Fits content like:* a new idea crowding old ones; a city expanding; generations.
- **The comb.** Parallel tines turn round stones into flowing bands. *Fits content like:* a reform; traffic organised; a field ploughed.
- **The curl flower.** Drops in drops, then one awl stroke pulls a petal. *Fits content like:* a birth; a turning point; a gift.
- **The lift.** Paper takes the pattern in one touch; the water is left broken. *Fits content like:* a photograph; a decision made permanent; a memory kept.
- **Exact rewind.** Run the maps backward: veins unwind into the original drops. *Fits content like:* tracing a rumour; reversing an error; finding a cause.
- **No two alike.** The same op list with tiny seed changes gives a wall of sibling sheets. *Fits content like:* twins; a product line; a community.

## 9. Pitfalls of the medium

- **Using a Navier–Stokes or noise-advection fluid** gives turbulent, blurry smoke → only drop, tine and curl maps.
- **Too many ops** blow the shader → bake to a texture every ~200 ops.
- **Gradients and soft edges** look like airbrush → hard boundaries with a thin halo.
- **Constant motion** loses the stillness → the surface rests between ops.
- **Saturated neon pigments** break the idiom → earthy pigments, one bright accent.
- **Imitating calligraphy or sacred texts in the margins** → ebru belongs to a living Turkish tradition that often frames religious writing; use plain margins or the film's own words.
- **Presenting the film as a handmade sheet** → credit it as code-made; consult or credit ebru artists for commercial or heritage work.

## 10. Engine

No demo engine yet (draft). A first demo should build:
- `marble.js`: the op list (`drop(c, r, col, t0, dur)`, `tine(b, m, α, λ, t0, dur)`, `comb(...)`, `curl(c, θ, falloff)`), forward maps for vector boundaries, inverse maps for rendering, op baking.
- `tray.js`: WebGL2 fragment shader evaluating inverse ops per pixel, halo and speckle, surface reflection and tool ripples.
- `lift.js`: paper contact sweep, mirrored copy, fibre texture, voids, drip edge.
- `tools.js`: hand gestures as op generators (sprinkle brush, awl, comb, rake).

Start from `core/lib.js` (`mulberry`, `hash`, `eo`, `eio`, `track`), `styles/microgame/demo/glpass.js` (a single WebGL2 canvas with full-screen fragment passes), `styles/risograph/demo/riso.js` (WebGL2 compositor scaffold and paper multiply), `styles/watercolor/demo/paper.py` (paper texture generation).

## 11. Variation space

You decide the pigments and their order, which patterns (stone, combed, wavy, curl, flower), whether the tray, the paper or both are seen, the meaning of each drop, and whether the film ever rewinds.

- Structures: **one sheet** (a single pattern built in real time from first sprinkle to lift); **a series** (one sheet per chapter, each pattern harder than the last); **the archive** (a stack of lifted sheets read one by one, each tray recalled).
- Openings: **an empty dark tray** and a first drop; **a finished sheet** that rewinds into drops; **the brush sprinkling** a ground colour in close-up.
- Endings: **the lift**, paper rising and the tray left broken; **the tray wiped clean** with newsprint; **one last drop** spreading over everything.

---

Status: **draft** — no demo film yet. Before this is used as a library style it needs a demo film, `DEMO.md`, stills and the checks in the Lemo-Opuscar `MAINTAINING.md` ("Gates").
