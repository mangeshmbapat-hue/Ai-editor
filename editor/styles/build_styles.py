"""Generate editor/styles/<slug>/STYLE_SHEET.md + style.json and INDEX.md from catalog.json.

Run: python3 editor/styles/build_styles.py
A style learned from a real reference (`publish-style`, style.json "measured": true) is
never overwritten; its catalog entry stays as the starting description only.
"""

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent


def sheet(s):
    p, e = s["pace"], s["edl"]
    caps = e.get("captions")
    cap_line = ("{} word(s) per caption, {} of frame height, {}, {}{}{}".format(
        caps["max_words"], "{:.0%}".format(caps["size"]), caps["position"], caps["color"],
        ", uppercase" if caps.get("uppercase") else "", ", boxed" if caps.get("box") else "") + (", animated `{}` ({} highlight)".format(caps["animate"], caps.get("highlight_color", "yellow")) if caps.get("animate") else "") if caps else "no burned captions by default")
    engine = [
        "- Grade preset `{}`{}{}".format(e["grade"], ", grain {}".format(e["grain"]) if e.get("grain") else "", ", vignette" if e.get("vignette") else ""),
        "- Transition `{}`{}".format(e.get("transition", "cut"), " every {} cuts, {}s".format(e["transition_every"], e.get("transition_s", 0.3)) if e.get("transition_every") else ""),
        "- Zoom: {}".format("every {} clip(s), {} -> {}".format(e["zoom_every"], *e.get("zoom", [1.0, 1.1])) if e.get("zoom_every") else "none"),
        "- Silence cut: {}".format("gaps over {}s removed".format(e["silence_cut"]) if e.get("silence_cut") else "pauses kept"),
        "- Music at {} dB{}".format(e.get("music_db", -18), ", beat-synced cuts" if e.get("beat_sync") else ""),
        "- Captions: " + cap_line,
    ]
    extras = []
    if e.get("fx_every"):
        extras.append("FX every N clips: " + ", ".join("{} /{}".format(k, v) for k, v in e["fx_every"].items()))
    if e.get("fx_all"):
        extras.append("FX on all clips: " + ", ".join(e["fx_all"]))
    for key, label in (("fx_last", "FX on the last clip"), ("freeze_last", "freeze last clip (s)"), ("freeze_first", "freeze first clip (s)"),
                       ("slowmo_last", "last clip speed"), ("speed_montage", "montage speed"), ("speed_alternate", "alternating speeds"),
                       ("broll_every", "B-roll insert every N cuts"), ("max_clip", "max clip length (s)")):
        if e.get(key):
            extras.append("{}: {}".format(label, e[key]))
    engine += ["- " + x for x in extras]
    lines = [
        "# Style sheet: {}".format(s["name"]), "",
        "`{}` · family **{}** · known from: {} · status **catalog (estimated)**".format(s["slug"], s["family"], ", ".join(s["known_from"])), "",
        "Best for: {}. Aspect {}, duration {}.".format(s["best_for"], s["aspect"], s["duration"]), "",
        "> Pace numbers are estimated starting targets, not measured. Run `/mann-style-lab` on a reference the owner shares to replace them with measured ones.", "",
        "## Pace (estimated)", "",
        "- Average shot {}s · about {} cuts per 10 s · first cut by {}s".format(p["avg_shot"], p["cuts_per_10s"], p["first_cut"]), "",
        "## Hook", "", s["hook"], "",
        "## Structure", "", s["structure"], "",
        "## Cutting", "", s["cutting"], "",
        "## Camera and framing", "", s["camera"], "",
        "## Transitions", "", s["transitions"], "",
        "## Typography and captions", "", s["type"], "",
        "## Motion graphics", "", s["mg"], "",
        "## Colour", "", s["colour"], "",
        "## Sound design", "", s["sound"], "",
        "## VFX", "", s["vfx"], "",
        "## Signature moves", ""] + ["- " + x for x in s["signature"]] + [
        "", "## Avoid", ""] + ["- " + x for x in s["avoid"]] + [
        "", "## Unique twists (experiments)", ""] + ["- " + x for x in s["twists"]] + [
        "", "## Footage it fits", "",
        "Speech {}, motion {}, orientation {}, footage: {}.".format(s["fit"]["speech"], s["fit"]["motion"], s["fit"]["orientation"], ", ".join(s["fit"]["footage"])),
        "", "## Engine defaults (`autocut --style {}`)".format(s["slug"]), ""] + engine + [""]
    return "\n".join(lines)


def main():
    data = json.loads((HERE / "catalog.json").read_text(encoding="utf-8"))
    built, kept = 0, []
    for s in data["styles"]:
        folder = HERE / s["slug"]
        existing = folder / "style.json"
        if existing.exists() and json.loads(existing.read_text(encoding="utf-8")).get("measured"):
            kept.append(s["slug"])
            continue
        folder.mkdir(exist_ok=True)
        (folder / "STYLE_SHEET.md").write_text(sheet(s), encoding="utf-8")
        targets = {"aspect": s["aspect"], "average_shot_seconds": s["pace"]["avg_shot"], "cuts_per_10s": s["pace"]["cuts_per_10s"],
                   "first_cut_seconds": s["pace"]["first_cut"], "grade_preset": s["edl"]["grade"]}
        (folder / "style.json").write_text(json.dumps({"slug": s["slug"], "measured": False, "targets": targets, "edl_defaults": s["edl"]},
                                                      indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        built += 1
    rows = ["# Editing style index", "", "{} styles. Pick by family; every sheet is in `<slug>/STYLE_SHEET.md`. Pace is estimated until a style is measured from a reference.".format(len(data["styles"])), ""]
    for fam, desc in data["families"].items():
        rows += ["## {} ({})".format(desc, fam), "", "| Style | Known from | Best for | Avg shot | Grade |", "|---|---|---|---|---|"]
        for s in data["styles"]:
            if s["family"] == fam:
                rows.append("| [{}]({}/STYLE_SHEET.md) `{}` | {} | {} | {}s | `{}` |".format(
                    s["name"], s["slug"], s["slug"], ", ".join(s["known_from"]), s["best_for"], s["pace"]["avg_shot"], s["edl"]["grade"]))
        rows.append("")
    rows += ["Sources for the craft descriptions:", ""] + ["- " + u for u in data["sources"]] + [""]
    (HERE / "INDEX.md").write_text("\n".join(rows), encoding="utf-8")
    print("built {} style sheets{}".format(built, "; kept measured: " + ", ".join(kept) if kept else ""))


if __name__ == "__main__":
    main()
