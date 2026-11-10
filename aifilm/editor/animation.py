"""Animation Editor: product-promo motion graphics in the house style learned from the owner's 4 samples
(editor/styles/animation-product-promo/STYLE_SHEET.md).

The owner gives the product (name, brand colour, screens/PNG icons, the feature lines) and the agent writes a
scene list, `spec.json`. `anim-new` turns it into a HyperFrames-compatible composition (one HTML page + the
house motion runtime, aifilm/editor/anim/runtime.js) themed with one of the four learned colour themes.
`anim-storyboard` renders one frame per scene for the owner. `anim-render` renders the video, and refuses until
the owner's approval of that exact spec and its assets is recorded with `anim-approve` (same gate as Mann)."""

import json
import shutil
import subprocess
import tempfile
from pathlib import Path

from ..core import file_hash, fingerprint, inside, project_lock, read_json, require, write_json
from . import edl as E
from .tools import vendor_gsap

HERE = Path(__file__).resolve().parent / "anim"
HOUSE_STYLE = "animation-product-promo"
ASPECTS = {"1:1": (1080, 1080), "9:16": (1080, 1920), "4:5": (1080, 1350)}
SCENE_TYPES = {"logo", "search", "cards", "button", "status", "pill", "chips", "rows", "orbit", "counter", "words", "swap", "endcard"}
END_SILENCE = 2.4   # the samples' sound stops about 2.4 s before the end card finishes (measured on all 4)

# The four learned themes (colours sampled from the samples' frames). One theme per video: a ground that is a
# light tint or a deep shade of the brand colour, white or glass cards, at most three accents, and the
# black end card with white glow.
THEMES = {
    "lavender": {  # s1 grocery app: lavender ground, white cards, purple + hot pink + blue
        "dark": False, "ink": "#1c1a1f", "ink_dark": "#f4f0f7", "muted": "#8a8392", "card": "#ffffff",
        "glass": "rgba(255,255,255,0.55)", "glass_line": "rgba(255,255,255,0.7)", "shadow": "rgba(120,40,150,0.12)",
        "track": "#ece3f1", "mark": "rgba(120,60,150,0.55)",
        "accents": {"primary": "#9b00ca", "secondary": "#eb1783", "tertiary": "#3b74f3", "glow": "#c26de6"},
        "grounds": {"light": "#f7e3fc", "white": "#fafafa", "night": "#000000"}, "default_ground": "light"},
    "midnight": {  # s2 chat app: deep indigo gradient, glass panels, electric blue
        "dark": True, "ink": "#e7e7ec", "ink_dark": "#e7e7ec", "muted": "#9c98a3", "card": "#202339",
        "glass": "rgba(255,255,255,0.08)", "glass_line": "rgba(255,255,255,0.12)", "shadow": "rgba(0,0,0,0.45)",
        "track": "rgba(255,255,255,0.12)", "mark": "rgba(255,255,255,0.6)",
        "accents": {"primary": "#4453e8", "secondary": "#3c73d4", "tertiary": "#e7e7ec", "glow": "#6f7dff"},
        "grounds": {"deep": "linear-gradient(180deg,#0a004a 0%,#04002e 55%,#000014 100%)", "night": "#000000"}, "default_ground": "deep"},
    "graphite": {  # s3 meeting app: light grey to graphite, black cards, call blue / red / green, cyan glow words
        "dark": True, "ink": "#f2f2f7", "ink_dark": "#f2f2f7", "muted": "#8e8e93", "card": "#121214",
        "glass": "rgba(255,255,255,0.08)", "glass_line": "rgba(255,255,255,0.12)", "shadow": "rgba(0,0,0,0.35)",
        "track": "rgba(255,255,255,0.14)", "mark": "rgba(255,255,255,0.6)",
        "accents": {"primary": "#2b6cef", "secondary": "#d11a31", "tertiary": "#22a447", "glow": "#35c3cc"},
        "grounds": {"light": "#e0e0e0", "dark": "#2e2e2e", "night": "#0b0b0b"}, "default_ground": "dark"},
    "sky": {  # s4 creator reel: white, sky-blue gradient, night navy; blue + coral pink + royal blue, cyan
        "dark": False, "ink": "#111318", "ink_dark": "#f2f4f8", "muted": "#8b8f99", "card": "#ffffff",
        "glass": "rgba(255,255,255,0.6)", "glass_line": "rgba(255,255,255,0.8)", "shadow": "rgba(36,131,239,0.16)",
        "track": "#e4eefb", "mark": "rgba(20,40,80,0.35)",
        "accents": {"primary": "#2483ef", "secondary": "#e85c6d", "tertiary": "#1b15d9", "glow": "#20a4e5", "gold": "#f0b400"},
        "grounds": {"white": "#fafafa", "sky": "linear-gradient(180deg,#62a4f2 0%,#7cb3f7 60%,#b6d4fa 100%)",
                    "deep": "linear-gradient(180deg,#000106 0%,#021630 100%)", "night": "#000000"}, "default_ground": "white"},
}


def _hex(c):
    c = c.lstrip("#")
    require(len(c) == 6 and all(ch in "0123456789abcdefABCDEF" for ch in c), "brand colour must be #rrggbb")
    return tuple(int(c[i:i + 2], 16) for i in (0, 2, 4))


def _mix(rgb, other, k):
    return "#%02x%02x%02x" % tuple(round(a * (1 - k) + b * k) for a, b in zip(rgb, other))


def theme_from_brand(brand, base="lavender"):
    """A new product's theme in the learned recipe: the nearest learned theme, its primary accent replaced by the
    brand colour, and its ground a light tint (light themes, about 88 % white) or a deep shade (dark themes)."""
    require(base in THEMES, "Unknown theme " + base)
    t = json.loads(json.dumps(THEMES[base]))
    rgb = _hex(brand)
    t["accents"]["primary"] = brand
    t["accents"]["glow"] = _mix(rgb, (255, 255, 255), 0.35)
    if t["dark"]:
        t["grounds"][t["default_ground"]] = "linear-gradient(180deg,{} 0%,{} 55%,#000010 100%)".format(_mix(rgb, (0, 0, 0), 0.72), _mix(rgb, (0, 0, 0), 0.86))
    else:
        t["grounds"][t["default_ground"]] = _mix(rgb, (255, 255, 255), 0.88)
        t["track"] = _mix(rgb, (255, 255, 255), 0.85)
        deep = tuple(round(v * 0.5) for v in rgb)  # shadows and the watermark take the brand's hue, like the samples
        t["shadow"] = "rgba({},{},{},0.14)".format(*deep)
        t["mark"] = "rgba({},{},{},0.55)".format(*deep)
    return t


def resolve_theme(spec):
    theme = spec.get("theme", "lavender")
    if isinstance(theme, dict):
        base = theme.get("base", "lavender")
        t = theme_from_brand(theme["brand"], base) if theme.get("brand") else json.loads(json.dumps(THEMES[base]))
        for k, v in theme.items():
            if k not in ("base", "brand"):
                t[k] = dict(t.get(k, {}), **v) if isinstance(v, dict) else v
        return t
    require(theme in THEMES, "Unknown theme {}; learned themes: {}".format(theme, ", ".join(THEMES)))
    return json.loads(json.dumps(THEMES[theme]))


def assets_of(spec):
    names = []
    for s in spec["scenes"]:
        for key in ("image", "icon"):
            if isinstance(s.get(key), str) and "." in s[key]:
                names.append(s[key])
        for it in s.get("items", []):
            for key in ("image", "icon"):
                if isinstance(it.get(key), str) and "." in it[key]:
                    names.append(it[key])
        names += [i for i in s.get("icons", []) if "." in i]
        names += [p["image"] for p in s.get("props", []) if p.get("image")]
    return sorted(set(names))


def validate(spec):
    require(isinstance(spec.get("scenes"), list) and spec["scenes"], "spec.json needs a non-empty `scenes` list")
    require(spec.get("aspect", "1:1") in ASPECTS, "aspect must be one of " + ", ".join(ASPECTS))
    for i, s in enumerate(spec["scenes"]):
        where = "scene {} ({})".format(i + 1, s.get("type"))
        require(s.get("type") in SCENE_TYPES, "{}: type must be one of {}".format(where, ", ".join(sorted(SCENE_TYPES))))
        require(isinstance(s.get("dur"), (int, float)) and 0.8 <= s["dur"] <= 8, where + ": dur must be 0.8-8 s")
        if s["type"] in ("cards", "chips", "rows"):
            require(s.get("items"), where + ": needs items")
        if s["type"] == "counter":
            require(isinstance(s.get("to"), (int, float)), where + ": needs a numeric `to`")
        if s["type"] == "endcard":
            require(i == len(spec["scenes"]) - 1, where + ": the end card is the last scene")
            require(s.get("handle") or s.get("wordmark"), where + ": the owner's handle or wordmark for this video")
    total = sum(s["dur"] for s in spec["scenes"])
    require(total <= 90, "total {:.1f} s is over 90 s".format(total))
    return total


def project_dir(edit_root, name):
    return Path(edit_root) / "anim" / name


def build(edit_root, name="promo"):
    """(Re)write anim/<name>/index.html and runtime.js from anim/<name>/spec.json, copying the assets from raw/."""
    root = Path(edit_root)
    proj = project_dir(root, name)
    spec = read_json(proj / "spec.json")
    total = validate(spec)
    W, H = ASPECTS[spec.get("aspect", "1:1")]
    theme = resolve_theme(spec)
    (proj / "assets").mkdir(parents=True, exist_ok=True)
    for a in assets_of(spec):
        src = inside(root, "raw/" + a)
        require(src.is_file(), "Asset raw/{} is missing; `ingest` it first".format(a))
        dest = proj / "assets" / a
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dest)
    tokens = {"ink": theme["ink"], "ink-dark": theme["ink_dark"], "muted": theme["muted"], "card": theme["card"], "glass": theme["glass"],
              "glass-line": theme["glass_line"], "shadow": theme["shadow"], "track": theme["track"], "mark": theme["mark"]}
    tokens.update({"accent-" + k: v for k, v in theme["accents"].items()})
    page = (HERE / "template.html").read_text(encoding="utf-8")
    payload = dict(spec, theme=theme, width=W, height=H)
    page = (page.replace("__TOKENS__", "\n".join("        --{}: {};".format(k, v) for k, v in tokens.items()))
            .replace("__W__", str(W)).replace("__H__", str(H)).replace("__DUR__", "{:.3f}".format(total))
            .replace("__SPEC__", json.dumps(payload, ensure_ascii=False).replace("</", "<\\/")))
    (proj / "index.html").write_text(page, encoding="utf-8")
    shutil.copy2(HERE / "runtime.js", proj / "runtime.js")
    vendor_gsap(proj)
    return {"project": str(proj), "duration": round(total, 2), "size": "{}x{}".format(W, H), "scenes": timeline(spec)}


def timeline(spec):
    t, rows = 0.0, []
    for i, s in enumerate(spec["scenes"]):
        what = s.get("label") or s.get("text") or s.get("title") or s.get("fixed") or s.get("handle") or ", ".join(s.get("phrases", []))
        rows.append({"n": i + 1, "type": s["type"], "start": round(t, 2), "dur": s["dur"], "what": str(what)[:60]})
        t += s["dur"]
    return rows


def anim_new(edit_root, spec_file, name="promo"):
    root = Path(edit_root)
    with project_lock(root):
        proj = project_dir(root, name)
        proj.mkdir(parents=True, exist_ok=True)
        spec = json.loads(Path(spec_file).read_text(encoding="utf-8"))
        validate(spec)
        write_json(proj / "spec.json", spec)
        return build(root, name)


def anim_fingerprint(edit_root, name):
    proj = project_dir(edit_root, name)
    spec = read_json(proj / "spec.json")
    files = {a: file_hash(proj / "assets" / a) for a in assets_of(spec)}
    return fingerprint({"spec": spec, "assets": files, "runtime": file_hash(HERE / "runtime.js"), "template": file_hash(HERE / "template.html")})


def renderer(page, out, size, extra=()):
    cmd = ["node", str(HERE / "render.cjs"), str(page), str(out), "--size", size] + list(extra)
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=7200)
    require(result.returncode == 0, "render failed: " + (result.stderr or result.stdout)[-800:])
    return result.stdout


def storyboard(edit_root, name="promo"):
    """One frame per scene (at 65 % of the scene, when it has settled) plus STORYBOARD.md: the owner's gate."""
    root = Path(edit_root)
    info = build(root, name)
    proj = project_dir(root, name)
    sb = proj / "storyboard"
    shutil.rmtree(sb, ignore_errors=True)
    sb.mkdir()
    times = [round(r["start"] + r["dur"] * (0.65 if r["type"] != "endcard" else 0.5), 2) for r in info["scenes"]]
    renderer(proj / "index.html", sb / "f", info["size"], ["--stills", ",".join(map(str, times))])
    lines = ["# Storyboard: {} ({} s, {}, theme {})".format(name, info["duration"], info["size"], read_json(proj / "spec.json").get("theme")), "",
             "| # | time | scene | on screen | frame |", "|---|---|---|---|---|"]
    for r, t in zip(info["scenes"], times):
        f = "{:02d}.png".format(r["n"])
        (sb / "f_{:02d}.png".format(r["n"])).rename(sb / f)
        lines.append("| {} | {:.2f}-{:.2f} s | {} | {} | storyboard/{} |".format(r["n"], r["start"], r["start"] + r["dur"], r["type"], r["what"], f))
    lines += ["", "Fingerprint: `{}`. The full render needs the owner's approval of this exact spec (`anim-approve`).".format(anim_fingerprint(root, name))]
    (sb / "STORYBOARD.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return {"storyboard": str(sb / "STORYBOARD.md"), "frames": len(times)}


def anim_approve(edit_root, name, words):
    require(isinstance(words, str) and words.strip(), "Quote the owner's exact approval words with --words")
    root = Path(edit_root)
    with project_lock(root):
        require((project_dir(root, name) / "storyboard" / "STORYBOARD.md").exists(), "Run anim-storyboard and show the owner first")
        return E.record(root, {"kind": "anim-storyboard", "name": name, "fingerprint": anim_fingerprint(root, name), "by": "owner", "words": words.strip()})


def require_anim_approval(root, name):
    current = anim_fingerprint(root, name)
    require(any(a.get("kind") == "anim-storyboard" and a.get("name") == name and a.get("fingerprint") == current for a in E.approvals(root)),
            "Storyboard not approved for this exact spec and assets. Run `anim-storyboard`, show the owner, and record their words with `anim-approve`.")


def prepare_audio(src, duration, out):
    """Music bed at the house level: -14 LUFS, -1 dBTP ceiling, faded out so the sound stops END_SILENCE s before the end."""
    stop = max(1.0, duration - END_SILENCE)
    chain = "loudnorm=I=-14:TP=-1.5:LRA=7,afade=t=in:d=0.05,afade=t=out:st={:.3f}:d=1.0,apad,atrim=0:{:.3f}".format(stop - 1.0, duration)
    r = subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(src), "-af", chain, "-ar", "48000", "-ac", "2", str(out)], capture_output=True, text=True)
    require(r.returncode == 0, "audio prep failed: " + r.stderr[-400:])
    return out


def anim_render(edit_root, name="promo", audio=None, fps=30):
    root = Path(edit_root)
    proj = project_dir(root, name)
    require_anim_approval(root, name)
    info = build(root, name)
    require_anim_approval(root, name)
    (root / "renders").mkdir(exist_ok=True)
    out = root / "renders" / (name + ".mp4")
    with tempfile.TemporaryDirectory() as tmp:
        extra = ["--fps", str(fps)]
        if audio:
            extra += ["--audio", str(prepare_audio(inside(root, audio), info["duration"], Path(tmp) / "bed.wav"))]
        renderer(proj / "index.html", out, info["size"], extra)
    return {"video": str(out), "duration": info["duration"], "size": info["size"]}
