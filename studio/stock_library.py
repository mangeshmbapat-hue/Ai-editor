"""Build the Faceless Editor's reusable stock photo library from Wikimedia Commons, once,
so a video never waits on downloads (owner: storyboards were taking an hour).

Only free licences (public domain, CC0, CC BY, CC BY-SA) are kept; each file's author,
licence and source page go into editor/library/stock/CREDITS.json. Commons rate-limits
the shared network, so requests are slow and back off on HTTP 429.

    python3 studio/stock_library.py            # fetch every missing item in ITEMS
    python3 studio/stock_library.py dog mic    # only these
"""

import json
import re
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

LIB = Path(__file__).resolve().parents[1] / "editor" / "library" / "stock"
UA = "AiEditorStudio/1.0 (https://github.com/mangeshmbapat-hue/Ai-editor; stock library)"
API = "https://commons.wikimedia.org/w/api.php"
OK_LICENCES = re.compile(r"^(public domain|pd|cc0|cc by(-sa)? ?[0-9.]*)", re.I)
WIDTH = 1280

# slug -> search terms (best first). Real photos of everyday things faceless videos talk about.
ITEMS = {
    "money-rupee-notes": "Indian rupee banknotes", "money-rupee-bundle": "stack of Indian 500 rupee notes photograph",
    "money-dollar-notes": "United States one hundred dollar bill 2013 series", "money-coins": "Indian rupee coins",
    "dog": "golden retriever dog", "dog-street": "Indian pariah dog", "cat": "domestic cat portrait",
    "microphone": "microphone studio condenser", "microphones-press": "press microphones podium",
    "news-studio": "television news studio", "camera-tv": "television studio camera equipment",
    "stage": "empty stage spotlight theatre", "crowd": "crowd concert audience",
    "earth": "The Blue Marble Earth",
    "laptop": "laptop computer", "smartphone": "smartphone in hand", "computer-desk": "desktop computer office",
    "supreme-court-india": "Supreme Court of India building", "parliament-india": "Parliament House New Delhi",
    "bank-building": "Reserve Bank of India Mumbai headquarters", "atm": "automated teller machine India photograph", "stock-market-screen": "stock market display board",
    "newspaper": "newspapers stack", "calendar": "wall calendar", "stopwatch": "stopwatch", "clock": "wall clock",
    "trophy": "trophy cup", "gavel": "judge gavel", "police": "police car India",
    "hospital": "hospital building", "school-classroom": "classroom India", "farmer-field": "wheat field India",
    "city-mumbai": "Mumbai skyline", "city-delhi": "India Gate New Delhi", "road-traffic": "traffic India road",
    "rocket-launch": "rocket launch", "satellite": "satellite in orbit", "factory": "factory industry",
    "gold": "gold bars", "chart-paper": "financial newspaper chart", "car": "car on road",
    "colour-swatches": "paint colour sample cards", "wristwatch": "luxury wristwatch photograph",
    "editing-suite": "video editing workstation monitors", "headphones": "studio headphones",
}


def get(url, tries=6):
    wait = 8
    for _ in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=40) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            if e.code != 429:
                raise
            time.sleep(wait)
            wait = min(wait * 2, 120)
        except Exception:
            time.sleep(wait)
            wait = min(wait * 2, 120)
    raise RuntimeError("gave up on " + url)


def thumb(url, width=WIDTH):
    # upload.wikimedia.org/wikipedia/commons/a/ab/Name.jpg -> .../thumb/a/ab/Name.jpg/1280px-Name.jpg
    m = re.match(r"(https://upload\.wikimedia\.org/wikipedia/commons)/(\w)/(\w\w)/(.+)$", url)
    return "{}/thumb/{}/{}/{}/{}px-{}".format(m.group(1), m.group(2), m.group(3), m.group(4), width, m.group(4)) if m else url


def search(term):
    q = {"action": "query", "format": "json", "generator": "search", "gsrsearch": "filetype:bitmap " + term, "gsrnamespace": 6,
         "gsrlimit": 8, "prop": "imageinfo", "iiprop": "url|size|extmetadata"}
    data = json.loads(get(API + "?" + urllib.parse.urlencode(q)))
    pages = sorted((data.get("query") or {}).get("pages", {}).values(), key=lambda p: p.get("index", 99))
    for p in pages:
        ii = p["imageinfo"][0]
        ii["url"] = ii["url"].split("?")[0]          # Commons now appends utm_* tracking parameters
        meta = ii.get("extmetadata", {})
        lic = re.sub("<[^>]+>", "", meta.get("LicenseShortName", {}).get("value", "")).strip()
        if not OK_LICENCES.match(lic) or ii.get("width", 0) < 900 or not ii["url"].lower().endswith((".jpg", ".jpeg", ".png")):
            continue
        artist = re.sub("<[^>]+>", "", meta.get("Artist", {}).get("value", "unknown")).strip()
        return {"title": p["title"], "url": ii["url"], "page": ii.get("descriptionurl"), "licence": lic, "author": artist[:120]}
    return None


def main(argv=None):
    wanted = (argv if argv is not None else sys.argv[1:]) or list(ITEMS)
    LIB.mkdir(parents=True, exist_ok=True)
    cpath = LIB / "CREDITS.json"
    credits = json.loads(cpath.read_text(encoding="utf-8")) if cpath.exists() else {}
    for slug in wanted:
        if slug in credits and (LIB / credits[slug]["file"]).exists():
            continue
        try:
            hit = search(ITEMS.get(slug, slug.replace("-", " ")))
            if not hit:
                print("none  ", slug, flush=True)
                continue
            time.sleep(4)
            ext = ".png" if hit["url"].lower().endswith(".png") else ".jpg"
            (LIB / (slug + ext)).write_bytes(get(thumb(hit["url"])))
            credits[slug] = dict(hit, file=slug + ext, fetched=time.strftime("%Y-%m-%d"))
            cpath.write_text(json.dumps(credits, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
            print("ok    ", slug, hit["licence"], flush=True)
        except Exception as exc:
            print("fail  ", slug, str(exc)[:80], flush=True)
        time.sleep(6)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
