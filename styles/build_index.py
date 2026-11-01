"""Rebuild styles/README.md (the index table) and styles/catalog.json from every styles/<slug>/style.json.

Run: python3 styles/build_index.py          (writes the files)
     python3 styles/build_index.py --check  (exit 1 if they are out of date)
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
START, END = "<!-- index:start -->", "<!-- index:end -->"
ORDER = ["Indian Traditions", "World Folk", "Animation Techniques", "Art Movements", "Internet & Digital", "Cinema Eras"]


def load():
    rows = []
    for p in sorted(HERE.glob("*/style.json")):
        s = json.loads(p.read_text(encoding="utf-8"))
        rows.append(s)
    rows.sort(key=lambda s: (ORDER.index(s["category_en"]) if s["category_en"] in ORDER else 99, s["num"]))
    return rows


def table(rows):
    out, cat = [], None
    for s in rows:
        if s["category_en"] != cat:
            cat = s["category_en"]
            n = sum(1 for r in rows if r["category_en"] == cat)
            out += ["", f"### {cat} · {s['category_hi']} ({n})", "", "| # | Style | हिंदी | Slug | Status | Proposed demo |", "|---|---|---|---|---|---|"]
        line = s["line"].removeprefix("Proposed demo: ")
        out.append(f"| {s['num']} | [{s['en']}]({s['slug']}/STYLE.md) | {s['hi']} | `{s['slug']}` | {s['status']} | {line} |")
    return "\n".join(out).lstrip("\n")


def render(rows):
    readme = (HERE / "README.md").read_text(encoding="utf-8")
    a, b = readme.index(START) + len(START), readme.index(END)
    body = f"\n{len(rows)} styles.\n\n" + table(rows) + "\n"
    readme = readme[:a] + body + readme[b:]
    catalog = json.dumps([{k: s[k] for k in ("slug", "num", "en", "hi", "category_en", "status")} for s in rows], ensure_ascii=False, indent=1) + "\n"
    return readme, catalog


def main():
    rows = load()
    readme, catalog = render(rows)
    if "--check" in sys.argv:
        ok = (HERE / "README.md").read_text(encoding="utf-8") == readme and (HERE / "catalog.json").exists() and (HERE / "catalog.json").read_text(encoding="utf-8") == catalog
        print("index up to date" if ok else "index out of date: run python3 styles/build_index.py")
        return 0 if ok else 1
    (HERE / "README.md").write_text(readme, encoding="utf-8")
    (HERE / "catalog.json").write_text(catalog, encoding="utf-8")
    print(f"{len(rows)} styles indexed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
