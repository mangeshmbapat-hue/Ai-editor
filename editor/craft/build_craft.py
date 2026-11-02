"""Generate editor/craft/CRAFT.md (Mann's readable rulebook) from craft.json.

Run: python3 editor/craft/build_craft.py
"""

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main():
    d = json.loads((HERE / "craft.json").read_text(encoding="utf-8"))
    rules = [r for dom in d["domains"] for r in dom["rules"]]
    auto = sum(1 for r in rules if r["check"] == "auto")
    out = ["# Mann's craft rulebook", "",
           "{} rules in {} domains; {} are checked automatically by `craft-check` (also run by `storyboard` and `qc`), the rest are Mann's frame-by-frame checklist. Thresholds live in `editor/rules.json`; owner corrections change them there.".format(
               len(rules), len(d["domains"]), auto), "",
           "Contents: " + " · ".join("[{}](#{})".format(dom["title"], dom["title"].lower().replace(" ", "-").replace(",", "")) for dom in d["domains"])
           + " · [Safe zones](#safe-zone-profiles) · [Type scale](#type-scale) · [Font pairings](#font-pairings) · [Colour themes](#colour-themes) · [Sources](#sources)", ""]
    for dom in d["domains"]:
        out += ["## {}".format(dom["title"]), ""]
        for r in dom["rules"]:
            out += ["### {} `{}`{}".format(r["name"], r["id"], " · auto-checked" if r["check"] == "auto" else ""), "",
                    "- **What:** " + r["what"], "- **When:** " + r["when"], "- **How (Mann):** " + r["how"], "- **Avoid:** " + r["avoid"], ""]
    out += ["## Safe zone profiles", "", "Fractions of the frame kept clear of text and faces. Choose with `safe_zone_profile` in `editor/rules.json`.", "",
            "| Aspect | Profile | Top | Bottom | Left | Right |", "|---|---|---|---|---|---|"]
    for aspect, profiles in d["safe_zones"].items():
        for name, z in profiles.items():
            out.append("| {} | {} | {:.1%} | {:.1%} | {:.1%} | {:.1%} |".format(aspect, name, z["top"], z["bottom"], z["left"], z["right"]))
    ts = d["type_scale"]
    out += ["", "## Type scale", "", "Ratio x{} between levels. Sizes as a fraction of the frame height; set a text item's `role` and Mann sizes it.".format(ts["ratio"]), "",
            "| Role | Size | Weight |", "|---|---|---|"]
    out += ["| {} | {:.1%} | {} |".format(role, size, ts["weights"].get(role, "")) for role, size in sorted(ts["roles"].items(), key=lambda x: -x[1])]
    out += ["", "## Font pairings", "", "Set `\"typography\": {\"pairing\": \"<id>\"}` in the EDL; install with `fonts-install --pairing <id>`. Devanagari support verified on the npm registry (@fontsource, 2026-11-02).", "",
            "| Id | Display | Text | Devanagari | Mood | Use |", "|---|---|---|---|---|---|"]
    out += ["| `{}` | {} {} | {} {} | {} | {} | {} |".format(p["id"], p["display"], p["display_weight"], p["text"], p["text_weight"],
                                                       "yes" if p["devanagari"] else "**no**", p["mood"], p["use"]) for p in d["font_pairings"]]
    out += ["", "## Colour themes", "", "Set `\"typography\": {\"theme\": \"<id>\"}`; `mg-new` puts the theme into the Hyperframes composition and the grade preset matches it.", "",
            "| Id | Name | Harmony | Colours | Grade | Use |", "|---|---|---|---|---|---|"]
    out += ["| `{}` | {} | {} | {} | `{}` | {} |".format(t["id"], t["name"], t["harmony"], " ".join("`{}`".format(c) for c in t["colours"]), t["grade"], t["use"])
            for t in d["colour_themes"]]
    out += ["", "## Sources", ""] + ["- **{}:** {}".format(k, v) for k, v in d["sources"].items()] + [""]
    (HERE / "CRAFT.md").write_text("\n".join(out), encoding="utf-8")
    print("CRAFT.md: {} rules, {} auto-checked".format(len(rules), auto))


if __name__ == "__main__":
    main()
