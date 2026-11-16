# Style sheet: Vox paper cutout explainer

Slug `vox-paper-cutout` · family **documentary / collage** · learned from the owner's reference sample 1 (2026-11-16, 10.2 s WhatsApp clip, 16:9, English VO about Bill Gates). More owner samples are coming; this sheet is **sample 1 of N**, and anything marked *not seen yet* must be learned from a later sample, not guessed.

The last 4.1 s of the clip (6.13 s to the end) is the original creator's Instagram end card (dark overlay, logo, handle). It is not part of the style and was trimmed before measuring. Never copy it, the creator's handle or the Vox logo.

Status: **learned**. The Measured section is from FFmpeg. Every other section is Mann's observation from the frames and must be written before this sheet is used.

## Measured

- Source: 6.1s, 864x496, 30.0 fps, aspect 16:9
- Shots: 1 · shot length mean 6.1s, median 6.1s, range 6.1–6.1s
- Cuts per 10 s: 0.0 overall; per 10 s window: 0
- Hook: first cut at 6.1s · shots under 1 s: 0 · shots over 4 s: 1
- Palette: #eae2d8 (45%), #524b3c (18%), #f3c93f (12%), #968c76 (9%), #e2d4c0 (8%), #c9baab (8%)
- Luma mean 185.4 · saturation mean 0.21 · warmth (R−B) mean 41.6
- Loudness: -20.12 LUFS, true peak -4.71 dBTP, LRA 3.4
- Silences over 0.7 s: 0
- Speech rate: 2.48 words/s

## Targets for an edit in this style (machine-readable copy in style.json)

- Average shot 6.1s, cuts per 10 s 0.0, first cut by 6.1s
- Starting grade preset `warm-film` (check against the frames; adjust or build a LUT)

## Hook and structure

The scene is **built, not cut**: one 6.1 s shot in which the paper set is assembled layer by layer, back to front, while the VO speaks one sentence. Something new lands every 0.4 to 1.0 s, so the eye always has a fresh arrival.

Measured timeline of sample 1 (word times from Whisper; element times from 10 fps frames):

| Time | VO word | What arrives | How |
|---|---|---|---|
| 0.00 | (silence, -45 dB) | Paper background, beige cloud (top centre), blue torn-paper cloud (top right), scraps of handwritten letters and newsprint at the left and right edges | already on screen, no fade-in |
| 0.60–1.00 | "Bill" 0.78 | Tree cutouts from the bottom-right, then bottom-left corner | rise up from below frame, ~0.4 s, ease-out |
| 1.00–2.00 | "Gates" 1.54 | Big yellow torn-paper sun, centre, behind where the subject will stand | scales up from a dot to full size in ~1.0 s, ease-out |
| 1.75–2.90 | "was a young" | Bill Gates cutout, bottom centre-right, chest-up | bottom-to-top reveal with a straight horizontal mask edge, ~1.1 s |
| 3.10–3.90 | "computer enthusiast" 2.62/3.14 | Microsoft building cutout behind the subject, bottom-left | slides up diagonally from the bottom-left, ~0.8 s |
| 3.10–3.90 | "enthusiast" | "Bill Gates" name label, top centre, on a strip of torn cream tape | typewriter, one letter at a time, about 10 letters/s; the tape strip is there first |
| 3.80–4.50 | "with a big" | Brand sticker (yellow circle logo) with a small black "on" tag, top-left | 3D page-turn flip (rotateY on its right edge, back side shows mirrored), ~0.6 s |
| 4.40–4.70 | "big dream" 4.76 | Thin black ink line from the sticker to the name label | draws on along a curve, ~0.3 s |
| 4.70–6.10 | VO ends 5.22 | Hold of the finished collage | every layer keeps drifting 1–3 px and the trees sway (idle breathing); nothing is ever frozen |

Rules taken from this:
- **Images arrive slightly after the word, not on it.** The person's photo started ~0.2 s after "Gates" ended, and the building started ~0.5 s after "computer". Target: the visual for a noun starts 0.1–0.5 s after the word, so it reads as an answer to the VO.
- **Back to front.** Set (background, clouds, trees) first, then the colour shape behind the subject, then the subject, then context objects, then text, then the brand/connector. Text comes last, once the picture is built.
- **About one new element per 0.5–1 s** while the VO is talking; a 1–1.5 s hold after the sentence ends before the next scene.
- First 0.5 s: the paper world is already there (no black frame, no fade from black). First 3 s: the subject's face is fully up by 2.9 s.

## Cutting

No hard cuts inside a sentence. One scene = one sentence (or one idea), built as a single continuous shot. *Not seen yet:* how one scene changes to the next (sample 1 has only one scene). Learn it from the next sample before deciding it.

## Camera and framing

- A locked frame with no zoom or pan was measured over the 6.1 s. Movement comes from the layers, not the camera.
- 16:9 composition: subject chest-up, bottom centre-right, cropped by the bottom edge, taking ~45% of the frame height. Colour shape (sun) centred behind the head-to-shoulders area. Context object (building) bottom-left, overlapping behind the subject. Name label top centre. Brand sticker top-left. Trees frame both bottom corners. Clouds across the top.
- **9:16 version (to be confirmed by the owner, not seen in a sample):** same layer order stacked vertically. Clouds top, name label in the top third, sun behind the head in the centre, subject bottom half at ~55% of frame height, context object behind one shoulder, trees in both bottom corners. All text inside the 9:16 safe zones.

## Transitions

Inside a scene, every element has its own entrance:
- rise from below the frame (trees, building), ~0.4–0.8 s, ease-out (cubic-out)
- scale up from a point (sun / colour shape), ~1.0 s, ease-out, no bounce
- straight-edge bottom-to-top mask reveal (the main person), ~1.1 s
- typewriter (text)
- 3D page-turn flip (sticker), ~0.6 s
- ink line draw-on (connector), ~0.3 s

No whoosh pairs were measurable. *Not seen yet:* the scene-to-scene transition.

## Typography and captions

- **Name / title label:** a bold high-contrast serif (newspaper/Didone feel). Free build choice: `DM Serif Display` or `Playfair Display` Bold. Near-black ink `#2b2622` on a torn cream tape strip `#eadabd` with rough left and right ends and a faint paper texture. Cap height about 7% of frame height in 16:9. The text sits straight and the tape is slightly rotated (0–2°).
- **Small tag:** a black paper rectangle `#483e33` with yellow serif text `#f2d15e`, rotated about -5°, overlapping the sticker's edge.
- Entrance: typewriter, about 10 letters/s, no cursor; the tape strip is visible before the first letter.
- **No subtitles** in the sample. Burnt-in captions are off by default (house rule: subtitles only on request).
- **Underline: not seen in sample 1.** The only line-work is the thin curved black ink connector (~2 px, hand-drawn feel, draws on from start to end). Learn the underline (shape, colour, timing on the word) from the next sample before building it.

## Motion graphics

Layer stack, back to front (z-order), with what each layer is:
1. Paper background: warm cream `#ebe5dc` with fine grain and fibres, faint stains, scraps of handwritten letters and newsprint torn along the left and right edges.
2. Clouds: torn-paper clouds, one beige `#e2d0b5` and one dusty blue `#8d99a2` with a white torn rim.
3. Nature frame: tree photo cutouts in olive `#6c5c33` with a cream paper rim, bottom corners.
4. Accent shape: one big flat torn-paper shape in the accent yellow `#fbca36` (sun / blob) behind the subject, fibrous torn edge.
5. Context cutout: object photo (building) in muted real colour.
6. Subject cutout: person photo in warm monochrome (saturation ~0.19, sepia-grey), cream paper border.
7. Label: torn tape + serif text.
8. Brand sticker + tag + ink connector.

**Paper-cut look (the key):** every photo cutout has an uneven cream/off-white paper border about 4–8 px at 864 px width (≈ 0.6–0.9% of frame width) with a rough, slightly wobbly torn edge. There is no hard drop shadow; at most a very soft contact shadow. Flat colour shapes (sun, clouds) are torn paper with a visible lighter fibrous rim.

Idle motion: after landing, each layer drifts 1–3 px on its own slow loop (each layer with a different phase), and trees sway slightly. This is what keeps a held frame alive.

Build notes: one HTML/Hyperframes scene per sentence, each layer an absolutely-positioned PNG cutout (soft paper border baked in with `studio/soft_cutout.py`-style edge plus a torn-edge mask), GSAP timeline keyed to Whisper word times with the offsets above.

## Colour

Very few colours, each with one job:
- **Cream paper** `#ebe5dc` / `#eae2d8`: ~45% of the frame, the base of everything
- **Near-black ink** `#2b2622` – `#483e33`: type, tags, the connector line, the subject's dark clothes
- **One accent: warm yellow** `#fbca36` for the big shape behind the subject; a lighter yellow `#f2d15e` for the brand sticker and tag text. ~12% of the frame. Yellow is the only saturated colour.
- **Muted naturals:** olive trees `#6c5c33`, dusty blue cloud `#8d99a2`, beige cloud `#e2d0b5`, the building's muted blue glass `#38505b`
- **People in warm monochrome** (desaturated, sepia-grey); objects keep muted real colour

Overall: luma mean 185, saturation mean 0.21, warm (R−B +42). Grade preset `warm-film` as a start; push people to mono and keep the yellow clean.

## Sound design

Measured only (I cannot hear the audio): 0–0.7 s near silence (-45 dB mean) before the VO starts at 0.78 s; VO at about -20 dB mean; after the VO ends there is still a bed at about -24 dB mean with no silence, so a soft music bed runs under it. Overall -20.1 LUFS, LRA 3.4. Narration is a calm English documentary read at 2.5 words/s. *Not measured:* paper/pop SFX on entrances. Check by ear in the next sample or ask the owner.

## VFX

Paper grain and fibre texture on everything, torn-edge masks, the 3D sticker flip, line draw-on, idle drift. No glitches, light leaks, flashes or shake.

## Do / don't

Do:
1. Build each scene layer by layer on cream paper, back to front, one arrival every 0.5–1 s.
2. Give every photo a cream torn-paper border; make flat shapes torn paper too.
3. Keep the palette to cream + black ink + one yellow accent + muted naturals; people in warm mono.
4. Put the big yellow shape behind the subject's head.
5. Bring the image 0.1–0.5 s after its word, and the name text last, as a typewriter on torn tape.

Don't:
- No hard cuts mid-sentence, no camera zooms, no frozen holds.
- No second bright accent colour, no gradients, no glossy/glass UI.
- No clean digital vector edges on cutouts.
- Never reuse the Vox logo, another creator's watermark/handle or their end card; use the owner's own logo sticker.
- Don't invent the underline or scene transition before a sample shows them.

## Frames studied

- `frames/S001_0m03.0s.jpg` the single shot at 0:03.0
- 10 fps contact sheets of 0–10 s (100 frames), full-resolution frames at 0.0, 2.4, 3.5, 4.2, 5.9 s, crops of the label, sticker and cutout edge, a 15 fps strip of the sticker flip, and a difference image of 4.8 s vs 6.0 s (to confirm the idle drift)
