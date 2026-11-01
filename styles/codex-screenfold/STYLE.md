# Codex Screenfold — Style Prompt

> A folded book of painted deerskin opens panel by panel: figures with heavy even outlines and flat mineral colours on a white gesso ground, read along red guide lines that zigzag across the folds, with footprints for journeys, dots for numbers and name signs tied to each person.
> References (grammar only): Mesoamerican screenfold books, especially the Mixtec (Ñuu Savi) historical-genealogical codices of Oaxaca (deer hide coated in white gesso, folded like a screen, read in a meander along red lines, place signs, name signs, footprints, day signs with dot numerals) and the painting tradition shared with Nahua and Maya books; living Mixtec, Nahua and Maya communities keep this heritage. Never copy a known codex page, deity, calendar or lineage, and never name them in the film.

## 1. Essence, and what it is not

- **A physical screenfold**: one long strip folded into equal panels; opening it is the camera's main act, and a scene may run across a fold.
- **Heavy, even outlines and flat colour**: black contour of constant width (no taper), flat fills, no shading, no horizon. Heads are large; bodies are assembled from standard parts.
- **Reading paths**: thin red lines divide each panel into bands, and the reading turns at each band end like a plough (left to right, then right to left), so the eye snakes down the book.
- **Signs instead of words**: a person carries a small name sign tied by a thin line; a place is a hill sign with a feature; travel is a row of footprints; speech is a curl from the mouth; counts are dots.

Not Paper Pop-up Book (nothing stands up; the book only folds flat). Not Pictogram Motion (no modern icons, no information grid; figures are dressed people with names). Not Egyptian registers or a frieze (the reading path meanders and crosses folds; the book itself moves).

## 2. Materials & rendering

- **The book** (three.js): N panels (portrait, ~1 : 1.15), each a thin box (gesso face, hide edge), hinged to its neighbours at alternating mountain and valley folds. Opening is a chain of hinge angles driven by one parameter; panels sag slightly (a 2–3 % bend via vertex shader), edges curl a little, folds show a crease shadow.
- **Hide and gesso**: the panel texture is gesso white with fine cracks (a Voronoi crack net, sparse), worn edges showing tan hide, rubbed corners, small losses; a height map for the cracks and the paint's slight relief.
- **Paint layer**: drawn in 2D on each panel canvas: flat fills first, then the black outline on top at constant width (6–10 px at 1080p page height), with 0.5 px wobble and slightly darker overlaps where outline strokes meet. Colours have a chalky, matte surface (roughness ~0.85), the outline a touch glossier.
- **Figure kit**: head with a large eye, nose and open mouth in profile; headdress and hair as separate parts; torso, kilt or skirt, cape; limbs in a few set poses (stand, walk, sit, point, offer, carry). Bodies are built from parts, not drawn freely.
- **Sign kit**: hill (place), water band, footprint, speech curl, dots, a mat, a path line, and a growing library of invented name signs (animal, plant, object + a dot count).
- **Light**: a reading-table key, soft fill, a dark wood or cloth surface; DOF when close.
- Seeds are per panel; repainting re-uploads only that texture.

## 3. Colour logic

- **5–7 flat colours on white gesso**: red, a strong blue, yellow, green, black (outline), brown or ochre, sometimes a pale pink or orange. No gradients, no tints except a single lighter version.
- **Red does two jobs**: guide lines and one category of meaning (a dress, a path, a sign). Keep it the most frequent colour after black.
- **Gesso is the light.** Keep at least 35 % of a panel white so figures read.
- Colour identifies, as in a code: one person keeps the same cape colour and name sign through the whole book.
- Example: gesso `#efe7d4`, red `#b4302a`, blue `#2f6f9e`, yellow `#e0b23c`, green `#5a8a4a`, ochre `#a46a3a`, outline `#1b1612`, hide edge `#b9905e`.

## 4. Type & subtitles

- **Inside the book there is no alphabet.** Names, places and numbers are signs. If a label is essential, it goes on a small paper slip laid on the table, never painted into the codex.
- **Subtitles** sit on the table below the open book: **Mukta** 600, 36–44 px, warm white on the dark surface, a thin red rule above, two lines at most. Mukta also carries Devanagari, so Hindi subtitles keep the same face and size. Hold ≥ max(1.8 s, speech + 0.6 s).
- Titles: a panel painted with one large sign composition plus the title set in **Mukta** ExtraBold on the table, or on the book's cover board.
- Numbers are dots inside the book; digits only in subtitles.

## 5. Motion quality

- 24 fps. **Book, camera and light on ones**; **figures on twos**, but sparingly: a codex figure mostly holds a pose. Motion is the reading path.
- **Opening**: hinge angles eased (`eio`) with a small overshoot and settle (~0.4 s) as each panel lands flat; a soft paper-and-leather sound on each landing.
- **Paint-in**: fills appear area by area, then the outline is drawn along each contour at a steady pen speed; a name sign attaches with its tie line last.
- **Footprints** print one by one along the path at walking rhythm; a figure may slide along the prints in two or three held poses.
- **Dots count**: dots appear one per beat, the voice counting.
- Never moves: the red guide lines, a finished panel's paint, the gesso cracks.

## 6. Camera grammar

A reader's camera over a table. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Overhead on the book as panels unfold | the account opening step by step | a lineage; a migration; a treaty |
| Track along the meander, panning with the reading | following one path through events | a journey; a negotiation; a recipe |
| Low raking angle along the folded strip | the book as an object | a record kept; heritage; the archive |
| Push to one name sign | identity | a person introduced; an heir; a signature |
| Pull back to the whole open strip | the full span at once | a family tree; a map of places; a summary |
| Turn the book over (reverse side) | another side of the story | a second voice; what happened meanwhile; a secret |
| Hold while dots count | measured time | dates; quantities; a tribute counted |

Framing: the reading line stays roughly horizontal on screen; a fold never splits a figure's face; subtitles stay on the table. Transitions: a panel unfolding, the book flipped, a fold closing, a pan along the path; no crossfades.

## 7. Sound palette

- **Instruments**: clay flutes (`ocarina`, `recorder`, `flute` breathy), slit and log drums (`log_drum`, `woodblock`), frame drum, rattles (`shaker`), conch-like horn (a `horn` with a slow pitch rise and noise), a low drone. Nothing claims to be reconstructed pre-Hispanic music.
- **Foley from the book**: deerskin folds (soft leather flex), panels landing (padded tap), a brush on gesso (dry scratch), the table, fingers turning.
- **Story sounds** small and spaced: footsteps on dry ground, wind, water.
- **Silence**: only the book; a fold closing is a full stop.
- **Voice**: an elder reciting a record: names, places, dates. Music ducked ~8 dB; −14 LUFS.

## 8. Native moves

- **The unfold.** A folded book opens panel by panel, each new panel a new event. *Fits content like:* the steps of a process; generations of a family; a city's growth.
- **Footprint path.** Prints march from one place sign to the next across a fold. *Fits content like:* a commute; a trade route; a parcel's delivery.
- **Name sign.** A sign attaches to a figure by a tie line and identifies them for the rest of the film. *Fits content like:* a team introduced; characters in a legal case; species in a survey.
- **Dot count.** Dots fill, one per beat, to make a number. *Fits content like:* days of a drought; votes; a price.
- **Meander reading.** The camera snakes along red lines, back and forth down a panel. *Fits content like:* a decision tree; a board game; a negotiation.
- **Two faces.** The strip is turned over to show the other side. *Fits content like:* two accounts of one event; before and after; the hidden cost.

## 9. Pitfalls of the medium

- **Deities, calendar signs and ritual scenes used as decoration** → these are sacred to living Mesoamerican peoples; build invented daily-life signs, and consult Mixtec, Nahua or Maya scholars and artists for any film about them.
- **"Aztec" clichés** (sacrifice, gold, pyramids) → keep to the grammar of record-keeping and journeys.
- **Tapered or calligraphic outlines** read as another tradition → constant-width outline.
- **Shading and perspective** break the flat sign world → flat fills, events instead of views.
- **Folds slicing faces** → plan layouts so folds fall between figures.
- **Too much text in the book** → signs inside, words only on the table.
- **Presenting it as a genuine codex** → credit it as a code-made book; never imitate a museum codex or invent "ancient prophecies".

## 10. Engine

No demo engine yet (draft). A first demo should build:
- `book.js`: screenfold strip, alternating hinges, `open(u)` driving all hinge angles, sag and crease shadows, flip to reverse.
- `page.js`: gesso and hide texture, crack net, wear; one canvas per panel, re-uploaded on change.
- `paint.js`: flat fill then constant-width outline, paint-in order, `paintIn(panel, u)`.
- `signs.js`: figure parts and poses, place, footprint, speech, dots, tie lines, invented name signs; `path.js`: red guide lines and the meander reading path for the camera.

Start from `styles/paper-popup/demo/book.js` (pages hinged in three.js, paper textures), `styles/paper-popup/demo/paper.js` (canvases, paper fill, grain), `styles/paper-popup/demo/post.js` and `core/three/post.js` (DOF, AO), `styles/stained-glass/demo/glass.js` (`voronoi` for the gesso cracks, smooth polygons), `styles/papercut-red/demo/rig.js` (parts on an affine rig), `core/lib.js`.

## 11. Variation space

You decide what the book records, the panel count, which signs the film invents, the colour code for people, the table and light, and whether the book is new or old.

- Structures: **a lineage** (one couple per panel, descendants spreading across folds); **a route** (footprints from one place sign to the last, panels as stages); **a ledger of seasons** (each panel a season, dots counting harvests).
- Openings: **the folded book** closed on the table, one panel lifted; **a footprint** in close-up, pulled back to the path; **a blank gesso panel** being painted.
- Endings: **the book folds shut**; **the strip turned over** to a blank reverse; **the last panel left half-painted**, outline only.

---

Status: **draft** — no demo film yet. Before this is used as a library style it needs a demo film, `DEMO.md`, stills and the checks in the Lemo-Opuscar `MAINTAINING.md` ("Gates").
