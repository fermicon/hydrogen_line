from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "secondary_tradeoff.csv"
OUT = ROOT / "plots" / "secondary_tradeoff.svg"

WIDTH = 900
HEIGHT = 560
LEFT = 90
RIGHT = 40
TOP = 50
BOTTOM = 90

def x_map(x: float, xmin: float, xmax: float) -> float:
    return LEFT + (x - xmin) / (xmax - xmin) * (WIDTH - LEFT - RIGHT)

def y_map(y: float, ymin: float, ymax: float) -> float:
    return HEIGHT - BOTTOM - (y - ymin) / (ymax - ymin) * (HEIGHT - TOP - BOTTOM)

def polyline(points: list[tuple[float, float]]) -> str:
    return " ".join(f"{x:.1f},{y:.1f}" for x, y in points)

rows = []
with DATA.open() as f:
    reader = csv.DictReader(f)
    for row in reader:
        rows.append(
            {
                "d": float(row["secondary_diameter_m"]),
                "classical": float(row["classical_score"]),
                "oversized": float(row["oversized_score"]),
                "prime": float(row["prime_focus_score"]),
            }
        )

xmin = min(r["d"] for r in rows)
xmax = max(r["d"] for r in rows)
ymin = 0.45
ymax = 0.80

classical_pts = [(x_map(r["d"], xmin, xmax), y_map(r["classical"], ymin, ymax)) for r in rows]
oversized_pts = [(x_map(r["d"], xmin, xmax), y_map(r["oversized"], ymin, ymax)) for r in rows]
prime_y = y_map(rows[0]["prime"], ymin, ymax)

xticks = [0.35, 0.50, 0.65, 0.80, 0.95]
yticks = [0.50, 0.55, 0.60, 0.65, 0.70, 0.75]

parts = []
parts.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}">')
parts.append("""
  <style>
    text { font-family: Arial, Helvetica, sans-serif; fill: #111; }
    .small { font-size: 14px; }
    .axis { stroke: #222; stroke-width: 2; fill: none; }
    .grid { stroke: #ddd; stroke-width: 1; }
    .classical { stroke: #1f77b4; stroke-width: 3; fill: none; }
    .oversized { stroke: #d62728; stroke-width: 3; fill: none; }
    .prime { stroke: #2ca02c; stroke-width: 3; stroke-dasharray: 8 6; fill: none; }
    .pt1 { fill: #1f77b4; }
    .pt2 { fill: #d62728; }
  </style>
""")
parts.append(f'<text x="{WIDTH/2:.0f}" y="28" text-anchor="middle" font-size="22">5 m radio telescope optics trade</text>')
parts.append(f'<text x="{WIDTH/2:.0f}" y="50" text-anchor="middle" class="small">Prime focus baseline versus secondary-fed options</text>')
parts.append(f'<line x1="{LEFT}" y1="{TOP}" x2="{LEFT}" y2="{HEIGHT-BOTTOM}" class="axis"/>')
parts.append(f'<line x1="{LEFT}" y1="{HEIGHT-BOTTOM}" x2="{WIDTH-RIGHT}" y2="{HEIGHT-BOTTOM}" class="axis"/>')

for y in yticks:
    yy = y_map(y, ymin, ymax)
    parts.append(f'<line x1="{LEFT}" y1="{yy:.1f}" x2="{WIDTH-RIGHT}" y2="{yy:.1f}" class="grid"/>')
    parts.append(f'<text x="{LEFT-12}" y="{yy+5:.1f}" text-anchor="end" class="small">{y:.2f}</text>')

for x in xticks:
    xx = x_map(x, xmin, xmax)
    parts.append(f'<line x1="{xx:.1f}" y1="{TOP}" x2="{xx:.1f}" y2="{HEIGHT-BOTTOM}" class="grid"/>')
    parts.append(f'<text x="{xx:.1f}" y="{HEIGHT-BOTTOM+24}" text-anchor="middle" class="small">{x:.2f}</text>')

parts.append(f'<polyline points="{polyline(classical_pts)}" class="classical"/>')
parts.append(f'<polyline points="{polyline(oversized_pts)}" class="oversized"/>')
parts.append(f'<line x1="{LEFT}" y1="{prime_y:.1f}" x2="{WIDTH-RIGHT}" y2="{prime_y:.1f}" class="prime"/>')

for x, y in classical_pts:
    parts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4.5" class="pt1"/>')
for x, y in oversized_pts:
    parts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4.5" class="pt2"/>')

parts.append(f'<text x="{(LEFT + WIDTH - RIGHT)/2:.0f}" y="{HEIGHT-28}" text-anchor="middle" class="small">Secondary diameter (m)</text>')
mid = (TOP + HEIGHT - BOTTOM) / 2
parts.append(f'<text x="24" y="{mid:.0f}" transform="rotate(-90 24 {mid:.0f})" text-anchor="middle" class="small">Normalized architecture score</text>')

parts.append(f'<line x1="{WIDTH-270}" y1="82" x2="{WIDTH-220}" y2="82" class="classical"/>')
parts.append(f'<text x="{WIDTH-210}" y="87" class="small">Classical Cassegrain</text>')
parts.append(f'<line x1="{WIDTH-270}" y1="108" x2="{WIDTH-220}" y2="108" class="oversized"/>')
parts.append(f'<text x="{WIDTH-210}" y="113" class="small">Oversized secondary</text>')
parts.append(f'<line x1="{WIDTH-270}" y1="134" x2="{WIDTH-220}" y2="134" class="prime"/>')
parts.append(f'<text x="{WIDTH-210}" y="139" class="small">Prime focus baseline</text>')
parts.append(f'<text x="{LEFT+10}" y="{prime_y-10:.1f}" class="small">Prime focus preferred for Rev A</text>')
parts.append('</svg>')

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text("\n".join(parts))
print(f"Wrote {OUT}")
