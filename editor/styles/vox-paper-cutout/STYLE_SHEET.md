# Style sheet: Vox paper cutout explainer

Slug `vox-paper-cutout` · family **documentary / collage** · learned from the owner's reference samples (2026-11-16):

- **Sample 1:** 16:9, 10.2 s, English VO about Bill Gates. One scene built layer by layer on cream paper.
- **Sample 2:** 9:16, 47.4 s, English VO about Elizabeth Loftus's 1974 memory experiment. 21 scenes on kraft/sepia paper, with highlights, underlines and circles.

More owner samples may come; anything marked *not seen yet* must be learned from a sample, not guessed. Each sample's last seconds are the original creator's Instagram end card (sample 1 after 6.13 s, sample 2 after 43.3 s). They were trimmed before measuring. Never copy end cards, creator handles, watermarks or the Vox logo. Owner's CTA/end card only.

A third clip the owner sent the same day (Nvidia/Jensen Huang, 9:16) is **not** this paper-cutout style. Its notes are in `editor/styles/cinematic-ai-kinetic/STYLE_SHEET.md`.

## Measured: sample 1 (16:9)
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

## Measured: sample 2 (9:16)
- Source: 43.3s, 480x864, 30.0 fps, aspect 9:16
- Shots: 29 · shot length mean 1.49s, median 1.23s, range 0.07–5.6s
- Cuts per 10 s: 6.47 overall; per 10 s window: 6 5 3 13 1
- Hook: first cut at 1.667s · shots under 1 s: 13 · shots over 4 s: 3
- Palette: #9b8a79 (21%), #b6a997 (18%), #7d7060 (18%), #d5cab7 (15%), #534b41 (14%), #231e1a (13%)
- Luma mean 127.3 · saturation mean 0.2 · warmth (R−B) mean 26.54
- Loudness: -14.6 LUFS, true peak -0.57 dBTP, LRA 2.3
- Silences over 0.7 s: 0
- Speech rate: 3.31 words/s

## Targets for an edit in this style (machine-readable copy in style.json)

- Average shot 1.49s, cuts per 10 s 6.47, first cut by 1.667s
- Starting grade preset `warm-film` (check against the frames; adjust or build a LUT)

The cut detector counts blur-dissolve and zoom-through frames as cuts (35.9–36.6 s alone reads as 10 cuts). Counted by hand from the frames: **21 scene changes in 43.3 s ≈ one new scene every 2.1 s** (shortest 0.7 s, longest 3.4 s). Use 2.0 s as the 9:16 pace target, not 1.49 s.

`style.json` carries the sample 1 (16:9) targets as `targets` and the sample 2 (9:16) targets as `targets_9x16`.

## Two speeds of the same style

| | 16:9 long form (sample 1) | 9:16 short (sample 2) |
|---|---|---|
| Scene length | one sentence per scene, ~6 s, built layer by layer | ~2 s per scene; a new picture for each phrase |
| Inside a scene | 6–8 elements arrive one by one | 1–3 elements: one picture + one text treatment |
| Paper | light cream `#ebe5dc` | kraft / sepia `#a38b73` and light grid paper `#dccdbc`, heavy vignette |
| Accent | one yellow `#fbca36` | red `#9d2220`–`#b4342e` + yellow `#f0d226`–`#fbce31` as a pair |

## When images arrive on the VO

- **Sample 2 cuts are word-locked.** A new scene starts on the first word of a new phrase, within 0.0–0.4 s before it. Measured: "psychologist" 1.60 → cut 1.67; "Could" 6.10 → cut 6.10; "watched" 13.18 → cut 13.17; "Nothing" 15.42 → cut 15.33; "a week" 24.52 → cut 24.57; "She asked" 25.20 → cut 25.23; "Many" 26.94 → cut 27.13; "There was" 30.58 → cut 30.6; "That experiment" 37.16 → cut 37.23; "It proved" 39.58 → cut 39.37; "story" 42.48 → cut 42.1.
- **The picture shows the noun just said.** brain → anatomy engraving; "volunteers" → line-up of blindfolded people; "car accident" → old TV playing a crash; "broken glass" → glass shards under the crashed cars.
- **The VO can change the picture inside a scene.** On "broken glass" (32.9 s) a yellow highlighter box swipes over the shards. On "never been any" the shards disappear (33.4 s). On "a single word" the two crashed cars morph into the word *smashed* (34.0 s).
- Sample 1 (16:9): inside a built scene, an image starts 0.1–0.5 s after its word ("Gates" → photo; "computer" → building).

## Scene timeline: sample 2 (9:16)

| Time | VO | Picture | Text treatment |
|---|---|---|---|
| 0.0 | "In 1974" | grid paper, blurred 70s photo at bottom | `[in1974]` italic serif, square brackets open outward as the letters write on |
| 1.67 | "psychologist Elizabeth Loftus" | B&W full-body cutout in her study, anatomy-head cutout bottom-left | name on a brown tape strip, yellow italic serif; the strip wipes left→right, then the text |
| 3.83 | "one disturbing question" | at a desk under a lamp beam, typewriter, paper | two small red paper tags "disturbing", "question" pop near her hands |
| 6.1 | "Could the human brain" | anatomy engraving of a skull on torn paper; brain/head engraving rises | none |
| 7.33 | "remember something…" | magnifying glass over the brain shows pinned polaroids; a hand moves the photos | none |
| 9.67 | "To find out" | dark brown sign hung on two red strings | words build one by one on their spoken word, cream + yellow bold sans; the sign then shrinks upward as the scene widens |
| 10.6 | "volunteers into her lab" | line-up of 70s people with black bars over eyes | "into her lab" on a red stamped card with a dotted border, slides in rotated from bottom-left |
| 13.17 | "watched a short video of a car accident" | old TV on a 70s shelf playing a crash | "car accident" yellow bold sans, **red ellipse draws around it** |
| 15.33 | "Nothing unusual" | plain kraft | a brown paper circle scales up; black "nothing" + big yellow "unusual." |
| 16.6 | "she asked them a simple question" | B&W cutout at a table with books | white sans subtitle; "question" yellow on a red block that pops in |
| 18.97 | "How fast were the cars going…" | a clipboard slides in rotated on kraft, newspaper corner | white bold sans, phrase by phrase; "smashed" yellow chunky italic serif |
| 22.2 | "Just one word, smashed" | zoom into kraft, only "smashed" left | **red brush stroke wipes behind "smashed" left→right in ~0.4 s, landing on the spoken "smashed" (23.68)** |
| 24.57 | "A week later" | calendar of "day 1 … day 7" circles | a yellow dot climbs from day 2 to day 7 |
| 25.23 | "she asked the volunteers what they remembered" | real talk footage, B&W | thin italic serif white captions, 1–2 words |
| 27.13 | "Many confidently recalled… broken glass" | torn pink paper sheet; two crashed cars, glass shards appear | spotlight iris closes in; **yellow highlighter box over the shards** |
| 30.6 | "There was only one problem" | clipboard | words build; "problem." yellow on a red block |
| 31.87 | "never been any broken glass" | same crash sheet | highlighter on shards, then the shards vanish |
| 34.0 | "A single word had quietly rewritten" | cars morph into the word *smashed*; ink blots spread like neurons | white italic serif "smashed" |
| 35.9 | "their memory" | zoom out through neurons to a brain-head engraving | **"memory" yellow italic serif with a red hand-drawn ellipse around it** |
| 37.23 | "That experiment changed psychology forever" | B&W footage of a hand writing notes | thin italic serif captions; "psychology" in yellow |
| 39.37 | "It proved that memory isn't a perfect recording of the past" | B&W lab footage | same captions; "memory" in yellow |
| 42.1 | "It's a story." | newspaper paper with an oval vignette | "story" yellow on a red tag |

## Hook and structure

- **First frame = the date or the number, as designed type** (`[in1974]`), on paper, with a hint of the era behind it. No black frame.
- Then: who (name label) → the question → the experiment step by step → the twist ("only one problem") → the meaning → a one-word close ("story") on a red tag.
- 16:9 (sample 1): the first scene builds from the set inwards; the subject's face is fully up by 2.9 s.

## Cutting

- 9:16: word-locked scene changes every ~2 s, as measured above. 16:9: one scene per sentence, built in one continuous shot.
- Real footage (talks, labs) is allowed between collage scenes, always desaturated to warm B&W.

## Camera and framing

- Slow push-ins on every still (about 3–6% over a scene) and parallax between the cutout and the background; nothing sits frozen. Sample 1 measured a locked frame with 1–3 px layer drift instead.
- 9:16: subject centred, top of the head at ~15–20% of frame height, text in the centre band (35–75% height), corners kept clear for platform UI.
- Zoom-through transitions: into the kraft before "smashed"; out of the neurons to the brain at 35.9 s.

## Transitions

Measured in sample 2:
- **Blur dissolve with a small scale-up**, 0.2–0.3 s. The most common transition (2.2, 6.6, 16.6, 22.2, 30.6 s).
- **Slide in, rotated:** clipboard and cards enter rotated 10–20° and settle straight, ~0.4 s, ease-out.
- **Iris / spotlight:** a soft circular vignette closes onto the subject (28.4 s) and opens again (29.6 s).
- **Morph:** objects become a word (cars → *smashed*).
- **Zoom-through:** push into texture, or pull out to a wider engraving.
- Inside a scene (sample 1): rise from below, scale up from a point, straight-edge bottom-to-top reveal, page-turn flip.

## Typography and captions

Two type voices and one colour rule:
- **Serif voice:** high-contrast serif. Roman bold for names and labels (sample 1 "Bill Gates"; free build: `DM Serif Display`); italic for dates, names and talk captions (`[in1974]`, "Elizabeth Loftus", "that memory"; free build: `Playfair Display Italic` / `Instrument Serif Italic`). The punch word is a chunky italic serif (*smashed*, *problem.*, *memory*, *story*; free build: `Fraunces Black Italic` or `Recoleta Black`).
- **Sans voice:** heavy grotesque for kinetic phrases ("to find out", "car accident", "nothing unusual.", "question"; free build: `Archivo Black` / `Inter ExtraBold`), tight tracking.
- **Colour rule:** normal words are cream/white `#f1e9dc` or dark ink `#2b2622`. **The one key word in each line is yellow** `#f0d226`, often on a red base `#9d2220`.
- **Carriers** (text never floats bare on a busy picture): torn tape strip, brown sign on strings, red stamped card with a dotted border, small red paper tag, brown paper circle, clipboard.
- **How text arrives:** word by word on its spoken word (sample 2 "to find out", clipboard phrases); letter-by-letter typewriter (sample 1 label, sample 2 `[in1974]`); a tag pops in with a short blur-to-sharp (~0.15 s); a card slides in rotated.
- Captions on real footage: 1–2 words at a time, thin italic serif, lower-centre, keyword in yellow.
- 9:16 sizes at 480×864: kinetic sans ~45–60 px; punch word ~65–80 px; caption serif ~30 px. Scale proportionally at 1080×1920 (×2.25).

## Underline, highlight and circle (the annotation set)

All measured in sample 2:
1. **Red brush swipe behind a word:** a rough-edged red `#9d2220` brush bar wipes left→right behind the yellow word in ~0.4 s. It starts ~0.3 s before the word and finishes on it ("smashed" 23.4–23.8 s for the word at 23.68 s). Bar height ≈ 1.3× the cap height; it overhangs the word by ~5% on each side.
2. **Red ellipse drawn around a word:** a hand-drawn ~3 px red `#8c3130` loop, slightly tilted, with the end overshooting the start. Draws on in ~0.4 s as the word is spoken ("car accident" 14.4–14.8; "memory" 36.4–36.8).
3. **Yellow highlighter box over part of a picture:** translucent yellow `#f0d226` at ~35% opacity, a rough rectangle swiping left→right over the detail the VO names ("broken glass" 28.6 and 33.0 s), ~0.3 s.
4. **Brackets around a date:** square brackets in red-brown open outward as the date writes on (0.2–0.8 s).
5. **Red block under a punch word** ("question", "problem.", "story"): a flat red rectangle with a slightly rough edge; it pops with blur-to-sharp, then the yellow word sits on it.
6. Sample 1: a thin black ink connector line draws on between two items (~0.3 s).

Use at most one annotation per scene, always on the key word or the detail the VO names.

## Motion graphics

- Paper layers: background paper (grid, kraft, cream or newsprint) → torn paper sheet or engraving → photo cutouts (B&W, cream/white paper border, torn edge, soft contact shadow) → text carrier → annotation.
- **Paper-cut look:** a 4–8 px uneven cream border on every cutout (at 864 px height in 9:16 and 864 px width in 16:9), a rough torn edge, flat shapes cut from paper with a fibrous rim. Kraft and paper sheets have wobbly edges (the pink sheet at 27.2 s).
- Prop vocabulary seen: old engravings (anatomy, skulls, brains), polaroids with red pins, magnifying glass, clipboard, old TV, 70s shelf objects, calendar dots, ink blots, red strings.
- Black bars over eyes for anonymous people.
- Idle life: every still has a slow push or layer drift; hands and objects move inside the magnifier.

## Colour

- **Base:** paper, about 70% of every frame. 16:9 sample: cream `#ebe5dc`. 9:16 sample: kraft `#a38b73`, sepia `#b6a997`, light grid `#dccdbc`, and dark brown `#534b41` / `#231e1a` in the vignettes.
- **Accent:** sample 1 uses yellow alone (`#fbca36`). Sample 2 uses **red `#9d2220`–`#b4342e` + yellow `#f0d226`–`#fbce31`**, red as the base or line and yellow as the word or highlight. In sample 2 the accent covers ≤ 9% of any frame (measured: red 8.6% on the "smashed" frame, usually 1–4%).
- **People and footage:** warm B&W (saturation ~0.2), never full colour. Objects can keep muted colour (the TV crash in faded teal, the 70s shelf in warm brown).
- No other saturated colour anywhere.
- Grade: `warm-film` start, desaturate, heavy oval vignette (corners −40 to −60% luma in 9:16), fine grain.

## Sound design

Measured only (I cannot hear the audio). Sample 2: −14.6 LUFS, LRA 2.3, no silences over 0.7 s, so VO and bed run continuously. Narration is a calm English documentary read at 3.3 words/s (9:16) versus 2.5 words/s (16:9). Sample 1: a near-silent 0.78 s before the VO, then a soft bed under it. *Not measured:* paper, pop or swipe SFX. For the owner's videos, follow the house rule (corporate/faceless: no SFX unless asked) until the owner decides for this style.

## VFX

Paper grain and fibres, torn-edge masks, a heavy oval vignette and spotlight iris, blur dissolves, the object-to-word morph, ink blots spreading, a magnifier lens with parallax inside, the brush/ellipse/highlighter draw-ons. No glitches, light leaks, RGB splits or shake.

## Do / don't

Do:
1. Paper everywhere: cutouts with cream torn borders on cream, kraft or grid paper.
2. Change the picture on the VO's phrase (9:16, ~2 s) or build the scene element by element (16:9, ~0.5–1 s per element); the picture always shows what was just said.
3. One key word per line in yellow, on red, inside a carrier; everything else cream/ink.
4. Annotate the word or the detail the VO names: red brush swipe, red ellipse, yellow highlighter box, brackets. One per scene, landing on the word.
5. People and footage in warm B&W; the accent is the only saturated colour.

Don't:
- No full-colour photos of people, no gradients, no glossy/glass UI, no clean vector edges.
- No text floating bare over a busy photo; no more than two accents.
- No frozen stills; no hard cut that lands mid-word.
- Never reuse the Vox logo, other creators' handles, watermarks or end cards.

## Owner rules (2026-11-28, SP Guide Publications video)

- Keep the paper base and the red + yellow accent; do not change colours much. Briefs that ask for 3D wireframes, exploded engines or dashboards are rebuilt in the paper look: ink line drawings on grid paper, paper-card devices, paper charts.
- Every image and text lands on its spoken word (forced-aligned word times); nothing overlaps.
- Not too fast: entrances about 0.6-0.9 s; text stays until its scene changes (aim for at least 2 s on screen).
- No empty screen for long and never a blank first frame.
- Everything arrives with motion (rise, scale from a point, draw-on, rotated slide, blur dissolve, iris).
- Owner-supplied logos are used exactly as given (white background cut out, no recolouring) on a cream torn-paper card.

## Frames studied

- Sample 1: 100 frames at 10 fps (0–10 s), full-resolution frames at 0.0, 2.4, 3.5, 4.2, 5.9 s, crops of label, sticker and edges, a 15 fps sticker-flip strip, and a 4.8 vs 6.0 s difference image.
- Sample 2: 224 frames at 5 fps (0–44.6 s) and 12 full-resolution key frames (1.2, 3.0, 5.8, 14.8, 16.2, 18.6, 23.9, 28.7, 31.6, 36.8, 38.2, 42.6 s), with red/yellow/base colours measured per key frame.
