# Bauhaus — Style Prompt

> Built geometry in primary colours: circle, square and triangle in red, yellow and blue on off-white with heavy black bars, constructed with ruler and compass and moved like parts of a machine or figures on a stage.
> References (grammar only): the Bauhaus school (Weimar and Dessau, 1919–33); Wassily Kandinsky's pairing of colour and form (yellow triangle, red square, blue circle) and his point-line-plane teaching; Oskar Schlemmer's *Triadic Ballet* (1922) for geometric costumed figures and mechanical choreography; the reflected colour-light plays of Kurt Schwerdtfeger and Ludwig Hirschfeld-Mack (1922–23) for moving, overlapping coloured light; László Moholy-Nagy's light-space experiments and photograms; Herbert Bayer's lowercase-only typography and the school's workshop objects (tubular steel, glass, metal lamps). Never reproduce a specific poster, logo, object design or typeface.

## 1. Essence, and what it is not

- **Three forms, three primaries**: circle, square, triangle; red, yellow, blue; plus black, off-white and one grey. Everything is built from them, figures and type included.
- **Construction is visible**: shapes are drawn with ruler and compass; construction lines and arcs show before the fill arrives.
- **Asymmetric balance with heavy bars**: thick black rules, off-centre blocks, a composition that feels engineered.
- **Function and mechanism**: things are assembled, fitted and pivoted; motion is gears, levers and rails.
- **Lowercase geometric type** used as structure, not decoration.

Not Swiss Motion Graphics (a typographic grid with one signal colour; here geometric primitives in three primaries are the cast), not De Stijl (only rectangles and orthogonals; here circles and triangles lead and diagonals are allowed), not Pictogram Motion (no five-tone grid pattern, no pictogram set), not Memphis Diorama (no pastels, squiggles or playful patterns).

## 2. Materials & rendering

- **2D mode** (Canvas 2D vector): flat fills on an off-white ground with optional offset-print feel (colour plates misregistered 1–2 px against the black, light ink grain).
- **Drawing tools**: `compass(cx, cy, r, a0, a1)` arcs and `ruler(p0, p1)` lines drawn on progressively as pencil-grey construction lines (1 px, 40 % opacity); the fill floods only after the outline closes.
- **Overlap rule, one per film**: opaque knockout, or transparent primaries multiplied (red × blue → near-black violet) as in printed overprint.
- **Light-play mode**: additive coloured shapes on black (screen blend), edges softened 2–6 px; overlaps make secondaries; shapes slide behind masks like stencils in front of a lamp.
- **Stage mode** (three.js): spheres, cones, cylinders, boxes and tori with flat or two-band toon shading in the primaries, an orthographic or long-lens camera, hard stage shadows. Figures are built from primitives (sphere head, cone or cylinder body, disc hands), faceless or with a single line, jointed at pivots.
- **Objects**: chrome tube (a simple environment gradient), opal glass globe, black lacquer, matte paint, used sparingly.
- Geometry cached; every position a function of t; any jitter seeded.

## 3. Colour logic

- **Red, yellow, blue + black + off-white + one grey.** Secondaries appear only where colours overlap.
- **Form–colour code** by default: yellow = triangle (sharp, active), red = square (heavy, grounded), blue = circle (calm, deep). Keep it, or break it once with meaning.
- Black is for bars, text and structure; off-white is space; red marks the strongest point of a composition.
- Never: gradients (outside light-play mode), pastels, extra hues, soft drop shadows.
- Example print: ground `#efe9dc`, red `#d7372a`, yellow `#f2c230`, blue `#1f4f9e`, black `#1b1b1b`, grey `#9a978f`.
- Example light play: ground `#0c0c0e`, lights `#ff3b2f`, `#ffd23a`, `#2f6bff`.

## 4. Type & subtitles

- **One alphabet, lowercase only** for Latin; geometric sans: Jost (titles, body), Poppins, or Space Grotesk for small technical notes.
- Devanagari: Poppins (its Devanagari is built on the same geometric logic); Devanagari has no case, so the lowercase rule applies to Latin only.
- Type runs flush left, ragged right, often rotated 90° along a bar; heavy rules separate blocks. Titles 120–300 px Jost Bold; numbers large in Jost.
- **Subtitles**: Jost Medium 36–42 px (Poppins Medium for Devanagari), black on the ground or white on a black bar, flush left at a fixed margin, never animated. Hold ≥ max(1.8 s, speech + 0.6 s).

## 5. Motion quality

- 24 fps on ones. **Mechanical motion**: constant velocity on rails, rotation about pivots, ratchets that step on the beat, gears coupled by tooth ratio.
- Easing: `eio` for constructions, linear for machines, a snap with ≤ 2 % overshoot when a part fits.
- Construction order: ruler lines, then compass arcs, then fill.
- Figures move like the stage figurines: walking along floor lines, turning in 90° steps, spinning on their axis, arms as rods.
- Appear: constructed, or slid in along a rail. Disappear: disassembled, slid out, folded flat.
- Never moves: the ground, the margin system.

## 6. Camera grammar

A frontal, engineering camera. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Frontal orthographic view | a diagram you can trust | a process; a machine; a lesson |
| Close on the compass at work | making, precision | a design; a plan; a measurement |
| Lateral slide along a rail of parts | an assembly line | a sequence; a catalogue; a factory |
| Top-down floor plan | choreography as geometry | a dance; a meeting; traffic |
| 90° rotation of the whole composition | a change of system | a reframe; a new rule; a twist |
| Light play on black | feeling as abstraction | music; a memory; a dream |
| Pull back from a part to the whole | the system revealed | a summary; a building; a team |

Framing: off-centre balance with the heavy element low or left and large voids; a coarse grid of thirds and concentric circles for placement. Transitions: a black bar sliding across, a circle iris, a shape scaling to fill the frame, a 90° turn; no crossfades or organic wipes.

## 7. Sound palette

- **An exact, mechanical ensemble**: piano played with machine-even velocities (player-piano feel), xylophone, marimba, glockenspiel, woodblock, claves, snare, timpani, clarinet_stac, bassoon_stac, trumpet_stac, vibraphone_hard.
- **One timbre per form**, kept all film: triangle = triangle and glockenspiel, square = woodblock and snare, circle = vibraphone and contrabass_pizz.
- Machine foley: ratchet clicks, meshing gears, compass point scratching, ruler slides, a rubber stamp, tube clinks, a light switch.
- Silence: the machine stops; one tick remains.
- Voice: precise, neutral, didactic, dry. Music ducked ~8 dB under voice; −14 LUFS.

## 8. Native moves

- **Form–colour casting.** The three primitives are the characters. *Fits content like:* three departments of a company; three ingredients; three roles in a family.
- **Ruler-and-compass construction.** An object is drawn and filled before our eyes. *Fits content like:* a logo's logic; a chair's proportions; a geometry lesson.
- **Colour-light play.** Coloured shapes overlap on black and mix into new colours. *Fits content like:* a piece of music; how screens make colour; a mood.
- **Figurine choreography.** Geometric figures walk floor patterns. *Fits content like:* an office's daily routes; a sports tactic; a ritual of greeting.
- **Workshop assembly.** A useful object is built from primitives. *Fits content like:* a lamp; a kettle; a bicycle.
- **Type as architecture.** Bars of lowercase words rotate and become the walls of a building. *Fits content like:* a school's founding rules; a manifesto; a floor plan explained.

## 9. Pitfalls of the medium

- **Poster pastiche** → use the forms as cast and mechanism, not as wallpaper.
- **Colour creep** → secondaries only from overlap.
- **Friendly rounded fonts** → Jost or Poppins, lowercase Latin.
- **Dull robotic motion** → syncopate with gear ratios and ratchet anticipation.
- **An inconsistent form–colour code** → fix the mapping at the start and keep it.
- **Copying recognisable objects or posters** → invent objects from primitives.
- **Symmetry** → asymmetric balance with heavy bars.

## 10. Engine

No demo engine yet (draft). A first demo should build:
- `geom.js`: `compass`, `ruler`, construction-line draw-on by length, flat fills, knockout and overprint modes.
- `mech.js`: `gear(teeth, r)`, coupled rotations, `ratchet(t, steps)`, rails and pivots.
- `light.js`: additive colour-light play with soft masks.
- `stage3d.js`: three.js orthographic stage, primitive figurines, two-band toon shading.
- `type.js`: lowercase layout, rotated bars, Poppins for Devanagari.
- Start from `styles/blueprint/demo/draw.js` (polylines drawn on by length), `styles/one-line/demo/geom.js` (path sampling by arc length), `styles/swiss-motion/demo/ease.js` (precise ease, `snap`, `steps`), `styles/memphis-diorama/demo/memphis.js` (flat-colour three.js world), `core/three/post.js`, `core/lib.js`; music via `core/audio/sampler.py`, foley via `core/audio/sfx.py`.

## 11. Variation space

The agent decides the mode (print, light play or stage), the form–colour code, what is constructed, and how mechanical the rhythm is.

- Structures: **a workshop course** (each section a lesson: point, line, plane, colour, object); **a stage piece** (three figurines, three primaries, one floor plan); **a machine that builds itself** (each part constructed, then fitted, until it runs).
- Openings: **a single point** that becomes a line, then a plane; **a black bar** sliding in to divide an empty ground; **three coloured lights** on black that slowly overlap.
- Endings: **the machine stops** on its last ratchet click; **disassembly** back to three primitives in a row; **a 90° turn** that shows the whole film was one composition.

---

Status: **draft** — no demo film yet. Before this is used as a library style it needs a demo film, `DEMO.md`, stills and the checks in the Lemo-Opuscar `MAINTAINING.md` ("Gates").
