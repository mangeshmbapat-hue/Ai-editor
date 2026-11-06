# Kalamkari — Style Prompt

> Pen-drawn, dye-painted cotton that tells a story in panels: a black line drawn with a bamboo kalam, colour that soaks into the weave in maroon, indigo and mustard, and reds that appear only where a mordant was painted before the cloth went into the dye bath.
> References (grammar only): the Srikalahasti kalamkari of Andhra Pradesh (freehand pen drawing, narrative cloths in registers with written captions) for line and layout; the Machilipatnam (Pedana) tradition for block-printed repeats; the dye process common to both (myrobalan, iron-black, alum mordant, red dye bath, indigo, repeated washing). Take the process logic and the panel grammar; never copy a specific cloth or its scenes, and never name them in the film.

## 1. Essence, and what it is not

- **Cloth, not paper.** A cream cotton ground with visible weave; colour sits *in* the fibres, with soft feathered edges.
- **The kalam line** is the drawing: brown-black, fluid, slightly bleeding, with ornament everywhere (jewellery, borders, flame-like leaves).
- **Story in registers.** The cloth is divided into horizontal bands of panels, each panel one episode, separated by patterned borders, often with a written caption strip.
- **A dye palette**: maroon/red, indigo, mustard, a green made by yellow over blue, black, cream. Colours are transparent and slightly uneven.
- **Process is visible**: drawing, mordant, dye bath, washing in water, sun-drying; the film can show any stage.

Not Pattachitra (opaque mineral paint on a chalk-coated cloth with a lacquer sheen; kalamkari colour is transparent dye in the weave), not Watercolor Brush (no paper, no brush strokes; the line rules and colour follows mordant logic), not Ukiyo-e (no woodblock, no paper, no misregistration), not Risograph (no print plates or halftone).

## 2. Materials & rendering

- **Cloth**: procedural plain weave (warp and weft threads as `sin × sin` with per-thread thickness noise ±15 %, slubs, a few loose threads), cream ground tinted by myrobalan (slightly yellow); cached and world-anchored. Optional folds as low-frequency displacement for shots of cloth hanging or washed.
- **Composite model**: `image = cloth × Π(1 − dyeᵢ · absorptionᵢ)`, a subtractive multiply of transparent dye layers onto the cloth. Each dye layer is a coverage mask feathered along the weave: blur anisotropically along warp and weft (2–4 px), then multiply by thread-level noise so colour pools in threads.
- **Kalam line**: variable width (1.5–4 px) with pressure from curvature (thicker on slow curves, thinner at flicks), a capillary halo (the same path blurred 2 px at 25 % opacity), and ink starvation over long strokes. The line is drawn at hand speed, ornament after contour.
- **Mordant logic**: a hidden `mordant` mask is painted first (invisible or a faint grey-violet); when the dye bath happens, red develops **only where the mordant is**, with uneven strength. Indigo uses a resist mask (areas waxed are protected). Yellow is painted on locally; green is yellow over indigo.
- **Washing**: each wash pass lowers dye on unmordanted ground, slightly widens feathering and brightens the cream; animate as a value `wash ∈ [0,1]`.
- **Block-print variant**: repeats stamped from one carved motif with ±1 px offset, per-stamp pressure noise and a darker rim.
- Layers cache per panel; everything is a function of t under fixed seeds.

## 3. Colour logic

- Five dyes at most: **red/maroon, indigo, mustard, green (= mustard over indigo), iron-black**, on cream. Never white paint; light is the cloth.
- Colours are **transparent and uneven**: a darker shade is more dye, never an added grey.
- **Black is line and hair only**; red is the main field colour; indigo is reserved for one role (water, sky, a god-like or night element; choose one per film).
- No gradients beyond dye unevenness, no highlights, no shadows.
- Example: cloth `#efe3c4`, iron-black `#2a1f19`, maroon `#8c2a1f`, red `#b5402a`, indigo `#2d3e66`, mustard `#c9952f`, green `#5b6e3a`.

## 4. Type & subtitles

- Captions belong to the cloth: a **caption strip** inside the panel border, kalam-written, the way narrative cloths label their episodes.
- Latin: **Kalam** (34–42 px) for captions and subtitles, **Cormorant Garamond** semibold for titles (60–96 px), both rendered through the dye pass (feathered into the weave, iron-black or maroon). Devanagari: Kalam or **Tiro Devanagari Hindi**; Telugu captions: **Noto Serif Telugu**. Hindi subtitles are supported.
- Subtitles sit in a cream strip at the bottom of the frame bounded by a thin border band; writing reveals left to right (~0.4 s). Hold each ≥ max(1.8 s, speech + 0.6 s).

## 5. Motion quality

- **24 fps** for the pen, dye and camera; figure animation on twos (12 fps) with flat pose swaps and pivots, as if drawn anew.
- The pen draws contours first, then ornament, then the mordant is brushed (a soft pass), then dye stages develop with `eio` over 1–2 s.
- **Dye develops, it never fades in**: red blooms from mordanted threads outward; indigo darkens over several dips (each dip a step).
- Washing ripples the cloth (low-frequency displacement, 0.6–1.2 s) and brightens it.
- Figures act within their panel; they never leave the border except in a designed transition.
- Never moves: the panel grid of a cloth once drawn, the weave.

## 6. Camera grammar

A long cloth on a wall, a table or in the river: the camera reads it panel by panel.

| Move | What it expresses | Can serve |
|---|---|---|
| Lateral track along a register | episodes in order | steps of a process; a journey; a timeline |
| Drop to the next register | a new chapter | the next day; the next generation; part two |
| Locked panel, figures acting | one episode told fully | a key decision; a scene; a lesson |
| Push into the kalam line | the hand and its care | craft; precision; a signature |
| Pull back to the whole cloth | the story as one object | a summary; an archive; scale |
| Top-down on cloth in a dye bath or river | process, transformation | change; cleansing; time passing |
| Close on cloth drying in sun, wind moving it | rest, completion | an ending of a phase; a pause; a result |

Framing: one panel, or one register strip, fills the frame; borders stay visible as structure. Transitions: a panel border as wipe; a dye bath (the frame submerges, the cloth comes up a new stage); a lateral move to the next panel. Forbidden: dissolves, lens blur, perspective tilts of the cloth surface beyond a few degrees, light effects.

## 7. Sound palette

- **Instruments as options**: a double-reed lead in the South Indian temple-band manner (`oboe` through a 1.2–3 kHz formant + saturation), a barrel drum (synthesised tabla model, lower and drier) and a struck drum (`toms`, `frame_drum`), a plucked lute with glides (`pluck('koto'|'shamisen', …)` with bend), tanpura drone (`pluck('shamisen', …)`, long t60, buzz), small cymbals (`nepal_bells`). Never imitate temple ritual music or a specific composition.
- **Foley by material**: kalam scratch on cloth (soft, fibrous noise), brush on wet cotton, dye bath (deep slosh), river water, cloth slapped on stone, wringing, wind on drying cloth, birds by a river.
- **Silence**: the pen lifted; water drips only.
- **Voice**: a storyteller reading captions, calm; Hindi or Telugu narration fits. Music ducked ~8 dB under voice; −14 LUFS.

## 8. Native moves

- **Mordant reveal.** Something invisible is painted; only the dye bath shows what it was. *Fits content like:* a hidden plan; a policy's effect appearing later; a seed's work underground.
- **Registers.** A story laid out in bands of panels; the camera reads like a viewer walking along. *Fits content like:* a company history; steps of a recipe; a trip day by day.
- **The wash.** The cloth is washed and what is not fixed fades away. *Fits content like:* separating fact from rumour; testing; what survives time.
- **Overdye.** A second dye over a first makes a new colour (yellow over indigo = green). *Fits content like:* two ideas combined; a merger; mixing cultures.
- **Block repeat.** One carved motif stamped into a pattern that grows. *Fits content like:* mass production; a habit; a movement spreading.
- **Caption and scene.** A panel's caption is written as its scene is drawn. *Fits content like:* labelled steps; a museum piece; a documentary chapter.

## 9. Pitfalls of the medium

- Opaque, perfectly flat colour reads as vector art → transparent dye, anisotropic feathering, thread-level unevenness.
- Brush strokes or watercolour blooms → dye fills follow masks, not strokes.
- Lines too uniform → curvature-driven width, capillary halo, starvation.
- Red that fades in → red develops from the mordant in the bath.
- Panels without borders lose the narrative structure → border bands and caption strips.
- Too many hues → five dyes, green only as overdye.
- **Sacred narratives as decoration.** Many cloths tell temple epics and depict deities: do not use deities or sacred episodes as ornament or for a product. Do not present a code-made film as authentic handmade kalamkari; for commercial work, credit or consult kalamkari artists.

## 10. Engine

No demo engine yet (draft). A first demo should build:
- `cloth.js`: `weave(seed, w, h)`, `folds(t)`, the subtractive composite `dyeComposite(layers, wash)`.
- `kalam.js`: `kalamStroke(pts, {pressureFromCurvature, halo, starve, seed})`, `ornament(path, kind)`.
- `dye.js`: `mordantMask`, `resistMask`, `develop(mask, dye, p)`, `wash(p)`, `overdye`, `blockStamp(motif, grid, seed)`.
- `panels.js`: registers, border bands, caption strips, `render(t)`.

Start from `styles/risograph/demo/riso.js` (`makeRiso`: subtractive layer composite, ink unevenness), `styles/watercolor/demo/engine.js` (`mk`, `drawS`, `withSeed`, sprite cache), `styles/ukiyoe/demo/print.js` (`fibers`, `stampLayer`, `bokashi`), `styles/one-line/demo/ink.js` (ink line), `core/lib.js`, `core/render/`, `core/audio/sampler.py`, `core/audio/pluck.py`, `core/audio/sfx.py`.

## 11. Variation space

You decide the panels, the captions, which dye stages are shown, freehand or block-printed, the opening, the ending, the camera path and the pacing.

- Structures: **one cloth read end to end** (registers as chapters); **the making** (the same panel shown at each process stage, the story told in parallel); **block-printed repeats** (one motif multiplies into a field that becomes the subject).
- Openings: **bare cloth in water**, myrobalan-tinted; **the kalam's first line** across empty cream; **a finished cloth drying in wind**, then into its first panel.
- Endings: **the last caption written**; **the final wash**, colours settling as the water clears; **the cloth folded** away into a stack of others.

---

Status: **draft** — no demo film yet. Before this is used as a library style it needs a demo film, `DEMO.md`, stills and the checks in the Lemo-Opuscar `MAINTAINING.md` ("Gates").
