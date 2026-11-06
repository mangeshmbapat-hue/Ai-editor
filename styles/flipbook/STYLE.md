# Flipbook — Style Prompt

> Pencil drawings on the corners of a notebook or pad, one drawing per page, brought to life by a thumb flipping the pages: graphite lines that boil because every page is a new drawing, paper that changes with every frame, and a flip rhythm that speeds, stutters and stops.
> References (grammar only): the kineograph (the flip book patented in 1868) and the long tradition of margin doodles in school notebooks; pencil animation tests on punched paper (rough lines, construction marks, timing charts). Never copy a published flip book or a known character, and never name the references in the film.

## 1. Essence, and what it is not

- **One page = one frame.** Each frame is a separate sheet with its own drawing, its own paper grain and a slightly different position: registration drifts and corrects.
- **Graphite on cheap paper**: grey pencil lines with pressure, smudges, eraser ghosts, ruled lines or squared paper, a margin, a page number.
- **Show-through**: the next drawing ghosts faintly through the thin page before it arrives.
- **The thumb is the clock**: playback speed varies (a catch at the start, a run in the middle, a slowdown at the end); the pad can flip back.
- **Economy**: doodle-simple figures; the joke and the feeling come from timing and a few lines.

Not Crayon Picture Book (wax colour on one page drawn live), not Urban Sketch · Pen & Wash (ink and wash drawn from observation on one sheet), not Whiteboard Explainer (marker drawn live by a hand on a board), not 1930s Rubber Hose Cartoon (inked cels, painted backgrounds). Here every frame is a different piece of paper.

## 2. Materials & rendering

- **Page view** (full frame is one page corner): per page index `i`, a fresh paper texture seeded by `i` (grain, fibres, a faint fold), ruling with a per-page offset (±1–2 px), and a registration jitter of the whole page (translate ±2–4 px, rotate ±0.3°) that the drawing shares.
- **Pencil engine**: graphite strokes that deposit on paper tooth peaks (pressure decides how much tooth fills), slightly lighter at stroke ends, layered darker where strokes cross; construction lines in a lighter grade under the final line; smudges as blurred graphite at 5–10 % opacity.
- **Each page is redrawn**: line positions boil by 0.5–2 px per page from a per-page seed; held poses are retraced, so even stillness boils.
- **Show-through**: the next page's drawing multiplied at 3–8 % under the current page, not mirrored; the eraser ghost of earlier attempts at 4–8 % on the same page.
- **Physical view** (three.js): the pad on a desk, pages as strip meshes bending around the binding with a monotonic curl `bend(i, t)` driven by thumb release; each page's texture comes from the same page renderer; motion blur by temporal supersampling on the flipping pages only; desk lamp and soft shadows.
- **Determinism**: `page(t) = floor(F(t))`, where `F` is the integral of a thumb-speed curve; every page's paper, jitter and boil is seeded by its index.

## 3. Colour logic

- **Graphite grey on paper**: the paper colour (white, cream, yellow legal pad, sticky-note yellow) is the neutral; graphite from light grey to soft near-black.
- Ruled lines in pale blue with a red margin, or grey squares; they stay quieter than the drawing.
- **One accent**: a red pencil, a blue ballpoint or a highlighter stroke, reserved for one element or one moment.
- Coloured pencil only in hatching, never flat digital fills.
- Example: paper `#f5f1e6`, rule `#a9c4dc`, margin `#d97a72`, graphite `#4a4a4d` to `#1f1f22`, accent `#d2412f`.
- Example: sticky note `#f6e27a`, graphite `#3d3b36`, accent ballpoint `#2c4fa8`.

## 4. Type & subtitles

- **Lettering is handwriting**: Caveat or Kalam rendered through the pencil engine (graphite texture, pressure); Kalam also carries Devanagari. Titles on the pad's cover label or on the first page; page numbers in the corner in small handwriting.
- **Subtitles**: Kalam 34–40 px in dark graphite on a paper-coloured halo at the bottom, or on a torn sticky-note strip; Kalam or Hind for Devanagari. Steady, never boiling. Two lines max.
- Hold each subtitle ≥ max(1.8 s, speech + 0.6 s).

## 5. Motion quality

- **24 fps output; pages advance at the thumb's rate**: typically 10–16 pages per second, so pages hold for 1–3 output frames, unevenly.
- Starts stutter (pages catching), the middle runs smooth, the end slows; a flip back plays pages in reverse.
- Drawn timing is broad: big key poses, few in-betweens, simple arcs, a held drawing retraced for stillness.
- Registration drift accumulates over a few pages, then jumps back (the artist realigned).
- **Appear** by being drawn across consecutive pages (a line grows page by page); **disappear** by being erased (ghost remains) or leaving the corner.
- **Never moves**: in page view, the page edge and binding stay within ±1 px; the pad's frame is the reference.

## 6. Camera grammar

In page view the camera is the reader's eye, locked on the corner; camera moves must be drawn. In physical view it is a macro lens at the desk. Opening and ending come from the topic.

| Move | What it expresses | Can serve |
|---|---|---|
| Locked page view | Pure animation, the doodle's world | a gag; a short life; a chase |
| Drawn pan (the background slides page by page) | Travel inside the drawing | a run; a journey; a race |
| Macro side view of pages flipping | The machine of the illusion | a making-of; a moment slowed; a rewind |
| Top-down on the open pad, thumb lifting a page | Anticipation | a reveal; a decision; a next chapter |
| Pull back from the corner to the whole page | Context around the doodle | the lesson being ignored; a diary; a margin |
| Freeze on one page held open | A single frame examined | a key moment; a mistake; evidence |

Framing: the drawing lives in the corner region; text, ruling and margin around it are part of the world. Transitions: the pad flips past its last page, flips back, a page is torn out, a new pad is picked up, cut between page view and physical view; no crossfades.

## 7. Sound palette

- **Lo-fi and playful**: `ukulele`, `upright` piano or `honky_tonk`, `glockenspiel`, `xylophone`, `woodblock`, `kalimba`, whistled melody via `flute` or `ocarina`, a kazoo approximated with a sawtooth through a nasal formant.
- **The flip is the rhythm**: a paper flutter where each page release is a tiny click (band-passed noise impulse), so click rate = page rate; it slows, speeds and stops with the thumb.
- **Foley**: pencil scratch (filtered noise with pressure envelope), eraser rub, page tear, pad slapped on a desk, a sharpener.
- **Silence**: the pad held still; one pencil tap.
- **Voice**: casual and close, a student or a narrator; music ducked ~8 dB under voice; final −14 LUFS.

## 8. Native moves

- **Thumb time.** Slow motion, rewind and stop happen by changing the thumb's speed. *Fits content like:* a replay of a goal; a regret revisited; a decision reconsidered.
- **Show-through foreshadow.** The next drawing is faintly visible before it arrives. *Fits content like:* a threat approaching; a surprise half-seen; a future that can be guessed.
- **Margin escape.** The doodle walks out of the corner onto the page's text, ruling and holes. *Fits content like:* boredom in a lecture; a character breaking free; a daydream taking over.
- **Erase ghost.** An erased drawing stays faintly under the new one. *Fits content like:* a deleted plan; a past relationship; a correction.
- **Last page.** The story ends because the pad runs out. *Fits content like:* a deadline; a life span; a battery dying.
- **Getting better.** The drawing improves or degrades over pages. *Fits content like:* learning a skill; a long illness; a country's history.

## 9. Pitfalls of the medium

- Smooth digital tweening → every page a fresh seeded drawing with jitter and boil.
- Boil so strong it buzzes → cap at 2 px on main lines; subtitles steady.
- Even playback reads as a video → a thumb-speed curve with catches and slowdowns.
- Clean vector lines → graphite deposited on tooth, pressure, smudge, construction lines.
- Pages intersecting in the physical view → monotonic bend per page, layer offsets.
- Show-through too strong → muddy pages; keep it ≤ 8 %.
- Ruling moiré → rules ≥ 2 px and anti-aliased, world-anchored to the page.

## 10. Engine

No demo engine yet (draft). A first demo should build:
- `pencil.js`: graphite strokes with pressure and tooth adhesion; start from the stroke engine and per-two-frame boil in `styles/crayon-book/demo/crayon.js` and the adhesion shader in `styles/crayon-book/demo/gl.js`, with a finer tooth and grey pigment; hand wobble ideas from `styles/urban-sketch/demo/engine.js`.
- `page.js`: per-page paper, ruling, registration jitter, show-through and eraser ghosts (`pageCanvas(i)`).
- `flip.js`: thumb-speed curve and `page(t)`, plus a page-click event list for the flutter sound via `core/render/events.mjs`.
- `pad3d.js`: three.js pad with bending page strips, desk and lamp; paper canvases after `styles/paper-popup/demo/paper.js`, post from `styles/paper-popup/demo/post.js` or `core/three/post.js`.
- `mix.py`: flutter, pencil and eraser foley via `core/audio/sfx.py`, music via `core/audio/sampler.py`, voice via `core/tts/tts.py`.
Seeds from `mulberry` and `hash` in `core/lib.js`; render with `core/render/video.mjs`, `srt.py`, `mux.sh`.

## 11. Variation space

You decide the pad and paper, the drawing's skill level, the accent, page view or physical view or both, the thumb's rhythm, the opening and the ending.

- Structures: **one gag in one pad** (a single action told across a hundred pages); **several pads** (each pad a chapter, picked up and flipped in turn); **a school year** (the doodle evolves through the margins of one notebook).
- Openings: **the closed pad** on a desk and a thumb bending its corner; **page one**, a single dot that starts to move; **a flip already running**, caught mid-chase.
- Endings: **the last page**, with the figure looking at the blank cover; **flipped back** to the first page; **a page torn out** and kept while the pad is closed.

---

Status: **draft** — no demo film yet. Before this is used as a library style it needs a demo film, `DEMO.md`, stills and the checks in the Lemo-Opuscar `MAINTAINING.md` ("Gates").
