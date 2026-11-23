# Product style: Food & drinks

Status: **not learned yet** (approval pending). Breakdown of the first 5 **packaged-food** samples (biscuits, cookies, chips, chocolate bars) done 2026-11-23 and shown to the owner. Waiting for the owner's approval. Drinks, restaurant food and more samples are still to come. Do not make a video in this category until the owner approves this sheet.

Products in this category: snacks, chai and coffee, cold drinks, packaged food, sweets, restaurant dishes.

## What the owner asked me to notice
_From the owner's own words (2026-11-23), before any sample. These are what to look for in the samples, not learned rules._
- **Open the food up, layer by layer:** a burger or sandwich comes apart so the bun, patty, cheese, onion, tomato and leaves each show on their own, then close again. Source: "food hai, burger types, to burger ke andar sandwich aur sabziyan, pyaaz, tamatar, jaise bhi hon, vo poora khol ke"
- **A drink bottle as the hero:** a close-up of the bottle and its name, the bottle turns, the cap opens, and the drink inside is shown in its real colour and flavour (for example a rich mango shake). Source: "drink ki bottle hai, to uska drink ka close-up karke, naam, usko ghuma ke, uska dhakkan open karke, aur uske andar ka color wala, flavor wala achha sa mango shake dikha ke"
- **Packaged food (2026-11-23):** for any packaged food (chips, biscuits, juice, anything), know how to zoom in and out, how to break it, how to turn it, which ingredients are inside and how to show them well, and when the text comes. Source: "kaise usko zoom out, zoom in karna hai, kaise usko break karna hai, kaise use ghuma ke dikhana hai ... uske andar kaun se ingredients hain, jo tumhein achhe se dikhane hain"
- **Chips (s4):** first the raw ingredient (the potato), then it moves and becomes the product, then it turns. Source: "pehle potato vo dikhaya hai, phir vo kaise move hota hai, phir kaise ghoom raha hai"
- **Biscuit text and roll (s2):** how the text comes in, and the biscuit being rolled. Source: "OREO mein, dekho kaise text aa raha hai. OREO ke biscuit ko roll kar rahe hain"
- **Cookie break (s1):** the biscuit breaks down the middle, the chocolate inside melts and pulls out, it comes close and goes far, how many parts it breaks into, the roll, and the close. Source: "biscuit beech se break ho gaya, usmein poora chocolate melt ho gayi hai ... close ho raha hai, door ho raha hai ... usmein kitne parts, use roll kiya ja raha hai"
- How food videos are made differs from makeup or automobile; learn it only from the owner's food samples. Source: "khane ki alag kaise banti hain"

## Samples
| # | File (in `projects/_product-train/food-drinks/`, git-ignored) | Brand or kind | What the owner likes in it |
|---|---|---|---|
| s1 | `s1/sample.mp4` | Chocolate cookie with a molten centre (made with AI video, 9:16) | the break down the middle, the chocolate melting and pulling out, close and far, the parts, the roll, the close |
| s2 | `s2/sample.mp4` | Sandwich biscuit, new flavours (3D, 9:16) | how the text comes in, the biscuit rolling |
| s3 | `s3/sample.mp4` | Caramel biscuit brand film (2D motion graphics + product photos, 16:9) | (sent with the set; mostly type and brand motion) |
| s4 | `s4/sample.mp4` | Potato chips, 3 flavours (3D packet, 16:9) | the potato first, then it moves, then it turns |
| s5 | `s5/sample.mp4` | Chocolate bars with biscuit pieces (2D/3D flat-lay motion graphics, 16:9 letterboxed) | (sent with the set) |

## Measured (FFmpeg and OpenCV, from the samples)
_Length, aspect, frame rate, cuts, colour of the background and the product, loudness, and when the sound stops._

| # | Length | Size, fps | Hard cuts (FFmpeg scene > 0.25) | Scene changes counted by hand | Loudness | Background (sampled) |
|---|---|---|---|---|---|---|
| s1 | 10.0 s | 720×1280, 60 | 8 (1.0, 3.0, 4.0, 5.0, 6.2, 7.3, 8.1, 8.9) | 10 shots, ~1 s each | −8.2 LUFS (very loud) | deep purple with gold light streaks; cookie `#a67b57` |
| s2 | 15.8 s | 720×1280, 25 | 0 | 6 beats, joined by whips, splash wipes and diagonal colour wipes | −14.1 LUFS | royal blue gradient `#0734ad` |
| s3 | 50.0 s | 1920×1080, 24 | 5 | ~20 beats (most are type moves on a flat colour field) | −12.2 LUFS | brand red; yellow `#fad01d` and caramel `#cf8b3e` per product |
| s4 | 19.8 s | 1280×720, 60 | 1 (8.3) | 5 beats: potato, red packet, green packet, yellow packet, 3-pack | −9.2 LUFS | red `#8a0000` → green `#447214` → yellow `#f7b212`, one per flavour |
| s5 | 20.6 s | 1280×720 letterboxed, 25 | 0 | 8 beats, joined by stripe and diagonal wipes | −12.0 LUFS | yellow and white stripes on light grey paper |

Shared numbers: every sample is one flat or gradient colour field per flavour, never a real location. One beat lasts **1–3 s** (s1 about 1 s, the others 2–3 s). Packaged-food ads run **10–20 s** (s3 at 50 s is a brand film).

## Observed (frame by frame, from the samples)

### s1: chocolate cookie, 10 s, 9:16 (AI video)
| Time | What happens |
|---|---|
| 0.0–0.25 | The whole cookie stands centred on purple, a crack already down the middle. |
| 0.25–1.0 | It **splits in two**, and thick molten chocolate stretches between the halves (a "cheese pull"); crumbs fly. |
| 1.0–2.0 | It **shatters into ~10 pieces** that fly at the camera with motion-streak light trails: an explosion of parts. |
| 2.0–3.0 | A whole cookie flies diagonally, riding a **ribbon of liquid chocolate**. |
| 3.0–4.0 | Front view: the cookie **cracks open** and chocolate erupts out of the crack. |
| 4.0–5.0 | **Macro zoom in**: the two halves pull apart, with chocolate strands between them filling the frame. |
| 5.0–6.2 | The cookie floats centred in a **chocolate swirl vortex** that turns around it (a slow orbit). |
| 6.2–7.2 | Macro top shot: chocolate **pours** onto the cookie surface and makes a crown splash. |
| 7.3–8.9 | **Pack reveal**: the box with a broken cookie on a dark floor, inside a glowing ring of light and dust; then a low close-up of the box next to a cookie oozing chocolate. |
| 8.9–10.0 | The box tumbles in while cookies fly in and **arrange into an arc** behind it: the hero end frame with cookies at its foot. No text except the pack. |

### s2: sandwich biscuit, new flavours, 15.8 s, 9:16 (3D)
| Time | What happens |
|---|---|
| 0.0–1.6 | Calm open: one biscuit centred, the question text "LOVE ME?" above it in white heavy rounded caps (~⅙ of the width), a slow float. |
| 1.6–2.0 | The biscuit **rolls on its edge** (turns 90° to show its side). |
| 2.0–4.7 | It **flips to the new flavour** (hazelnut) in an explosion of hazelnut splash; a jar of spread and a spoon float in; hazelnuts fly in the background with depth blur. |
| 5.0–7.0 | Text "MEET MY NEW / HAZELNUT / SIDE" builds in above (a small line plus one big word); a second biscuit of the original flavour **rises from below**, and both float stacked. |
| 7.0–8.0 | Text clears; the biscuits **spin and whip** out into the next beat. |
| 8.0–9.7 | Flavour family: biscuits of both flavours, curls of chocolate and nuts float around "OREO'S NEW FLAVORS" in tilted type; a **diagonal two-tone wipe** divides the blue. |
| 10.0–11.7 | "FEELING DARK OR NUTTY?" plus big "TWIST ON IT" in **chocolate-textured 3D letters**, with a chocolate splash. |
| 12.0–14.7 | The background turns empty; the two **packs slide in on a diagonal** and line up stacked; "TRY NEW" pops above; flavour tags (DARK, HAZELNUT) slide out from the packs. |
| 15.0–15.8 | End: one biscuit centred, the slogan "Stay playful" under it. |

### s3: caramel biscuit brand film, 50 s, 16:9 (2D motion graphics + product photos)
| Time | What happens |
|---|---|
| 0–2.5 | The logo **assembles letter by letter**, the letters falling and bouncing into place; the brand mark pops on top. |
| 2.5–5.5 | The pack slides in; the logo on the pack **morphs** into the clean brand logo. |
| 6–8 | Zoom out to a **wall of all the products** (packs, jars, single biscuits) in a flat lay. |
| 8.5–10 | Hard switch to a yellow field: "Unique taste" with **bouncy letters** that drop in one by one. |
| 10.5–13 | A spread jar **drops in from the top**, turns to show the back, and the **background changes colour** to match each variant (Crunchy yellow, Smooth caramel). |
| 13.5–14.5 | Biscuits fly through **milk-splash blobs** (flat white shapes). |
| 14.5–35 | Brand values as pure type on red or white (a counter "62 → 70 countries", "Unique typeface", "friendly", "unexpected", "Delight in every bite!"); circle and blob wipes carry one beat into the next. |
| 36–44 | "Unique moments" with social like and heart badges popping around it, then phone screens of people eating. |
| 44.5–50 | The logo assembles again and holds as the end card. |

### s4: potato chips, 3 flavours, 19.8 s, 16:9 (3D)
| Time | What happens |
|---|---|
| 0.0–1.8 | **The raw ingredient first**: one potato floats centred on a red radial gradient, gently turning. |
| 1.8–2.1 | The potato **pops into the packet**: the pack scales up from small (a burst) with chips and chillies bursting out around it. |
| 2.1–5.0 | The chilli pack floats, slightly tilted, slowly **swaying in 3D**, with chips and red chillies (the flavour ingredient) drifting all round in depth. |
| 5.0–5.7 | The pack **spins on its vertical axis** (back panel, then side); during the spin the background **cross-fades to green**, and it lands as the mint pack with mint leaves around. |
| 6–8 | The mint beat, the same float. |
| 8.3 | A cut to yellow: the lemon pack with lemon slices and chips. |
| 11.5–12.5 | The lemon pack spins, and the other two packs **slide out from behind it** into a row of three. |
| 12.5–14.5 | All three flavours' ingredients (chillies, mint, lemon) swirl round the row. |
| 14.5–19.8 | The title "Yummy Potato Chips" **types on** above, then "in 3 flavours" under it; the end frame holds ~5 s. Its text is small and plain, the weakest part of the set. |

### s5: chocolate bars with biscuit pieces, 20.6 s, 16:9 (flat-lay 2D/3D)
| Time | What happens |
|---|---|
| 0–1.0 | The brand names in their own fonts on **vertical colour stripes** that wipe in. |
| 1.5–2.0 | The **ingredients line up** from the top: a biscuit, a white bar, a cookie, a dark bar. |
| 2.5–4.5 | The biscuit **breaks into crumbs** (with a cartoon burst) that scatter. |
| 5.0–7.0 | The crumbs **rain onto the dark bar** and stick into it, so the bar now shows the biscuit pieces; then zoom out. |
| 7.5–10.5 | A diagonal wipe; the cookie breaks into 4 quarters, then into crumbs. |
| 11.0–12.5 | The crumbs land in the white bar; a little sparkle "ding" tick. |
| 13–15.5 | Both bars appear with **a bite taken out**, on ice-cream sticks, over stripes that slide. |
| 16–20.6 | The two packs swap and slide in; blue blob bursts; a stack of the two packs with four words **typing in** along the bottom (SMOOTHER, CHUNKIER, NEWER, FUNKIER). |

### What the 5 have in common (house moves for packaged food)
- **Ingredient → product:** every sample shows what is inside or what it is made from before, or as, the product appears (s4 potato, s1 molten chocolate, s2 hazelnut jar, s5 biscuit becoming crumbs in the bar).
- **Break it open:** s1, s5 and s2 each break, split or bite the product to show its inside.
- **Float in zero gravity:** the product hangs mid-frame with a slow sway or turn. Ingredient pieces drift around it at three depths (large and blurred in front, sharp in the middle, small behind).
- **One colour field per flavour**, taken from the flavour (chilli red, mint green, lemon yellow, hazelnut brown on blue); a flavour change = a colour change.
- **The pack is always the last hero:** every ad ends on the pack or packs, often several flavours in a row, plus one short line.
- **Text is short and big:** 1–4 words per beat, in heavy rounded caps or a playful font, either a question/teaser or a flavour name; never a paragraph.

## Move library (pooled from all samples)
_Every move seen in this category's samples, merged across all of them: what it is, how it is done, timing, which samples show it, and which kind of script line it suits. The Product Animator picks from this whole library for each script; the owner does not name a sample. "Build" says how our pipeline (HyperFrames page + cutouts + FFmpeg) makes it, or whether it needs a 3D or AI-video tool._

| Move | How it is done | Timing | Seen in | Suits a line about | Build |
|---|---|---|---|---|---|
| **Ingredient first** | the raw ingredient alone, centred on the flavour colour, slow turn or float | 1.5–2 s | s4, s5 | what it is made from, "pure", "real" | cutout + slow rotate/scale: yes |
| **Ingredient → pack pop** | the ingredient bursts and the pack scales up from 0 in its place with pieces flying out | 0.3–0.5 s | s4 | the product name, first reveal | cutouts + scale/burst + particles: yes |
| **Zero-gravity float** | product mid-frame with a slow sway and tilt (±8°); ingredients drift at 3 depths, the front ones big and blurred | 2–3 s per beat | s1, s2, s4 | any feature or flavour line | cutouts with parallax + blur: yes |
| **Pack spin + flavour swap** | the pack turns on its vertical axis; the background cross-fades to the next flavour colour mid-spin; it lands as the next flavour | 0.6–0.8 s | s4, s2 | "also in …", the next flavour | 2.5D: squeeze the width to 0 and swap the face: yes. A true 3D turn needs a 3D tool |
| **Edge roll / flip** | a round biscuit turns 90° onto its edge and flips to show the other side or the new flavour | 0.4 s | s2 | a new flavour, "the other side" | scaleX flip + side strip: yes |
| **Split with a pull** | the product splits down the middle; the filling stretches between the halves | 0.7–1 s | s1 | the filling, "inside", "molten", "cream" | two half cutouts + an SVG stretch shape: approximate. A realistic pull needs AI video |
| **Shatter into pieces** | breaks into 4–10 pieces that fly apart (to the camera with streaks, or flat into crumbs) | 0.5–1 s | s1, s5 | "crunchy", "chunks", the bite | pre-cut piece cutouts + GSAP physics: yes |
| **Pieces into product** | the crumbs rain down and stick into the bar or base, showing it contains them | 1–1.5 s | s5 | "with real biscuit pieces" | yes |
| **Bite mark** | the product shown with a bite taken out | 1–2 s held | s5 | taste, "every bite" | a bite mask on the cutout: yes |
| **Macro zoom-in** | the camera pushes until the inside texture fills the frame | 1 s | s1 | texture, filling, richness | needs a high-res texture photo; yes as a scale push |
| **Pour / drip / crown splash** | liquid (chocolate, milk, sauce) pours onto the product and splashes up | 1 s | s1 | sauce, coating, "loaded" | flat 2D splash shapes (s3 style): yes. A realistic liquid needs AI video or a licensed clip |
| **Splash explosion around the product** | the product bursts out of a splash of its flavour colour | 0.5 s + hold | s2, s1 | the flavour reveal | 2D splash shapes or licensed splash PNG sequences: yes |
| **Vortex / orbit** | the product holds centre while a ring or swirl of the ingredient turns around it | 1–1.5 s | s1, s4 (end) | the "hero" moment, richness | rotating ring of cutouts: yes |
| **Light ring pack reveal** | the pack on a dark floor inside a glowing ring of light and dust | 1–1.5 s | s1 | the pack name, launch | yes (glow ring + particles) |
| **Packs slide into line-up** | packs slide in on a diagonal or out from behind the hero into a row or stack, one per flavour | 0.5–1 s | s2, s4, s5 | the range, "3 flavours", the close | yes |
| **Products arrange into a frame** | products fly in and arrange in an arc or wall behind the pack | 1 s | s1, s3 | the end card, the whole family | yes |
| **Colour-field change** | a flavour change = a background change (cross-fade, diagonal two-tone wipe, stripes, circle or blob wipe) | 0.3–0.5 s | all | a new flavour or new idea | yes |
| **Teaser text** | a 2-word question above the product ("LOVE ME?"), heavy rounded white caps, ~⅙ of the width, while the product is calm | 1.5 s | s2 | the hook | yes |
| **Big word + small line** | a small upper line plus one huge word ("MEET MY NEW / HAZELNUT / SIDE") building over 0.3 s | 2 s | s2, s3 | the flavour or claim | yes |
| **Bouncy letter drop** | letters drop and bounce into place one by one, or assemble the logo | 0.5–1 s | s3 | the brand name, a value word | yes |
| **Ingredient-textured title** | the title letters are made of the food (chocolate 3D letters) with a splash | 1.5 s | s2 | the key claim | needs a texture-filled font; approximate in 2D |
| **Counter** | a number counts up in the type | 1.5 s | s3 | numbers ("70 countries") | yes |
| **Typed end line** | the end line types on above or below the pack row | 1–2 s | s4, s5 | the close, the CTA | yes |
| **Hero end frame** | the pack (or row of packs) plus one slogan, held 1–5 s | 1–5 s | all | the close | yes |

**Default order for a packaged-food script (from the pooled samples):** hook (teaser text over a calm product, or the ingredient first) → reveal the product (ingredient → pack pop, or a splash) → show the inside (break, split, shatter or pour, zoom in) → one beat per flavour or feature (float plus ingredients, colour-field change, pack spin) → the range line-up → hero end frame with one slogan. Fit it to the script's lines; never copy one sample's order whole.

**What we can make now and what we cannot:** the 2D/2.5D moves (floats, pops, spins by squeeze, breaks into pre-cut pieces, colour wipes, all the text moves, line-ups) are made with HyperFrames and clean cutouts. Photoreal liquid (molten chocolate pulls, real pours) and a true 3D packet turn, as in s1, s2 and s4, are made with AI video or 3D tools that this project does not have yet. For those, use the flat-splash version (s3, s5) or ask the owner for a clip or tool. Never pretend a 2D version is the 3D one.

## Brand styles in this category
_A brand the owner names, for example "Nike jaisa chahiye", gets its own sheet in `brands/<brand>/STYLE_SHEET.md` when the owner teaches it._

## Rules from the owner's corrections
_Every correction for this category, dated, with the owner's words._
