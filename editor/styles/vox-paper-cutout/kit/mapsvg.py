#!/usr/bin/env python3
"""Vox kit: Natural Earth countries -> one SVG <path> per country in a Mercator box (offline, no deps).

    python3 mapsvg.py <ne_admin_0_countries.geojson> <out.json> --box 30,-15,130,45 --k 28 [--tol 0.35]

Writes {"box", "k", "y0", "paths": {ISO_A3: "M..."}}; the page projects lon/lat with the same k and y0:
x = (lon - lon0) * k, y = (y0 - merc(lat)) * k, merc(lat) = degrees(ln(tan(pi/4 + lat/2))).
Data: Natural Earth (public domain). For India use ne_10m_admin_0_countries_ind.geojson (India point of view boundaries)."""
import argparse, json, math


def merc(lat):
    return math.degrees(math.log(math.tan(math.pi / 4 + math.radians(lat) / 2)))


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("src"); ap.add_argument("out")
    ap.add_argument("--box", default="30,-15,130,45"); ap.add_argument("--k", type=float, default=28); ap.add_argument("--tol", type=float, default=0.35)
    a = ap.parse_args()
    lon0, lat0, lon1, lat1 = map(float, a.box.split(",")); k = a.k; y0 = merc(lat1)
    P = lambda lon, lat: ((lon - lon0) * k, (y0 - merc(max(-80, min(80, lat)))) * k)
    gj = json.load(open(a.src, encoding="utf-8")); paths = {}
    for f in gj["features"]:
        pr = f["properties"]; code = pr.get("ADM0_A3_IN") or pr.get("ADM0_A3") or pr.get("ISO_A3")  # India point-of-view file first
        g = f["geometry"]; polys = g["coordinates"] if g["type"] == "MultiPolygon" else [g["coordinates"]]
        d = []
        for poly in polys:
            for ring in poly[:1]:
                xs = [c[0] for c in ring]; ys = [c[1] for c in ring]
                if max(xs) < lon0 - 5 or min(xs) > lon1 + 5 or max(ys) < lat0 - 5 or min(ys) > lat1 + 5:
                    continue
                pts, last = [], None
                for lon, lat in ring:
                    x, y = P(lon, lat)
                    if last is None or abs(x - last[0]) + abs(y - last[1]) >= a.tol:
                        pts.append((x, y)); last = (x, y)
                if len(pts) < 3:
                    continue
                d.append("M" + "L".join("{:.1f},{:.1f}".format(x, y) for x, y in pts) + "Z")
        if d:
            paths[code] = "".join(d)
    json.dump({"box": [lon0, lat0, lon1, lat1], "k": k, "y0": y0, "paths": paths}, open(a.out, "w"))
    print(len(paths), "countries,", sum(len(v) for v in paths.values()) // 1024, "KB")


if __name__ == "__main__":
    main()
