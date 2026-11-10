# Stock photo library (free-licensed, real photos)

Real photos for the Faceless Editor (owner rule 2026-11-10: objects, animals and places are realistic, never cartoon). They are fetched once by `studio/stock_library.py` from Wikimedia Commons and NASA. Each file's licence, author and source page are in `CREDITS.json`. CC BY and CC BY-SA photos need the credit line in the video description, and the editor writes it into the job's `CREDITS.md`.

- **Check a photo by eye before using it.** The search takes the first match, and the 2026-11-10 pass caught wrong hits: an old Confederate note, a cartoon and a sign.
- **No real people's faces** from here. People follow the owner's face rule.
- **Use the object as a cutout** (`python3 -m aifilm.editor cutout <photo> <out.png>`) where the VO names it.
- **To add an item:** put it in `ITEMS` in `studio/stock_library.py`, run `python3 studio/stock_library.py <slug>`, check it, and commit.
