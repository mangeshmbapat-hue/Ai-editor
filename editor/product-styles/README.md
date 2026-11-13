# Product style library (Animation Editor)

Every product category is animated differently, so each one has its own style sheet. The owner teaches them one category at a time (owner rule 2026-11-13).

| Category | Products | Status | Sheet |
|---|---|---|---|
| Makeup & beauty | lipstick, foundation bottle, cream jar, serum, perfume | not learned | `makeup-beauty/STYLE_SHEET.md` |
| Food & drinks | snacks, chai and coffee, cold drinks, packaged food | not learned | `food-drinks/STYLE_SHEET.md` |
| Fashion & clothing | clothes, shoes, sportswear, bags | not learned | `fashion-clothing/STYLE_SHEET.md` |
| Automobile | cars, bikes, EVs | not learned | `automobile/STYLE_SHEET.md` |
| Animated explainer | corporate SaaS explainer with a VO, everything said appears on its word | breakdown done, waiting for approval | `animated-explainer/STYLE_SHEET.md` |
| Apps & digital | apps, websites, software | learned 2026-11-10 (Chamosa result rejected) | `../styles/animation-product-promo/STYLE_SHEET.md` |

`LIBRARY.json` is the registry the agent reads. A new category is added when the owner asks for one.

## How a category is learned
1. The owner sends 3–4 ads of the category as files and says what to notice. The files stay in `projects/_product-train/<category>/` (git-ignored); only the sheet is committed.
2. Fill the sheet: the owner's points (in their words), Measured, then Observed. Show the owner the breakdown.
3. When the owner approves, set the category's `status` in `LIBRARY.json` to `learned <date>`, with the owner's words.
4. Brand styles inside a category (for example "Nike jaisa") go in `<category>/brands/<brand>/STYLE_SHEET.md` and under `brands` in `LIBRARY.json`.

## How a request is served
The owner names the category and, optionally, a brand ("makeup ka, Nike jaisa"). The agent opens that category's sheet, and the brand sheet if there is one. If the category or brand is not learned yet, it says so and asks for samples. It never makes the video in another category's style.
