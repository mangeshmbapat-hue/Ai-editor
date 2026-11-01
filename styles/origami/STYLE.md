# Origami — Style Prompt

> Single sheets of paper folded into every shape on screen: flat facets with crisp creases, coloured on one side and white on the other, and transformations that happen by folding and unfolding, never by morphing.
> References (grammar only): the Japanese paper-folding tradition and its traditional models (crane, boat, frog, balloon, cup); the diagram notation that grew from Akira Yoshizawa's system (valley fold dashed, mountain fold dash-dot, arrows for each action); the geometry of crease patterns and flat-folding. Never copy a modern designer's model or diagrams, and never name the references in the film.

## 1. Essence, and what it is not

- **Every object is one folded sheet.** Planar facets meet at sharp creases; light changes facet by facet as folds move.
- **Two-sided paper**: colour outside, white inside; the white shows whenever a fold opens or a flap turns.
- **Change by folding**: shapes transform through rotations about crease lines; unfolding leaves crease scars that stay on the sheet.
- **Paper physicality**: thickness at edges, layered flaps, slightly soft creases, fibre texture, small gaps where layers do not meet.
- **Soft studio light** with a rim: facets read as 3–4 clear values.

Not Paper Pop-up Book (cut card hinged on a book page, printed art, a book in a room), not Low-poly Isometric Island (flat-shaded CG with no paper, no folds, no white reverse), not Red Paper-cut (cut, flat, front-lit motifs), not Paper-cut Lightbox (stacked cut sheets lit from behind).

## 2. Materials & rendering

- **Model**: a crease graph (vertices, faces, creases with target fold angles) on a square or rectangular sheet. Simple sequences fold as a hinge hierarchy: groups of faces rotate about a crease axis by an angle `θ(t)`.
- **Collapses** (many creases at once, e.g. a squash or a bird base) are solved offline: a compliant solver drives fold angles toward targets while keeping edge lengths and face planarity, baked per frame to vertex positions (morph targets). Bake once; render reads the bake.
- **Layers**: each face carries a layer index; offset by paper thickness (0.1–0.3 mm at model scale) plus polygon offset so stacks never z-fight; show thickness on exposed edges as a thin lighter strip.
- **Creases**: replace each hard crease with a narrow strip (fold radius ~0.3–0.6 mm) whose normals interpolate, so ridges catch a fine highlight and valleys get a soft dark line (GTAO helps).
- **Crease scars**: unfolded creases persist as a normal and roughness map that accumulates over the film.
- **Paper material**: `MeshStandardMaterial`, front colour and white back (`side` split or two meshes), roughness 0.8–0.95, fibre noise in albedo and normals (smooth kami or long-fibred washi), optional slight translucency when backlit.
- **Set**: a plain surface (grey board, wood, a large white sheet as sky) in real units; key softbox, rim light, low HDRI; DOF, GTAO and grade from `core/three/post.js`.
- Diagram overlays (dashed valley lines, dash-dot mountain lines, arrows) are drawn in screen space only when the film teaches a fold.

## 3. Colour logic

- **One sheet = one colour** on its front, white on its back. A scene holds 3–5 sheet colours.
- **The neutral** is the ground (grey board or white paper); everything else is a sheet.
- **One accent sheet** (vermilion, a deep blue, or a patterned print you generate) reserved for the hero or the meaning.
- Facets give each sheet 3–4 values; no gradients painted on, no outlines.
- Patterned papers must be original procedural patterns, not copied prints.
- Example: ground `#d9d6cf`, sheets `#2f6d8f`, `#e2b13c`, `#5e8c5a`, accent `#d2452f`, reverse `#f6f2ea`.

## 4. Type & subtitles

- **Titles are paper**: printed on a sheet that folds into or out of view, or built from folded strips; set in Cormorant Garamond, Space Grotesk or Inter; Devanagari in Noto Sans Devanagari or Hind.
- **Fold labels** (when teaching) use the diagram language: step numbers, short labels in Space Grotesk 20–28 px, dashed and dash-dot lines, arrows.
- **Subtitles**: Inter or Space Grotesk 32–38 px in near-black on a narrow white paper strip at the bottom, or cream with a soft shadow on dark scenes; Devanagari in Hind or Noto Sans Devanagari. Two lines max.
- Hold each subtitle ≥ max(1.8 s, speech + 0.6 s).

## 5. Motion quality

- **24 fps, folding on ones**; a stop-motion variant may step on twos for the whole film.
- A fold has a physical arc: slight pre-bend (anticipation), acceleration (`eio`), a crisp landing and a small spring-back (overshoot 3–5° then settle with `spring`).
- **One fold per beat** reads; collapses are saved for peaks.
- Paper never stretches and never bends between creases, except a deliberate gentle curl on a large flap.
- **Appear** by folding out of a flat sheet; **disappear** by unfolding flat or folding small and sliding away.
- **Never moves**: the ground; faces not involved in the current fold stay rigid.

## 6. Camera grammar

A tabletop camera, often near the paper. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Top-down diagram view | Instruction, clarity | a process; a recipe; a method |
| Orbit around a finished model | Admiration, completeness | a product; an achievement; a gift |
| Follow a flap's edge as it swings | The action itself | a decision; a turning point; a transformation |
| Low hero angle on a model | Character and dignity | a creature; a building; a person |
| Push into a pocket or fold | Hidden structure | a secret; an inside story; a mechanism |
| Pull back from crease scars to the whole sheet | The history of a shape | a career; a city plan; a lifetime |

Framing: keep the active fold line and the moving flap in frame; leave paper-white or ground space for subtitles. Transitions: a sheet folding over the lens, unfold-to-next (a model unfolds into the next model's crease pattern), a flap closing past the camera, a cut on a completed fold; no crossfades or digital morphs.

## 7. Sound palette

- **Sparse and plucked**: `harp`, `marimba`, `kalimba`, `glockenspiel`, `hand_chimes`, `piano`, `flute`, music box via `pluck('music_box', …)`, `koto` via `pluck('koto', …)` used sparingly so the film does not lean on cliché.
- **Paper foley**: crease snap (short broadband crack with a crackle tail), flap swish, slide on the table, a sheet laid down, unfolding rustle; each fold event exported from the page and voiced from `core/audio/sfx.py` building blocks (`bp`, `noise`, `click`).
- **Silence**: one crease in an empty room.
- **Voice**: calm, precise, a teacher or a quiet narrator; music ducked ~8 dB under voice; final −14 LUFS.

## 8. Native moves

- **Fold into being.** A flat square becomes the subject in a few clear folds. *Fits content like:* a product assembled; an animal born; a house built.
- **Unfold to the crease pattern.** A model opens flat and its scars form a map. *Fits content like:* a life story as lines; a city plan; the hidden logic of a design.
- **White reveal.** Turning a form inside out shows the white reverse. *Fits content like:* a change of heart; the truth behind a front; winter arriving.
- **Collapse.** Many creases fold at once into a new form. *Fits content like:* a sudden insight; a market crash; a creature waking.
- **Modular assembly.** Identical folded units slot together. *Fits content like:* a community; a molecule; a team.
- **Action model.** Pulling a tail flaps wings, pressing a back makes a frog jump. *Fits content like:* a mechanism; cause and effect; a toy explained.

## 9. Pitfalls of the medium

- Stretching or interpenetrating faces (a morph look) → rigid faces, edge-length checks in the bake, layer order per face.
- Z-fighting in stacks → thickness offsets and polygon offset per layer.
- Clean low-poly CG → fibre texture, rounded creases, visible thickness, white reverse, soft light.
- Unfoldable or impossible models → use traditional models, original designs checked in the solver, or simple hierarchical sequences.
- Too many folds per shot → one fold per beat, with optional diagram arrows.
- Copying a modern designer's model → traditional public-domain models or original designs only.
- Tradition used as decoration → the crane and other folded forms carry meanings in Japan (wishes, remembrance); use them with care, credit the tradition, and do not present a code-made film as hand-folded work.

## 10. Engine

No demo engine yet (draft). A first demo should build:
- `fold.js`: crease graph, hinge hierarchy, `foldStep(axis, faces, θ)`, layer bookkeeping; the fold–unfold timing and camera ideas in `styles/papercut-red/demo/fold.js` (`camFold`, `drawFold`) are a 2D starting point.
- `solve.mjs`: offline compliant solver for collapses, writing baked vertex positions per frame.
- `sheet.js`: two-sided paper material, fibre texture, rounded crease strips, accumulating crease-scar maps; two-sided cut-paper materials and shadows from `styles/paper-popup/demo/cutmesh.js`, paper grain from `styles/paper-popup/demo/paper.js`.
- `notation.js`: valley and mountain lines, arrows, step numbers.
- `set.js`: real-unit table, softbox and rim; flat-facet material handling from `styles/lowpoly-island/demo/world.js`; post from `core/three/post.js` and `styles/paper-popup/demo/post.js`.
- `mix.py`: paper foley via `core/audio/sfx.py`, music via `core/audio/sampler.py` / `core/audio/pluck.py`, voice via `core/tts/tts.py`. Easing from `core/lib.js` (`eio`, `spring`, `back`).

## 11. Variation space

You decide the models, the sheet colours and paper type, whether folds are taught or simply happen, continuous or stepped motion, the opening and the ending.

- Structures: **one sheet, many lives** (the same square becomes five things, its scars accumulating); **a modular build** (unit after unit until a large form stands); **a folded town** (houses, boats and animals each fold up as the narrator names them).
- Openings: **a blank white square** dropping onto the table; **a crease pattern** on a flat sheet that starts to fold itself; **a finished model** that slowly unfolds to show how it began.
- Endings: **unfolded flat**, every scar visible like a map; **folded small** and set down among others; **an action model** that flaps once and stops.

---

Status: **draft** — no demo film yet. Before this is used as a library style it needs a demo film, `DEMO.md`, stills and the checks in the Lemo-Opuscar `MAINTAINING.md` ("Gates").
