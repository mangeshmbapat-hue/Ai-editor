# Style sheet: long voiceover explainer

Slug `voiceover-explainer` · family **explainer** · owner: Explainer Editor (`.claude/agents/explainer-editor.md`).

Long explainers on a voiceover, about 3, 4, 10 or 12 minutes. Started 2026-11-23. Everything here comes from the owner's samples (`SAMPLES.md`); anything marked *not seen yet* must be learned from a sample, not guessed. **Status: learning, not yet approved by the owner.**

Learned so far from **sample 1** (9:16, 90 s, English VO, "Is IMAX really bigger than your TV?"). The last 4 s (86–90 s) are the creator's end card and were trimmed before measuring. Never copy its illustration, brand name, end card or wording. A 90 s short is not the 3–12 min length the owner wants, so the long-video structure (§8) is still *not seen yet*.

Name for this look: **look 1, navy blueprint line-art**. Later samples may add other looks; keep each one apart.

## Measured: sample 1
- Source: 86.0 s after trimming, 720x1280, 30 fps, 9:16
- Hard cuts: **0** (the detector found none at 0.2). The whole video is one continuous animated world; the "camera" moves, orbits and morphs from scene to scene.
- Picture setups counted by hand: **18 in 86 s, one every ~4.8 s** (shortest ~2 s, longest ~9 s).
- On-screen captions counted by hand: **27 in 86 s, one every ~3.2 s**, one per VO phrase.
- Palette: navy ground #08192C (78% of the frame), grid/line greys #505859 and #25364B, deep navy #0F213A
- Accents, sampled from text (approx.): white #F2F2F0, yellow #F4C430, sky blue #2FB4F2, coral red #F26450
- Luma mean 29 (very dark) · warmth (R−B) −34 (cool)
- Loudness −14.1 LUFS, true peak −1.5 dBTP, LRA 2.1 · no silences over 0.7 s · speech rate 2.7 words/s

## 1. Animation over the video
- There is no live footage. Everything is drawn: one **navy ground with a faint blueprint grid**, thin white/grey **line-art (wireframe)** for the world (cinema seats, room walls, a living room, a VR headset, an eyeball), and one flat-colour **hero illustration** that plays "on" every screen.
- **The camera never cuts.** It dollies, orbits and tilts through the same wireframe world. Between ideas the 3D view **morphs into a flat top-down diagram** and back (15.4–15.6 s: the 3D view of eye and screen folds into a 2D triangle of rays in ~0.3 s).
- The same object is transformed rather than replaced: the picture gets pixelated to show resolution (33–38 s), the TV and IMAX frames scale and slide next to each other, the room darkens around the screen (63–65 s).
- Rays and outlines **draw on** from the eye outwards; screens get a soft **blue outer glow**; small arrows (↑ ↓) and sound arcs pulse in.
- Nothing is still: when a picture holds, there is a slow drift or push.

## 2. When text comes
- One caption per VO phrase, **always one caption on screen at a time.**
- **In:** line by line, each line rises from a mask at its baseline. The first line starts **~0.1–0.15 s after the phrase's first spoken word** (6.36 s "Sit" → text 6.5 s; 15.04 s "Both" → text 15.2 s). The second line follows ~0.2 s later; the caption is complete in ~0.5 s, before the key number is said.
- **Out:** fade out with a slight upward drift over ~0.3 s, then **~0.2 s of no text** before the next caption.
- It stays for the whole phrase (2–5 s). Short reaction words get their own caption ("Obviously.", "Here's why.").

## 3. Which text matters
- The caption is a **short rewrite of the phrase, not the transcript.** "Sit one and a half meters from a 55 inch TV" becomes "1.5 m from a 55″ TV."; "Both fill about 44 degrees of your vision" becomes "Both: 44° of your vision."
- Numbers become digits with units and symbols (1.5 m, 55″, 20 m, 44°, 1.90 : 1, 26%).
- Questions stay as questions ("So why does IMAX feel enormous?"). Run-on thoughts use "…" at the end or start to tie two captions together ("…no extra detail.", "…depth cues push it far away.").
- At most 2 lines, about 2–7 words.
- **Labels inside the diagram** carry what the caption does not: names of parts (IMAX SCREEN, YOUR TV, DISPLAY, LENS, FRAME, WALL, LAMP) and measures (20 m WIDE, 25 m, 1.5 m, 23°, 42°, 44°, "1.90 : 1 · UP TO 26% MORE").

## 4. Text colour and type
- **Caption:** a geometric grotesk sans (medium-bold, sentence case), white. Font size ~4% of the frame height, two lines, top-left at ~10% from the left and ~18% from the top. Never over the picture's key area.
- **1–2 accent words per caption**, coloured by meaning, and the **same colour is used for that thing in the drawing**:
  - **coral red = the small / TV side** ("55″", "smaller", "detail"; the TV frame and its label are coral)
  - **sky blue = the big / IMAX / virtual side** ("screen", "enormous", "virtual", "far away", "further"; the IMAX frame is blue)
  - **yellow = the measured idea or the answer** ("bigger", "wider", "44°", "angle", "resolution", "distance", "above and below"; the angle rays are yellow)
- **Diagram labels:** small uppercase monospace with wide letter-spacing, in the colour of the thing they name, sometimes on a dark navy pill.

## 5. Themes
- **One theme for the whole video:** navy blueprint grid. It never changes; mood is changed with light only:
  - darker vignette around the screen for "in the dark, they fade" (63–65 s)
  - a soft lighter radial glow behind the screen for "sound surrounds you" (65–72 s)
- How themes switch between chapters in a long video: *not seen yet*.

## 6. Images with each theme
- **One hero illustration reused all through** (here a flat moonlit mountain lake in blues with a yellow moon). It is "the picture" in every screen, TV, IMAX and pixel grid, so the eye always knows what it is comparing.
- Everything else is line-art in white/grey. No photos, no stock footage, no people.
- Colour inside the line-art comes only from the three accents (red, blue, yellow) and the screen glow.

## 7. Infographics
- **Comparison diagram:** the two things side by side in their colours (TV coral, IMAX blue), same picture inside each, with a label under each.
- **Angle-of-view diagram:** rays from an eye, yellow filled triangle, the angle drawn as a number inside (23°, 42°, 44°); distances as thin white dimension lines with tick ends and a small label.
- **Cross-section:** an eyeball circle with two images landing on the retina, colour-coded and labelled "same width".
- **Resolution:** the same picture pixelated in both frames, with a pixel grid drawn over it.
- **Ratio strip:** arrows above and below the screen and one mono label line "1.90 : 1 · UP TO 26% MORE".
- Each infographic builds on the spoken number: the line draws on during the phrase and the number lands as it is said.

## 8. Structure of a long video
- Sample 1 (short): question hook in the first frame (the title question as the first caption over the hero image), a fast "Obviously. / But…" twist by 4 s, then step-by-step reasoning, then the turn ("So why does it feel enormous?"), and a closing line that answers the hook.
- Chapters, chapter cards, pace across 3–12 minutes and the CTA: *not seen yet*.

## 9. Transitions, sound and music
- Transitions: camera moves and morphs inside one world; no hard cuts; captions fade between phrases.
- Sound: VO at about −14 LUFS with no gaps over 0.7 s. Music and SFX were not judged (cannot be judged from numbers alone): *not seen yet*. The owner's SFX rules in `studio/LEARNINGS.md` apply.

## Do / don't
- Do keep one caption on screen, a rewrite with digits and units, with 1–2 colour-coded words.
- Do keep the colour code fixed: the same thing has the same colour in text and drawing for the whole video.
- Do explain by transforming one world (zoom, orbit, morph, pixelate) rather than cutting to new pictures.
- Don't put the full transcript on screen; don't use more than three accent colours; don't change the theme mid-video (in sample 1).
