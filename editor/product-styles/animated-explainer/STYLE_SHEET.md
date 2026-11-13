# Product style: Animated explainer (corporate SaaS motion graphics)

Status: **breakdown done, waiting for the owner's approval** (2026-11-13). Learned from 2 owner samples, both kept as study material in the git-ignored `projects/_product-train/`:
- **Sample 1, look A, "premium dark":** a 52 s explainer for an AI product-management tool (`explainer-collato/`). The owner called it the best animation sample.
- **Sample 2, look B, "flat line-art":** a 98 s enterprise IT (virtual desktop) explainer (`explainer-jos/`), sent by the owner as "sab animation h ye".
- **Sample 4, look D, "soft pastel SaaS":** a 144 s enterprise procurement-software explainer (`explainer-aerchain/`). The owner asked me to learn its theme, text, animation and effects, what comes on which words, and the ways each effect is built.
- **Sample 5, look E, "monochrome with one red accent":** a 52.6 s corporate-training explainer (`explainer-training/`), which the owner called short and very good. The owner asked me to study its background, how it animates, its faces, bodies and text, its colour and how the theme is kept.
- **Sample 3, look C, "health-tech navy and sky":** a 110 s dental AI software explainer (`explainer-dental/`). The owner asked me to notice the cartoon faces, the single theme, spoken words becoming text, the same colours for the ground, text and bubbles, the doctor tapping screens that grow, the graphs, the light streaks, the doctor's actions and the names, and every transition.

The line-by-line table, the measurements and the theme rule just below are sample 1 (look A). Sample 2 (look B) has its own section further down. **Learn the style, never the sample's brand, logo, script, characters, UI or music.**

How it was studied: 1 fps and 4 fps frame sheets of the whole video, full-resolution stills for fonts and colours, OpenCV colour sampling, FFmpeg loudness, silence and cut detection, and word timings from offline speech recognition (pocketsphinx). The recognition was rough, so the script below was **reconstructed** by matching it to the on-screen text. Its word times are good to about 0.2 s; some words are my reading and are marked (?). The sound was measured, not heard.

## What the owner asked me to notice (owner's words, 2026-11-13)
- Whatever is said arrives on screen at that moment, as text or as a visual, and animates right then: people's icons with faces when people are named, a globe when "globe" is said, the logo and then the logo's name, stars when "five star" is said.
- When text comes in and when the font changes.
- The colour theme: purple sometimes, white sometimes, but the theme is never left. No random colours. The look must be professional and corporate.
- The whole video: text, font, background, what animates when, and what is said on which line.

## Measured
| | Value |
|---|---|
| Format | 1920×1080 (16:9), 25 fps, 52.0 s |
| Hard cuts | **0** (the scene detector found none: every change is a wipe, a camera move or a morph) |
| Voice | starts at 0.1 s and runs nearly without a gap to 49.0 s, about 2.6 words per second |
| Loudness | −19.1 LUFS, LRA 3.1 LU, peak −3.6 dBFS (calm VO plus a soft bed) |
| Ending | silence for the last 2.1 s (49.98 → 52.1 s) on the held CTA |
| Dark ground | radial purple: deep `#150728` corners, body `#3d1f6c`–`#4b247e`, a lighter `#5c329a`–`#6b39b8` glow behind the subject |
| Light ground | off-white `#f8f8f8`, white cards `#fefefe`, soft lilac shadows `#dfd8e3` |
| Text | white on purple, dark slate `#49475f` on white, grey `#908f9b` for UI text |
| Accents | purples `#622caf`, `#7842ae`, lilac `#b668df`/`#c184e1` (buttons), CTA purple `#654db3` |
| Brand gradient | violet `#7b5cf5` → pink `#f2788a` → peach `#f6b38e`, **only** on the logo, its orb and the wordmark |

## The theme rule (why it looks corporate)
1. **Two grounds, one family:** deep purple scenes and off-white scenes alternate. The rhythm is dark 0–14 s, white 14–17.5, dark 17.5–23.3, white 23.3–28, dark 28–46, white 46–52. The switch always comes through a wipe in the theme's own colours.
2. **Every colour on screen comes from the brand:** purples, lilac, white, slate and grey. The warm pink and peach appear only inside the brand gradient (the logo, the glowing orb, the wordmark). Real product icons (Docs, Sheets, PDF, Figma, Jira, Notion) keep their own small colours, and that is the only exception.
3. **One type family**, a bold geometric sans (it reads like Gilroy or Gordita; the closest open fonts are Plus Jakarta Sans and Outfit). Headlines are bold, sentence case, white or slate, usually 2 lines. UI text uses the same family at small sizes. The "font change" is **weight and size**, not a new typeface.
4. **Soft depth:** cards float with large soft shadows, the dark scenes have a vignette and light glows, and glass and neon edges appear on hero UI (the timer card).
5. **Faces are real photos in round badges** (a thin white ring, sometimes three small stars above them), never cartoons.

## Line-by-line: what is said, what appears, what moves
| Time (s) | Spoken (reconstructed) | On screen at that moment | Motion |
|---|---|---|---|
| 0.1–1.1 | "As a **product manager**," | a laptop with typing hands and app windows on purple; a pill badge with a real face and **"Product Manager"** | the windows fly in tilted in 3D; the badge pops in at 0.5 s, 0.15 s before the words |
| 1.6–2.9 | "your goal is to **make an impact**." | the headline **"Make an impact"** (2 lines, white bold), and a curved peach line that draws around the laptop | the headline slides in at 2.0 s, on "goal is to", about 0.4 s before "make"; the line draws for 1 s |
| 3.4–5.6 | "But **tedious chores** like **getting updates**" | the camera flies off the laptop into a dark space full of floating DOC, PDF, PRD, Sheets and calendar cards and task lists | at 3.5–4.0 s the scene tilts and recedes; cards fly in with parallax, 0.1 s apart, about 0.3 s before "tedious" |
| 5.7–8.2 | "and **endless documentation**, they eat up most of your day (?)." | more documents pile up (PDF Requirements, PRD) | slow drift; the pile grows on "documentation" |
| 8.2–8.7 | — | everything sweeps out to the left | a fast push with motion blur |
| 9.0–13.1 | "**Imagine** having more time to focus on the parts of your job you actually enjoy." | a rising area chart; **people's face badges with 3 stars** pop up one by one along it; a glowing brand orb travels along the curve | the chart grows from left to right on "imagine"; a badge every 0.5 s; the orb rolls from 11 s to 13.8 s |
| 13.9–15.5 | "Introducing **Collato** (the product name)," | white ground; the orb becomes the **logomark**, then the **wordmark** slides out of it | white wipe at 14.0 s; mark at 14.25 s; the name reveals at 15.0–15.5 s, landing on the spoken name (15.2 s) |
| 15.8–17.5 | "the **AI assistant for product teams**." | the logo moves up; the tagline in 2 lines; an "Ask anything" input with an **Ask** button; a cursor | the tagline lands on "AI assistant"; the input rises with a soft shadow |
| 17.5–19.3 | "What used to take **hours**" | a purple wave wipes from the right; a neon-edged **timer card "4 hr 35 min 58 sec"** that ticks | the wave lasts 0.7 s; the timer counts up live |
| 19.3–20.8 | "will take **seconds**." | a magic wand with sparkles hits the timer, and it drops to **"0 hr 0 min 01 sec" → "03 sec"** | the wand swings at 18.5–19.5 s; the hours and minutes dim; the seconds tick on "seconds" (19.8 s) |
| 20.8–22.5 | "**Connect your tools**" | tool icons in a column on the left (Notion, Jira, Docs, Confluence, Figma); a settings panel with checkboxes; a Connect button that the cursor clicks; a wireframe **brain** in a circle | the icons stagger in from the left; the checkboxes tick; the click lands about 21.7 s |
| 21.8–23.2 | "and **let Collato handle the rest**." | the tool icons fly into the brain, and its nodes light up as a network | the icons arc into the brain at 22.5–23.2 s |
| 23.3–25.0 | "**Need to draft release notes**," | a white wave rises from the bottom; the headline **"Need to draft release notes?"**; the input types "Draft a release note for …" | the wave at 23.3 s; typing letter by letter about 0.07 s per character |
| 25.1–27.0 | "**a requirements doc, or a help article**?" | the headline swaps to **"a requirements doc, or a help article?"**; typing continues | the old line fades up and the new one fades in on "requirements" |
| 27.0–28.0 | "**Just ask Collato**." | the camera zooms into the input (about 2×), **"Just ask Collato"**, and the cursor clicks **Ask** | the zoom from 26.75 s; the click on "ask" (27.7 s) and the button presses |
| 28.0–30.9 | "Collato goes through **hundreds of sources** (?)" | a purple ground; the generated **release-note card** with a list of sources rises | the card rises at 28.25–28.75 s; the cursor hovers over the sources |
| 31.0–34.6 | "like **Confluence pages**, Figma files, **notes** and **Jira tickets**" | source cards fly in from the right, each with the named tool's icon (Technical specifications, Communications plan, Epic: Tagging feature) | **one card per named source, on its word**, staggered about 1 s |
| 35.2–36.9 | "or **wherever you store your product knowledge**." | the cards fan out into a collage (Competitor analysis, Design specifications, …) | the cards spread out, then all blur away at 36.5 s |
| 37.4–39.0 | "With Collato **by your side**," | a glowing brand **orb**, then the logomark on deep purple | the orb grows from a point with a soft glow |
| 39.5–41.0 | "you can **focus on what matters most**:" | **"Focus on what matters most"** slides out to the right of the mark | it lands on "focus" (39.75 s) |
| 41.4–42.9 | "**shaping your product**," | a brain in a circle sits on a "plug" with the logo (a product lightbulb); the title **"Shaping your product"**; face badges orbit | the title lands on "shaping"; the badges pop in one by one |
| 43.0–44.2 | "**guiding your team**," | the title swaps to **"Guiding your team"**; the badges link with arrows | the title crossfades on the word |
| 44.3–46.0 | "and **making an impact**." | **"Making an impact"**; the arrows pass between the people | the title crossfades on the word |
| 46.0–48.0 | "Visit **collato.com**" | a white wave from the bottom; the orb drops in; a URL pill types **"collato.com"**; the wordmark reveals | the URL types on "dot com" (47.4 s) |
| 48.1–52.0 | "and **start for free today**." | the URL pill morphs into the CTA button **"Start for free today"** under the logo | the morph on "start" (48.1 s); a still hold, and silence from 50 s |

## Timing rules (from the table)
- **Every named thing appears on its word.** Visuals and scene changes arrive **0.1–0.4 s before** the word, so the picture is ready when it is said. Headlines land **on** their keyword and swap phrase by phrase.
- People named → real **face badges** (round, white ring, sometimes stars). A tool or app named → its **real icon**. A time or number said → a **live counter**. An action said ("ask", "connect") → a **cursor clicks** it on the word. The brand said → the **logo and then the name**.
- There is **one idea per beat of 1.5–3 s**; nothing sits still for more than about 3 s.
- **No hard cuts.** The changes are colour waves (purple from the side, white from the bottom), camera fly-throughs, zooms into the UI, and morphs (orb → logo, URL → button).

## Motion language
- Eases are smooth and expensive: a long `power3/expo.out`, no bounce on the text, and a gentle overshoot only on the badges and icons.
- The camera is always moving slowly (drift and push), with parallax between the layers in the 3D card scenes.
- Text slides in a short way with a fade (it never pops), line by line.
- Glows are soft: the brand orb, the neon edge on the timer, the sparkles on the wand.

## Sound (measured, not heard)
- A calm, clear voiceover at about 2.6 words per second over a soft bed, about −19 LUFS here. For our reels we deliver −14 LUFS with a −1 dBTP ceiling.
- The ending is silent for 2 s on the CTA.

## Sample 2, look B: flat line-art enterprise explainer (98 s)

### Measured
| | Value |
|---|---|
| Format | 1920×1080, 30 fps, 98.1 s |
| Hard cuts | **0** (every change is a wipe, a draw-on, a zoom or a morph) |
| Voice | nearly continuous, 0.7 → 96.4 s, about 2.7 words per second |
| Loudness | −8.8 LUFS, peak +3.1 dBFS (very loud, it clips; we keep −14 LUFS / −1 dBTP) |
| Ground | **white `#ffffff` 74 %**, with soft **mint glows** in the corners (`#dcf6f2`, 13 %) that drift slowly |
| Accents | **teal `#11ebc4`/`#2ee4c3`**, **ocean blue `#11a0c3`**, light teal `#87e8d2`, a little green `#45dc82` |
| Lines and text | dark slate `#3d4752` for outlines and headings, grey `#838990` for small labels, light grey `#b3d7d1` for unfinished outlines |
| Skin | peach `#f8c49a` (the hands and the faces of the drawn people) |

### The theme rule (look B)
1. **White ground with mint glows, nothing else.** There is no dark scene at all. The only full-colour frames are the **wipes**: a teal circle iris, teal and blue diagonal stripes, and a teal diamond.
2. **Two accents only, teal and blue.** Everything is drawn in slate line-art and **filled with teal or blue only**, plus peach skin. Real app logos (Gmail, Office, Salesforce, Drive) appear only when apps are named.
3. **People are flat drawn characters with faces** (teal and blue clothes), shown at desks, in round or square frames with a label pill ("IT Department", "Team Lead", "IT Security Specialist", "IT Manager"). There are no photos.
4. **One clean sans** for everything: slate headings, small grey icon labels, and dark pill labels with white text.

### Line by line (spoken words reconstructed from rough recognition; times ±0.3 s)
| Time (s) | Spoken | On screen | Motion |
|---|---|---|---|
| 0.7–3.9 | "With the rise of **hybrid work** as a long-term business strategy," | people in square frames (drawn, with faces) and the words **HYBRID / WORK / CULTURE** | the frames pop in one by one from 0.5 s; the letters drop in one by one on "hybrid" |
| 4.6–8.6 | "managing complex and distributed **end-user devices** is challenging." | three people stand on an **"IT Department"** pedestal; monitors, laptops, phones and app windows fill the screen around them | the device outlines **draw on** as strokes and multiply until the screen is crowded ("challenging") |
| 9.0–14.5 | "You need a **resilient**, **agile** and **efficient** model to match the changing needs." | a teal circle iris wipe; one tower drawn in line, with a **Resilient**, **Agile** and **Efficient** label and icon each popping beside it **on its word**; more towers draw on into a city | the strokes draw at about 0.5 s per building; the labels pop 0.1 s before their words |
| 15.2–19.0 | "You need a tool to streamline your existing **IT ecosystem**." | a mind map of labelled icon cards (cybersecurity, work from anywhere, multiple devices, app modernisation …) | the cards blur in and connect on "ecosystem" |
| 19.1–23.0 | "That's why you need a **Virtual Desktop Infrastructure**," | a laptop outline draws on; the name **types letter by letter** on screen; 4 feature icons pop around it: Highly Secure, Centralised Management, Seamless Collaboration, Cost Efficient | typing about 0.05 s per letter, starting on "virtual"; the icons 0.25 s apart |
| 24.0–27.0 | "… designed and architected (?) for every industry (?)" | hands on a tablet dashboard; the industry labels Healthcare, Education, Manufacturing, Retail, Finance and Construction, each with an icon | the labels pop in one by one around the tablet |
| 27.0–29.9 | "**secure** distributed (?) **cloud-based applications**," | **"Secure Distributed Workspace"** types in the centre of a dotted orbit ring of small icons | the ring rotates slowly; the icons fade in around it |
| 29.9–34.6 | "deploying **seamless integration** and user experience to more than **30,000 users**." | a workspace window with a grid of **real app logos**, then a network of many face avatars linked by lines | the grid fills tile by tile on "integration"; the camera pulls back through the network on "30,000 users" |
| 35.0–39.4 | "Our VDI solutions provide end-to-end **security** measures," | a woman at a desk with a laptop and a **"Team Lead"** pill; a big **padlock** draws on behind her | the padlock draws on with the word "security" (38.2 s) |
| 39.7–43.3 | "**flexible scaling capabilities** and **simplified desktop management**," | **"Flexible Scaling Capabilities"** types, then **"Simplified Desktop Management"**; employee cards A to D arrive with arrows | each headline types on its first word |
| 44.0–48.4 | "enabling you and your team to **work from anywhere**, on any device," | a man on a beach under a palm tree with a laptop, linked by a dotted line to a woman at an office desk | the dotted line runs from the beach to the office on "anywhere" |
| 49.0–52.0 | "with a high-definition experience and seamless **collaboration**." | a dashboard monitor surrounded by people in frames with chat bubbles | the bubbles pop in turn, like a conversation |
| 53.0–58.5 | "In the face of ever-growing **cyber threats**, we **safeguard** your IT infrastructure" | an **"IT Security Specialist"** with a tablet; a **globe with a lock** appears beside her, then **Cloud Based** and **On-Premise** labels with server icons | the globe arrives on "safeguard"; the labels draw on |
| 59.2–63.0 | "…and the mission-critical **business applications**," | circuit lines carrying app nodes; two people point at a large app grid | the nodes travel along the circuit lines |
| 63.4–65.0 | "assuring complete **data protection**." | a **"Data Protection"** lock module with icons orbiting it | the module scales in; the icons orbit |
| 65.6–69.4 | "Act now. Free up your **IT teams** to focus on higher-value tasks" | an **"IT Manager"** in a frame with devices around him, then pointing at charts | the charts draw on as he points |
| 70.4–73.0 | "by centralising end-user management." | (the manager scene continues) | a **teal diamond wipe** at about 73 s |
| 73.6–75.7 | "No matter the **size of your organisation**," | a wall of many face avatars (the organisation's size) | the faces fill the frame, scaling in |
| 76.1–78.3 | "choose from **cloud-based** and **on-premise** solutions" | a **Cloud Based** card, then an **On-Premise** card, over the faces | each card lands on its word (76.8 s, 77.6 s) |
| 79.0–84.5 | "to support end-user devices and managed services, and **quickly customise** everything" | rows of people with devices and a big drawn hand that **ticks the checkboxes**; a settings dashboard | each tick on the beat; the hand slides in from the side |
| 84.5–86.2 | "to maximise the **productivity** of your team." | a woman at a desk with a **5-star rating** bubble | the stars pop in |
| 86.5–90.0 | "…optimise your **technology investments**" | **teal and blue diagonal stripes** wipe; a skyline **draws on** in line; a **$ coin** rolls in | the strokes draw building by building; the coin on "investments" |
| 90.0–93.5 | "and **scale your business exponentially** with greater cost efficiency." | the skyline **fills with teal from the bottom up** | a liquid fill from the base on "scale … exponentially" |
| 93.5–98.0 | "**Contact us** to find out more today." | concentric teal squares morph into the **square logo**; a dark **"Contact us today"** button; the URL | the logo scales in; the button lands on "contact"; the URL types last |

### Signature moves (look B)
- **Line draw-on:** buildings, devices, padlocks and laptops are drawn as strokes in real time (about 0.4–0.6 s each), then sometimes **filled with teal**.
- **Typewriter headlines** in slate, typed letter by letter on the spoken phrase.
- **Icon and label pops:** each named quality (Resilient, Agile, Secure, Cloud Based) is a line icon plus a word that pops on its word.
- **Orbits and networks:** dotted rings with icons, and avatars linked by lines.
- **Colour wipes** (circle iris, diagonal stripes, diamond) are the only big blocks of colour.
- **The drawn hand** taps and ticks in the UI scenes.

## Sample 3, look C: health-tech explainer, sky-white and deep navy (110 s)

### What the owner asked me to notice (owner's words, 2026-11-13)
"agr face nhi h to kese usne cartoon face use kie h, kese 1 hi theme rkh rkhi h, kis trh se jo bolra h wo text a rhe h, color same h bg ka text ka bubble same theme chlri h, kese jb explain kr rhe h to dr. ek ek screen ko click kr rhi h to badi ho rhi h images, kese graphs ate h lightning ati h, kese dr. chize kr rha h unke nam or sbkuch ... ek ek transition effect theme"

### Measured
| | Value |
|---|---|
| Format | 1920×1080, 30 fps, 110.0 s |
| Hard cuts | **0** |
| Voice | 0.7 → 106.7 s, about 2.5 words per second; silence for the last 1.7 s |
| Loudness | −17.9 LUFS, LRA 3.0, peak −3.6 dBFS |
| Light scenes (121 samples) | white `#f8fafd` 61 %, **sky-blue glow `#d8e9f4`** 22 %, navy text and pills `#193447`, accent blue `#1067a7`, teal `#65c1d3`, pink skin `#eba1ab` |
| Dark scenes (100 samples) | deep navy `#011621` → `#043247` → `#074668`, with a **teal-green glow `#12698c`/`#0e5b65`** rising from one corner; white text |
| Accents overall | navy and ocean blues `#053d5f`, `#064e80`, `#0b73b9`, cyan `#3baed4`/`#6cd3e2`. **There is no colour outside blue, navy and teal** (apart from skin and hair). |

### The theme rule (look C)
1. **One blue family across 2 grounds:** a sky-white ground (white with soft sky-blue glows) for the story scenes, and a **deep navy with a teal glow** for the "problem" and "product" scenes. The switches are circle wipes in those same colours.
2. **The same colours everywhere:** headlines in ocean blue on white and in white on navy; **bubbles and chips** are navy pills with white text on white grounds, or translucent teal glass panels on navy. The ground, the text and the bubbles always share one palette.
3. **Cartoon faces instead of photos:** every person (the doctor, the patients) is the **same flat vector character style**: round white badges with a soft shadow, diverse skin tones, simple friendly faces, the doctor with glasses and scrubs. A **name tag** sits next to each patient badge (Elizabeth, Jennifer, Thomas, James, Michael, William).
4. **Type:** one clean geometric sans. Headlines are semibold; the product line ("Oral Health Therapy") is a **light weight** under a bold name. Labels are small caps-style headings (NEEDS, CONDITIONS, RISK FACTORS) with chips under them.

### Line by line (spoken words reconstructed from rough recognition; times ±0.3 s)
| Time (s) | Spoken | On screen | Motion |
|---|---|---|---|
| 0.5–4.0 | "What if **every** preventive treatment were truly **individualized**?" | the doctor's cartoon face badge on top, a tooth icon below, joined by a line; **patient face badges with name tags** branch out of the line like a tree | the line grows from 0.5 s; the badges pop out along the branches at 1.5–3.5 s, one by one on "every … individualized" |
| 4.5–8.0 | "The best possible treatment, one that adapts to …" | the tree holds, then all but one patient fade | the camera pushes towards one patient |
| 8.0–12.5 | "… each patient's **needs**, **conditions** and **risk factors**." | one patient's big face badge in the centre; **NEEDS** with the chips Aligner Therapy, Deep Cleaning, Restorative Treatment; **CONDITIONS** with Malocclusion, Cavities, Gum Inflammation; **RISK FACTORS** with Poor Oral Hygiene, Allergies | each heading **types on its word** (needs 9.5, conditions 10.4, risk 11.8 s) and its chips pop 0.1 s apart |
| 14.0–19.5 | "… personalized **diagnostics**, **procedures**, **accompanying therapy** and **routine check-ups** for every situation." | from the patient, a path line leads to icon circles: Diagnostic (X-ray), Procedure (tools), Accompanying Therapy (tube), Routine Check-up (mouth) | the camera **pans right along the line**; a green progress stroke draws round each circle as its label types on the word |
| 19.7–23.5 | "But in today's dental practices …" | the doctor stands among **floating holographic screens** (X-rays, tooth scans, patient cards) in light blue glass | the screens fan out in 3D around her at 21–22 s |
| 23.7–29.9 | "… a **shortage of skilled staff**, **time pressure** and a **one-size-fits-all approach** …" | chips with icons appear at the top: **Shortage of Staff**, **Time Pressure**, **One-fit-all Approach** | each chip on its phrase (23.7, 26.2, 27.5 s); meanwhile the doctor **taps a screen and it grows** about 1.3× and brightens, then the next one, about every 1.5 s |
| 30.0–39.0 | "… information is collected: **personal data**, **saliva**, **microbiome**, **X-rays**, **medical history**, the **digital patient record**, **intraoral scanner data**, **current findings** …" | the doctor treats a patient in the chair; data chips around them, grey and faded until **each one turns into a navy pill on its word** | the active chips pop, and the old ones fade back to grey |
| 39.9–42.9 | "**Result?** The **same standard procedure** …" | **"Result?"** in blue, then **"Same Standard Procedure"** with a small card "PROCEDURE 02 +15" with avatars | the headline types; the card pops in |
| 43.0–46.0 | "… **fluctuating quality** …" | a **navy circle wipe** grows from the corner; a **jagged line graph draws on**, its points pop; **"Fluctuating Quality"** in white | the wipe at 44.0 s; the graph draws left to right; "Fluctuating" at 44.25 s and "Quality" at 44.75 s |
| 46.0–50.0 | "… and **inconsistent patient experience**." | many **review cards with 3, 4 and 5 stars** float across the navy | the cards rise with parallax at different speeds |
| 50.0–55.0 | "**VivaDent Oral Health Therapy** (the product) was created to **change that**." | **"VivaDent"** bold white, then **"Oral Health Therapy"** light, in the centre of the navy | the name lands on its word; the subline fades up on "health" |
| 55.1–58.3 | "Its centrepiece: **the Matrix**." | **light streaks**: glowing data lines pour down from the top into a **wireframe globe of nodes**, and the giant ghost word **MATRIX** sits behind it | the beams flow downwards continuously (the "lightning"); the globe pulses; the word fades in on "matrix" (57.6 s) |
| 58.6–65.3 | "An **intelligent**, evidence-grounded **decision engine** that serves as a co-pilot to the specialists." | the doctor (cartoon) on navy beside a **glass patient-list panel** | the panel slides in; the rows **highlight one by one**, as if selected |
| 65.3–75.6 | "It uses **personal data**, **history**, **habits**, **clinical findings**, **saliva data** and **risk factors** …" | a glass dashboard: white cards **Personal Data**, **History**, **Habits**, **Clinical Findings**, **Saliva Data**, **Risk Factors** | **one card per word, exactly on the word** (habits 70.5 s, risk factors 74.5 s); each card scales up from the panel |
| 75.6–84.0 | "… into a **structured, personalized protocol** with clear guidance and seamless documentation." | a **white circle wipe** from the right; the doctor with the patient; navy bubbles **PROCEDURE**, **RISK FACTORS** and the patient's name card **"James"** | the bubbles pop next to the people, on their words |
| 84.0–91.0 | "… consistency … patient experience … less repetitive tasks." | **"Saving Time Per Session"** in blue next to the doctor | the headline types word by word |
| 91.0–100.0 | "With VivaDent, prevention becomes **scalable**, individual and measurably better, no matter **who** performs it." | a **navy iris** opens; the wireframe globe with **patient face badges orbiting** it | the faces join the orbit one by one on "scalable … who" |
| 100.0–110.0 | "VivaDent … intelligence-driven …" | a planet-like dot travels an orbit line and becomes the **"VivaDent / Oral Health Therapy"** end title | the letters type in; a still hold, and silence for the last 1.7 s |

### Signature moves (look C)
- **Tap to grow:** the character taps a floating screen, and it scales up about 1.3× and glows while the others stay. Use it when the voice says "check", "open", "review" or "analyse".
- **Grey to active chips:** all the options sit faded, and the one being said turns into a solid navy pill on its word.
- **The path pan:** a line leads from a person through icon circles, the camera follows it, and each stop types its label as it is said.
- **Graph draw-on** for a problem ("fluctuating"): a jagged line with points popping, on navy.
- **Light streaks into a node globe** for the "AI engine" moment (the "lightning").
- **Orbit of faces** for "scalable" and "every patient".
- **Circle wipes** in the theme's colours (a navy circle from the corner, a white circle from the side, a navy iris) for every change between light and dark.

## Sample 4, look D: soft pastel SaaS explainer (144 s)

### Measured
| | Value |
|---|---|
| Format | 1920×1080, 30 fps, 144.2 s |
| Hard cuts | **0**: every change is a morph, a circle wipe, a camera pan or a physics move |
| Voice | 1.0 → 143.3 s, a calm male VO at about 2.4 words per second, with 1 s of silence at each end |
| Loudness | −23.4 LUFS, LRA 4.7, peak −5.9 dBFS (quiet; we deliver −14 LUFS / −1 dBTP) |
| Ground | **near-white `#fbfdff`, 90 % of all pixels**; a big soft **sky-blue half-circle `#8bc1f0` at about 25 %** sits behind the subject in most scenes, like a stage |
| Accents | eight pastel candy colours used together: lime `#aaf57d`, periwinkle `#7c9cef`, blue `#418ae0`, pink `#ed658c`, sky `#8bcef3`, orange `#f1a539`, butter `#f2da81`, violet `#cf6eeb` |
| Lines and text | slate `#434b58` for outlines and headings, lilac-grey `#cac4d8` for faint UI |

### The theme rule (look D)
1. **A white ground, one sky-blue half-circle stage, and pastel accents on top.** There are no dark scenes. The colour lives in the round icon badges, chips, coins and UI blocks, never in the ground.
2. **Many colours, one family.** Every accent has the same pastel lightness, so 8 hues still read as one theme. Each product feature owns one colour, used for its badge, its pill and its highlight.
3. **People are flat vector characters with faces,** in pastel tops (orange, blue, violet, pink), at desks or standing beside a big UI, each with a role label (Procurement Team, Accounts Processing Team, End Users, Vendors, AP Team, Management).
4. **The product UI is real but simplified:** white dashboard cards with soft shadows, pastel status chips and donut rings. Feature names sit in **pill tags** in the feature's colour above the UI (AerSource, AerScan, AerMatch, AerReco, AerAssist, AerPrompt).
5. **One clean geometric sans.** Headings are slate semibold, labels small and grey, and pill text white. The wordmark is a custom logotype that **types on letter by letter**.

### Line by line
Spoken words are reconstructed from a rough recognition; times are ±0.4 s.

| Time (s) | Spoken | On screen | Motion |
|---|---|---|---|
| 1.0–7.5 | "Are you spending too many hours … processing complex requirements …" | the **Procurement Team** at their desks; a **clock**; requirement cards with faces | the characters pop up from behind the half-circle; the clock hands spin fast for "too many hours"; the cards pile up on "complex requirements" |
| 6.5–8.5 | "… in accounting files …" | **Accounts Processing Team**, a pink **"Invoice"** pill, stacking paper sheets | the sheets drop one by one |
| 8.5–9.0 | (scene change) | a sky-blue circle grows from a dot to fill the frame, then shrinks to the half-circle stage | a circle wipe in the theme's own blue (0.5 s) |
| 9.0–13.0 | "… legacy systems … rigid … long time to value … complex interfaces … high maintenance cost" | a vertical stack of coloured round icon badges with labels | each badge **drops in on its phrase**; its label types in beside it |
| 13.0–17.5 | "… costing you money …" | the badges **turn into gold coins** that fall **into a glass jar**, then spill out | badge → coin morph, then gravity: fall, bounce, stack; the jar tips on "money" |
| 17.5–21.5 | "… such complexity … the whole process is risky …" | a **hand stacks coloured blocks** (Repetitive Tasks, Conventional Negotiation, Cost Leakage, Manual Data Entry, Siloed Processes) into a **Jenga-like tower** | the tower leans, wobbles and **collapses**, with the blocks tumbling flat, on "risky" |
| 22.0–24.0 | "AerChain" (the brand) | the wordmark **types on letter by letter**, centred | about 0.15 s per letter, with a caret |
| 24.0–26.0 | "… the central nervous system …" | the wordmark shrinks into the **header bar of a dashboard**, which grows open | logo → UI header → full card |
| 26.0–30.0 | "… for all your source-to-pay operations …" | round feature icons **orbit out** around the dashboard (Contracts, Purchase Orders, Invoice, Requisitions, Analytics, Reports, Payments) | they fly out from behind the card one by one and settle in a ring |
| 30.0–34.0 | "… learns from the data across your systems …" | a **tree of integration logos** (SAP, Oracle, Azure, SYSPRO, IBM DB2, QuickBooks, Zoho) joined into an **AerChain** pill; a hand presses the pill | the lines grow down into the pill, which turns **lime** and reads **"Integrated ✓"** |
| 34.0–39.0 | "… each and every user interaction …" | framed people joined by **elbow connector lines** | the frames pop in one by one as the line extends |
| 39.0–42.0 | "… optimise the procurement process … operational excellence" | a **triangle of nodes** (cart, $, star) linked by bars of **confetti dots** | the nodes pop and the bars fill; the star bounces |
| 42.0–50.0 | "This intelligence powers … smart suite …" | a **flowchart** of the suite (End User → AerProc → PR → AerSource → vendors → AerScan → AerMatch → ERP) | it builds left to right, a node every 0.3 s, while the camera pans |
| 50.0–56.0 | "AerProc … create a requisition in seconds by chatting …" | a businessman beside a big **chat window** | the bubbles pop like a real chat |
| 56.0–64.0 | "AerSource analyses your requirements …" | three PR documents; a **pink scanning frame** passes over them; the matching PR lifts out | a scanner sweep, then a lift and sort |
| 64.0–76.0 | "… predicts the pricing … negotiation histories …" | a quote table; **Historical Price Trends** and **Negotiation Intelligence** badges pop around it; the **Suggested Price** column fills blue | the badges land on their words; the column fills cell by cell |
| 76.0–82.0 | "AerPrompt … follows up with your team and vendors …" | reminder chips ("2 Days remaining…", "Last Day to Clear the Invoice"), a **gauge**, a messaging chat | the chips slide in; the needle swings; the messages pop |
| 82.0–88.0 | "AerScan … extracts invoices …" | a paper invoice; a **pink scan sweep**; a digital invoice builds beside it | the band moves down; the fields type into the copy |
| 88.0–95.0 | "AerMatch … cross-verifies …" | a table whose cells light **red/green**; a cursor marks **DISPUTE**, then **MATCHED** | the cells flash on "verify"; the cursor clicks |
| 95.0–108.0 | "AerReco … reconciliation …" | a **green tick burst** and the toast **"Tax Data Reconciled Successfully"** | the tick scales in with a ring burst; the toast slides up |
| 108.0–117.0 | "AerAssist … answers vendor queries instantly" | vendors' question bubbles around a blue bot, then a scrolling chat | the bubbles pop around the bot; the chat auto-scrolls |
| 117.0–125.0 | "… 360-degree visualisation … reports builder" | two characters assembling a big dashboard | the panels slot in like blocks |
| 125.0–129.0 | "… go live in a matter of days" | a lime circle **"Go Live in 10 Days"** | it pops with an overshoot on "days" |
| 129.0–132.0 | "… configure the way you want" | a **"100% Configurable"** pill on the UI cards | the cards rearrange |
| 132.0–140.0 | "… transparency … cost savings … efficiency … faster" | a vertical **timeline line** with round stat badges (100% Transparency, 5% Cash Savings, 70% Efficiency, 5X Faster) | the line grows; each badge pops off it on its words |
| 140.0–144.2 | "Why wait? Visit AerChain …" | the wordmark types on, then the URL and a blue **"Visit Website Now"** button | letter by letter; the button comes last; then 1 s of silence |

### Effect recipes (how to build each one in GSAP)
- **Pop from behind the stage:** clip the character with the half-circle and tween `y` from +120 to 0 in 0.35 s with `back.out(1.6)`.
- **Badge drop stack:** a round badge (a white icon on a pastel circle, about 90 px, with a soft shadow) falls from `y` −300 with `bounce.out` in 0.5 s, one per spoken phrase; its label types in 0.1 s later.
- **Morph to coin:** scale the badge to 0.8 while crossfading to a gold coin, then give it gravity (`y` with `power2.in`, a short bounce and a small rotation).
- **Jar or Jenga physics:**
  - Stack the blocks.
  - Wobble the tower ±2–4° twice.
  - Give each block its own `rotation` (±40–90°) and its own `y` to the floor with `power2.in`, staggered 0.05 s from the top down.
- **Typed wordmark:** split the word into letters; each one goes from `autoAlpha` 0 and `x` −6 to its place in 0.08 s, 0.12–0.15 s apart, followed by a blinking caret.
- **Logo to UI morph:** scale the wordmark into a header bar, then grow the white card down from it (`scaleY` 0 → 1 with the transform origin at the top, 0.5 s).
- **Orbit-out icons:** start every icon at the card's centre, behind it, and tween each to its ring position with `power3.out`, 0.15 s apart.
- **Integration tree:** draw each connector with `strokeDashoffset` (0.4 s). When the last one lands, swap the pill to lime and its text to "Integrated ✓".
- **Scanner sweep:** a pink-to-transparent gradient band, clipped to the document, moves top to bottom in 0.8 s; the fields then type into the copy.
- **Cell flash:** table cells tween to pastel red or green on the spoken word, and a cursor clicks a status chip.
- **Success burst:** a green tick goes 0 → 1.2 → 1 while a thin ring expands and fades; the toast slides up 30 px.
- **Chat build:** bubbles alternate left and right, each scaling from 0.8 at its tail corner in 0.25 s; the window scrolls one bubble per message.
- **Timeline badges:** the line grows with `scaleY`; at each stop a badge pops and its label types out.
- **Circle wipe in the theme colour:** a sky-blue dot grows over the frame (0.45 s, `power3.in`), then shrinks back to the half-circle stage.

## Sample 5, look E: monochrome with one red accent (corporate training, 52.6 s)

### What the owner asked me to notice (owner's words, 2026-11-13)
"iska bg dekhna or ye kese animation kr rha h wo bhi dekhna faces body text color kitna acha h theme kese maintain kari h ... ye wali choti or achi h"

### Measured
| | Value |
|---|---|
| Format | 1920×1080, 30 fps, 52.6 s (short and tight) |
| Hard cuts | **0** |
| Voice | 0.6 → 51.9 s, about 2.6 words per second |
| Loudness | −19.7 LUFS, peak −2.8 dBFS |
| Light scenes (40 %) | soft greys: `#f2f1f1` paper white, `#d0caca` and `#a29f9e` mid greys, `#2b2626` near-black clothes |
| Dark scenes (60 %) | charcoal `#202020` with a **radial vignette** to `#080808` at the edges, and white objects `#f7f7f7` |
| The only colour | **red** `#be022c` (logo ball, CTA button, small dots, chart arrows, emoji reactions), with warm skin `#ee9d8b`/`#c65160` as the only other warmth |

### The theme rule (look E)
1. **The whole world is greyscale.** The buildings, rooms, furniture, clothes, UI cards and icons are white, grey or black.
2. **Exactly one accent colour (the brand red),** and it marks only what matters: the brand's mark, the pain points (red question bubbles, a red curse bubble "#$&*? &%!&"), growth arrows, likes, the CTA. Because nothing else has colour, the eye always goes to the red.
3. **Faces and skin are the only natural colour.** The characters are elegant semi-flat 2D people with realistic proportions and soft shading on their faces, in black, white and grey clothes. They read as premium, not cartoony.
4. **Two grounds:**
   - light scenes: a pale grey office or city, with depth from blurred grey background figures and a soft light flare
   - dark scenes: charcoal with a spotlight vignette and floating red and white bokeh dots
5. **Text:** white on dark or charcoal on light, in a clean sans. Small caption labels sit under the framed cards (Pressure Mounted, Engagement Slipped, Collaboration Stuck). The brand script logo is white.

### Line by line (reconstructed; times ±0.4 s)
| Time (s) | Spoken | On screen | Motion |
|---|---|---|---|
| 0.0–2.0 | "Think about the last time…" | a grey city skyline rises with a soft light flare and drifting clouds | the camera pushes up and in; the buildings grow up from the ground |
| 2.0–4.0 | "… the frustration …" | an office meeting: a manager points; a **red curse bubble** and **red "?" bubbles** pop over the team | the bubbles pop one by one on the pain words |
| 4.0–12.0 | "… deadlines missed … collaboration … engagement … even in great teams" | **framed scene cards** (polaroid-like, with corner brackets) float on charcoal: a stressed woman, a falling chart, a broken pie chart; labels **Pressure Mounted**, **Engagement Slipped**, **Collaboration Stuck** | each card flies in from depth on its phrase; the cards drift in a slow 3D float; red dots drift |
| 12.0–15.5 | "… The Second City Works …" | a glowing **circular badge** with the white script logo; **white light arcs** orbit and swipe around it; it flips into the red **"YES AND"** ball | the arcs sweep (a light-streak swipe), then a card flip reveals the red ball |
| 15.5–19.5 | "… signature series … powerful workshops …" | the red ball at the centre of a **wheel of 5 white icon circles**: Innovation, Leadership, Presentation Skills, Team Building, Navigating Change, each with a 2-line label | the circles spawn out of the hub and orbit into place; the labels type in on their words |
| 19.0–20.0 | "… build real-life skills …" | a woman walks out from the middle of the wheel as the icons float around her | the character slides in from depth |
| 20.0–27.0 | "… breakthrough thinking … confidently speaking …" | a close-up of a woman; the **red "YES AND" ball** flies along a **white arc trail** to her colleague; a whiteboard bar chart grows, red arrows rise, gold stars pop on top | the ball travels with a motion trail (the guide that links the beats); the bars grow up in a stagger; the stars pop |
| 27.0–31.0 | "… working better together … what sets us apart …" | the team at a table; **red like/heart reactions** float up; the ball bounces across | emoji pop and float up like a live stream |
| 31.0–36.5 | "… led by … the Fortune 500 …" | three leaders on a stage with a spotlight; a grey crowd silhouette; client logos fade in around them in grey (Google, Facebook, Microsoft, Adobe, Uber …) | the logos fade in staggered on "Fortune 500"; the ball rolls past the leaders' feet |
| 36.5–43.0 | "… improv … science … facilitation … unlock your team's potential" | on charcoal, the ball **bounces** from white circle to circle: **Improv**, **Science**, **Facilitation** | each circle appears **where the ball lands**, on its word (a bouncing-ball guide), then zooms forward |
| 43.0–48.0 | "In fact, they didn't just survive change, they thrived" | two hands reach and **shake** (a close-up); a person helps another up **rising white steps** like a bar chart | the hands slide in from the sides; the steps grow up while the person climbs |
| 48.0–50.0 | "Ready for lasting results?" | the question types on above the red ball | word by word |
| 50.0–52.6 | "Connect with us to book your workshop today" | two face badges joined by a **red heartbeat line**; the white logo; a red pill CTA **"Book Your Workshop Now!"** | the heartbeat line draws; the CTA types; a still hold |

### Effect recipes (look E)
- **One-accent grade:** design everything in greys and keep one brand colour for the meaning-carrying items only. Check that no other hue appears (sample the frames).
- **Guide object:** one brand object (here the red ball) travels between the beats on an arc with a fading white trail (an SVG path drawn with `strokeDashoffset`, plus the ball on `motionPath`), and lands exactly where the next item appears. It ties the whole story together.
- **Bouncing-ball reveal:** the guide drops onto a spot with a `bounce.out` hop; on landing, a white circle scales 0 → 1 and its label types in on the spoken word.
- **Framed scene cards:** small illustrations in white frames with corner brackets and a caption label; they fly in from depth (`z`/`scale` 0.6 → 1 with a blur) and float slowly.
- **Light-arc swipe:** thin white arcs (stroked circle segments) sweep around a badge with `rotation` and a `strokeDasharray` growth, then fade out. It works as a premium logo reveal.
- **Badge flip:** `rotationY` 0 → 90 on the logo badge, swap the face, then 90 → 0 to reveal the brand object.
- **Icon wheel:** satellites spawn at the hub and tween out to their ring slots (`power3.out`, 0.1 s apart) while the ring rotates slowly.
- **Live reactions:** like and heart icons in the accent colour pop and float up 80–120 px while fading, staggered.
- **Spotlight vignette:** a dark radial-gradient overlay with drifting bokeh dots (accent and white, low opacity) behind the subjects.
- **Rising steps:** white blocks grow up with `scaleY` in a stagger while a character climbs them, for growth and support.
- **Heartbeat connector:** two face badges joined by an accent line drawn as an ECG spike path.

## All five samples: the rules that hold in each
1. **Say it, show it:** every named person, role, thing, number, tool or quality appears **on its word** (0.1–0.4 s before it), and the headlines land on their keyword.
2. **One theme per video, never left:** sample 1 is purple with white; sample 2 is white with teal and blue; sample 3 is sky-white with deep navy and teal; sample 4 is near-white with a sky-blue stage and one pastel family; sample 5 is greyscale with one red accent. The only colours outside the theme are the brand logo's own and the real app icons.
3. **No hard cuts:** wipes in the theme's colours, camera moves, draw-ons, zooms into the UI, and morphs (an orb or squares into the logo, a URL into a button).
4. **People always have faces:** photo badges (look A), or, when there is no photo, **one consistent cartoon character style** (looks B and C), always with a role pill or a name tag.
7. **The bubbles and chips use the theme's colours** (navy pill with white text, or glass in the dark scenes), never a new colour.
5. **The end card is the logo, a CTA button and the URL,** held still, with the sound fading out.
6. **One type family**, bold headlines and small labels; the "font change" is size and weight.

## What this means for our videos
- Script first (VO or text). Mark **every noun and action** in it and give each one a visual on its word.
- Pick **one brand theme** (dark ground + light ground + accents + one brand gradient) and use nothing outside it.
- **Choose the look per brand:** look A (premium dark, 3D cards, glows), look B (white flat line-art, draw-ons, drawn characters) look C (sky-white and navy health-tech, cartoon people, glass UI, tap-to-grow) look E (greyscale with one brand-colour accent, elegant 2D people, a guide object that travels between beats), or look D (white with a sky-blue half-circle stage, a pastel candy family, flat characters, playful physics: coins in a jar, a collapsing block tower, scanner sweeps, a typed wordmark). The owner picks it, or it follows the brand's colours.
- Use 16:9 as in the samples, or 9:16 for reels with the same rules.

## Brand styles in this category
_None yet._

## Rules from the owner's corrections
_None yet._
