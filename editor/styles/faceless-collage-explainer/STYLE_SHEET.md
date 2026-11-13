# Style sheet: Faceless collage explainer (Faceless Editor house style)

Status: **learned**. The owner approved it on 2026-11-09 ("badlne hatane jesa kch nhi h"). Learned from the owner's 4 sample videos. Measured = FFmpeg/Whisper numbers. Observed = what I saw in the frames (1 fps sheets plus 6 fps detail strips). Sound was not heard, only measured.

Samples: s1 The Scream (46 s), s2 Frame War promo (24 s), s3 Warren Buffett cash (51 s), s4 Project A119 moon (45 s). All four come from one creator. The files stay in the git-ignored `projects/_faceless-train/` and are study material only. **Learn the style, never their branding, watermark, CTA or assets.**

## Measured

| | s1 Scream | s2 promo | s3 Buffett | s4 Moon |
|---|---|---|---|---|
| Length | 46.3 s | 24.3 s | 51.3 s | 44.9 s |
| Format | 9:16, 30 fps | 9:16 | 9:16 | 9:16 |
| VO words / rate | 106 · 3.0 w/s | 45 · 2.6 w/s | 106 · 2.5 w/s | 93 · 2.5 w/s |
| VO starts | 0.0 s | 0.0 s | 0.0 s | 0.0 s |
| Hard cuts / 10 s (detector) | 2.4 | 14.0 | 10.3 | 1.1 |
| Loudness | −14.0 LUFS | −13.7 | −13.9 | −14.5 |
| True peak | +0.2 dBTP | +0.1 | +0.1 | +0.9 |
| Loudness range | 2.7 LU | 16.8 | 2.4 | 5.5 |
| Luma / saturation / warmth | 99 / 0.32 / +18 | 100 / 0.37 / +9 | 94 / 0.28 / +11 | 69 / 0.34 / +26 |

- The cut detector undercounts s1 and s4: those use seamless transitions (push-throughs, cloud wipes, light flashes), not hard cuts. Counted by eye on the 1 fps sheets, **the picture changes every 1.5–2.5 s** in all four. s2 and s3 add 1–2 frame flash and slot-machine frames, which inflate their counts.
- VO runs without a break from frame 1 to the end card. The only silence over 0.7 s is the ending.
- True peak goes over 0 dBTP in all four (they clip). We keep −14 LUFS but cap at −1 dBTP.

## Structure (observed, same in all four)
1. **Hook, 0–1 s:** a question or shock line *as on-screen type* while the VO says it ("What if Fear could be turned into a Painting?", "DESTROYING THE MOON", "$250 editing 13 seconds"). There is motion from frame 1: a cloud wipe, a title flying in, or a number counting up.
2. **Context, about 3–12 s:** the date, place and person. Every date gets its own graphic beat (1892, 1950s, 1999/2007).
3. **Turn, about 12–25 s:** "But…", "Why?", "And here's a strange fact".
4. **Payoff, about 25–38 s:** the meaning line ("It became a symbol of fear itself", "a nuclear billboard").
5. **End card, the last 4–6 s:** CTA plus the logo/handle over a darkened, blurred last scene that fades to black.

## Timing: when text, scenes and faces arrive (counted by eye at 6 fps against the Whisper word times)

| Event | Spoken word at | On screen at | Lead (−) or lag (+) |
|---|---|---|---|
| s1 "What if" builds | "What" 0.00 s | 0.50 s | +0.5 (the cloud wipe covers the first half second) |
| s1 *Fear* | "fear" 0.34 s | 0.83 s | +0.5 |
| s1 *Painting?* | "painting" 1.54 s | 1.67 s | +0.1 |
| s1 cut to the lit wall | "1892" 2.68 s | 2.50 s | −0.18 |
| s1 1892 builds digit by digit | "1892" 2.68 s | 2.67–3.17 s | 0 to +0.5 |
| s1 portrait of the painter | "Edvard" 4.58 s | 4.0 s | −0.6 (the person arrives before the name) |
| s1 name tag EDVARD MUNCH | "Munch" 5.06 s | 5.0 s | on the word |
| s3 number 300 → 381 rolls | "$381" 0.92 s | 1.17–2.17 s | +0.25, then rolls for 1 s |
| s3 *Billion dollars* handwriting | "billion" 2.64 s | 3.0–3.67 s | +0.4, writes on for 0.7 s |
| s3 cut to the cash | "cash" 4.00 s | 3.83 s | −0.17 |
| s3 S&P 500 chalkboard | "S&P" 13.60 s | 14.0 s | +0.4 |
| s3 WENT UP 80% | "went" 14.92 s | 16.0 s | the board waits for "80%" (15.90 s) |
| s4 1950s red tag | "1950s" 5.84 s | 6.0 s | +0.16, slides in for 0.5 s |
| s4 cut to the planners | "planners" 7.78 s | 7.33 s (red flash), 7.5 s (scene) | −0.3 |

Rules the Faceless Editor follows:
- **Scenes cut about 0.15 s before their word** (−0.1 to −0.3 s), so the picture is there when the word lands.
- **Text lands on its spoken word,** 0 to +0.5 s after it starts, and builds over 0.3–0.7 s (digit by digit, letter by letter, write-on or a number roll). It stays until the scene changes.
- **Numbers roll or count up** to the spoken value. Dates build digit by digit with an underline or a tag.
- **People (faces) appear as story characters only, never as a presenter.** The person's image arrives up to 0.6 s *before* the VO names them, and the name tag lands on the name.
- **The hook line is on screen within 1 s,** word by word, with the first word on a transition.

## Visuals (observed)
- **AI-made cinematic stills or clips** of the story: a period painter at an easel, a 1950s war room, a rocket on a pad, Buffett portraits. These are photoreal, warm and spot-lit.
- **3D paper/tabletop collage:**
  - a desk or cutting mat (green grid, white grid, wood) with props: money, coins, pens, a clipboard, a calendar, newspapers, a stopwatch, a calculator
  - people as cut-outs with a white paper border
  - real hands entering the frame to place, point at or lift things
  - hanging chalkboards and framed pictures on lit walls
- **Never a still that sits still:** every image has a slow push-in, parallax or a 3D tilt and drift.
- **Props carry the facts:** a newspaper spins in with the headline, a calendar circles the month, a chalkboard shows "S&P 500".

## Text and motion graphics (observed, this is the core of the style)
- **Every number, date, name and key word becomes a graphic**, synced to the VO word:
  - big bold numerals with a red underline (1892)
  - a red pill tag (1950s)
  - an odometer or slot-machine roll (300 → 381, 1 → 3, 200 → 230)
  - a name on yellow tape (EDVARD MUNCH)
  - a year in a green box in serif type (In 1999 / And 2007)
- **2–3 type families per video, chosen by meaning:**
  - **Serif italic** (Playfair/DM Serif-like) for emotion and nuance words: *Fear, strange, Paint, Pastel, Strangest*
  - **Heavy display sans**, all caps with 3D extrusion or shadow, for punch lines: THE SCREAM, WENT UP 80%, THAT'S VERY HIGH (yellow on red), SOME EDITORS REWATCH THIS
  - **Texture fonts for a theme:** pixel font (the Minecraft promo), handwriting on paper ("The real question is"), typewriter with a redaction box ("Could only have been painted by a ▇▇")
- **Builds:** word by word or letter by letter on the VO. Words scatter in 3D space and then collapse ("it became a symbol of fear"). Chrome/red 3D titles fly in with a light streak.
- **Captions:**
  - s3 has a classic caption track: small white sans on a dark box, in the lower third, 2–4 words, with the big kinetic word above it
  - s1 and s4 use the kinetic type only
- **Handle:** a small handle in the top right through the whole video.

## Transitions (observed)
- a cloud or smoke wipe
- a light bloom or whiteout flash
- a red-tint flash frame
- an iris or binocular vignette mask
- a push-through into the next scene
- a camera pan along a wall into the next frame
- an object match (newspaper → newspaper, frame → frame)
- a slot-machine number flip

No plain hard cut sits on a sentence boundary without a move, a flash or an SFX.

## Colour (measured and observed)
- Warm and contrasty: dark browns and charcoal with spotlight pools and vignettes. Average luma is 69–100, so the frames are dark-mid.
- **Red is the accent in every video** (#a6341e and #b06e45 in the measured palettes), with yellow and green for highlights.
- Each scene keeps its own lighting, but the warm-dark base stays the same throughout.

## Sound (measured only; I cannot hear it)
- An English male documentary VO, close and compressed. The loudness range is 2.4–5.5 LU on the three explainers.
- The promo (s2) has a 16.8 LU range, so it has drops and hits.
- Whooshes and pops on the transitions are likely, given the motion, but not confirmed.

## House targets for the Faceless Editor
- **Format:** 9:16, 30 fps, 1080×1920 (the samples are 480×864 uploads; we master at 1080p). Length 30–50 s.
- **VO:** 2.5–3 words/s, starting at 0.0 s, with no dead air.
- **Hook:** on-screen text plus motion inside 0–1 s.
- **Pace:** a visual change every 1.5–2.5 s. A graphic beat on every number, date and name.
- **Type:** 2–3 families from the roles above. Red accent, plus yellow or green highlights.
- **Motion:** every still moves (push-in, parallax, 3D tilt). Paper/prop cut-outs with real shadows.
- **Transitions:** from the list above, each paired with an SFX.
- **End card:** 4–6 s. The owner gives the CTA and handle with each video; never reuse a sample's CTA.
- **Mix:** −14 LUFS, true peak ≤ −1 dBTP. Music ducked under the VO.
- **Language:** Hindi, English or Hinglish, decided by the owner's VO for each video. Pick fonts with Devanagari support for Hindi (the `rozha-hind` pairing is the default).
- **Reference reel (owner, 2026-11-09):** the delivered `silhouette-follow` reel is the template for every new VO: match its scene look, pace, kinetic type density, transitions and SFX exactly.
- **Clarity over speed (owner, 2026-11-09):** one clearly matching visual per VO sentence, held about 2.0–2.5 s on average; no rapid sub-cuts inside a sentence. Promo-pace cutting is only for short hype promos.
- **Code-drawn visuals (owner, 2026-11-09):** when the owner sends no images, draw semi-realistic, cinematic, lit and shaded scenes on 3D paper/tabletop collage layers with drop shadows; never flat black silhouettes. Promo-pace VOs (like s2) get kinetic type on nearly every phrase, a transition plus a very quiet SFX on every cut, and parallax on layers. ~~Shake on hits~~ (superseded 2026-11-10: never shake).
- **Inputs:** the owner's images, AI clips and footage, plus the VO (the owner's recording or an AI voice). The engine builds the type, motion, collage moves, transitions, sound and captions.

## Owner rules, 2026-11-10 (these override anything above)
- **No shake, ever.** Every scene, image and text comes in with a smooth animation (fade, pop with a small settle, slide, push), then **sits still and stable**, then leaves with a smooth animation. Image moves are a slow, steady drift (about 4 % over a scene). `shake` is banned in `editor/rules.json`.
- **The VO comes first.** SFX stay very quiet, at least 15 LU under the VO (measured). The music sits at least 14 LU under the VO before ducking. Run `faceless-level`; `craft-check` fails a louder mix.
- **People with faces, no white borders.** When the owner gives no photo, draw people with a visible face: illustrated, cartoon-like but realistic (expression, eyes, hair, skin tone, clothes), with the right age and gender for the VO. They are generic people, never a real person. Do not put white paper-cut borders around figures; keep the realistic light and soft shadows. This replaces the white-border cut-outs above.
- **Social media = real logos.** When the VO names a platform or talks about social media, animate the owner's logos from `editor/library/social/` (Facebook, X/Twitter, Instagram, WhatsApp, Snapchat), not heart or message icons.
- **Subtitles only on request.** Burn subtitles (Hindi or English) only when the owner asks for them for that video; some clients refuse them. The kinetic text graphics, effects, transitions and animation are always part of the style.
- **Real photos for every object, animal and place.** Dogs, money, computers, mics, stages and the Earth are realistic stock photos (Pexels, Wikimedia Commons, NASA, all free-licensed, credited in `CREDITS.md`), never cartoon drawings. Faces follow the people rule above. TV channel logos come from the owner.

## Look v3 (owner, 2026-11-13; this overrides the warm/yellow bokeh, wood-table and paper look above)
- **Background:** a smooth, professional gradient from one theme in `editor/faceless/palettes.json`. The themes are midnight navy, crimson noir, black and white, emerald and gold, royal purple, slate and teal, and charcoal and orange. No yellow, no bokeh bubbles, no paper and no tables.
- **One theme per video.** Choose it by topic (each theme's `use` says where it fits) and pass `faceless-plan --theme <id>`. All text colours come from the theme:
  - the hook in the accent colour
  - numbers in the highlight colour
  - names and words in the text colour
  - small labels in the muted colour
- **Objects** are real-photo cutouts made with `faceless-card <photo> <out> --theme <id>`. Each gets a soft drop shadow, a contact shadow, a faint floor reflection and a light wrap from the background. A photo cut off at the bottom fades into the background. A flat object (a note, a card) gets a slight 3D tilt.
- **Places and scenes** (court, parliament, crowd, street) are full-bleed photos with theme bands at the top and bottom for the text: `faceless-card --photo`.
- **Black and white theme:** the photos are black and white too, and the text is white or grey only.

## Design system v3.1 (owner, 2026-11-13; the theme list above is replaced by `editor/faceless/palettes.json`)
- **Themes:** 8 designed themes, each following 60-30-10: navy-ivory (the default), graphite-crimson, mono-silver, teal-sand, plum-rose, forest-gold, midnight-electric, and ivory-navy-light. Choose one per video by mood (each theme has `use` and `mood`). Text is checked to at least 4.5:1.
- **Text:**
  - clean: no outline, a soft shadow, the Poppins and Hind pairing
  - colours: primary off-white, the key word or number in the accent, labels muted
  - one text block per scene, fitted to the real font width, at most two lines
- **Glass:**
  - `faceless-card --panel`: a 18 px blur, the theme surface at about 40 %, a hairline border and a soft shadow
  - for labels, numbers, names, quotes, the CTA and text over photos; text positions `glass-top` and `glass-lower` centre it in the panel
  - not for long text
- **Layout:**
  - a whole object sits in the upper zone with its text below
  - a cut-bottom photo rises from the bottom with its text on top
  - a cut-side photo enters from its side
  - the object and its text never overlap
- **Cutouts:** hole-free (`solid_cutout`) and checked by eye. Replace any that look bad.

## Variety and direction (owner, 2026-11-13)
`faceless-plan` runs a direction pass (`faceless.direct`) when the visuals are images. Put objects in `raw/`, places in `raw/places/`.

**Text treatments, chosen by what the text is:**

| Treatment | What it is | Used for |
|---|---|---|
| `plain` | clean off-white text | headlines, statements |
| `emphasis` | a line with the key word in the accent colour | turns ("Lekin asli sawaal"), claims |
| `tag` | solid accent box, text in the theme's ink | dates, places, names, categories |
| `glass` | frosted card | numbers and stats, quotes, the CTA, any text over a busy photo |
| `bgword` | a huge, faint word behind the object, plus the line itself | hooks, topic openers |

**Variety rules:**
- No treatment in two consecutive scenes, and none in more than about 35 % of a video.
- Text over a photo always gets glass or a tag.
- One text block per scene.

**Entrances:** rise, slide-left, slide-right, pop (with a settle) and fade-up. All are eased over 0.6 s; the object then holds still and fades out over 0.3 s. Never the same entrance twice in a row, and never a shake.
