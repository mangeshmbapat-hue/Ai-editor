# Style sheet: Animation product promo (Animation Editor house style)

Status: **learned, waiting for the owner's approval** (2026-11-10). Learned from the owner's 4 sample videos. *Measured* means FFmpeg/OpenCV numbers. *Observed* means what I saw on 2 fps sheets and 10 fps detail strips. The sound was measured, not heard.

Samples: s1 grocery-app promo (lavender, 16.9 s), s2 chat-app promo (midnight blue, 20.0 s), s3 meeting-app promo (grey to graphite, 23.5 s), s4 motion-designer intro (white, sky and night, 37.7 s). All four come from one creator. The files stay in the git-ignored `projects/_animation-train/` as study material. **Learn the style only. Never copy their brand names, app logos, the creator's handle, watermark, music or screens.**

## Measured

| | s1 lavender | s2 midnight | s3 graphite | s4 sky |
|---|---|---|---|---|
| Length | 16.9 s | 20.0 s | 23.5 s | 37.7 s |
| Received as | 368×368, 30 fps (WhatsApp copy, 1:1) | same | same | same |
| Ground (sampled) | `#f7e3fc` the whole video | gradient `#0a004a` → `#000014` | `#e0e0e0` 0–5.5 s, then `#2e2e2e` | `#fafafa`, sky `#62a4f2`→`#b6d4fa`, night `#000106`/`#021630` |
| Accents (sampled) | purple `#9b00ca`/`#7d01ce`, pink `#eb1783`, blue `#3b74f3` | blue `#4453e8`, `#3c73d4` | call blue `#2b6cef`, red `#d11a31`, green, cyan glow `#35c3cc` | blue `#2483ef`, coral `#e85c6d`, royal `#1b15d9`, cyan `#20a4e5`, gold cursor |
| Frames with no motion | 60 % | 41 % | 49 % | 26 % |
| Hard cuts | 1 (into the end card) | 1 | 1 | 6 (theme changes) |
| Loudness / true peak | −13.2 LUFS / +0.1 dBTP | −13.9 / +0.1 | −13.6 / +0.1 | −13.8 / +0.9 |
| Sound stops before the end | 2.4 s | 2.4 s | 2.4 s | 2.4 s |
| End card (black) | 11.4 → 16.9 s (5.5 s) | 13.3 → 20.0 (6.7 s) | 17.9 → 23.5 (5.6 s, glow on graphite first) | 31.7 → 37.7 (6.0 s) |
| Sound hits (transients) | 14 | 22 | 26 | 33 |

- There are almost no cuts. Each video is **one continuous animation**: one UI element turns into the next one through a ring pulse, a morph, a whip scroll or a blur-through. Only the move into the end card, and in s4 a change of theme, is a hard cut.
- The sound hits line up with motion starts within about 0.1–0.2 s (for example s1 at 1.28 s and the ring at 1.6 s, s2 at 4.06 s and the chips at 4.03 s). Every move gets a UI sound: a pop, a click, a whoosh or a tick.
- There is probably no voiceover (the text carries the message), but I could not hear it. The owner can confirm this.
- The samples clip (true peak above 0 dBTP). We keep their loudness (about −14 LUFS) with a −1 dBTP ceiling.

## The theme rule (why the colours always match)
1. **One product means one theme.** The ground is either a **light tint of the brand colour** (s1: purple brand on a lavender ground) or a **deep shade of it** (s2: blue brand on a midnight-indigo ground). s3 and s4 use neutrals (grey/graphite, white/sky) with the brand blue as the accent.
2. **Three accents at most**, all from the brand family plus one warm pop: purple + hot pink + blue (s1), blue only (s2), blue + red + green for the call buttons, and cyan only for glow words (s3), blue + coral + royal (s4).
3. **Cards are white on light grounds and glass or black on dark grounds.** A glass card is white at about 8 % on the deep ground with a 12 % hairline (sampled `#202339` over `#050032`). Secondary text is mid-grey (`#8a8392`, `#9c98a3`).
4. **Every video ends on black** with a white glowing wordmark, so all four feel like one series.
5. The watermark (the owner's own handle, never the samples') sits top right at about 35 % opacity, small, and stays on until the end card.

The four learned themes are in `aifilm/editor/animation.py` (`lavender`, `midnight`, `graphite`, `sky`). For a new product, `anim-themes --brand '#hex'` builds a theme the same way: the brand colour as the primary accent, and the ground as an 88 % white tint (light) or a 72–86 % black shade (dark).

## Motion: the house moves (counted frame by frame at 10 fps)

| Move | Seen in | Timing | Build |
|---|---|---|---|
| **Icon pop** | s1 0.0–0.3 s, s2 0.0–0.5 s | faint and blurred at 0.0 s, full at 0.2 s, overshoots about 6 %, settles by 0.3 s | `logo`: scale 0.8→1, blur 18→0, `back.out(2.2)`, 0.3 s |
| **Letters bounce in** | s1 0.7–1.0 s ("zep" + "to" land at different heights) | 0.05 s apart, 0.3 s each | letters from ±2 % with `back.out(3)` |
| **Hand-cursor tap** | s1 1.2, 2.6, 6.9 s; s2 sends; s4 social icons | glides in over 0.45 s, presses 0.08 s, and the target squashes to 93 % | `M.tap` |
| **Ring pulse** (links two states) | s1 1.6–1.9 s and 7.5 s | the icon shrinks into a glowing ring that grows about 2× and fades in 0.45 s, and the next element grows out of its centre | `M.ring` at the end of `logo` and `button` |
| **Search pill and typing** | s1 1.9–3.5 s | the pill grows from 10 % to full width in 0.3 s (`expo.out`), then a word every 0.09 s, each starting about 25 % bigger and blurred; the phrase changes by blurring out upwards | `search` |
| **Cards slide and whip** | s1 4.3–6.5 s | cards pop in from the right 0.1 s apart, whip-scroll 0.45 s with motion blur (about 9 px at 1080 px), the hero card zooms to centre in 0.4 s | `cards` |
| **Chip into CTA** | s1 6.6–6.9 s ("Place Order") | a small chip tilted −10° grows into the full pill in 0.35 s with a soft accent halo that breathes | `button` |
| **Status card and progress** | s1 8.0–8.8 s ("Rider Found") | the card blurs in, then the bar fills in the accent colour | `status` |
| **Tilt-blur exit** | s1 10.0 s ("Arriving in 10 minutes") | the pill tilts about −8°, grows 5 %, blurs and fades in 0.3 s | `pill` |
| **Glass rows stagger in** | s2 1.5–6.5 s, s3 dock | rows and chips 0.06–0.08 s apart, rising about 2 % | `chips`, `rows` |
| **Vertical whip scroll** | s2 7.5–8.0 s | the list scrolls 0.5 s with vertical blur and settles | `rows` |
| **Icons orbit** | s4 4.0–5.6 s | 3D-style PNG icons fly in from outside, blurred, into a ring around a black pill; the ring turns −70°→0° in 0.75 s, drifts, then spins away and shrinks | `orbit` |
| **Number roll and glow grow** | s4 5.5–7.0 s (980 → 1000 $) | the card blurs in, the value rolls in 0.65 s, the pill turns the accent colour, and the card grows to 1.45× with an accent glow | `counter` |
| **Word-by-word line** | s4 0.0–1.8 s, 22–31 s | a word about every 0.15 s; accent words come in larger (about 1.35×) and settle into the line | `words` |
| **Swap word** | s3 15.2–19.0 s ("Endless" + creativity / motion / vision) | the fixed word flies in; each accent word rises from below through blur and leaves upwards, about every 1.0 s; the last one grows the whole line 1.2× | `swap` |
| **Blur-through** (house exit) | every scene | grow 5–8 %, blur up to 16 px and fade in 0.25 s; the next scene enters sharp | `M.blurOut` |
| **End card** | all four | a white flash for 0.1 s, the white wordmark glows in (blur 18→0 in 0.3 s) and drifts to 1.05×; at about 1.7 s it dims to about 22 % and blurs, the platform mark pops in white (`back.out`), turns to brand colours about 0.6 s later and back to white near the end, with the handle below in small caps | `endcard` |

**Rule: nothing shakes and nothing sits dead.** Every element enters with an ease (overshoot for UI, `power3.out` for text), holds still and sharp, and leaves through blur. Scene lengths are 1.5–2.5 s for UI beats and 3–4 s for the text payoff. The video is 17–24 s (s4's longer self-intro runs 38 s).

## Transparency ("transparent thode aate hain")
- **Blur doubles as transparency**: elements fade in from about 0–60 % opacity *and* blurred, so they look see-through while they arrive. Exits do the same in reverse.
- **Glass cards** on dark grounds: white at about 8 %, a 12 % hairline and a backdrop blur. On light grounds the cards are near-opaque white (`#faf9fa`) with a soft tinted shadow.
- **Ghost text**: in the end card the wordmark stays at about 22 % behind the platform mark, and grey secondary lines sit at about 50 %.
- **Soft halos**: a radial accent glow at about 33 % opacity behind the CTA pill and the value card.
- **Motion blur** on fast moves (whips and orbits) instead of hard frames.

## Text
- **Type:** a clean geometric grotesque (it reads as SF Pro / Inter). We use **Inter** (installed; Devanagari needs a pairing from `pairings`). Weights: 800 for wordmarks and accent words, 700 for labels and headlines, 500 for UI text, 600 caps with +5 % tracking for handles.
- **Sizes (fraction of the frame width):** wordmark 7.5 %, payoff line 5.5–6 %, pill label 3.2–3.6 %, UI text 2.2–3 %, handle 2.6 % (end card) or 1.6 % (watermark).
- **Colours:** black-ink text on light grounds and off-white (`#e7e7ec`/`#f2f2f7`) on dark ones; **accent words** in the accent colour or cyan; white text on accent pills.
- **The white glow** (end card, s3 "thekrishray"): measured across the letters, the halo falls from 250 to about 90 (out of 255) at 4 % of the frame width and to about 22 at 8 %. Built as three shadows: `0 0 .12em` white 95 %, `0 0 .4em` 55 %, `0 0 .9em` 30 %. Coloured glow words use the same recipe in their accent (cyan `#35c3cc` in s3).
- Text arrives word by word (UI typing about 0.09 s per word, payoff lines about 0.12–0.16 s per word), never all at once.
- No subtitles unless the owner asks for them (owner rule, 2026-11-10).

## Icons and PNGs
- App and product icons are **squircles** (24 % corner radius) or **3D-style glossy PNGs** with a soft drop shadow (s4 orbit, s3 dock). The product's own screens and icons come from the owner (PNG with a transparent background; `cutout` makes one from a photo).
- Line icons inside pills and chips are white on the accent colour, or the accent on white. The runtime has built-in line icons (search, filter, bolt, check, send, plus, star, bike, bell, play, heart, user, camera).
- Social platforms use the owner's library (`editor/library/social/`) when a platform is named.

## Sound (measured, not heard)
- A music bed at about −14 LUFS that stops 2.4 s before the end (the end card ends in silence).
- A UI sound on every move: a pop on an icon pop, a click on a tap, a whoosh on a whip or ring, a tick on a number roll. We use recorded samples, never synthetic beeps, kept well under the bed (owner rule: quiet SFX).

## Do / don't
- Do: one theme per video, three accents at most, a continuous single-take flow, a blur-through between states, a cursor tap on every call to action, the black glow end card with the owner's handle.
- Don't: hard cuts inside the flow, shakes, more than three accents, stock-looking flat backgrounds, the samples' brands, handle or music, text that appears all at once.

## How the Animation Editor uses it
`spec.example.json` (a synthetic example) shows a full scene list. `anim-new` builds it, `anim-storyboard` makes one frame per scene for the owner, and `anim-render` renders only after `anim-approve` records the owner's words for that exact spec.
