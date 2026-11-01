# Batik — Style Prompt

> Wax-resist dyed cloth: lines of hot wax drawn or stamped onto cotton, the cloth dipped in successive dye baths from light to dark, each colour kept by wax before the next, fine crackle veins where the wax broke, and a final boiling that lifts the wax to reveal the whole design.
> References (grammar only): Indonesian batik, above all Javanese batik tulis (hand-drawn with the canting) and batik cap (stamped with a copper block), with its inland palette of indigo, soga brown and cream and its bright north-coast palettes; wax- and starch-resist textiles of other regions (Malaysia, India, West Africa) for related grammar. Indonesian batik is living heritage recognised by UNESCO. Never copy a specific cloth or a named traditional motif as a whole, and never name them in the film.

## 1. Essence, and what it is not

- **Colour is made by subtraction**: every area's colour is the record of which baths reached it. Lines are the colour the cloth was before the wax: usually the palest.
- **Wax lines** of near-constant width with soft, slightly bled edges, a drop at each start, occasional stray dots.
- **Layered dyes, light to dark**: two to five baths; overdyes mix (yellow under blue reads green).
- **Crackle**: thin dark veins where dye entered cracked wax, inside resisted areas.
- **Pattern fills everything**: motifs repeat in fields, borders and diagonals; figures and story elements are made of pattern, not painted over it.

Not Crayon Picture Book (wax resists dye on cloth, not watercolour on paper; no crayon texture). Not Woodcut Print (no ink pressed onto a surface; colour soaks through the cloth). Not Risograph Print (no halftone, no misregistered plates; edges bleed, not offset).

## 2. Materials & rendering

- **Cloth**: cotton or silk plain-weave tile with a normal map; folds only when handled. Dye shows on both sides.
- **Stage model** (WebGL): a list of stages `[wax₁, dye₁, wax₂, dye₂, …, boil]`. A wax mask accumulates (union) until boiling or scraping. Final colour per pixel = cloth × Π over baths k where the pixel was not resisted at k of the dye's transmittance Tₖ. Each bath is one uniform colour, so the palette is built by the order of baths, never by painting.
- **Wax lines** (canting): Catmull-Rom path, width 2–5 px at reference scale with ±8 % noise, a bulb at the start (the spout touching down), thinner trailing ends, slight bleed blur (1–2 px) at the edges; stray drops of 3–6 px seeded along long lines.
- **Wax fills**: areas blocked with a brush, edges lumpier than canting lines.
- **Stamped wax** (cap): a pattern tile pressed repeatedly; every repeat identical, joins visible where repeats meet (±1–2 px offset, a slightly heavier edge), unlike hand-drawn repeats, which vary.
- **Dye under the edge**: each bath creeps 0.5–1.5 px under wax edges with noise, so lines are never vector-clean.
- **Crackle**: a fracture network (Voronoi edges warped by noise, ~1 px) masked to waxed areas; at each bath, dye enters cracks at 30–60 % strength, so crackle darkens bath by bath.
- **Boiling**: wax mask fades to show the cloth plus all dyes; a faint waxy sheen and lifted fibres vanish.
- All paths, cracks and drops seeded; the stage list is the timeline.

## 3. Colour logic

- **The palette is a sequence of baths**, not a set of paints: choose 2–5 dyes in light-to-dark order; every visible colour is a product of them.
- **The ground colour** (undyed cloth or the first bath) is the line colour and the light.
- The **darkest bath** is the field: it fills the background and gives the cloth its weight.
- **Accent** = the one colour preserved earliest and kept smallest (a red or a yellow in a dark field).
- Never: a colour that could not result from the bath order, gradients beyond the soft bleed, white brighter than the cloth.
- Examples: inland — cream `#efe2c4`, soga brown `#8a5a2b`, indigo `#1f2f52`, overdye `#2b2421`; coast — white `#f4efe4`, yellow `#e3b23c`, red `#b8322a`, blue-green from overdye `#2f6a5a`, deep blue `#1c2b4a`.

## 4. Type & subtitles

- **Titles are waxed**: letters drawn as canting lines or blocked wax, revealed pale after a bath; **Baloo 2** shapes (rounded, even stroke) suit the spout's line, 60–120 px.
- **Subtitles**: **Baloo 2** Medium 36–44 px in the cloth's palest colour on a narrow band of the darkest dye at the bottom (a selvedge strip), two lines at most. Baloo 2 also sets Devanagari, so Hindi subtitles keep the same face. Hold ≥ max(1.8 s, speech + 0.6 s).
- Labels: short waxed words in a border, ≥ 32 px; anything finer floods.

## 5. Motion quality

- 24 fps. **Wax drawing** runs at the speed of a hand (a canting moves slowly: 80–200 px/s at reference scale); a stamp lands in a beat with a short press.
- **Baths change the whole cloth at once**: a dip is a dark wave crossing the frame or the cloth lowered out of frame and lifted back, wet (darker, glossier) then drying lighter over ~1 s.
- **Story motion is between stages**: a motif changes by being waxed in a new state and dyed; figures can animate on threes as successively waxed versions.
- **Crackle grows** with handling: new cracks propagate along the network over a few frames when the cloth bends.
- **Boiling out** is the release: wax sheen lifts in patches, colours brighten.
- Never moves: lines already dyed, the bath order, the weave.

## 6. Camera grammar

A workbench and dye-yard camera. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Overhead on the stretched cloth, wax line growing | patience, intention | a plan drawn; a route; a handwritten letter |
| Macro along a canting line | the hand, care | a vow; a signature; a mistake |
| Locked frame across a dye bath | transformation in one step | a season turning; a decision; a mood shift |
| Cloth lifted dripping, filling the frame | the result arriving | a reveal; news; harvest |
| Pull back from one motif to the whole repeat | the individual in the pattern | a crowd; a city grid; a family |
| Pan along a stamped border | repetition and rhythm | mass production; routine; a march |

Framing: patterns fill the frame edge to edge; the cloth's border or selvedge may frame text. Transitions: a dye dip, a crack spreading, wax boiled away, a stamp landing; no crossfades, no screen-space colour grading between baths.

## 7. Sound palette

- **Instruments**: gamelan-like metallophones built from `vibraphone`, `glockenspiel`, `marimba`, `gong`, `gong2` (detuned pairs shimmer), `kalimba` for small figures, a bamboo-flute colour from `flute` with breath, frame drum and `log_drum`. Do not claim a specific gamelan tuning; consult musicians for any film about the tradition.
- **Foley from the process**: hot wax (soft sizzle and drip ticks), the canting scraping the pot's rim, a copper stamp pressed (dull thump + wax squelch), cloth slapped into a vat (wet splash), dripping, wringing, wax cracking (tiny dry crackles), boiling water.
- **Ambience**: a workshop yard: birds, water, far voices.
- **Silence**: only the wax drip.
- **Voice**: calm, close, a maker explaining. Music ducked ~8 dB under voice; −14 LUFS.

## 8. Native moves

- **The dip.** One bath changes the whole cloth while waxed shapes keep their past colour. *Fits content like:* nightfall over a town; a policy changing everything but the protected; ageing.
- **Keep before you lose.** Wax a shape, then dye: what was waxed survives. *Fits content like:* what a family keeps through hardship; saved data; a memory preserved.
- **Crackle.** Fine veins spread through the waxed areas under stress. *Fits content like:* pressure on a structure; a drought; tension in a group.
- **The stamp.** One copper block repeated across the cloth, joins showing. *Fits content like:* a factory; bureaucracy; identical houses.
- **Boiling out.** Wax lifts and the full design appears at once. *Fits content like:* a verdict; a festival lit; a project finished.
- **Two hands.** Hand-drawn repeats beside stamped ones show the difference. *Fits content like:* craft versus mass; human versus machine; one versus many.

## 9. Pitfalls of the medium

- **Colours that the bath order cannot produce** read as digital painting → derive every colour from the stage model.
- **Vector-clean lines** → start bulbs, width noise, bleed under edges.
- **Crackle everywhere** looks like a filter → only inside waxed areas, density chosen per film.
- **Painting figures on top of the pattern** breaks the medium → make figures from waxed lines and fills.
- **Smooth animation of dyed shapes** → change motifs between stages or on threes.
- **Named traditional motifs and ceremonial cloths used as decoration** → many motifs carry court, regional or ceremonial meaning (some were once reserved for royal courts; some belong to life events); invent motifs or consult batik makers.
- **Presenting the film as handmade batik tulis** → it is a code-made imitation (like printed "batik" fabric, which makers contest); credit and consult Indonesian artisans for commercial work.

## 10. Engine

No demo engine yet (draft). A first demo should build:
- `wax.js`: `canting(path, {w, bulb, drops})`, `block(region)`, `stamp(tile, grid, jitter)` into the current wax mask; ordered so `drawWax(u)` grows lines over time.
- `dye.js`: WebGL stage compositor: cloth × Π Tₖ over unresisted baths, edge creep, wet/dry state, `bath(k, u)`.
- `crackle.js`: warped Voronoi fracture net, propagation by stress, per-bath penetration.
- `cloth.js`: weave tile, normal map, fold/lift deformation for dipping and handling.

Start from `styles/crayon-book/demo/gl.js` (a resist compositor: watercolour layers resisted by crayon pressure), `styles/risograph/demo/riso.js` (a separation canvas → multiplied ink plates in WebGL2), `styles/woodcut/demo/engine/knife.js` (strokes with width profiles and reveal times), `styles/stained-glass/demo/glass.js` (`voronoi`, `seedsIn`), `core/lib.js` (`vnoise`, `mulberry`).

## 11. Variation space

You decide the bath order and its meaning, hand-drawn or stamped (or both), how much crackle, whether the process or only finished cloth is shown, and the motif vocabulary the film invents.

- Structures: **one cloth, four baths** (each bath a chapter, the story told by what is kept); **stamp and hand** (a mass-made cloth and a hand-drawn one made side by side); **a worn cloth** (a finished batik handled across years, crackle and fading telling its life).
- Openings: **a drop of hot wax** on white cotton; **a cloth rising dripping** from the darkest vat; **a copper stamp** heated over the pot.
- Endings: **boiling out** to the full design; **the cloth hung to dry** moving in wind; **a single waxed line left undyed** in a dark field.

---

Status: **draft** — no demo film yet. Before this is used as a library style it needs a demo film, `DEMO.md`, stills and the checks in the Lemo-Opuscar `MAINTAINING.md` ("Gates").
