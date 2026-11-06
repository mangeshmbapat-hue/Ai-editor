# Mughal Miniature — Style Prompt

> An album page that comes alive: a jewel-bright scene in fine opaque colour, its ground tipped up so everything is seen at once, framed by rules and gold-illuminated margins; the camera leans in like a viewer with a magnifier and finds ever finer brushwork and smaller events.
> References (grammar only): the painting of the Mughal court workshops of the 16th–17th centuries, made in opaque watercolour on layered, burnished paper with very fine brushes, mineral pigments and shell gold, mounted in albums with illuminated margins (*hashiya*) and ruled borders; its court, garden, hunt and natural-history pictures and its blend of Persian, Indian and European elements. Take the stacked viewpoint, the fineness, the margins and the album; never copy a specific painting, portrait or calligraphy, and never name them in the film.

## 1. Essence, and what it is not

- **Stacked, tipped-up space.** Ground rises to a high horizon; carpets, pools and beds seen from above, walls from the front, people in profile, all in one picture. Farther is higher, barely smaller.
- **Fineness everywhere**: single-hair contours, patterned textiles, individual leaves, eyelashes; closer looks always find more.
- **Jewel colour**: lapis blue, malachite green, vermilion, orpiment yellow, lead white, with shell gold, flat and opaque, modelled only by fine stippling and hatching.
- **The page is the frame**: the picture sits inside coloured and gold rules, on a wide margin of tinted paper illuminated with gold flowers, plants or animals.
- **Calm, observed life**: many small figures each doing one thing; a garden, a hunt, a single bird studied alone.

Not Ukiyo-e (no woodblock, key line or bokashi; colour is painted and finely modelled), not Isometric Picture Book (no isometric grid, no type on the ground; each object keeps its own most readable view), not Watercolor Brush (opaque, burnished, gold; no wet strokes), not Pichwai (no dark dyed cloth or repeated rows; one observed scene).

## 2. Materials & rendering

- **Page**: burnished cream picture paper (very fine grain, faint sheen) mounted on tinted margin paper (buff, pale blue, pink) with sprinkled gold; slight age toning. Cached, world-anchored.
- **Rules (jadval)**: 4–8 thin lines (gold, blue, red, white, black, 0.6–2 px) and an inner gold band; a tree or rider may break across them.
- **Margin illumination**: plant sprays and animals in shell gold (granular fill, darker gold outline), seeded layout.
- **Stacked projection**: each element in its own canonical view (top view for floors, carpets, water, beds; elevation for architecture; profile or three-quarter for figures), placed by depth `d`: `y = yBase − H·d^0.8`, scale `1 − 0.25·d`. A high horizon (top 10–20 %), a graded sky, pale hazy distant hills.
- **Paint**: flat opaque fills with pigment grain; fine stipple and 0.5 px hatching on faces, rocks and folds only; contours 0.5–1.2 px in a darker hue, never heavy black.
- **Detail by zoom**: each element owns seeded detail layers (textile patterns, leaf veins, jewellery, lashes) drawn only above a zoom threshold, cached per level, so pushes reveal new marks without flicker.
- **Gold**: shell gold, granular, a micro-noise sheen from a slow light. The page is a Canvas 2D scene graph; everything is a pure function of t.

## 3. Colour logic

- **Jewel hues** at full strength on cream, balanced across the page so no one hue dominates; 6–9 hues plus gold and white.
- **Value**: the picture is mid-to-light; darks are small (hair, outlines, shadows of doorways). The sky may grade from deep blue to pale at the horizon; distance fades to blue-grey; nothing else is a gradient.
- **Gold** is reserved for margins, rules, textiles, ornaments and highlights in the sky; it never floods a figure.
- **White** for pearls, jali screens, marble and cloth folds.
- Example: lapis `#2a4b9b`, malachite `#3f8a5a`, vermilion `#d0432c`, orpiment `#e6b83a`, lead white `#f4efe2`, pink `#e8a0a0`, rose margin `#e9cfc4`, gold `#c9a24c`, ink `#3a2a20`.

## 4. Type & subtitles

- Text sits where an album puts it: a **calligraphy cartouche** (gold-ruled panel above or below the picture) or the **lower margin**, dark ink, no box.
- Urdu or Persian: **Noto Nastaliq Urdu**, only with real text supplied by the film. Latin: **EB Garamond** or **Cormorant Garamond** (36–44 px) for subtitles, **Playfair Display** italic for titles (70–110 px). Devanagari: **Tiro Devanagari Hindi**. Hindi subtitles are supported.
- Subtitles fade in 0.3 s within the margin band; never cover the picture field. Hold each ≥ max(1.8 s, speech + 0.6 s).

## 5. Motion quality

- **24 fps**; figures on twos (12 fps) with small, precise acting (a head turn, a raised hand, a falcon lifting); several small events at once in one tableau.
- Riders and animals cross the tipped plane on climbing paths, scaled only by the stacked rule; water flows as fine line patterns; leaves stir ±1°.
- **Painting stages** may show: red-brown underdrawing → tinted drawing → flat colour → modelling → gold → burnish (layers revealed with `ss`). Camera slow and eased (`eio`).
- Never moves: the rules and the margins, except when a page turns.

## 6. Camera grammar

A page held under a lamp, with a magnifier: the camera reads, climbs and leans in.

| Move | What it expresses | Can serve |
|---|---|---|
| Whole page with margins, locked | an object in an album | a chapter; a document; a summary |
| Push through the rules into the picture | entering the scene | the start of a story; a case; a place |
| Vertical climb up the tipped ground | moving into the distance, or forward in time | a journey; a sequence of events; a hierarchy |
| Magnifier push to a tiny detail | hidden fineness | the decisive clue; a craftsman's care; a small life |
| Lateral pan across a crowded scene | many lives at once | a court; a market; a workplace |
| Slide along the gold margin | commentary beside the main event | context; a parallel story; footnotes |
| Page turn to the facing page | a new entry | a new chapter; a contrast; calligraphy and image |

Framing: rules visible in wides; in pushes, one clear subject and its neighbours. Transitions: a page turn; a push through a painted doorway into the next scene; the painting reverting to underdrawing and repainted as another. Forbidden: vanishing-point moves, depth of field, crossfades, lens effects.

## 7. Sound palette

- **Instruments as options**, in the manner of North Indian court music: a plucked lute with slides (`pluck('pipa', …)` with bend), a bowed voice with shimmer (`erhu` lowered, like a sarangi), a drone (`pluck('shamisen', …)`, long t60, buzz), `flute`, `frame_drum`, dry ceremonial kettle drums (`timpani`, short), `nepal_bells`. Never imitate a specific composition.
- **Foley by place**: fountains, songbirds (synthesised), wind in trees, robes, horses and hounds, falcon bells, turning pages, a reed pen, burnishing on paper.
- **Silence**: the magnifier hovering; only a page's room tone.
- **Voice**: measured, literate, a chronicler; Hindi or Urdu narration fits. Music ducked ~8 dB under voice; −14 LUFS.

## 8. Native moves

- **The magnifier.** Each push reveals finer marks and a new small event. *Fits content like:* a fraud found in the details; a cell inside a leaf; a city's hidden trades.
- **Climb the page.** Moving up the tipped ground is moving forward or farther. *Fits content like:* a pilgrimage route; a career; a product's journey from farm to city.
- **Many things at once.** One page holds a dozen simultaneous events; the camera picks them in order. *Fits content like:* a day in a hospital; a festival; a supply chain.
- **Underdrawing to colour.** The scene reverts to its first fine lines and is painted again differently. *Fits content like:* a plan revised; a memory reconsidered; a draft to final.
- **Margin echo.** Gold animals and plants in the margin react to the picture's events. *Fits content like:* commentary; public opinion; nature responding.
- **Single study.** One bird or flower alone on the page, observed with care. *Fits content like:* a species profile; a product close-up; a person's portrait.

## 9. Pitfalls of the medium

- Vanishing-point perspective → stacked planes, each object in its own view.
- Heavy black outlines read as cartoon → fine contours in darker hues.
- Smooth gradient shading → stipple and hatch modelling, only where needed.
- Detail popping in at zoom → seeded LOD layers that fade in over 0.3 s.
- Fake calligraphy or invented script → real text in Noto Nastaliq Urdu, or none.
- Exotic clichés (harem fantasies, gilded "East") → observed, dignified life.
- **Sacred and historical material.** Albums include religious texts and portraits of saints and rulers: never use scripture, religious inscriptions or saints as decoration, and do not invent scenes for real historical people. Do not present a code-made film as an authentic miniature; for commercial work, credit or consult miniature painters working in the tradition today.

## 10. Engine

No demo engine yet (draft). A first demo should build:
- `page.js`: paper, margin tint, `rules(rect, lines)`, `marginIllumination(seed)`, `pageTurn(p)`.
- `stack.js`: the stacked projection `place(el, d)`, canonical views, horizon, sky and haze.
- `paint.js`: `fillOpaque`, `contour(path, w)`, `stipple(region, density)`, `fineHatch`, shell gold sheen.
- `lod.js`: per-element detail layers, `drawAt(zoom)` with seeded marks and fade-in.
- `film.js`: camera (magnifier pushes, climbs), tableau events, subtitles in margins, `render(t)`.

Start from `styles/engraving/demo/engine/burin.js` (`stipple`, `hatchAlong`, `outline`), `styles/ukiyoe/demo/print.js` (`fibers`, `fillPath`, `kasumi` haze, `cartouche`), `styles/art-deco/demo/engine/deco.js` (`goldGrad`, `rules`), `styles/watercolor/demo/engine.js` (sprite cache, `withSeed`), `core/lib.js`, `core/render/`, `core/audio/sampler.py`, `core/audio/pluck.py`, `core/tts/tts.py`.

## 11. Variation space

You decide the setting, the events on the page, the margin's creatures, how deep the magnifier goes, the opening, the ending, the camera path and the pacing.

- Structures: **one page, ever closer** (the story told by successive magnifier pushes); **an album** (each page a chapter, page turns between); **the climb** (one tall page read bottom to top as a journey).
- Openings: **a closed album** opening to its first page; **an extreme detail** (an eye, a bird's feather) pulled back to the whole page; **the underdrawing alone**, colour arriving as the story starts.
- Endings: **the page turns** to a blank one; **the magnifier withdraws** to the album on a table; **the margin's gold creatures** close around the picture.

---

Status: **draft** — no demo film yet. Before this is used as a library style it needs a demo film, `DEMO.md`, stills and the checks in the Lemo-Opuscar `MAINTAINING.md` ("Gates").
