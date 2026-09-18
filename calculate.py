#!/usr/bin/env python3
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def read_csv(name):
    with open(ROOT / name, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))

model = read_csv("SCORING_MODEL.csv")
matrix = read_csv("SCORE_MATRIX.csv")
weights = {r["metric_id"]: float(r["weight"]) for r in model}
criteria = [r["metric_id"] for r in model]

rows = []
for row in matrix:
    score = sum(float(row[c]) / 5.0 * weights[c] for c in criteria)
    rows.append((row["participant"], score, {c: float(row[c]) for c in criteria}))

tie_order = ["C1", "C2", "C6", "C3", "C4", "C5"]
rows.sort(key=lambda x: tuple([-x[1]] + [-x[2][c] for c in tie_order] + [x[0]]))

for i, (name, score, _) in enumerate(rows, 1):
    print(f"{i:>2}. {name}: {score:.1f}")
