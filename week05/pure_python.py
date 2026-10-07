f = open("scores.csv", "r",
         encoding="utf-8")
lines = f.readlines()
f.close()

count = 0
totals = {}
counts = {}

score_idx = 2

for line in lines [1:]:
    parts = line.strip().split(",")
    raw = parts[score_idx].strip().strip(",")
    if raw == "":
        continue
    try:
        score = float(raw)
    except ValueError:
        continue

    category = parts[cat_idx]
    if category not in totals:
        totals[category] = 0.0
        counts[category] = 0

        count = count + 1

    print(totals)
    print(counts)

    for c in sorted(totals.key()):
        avg = totals[c] / counts[c]
        print(c, round(avg, 2))


import pandas as pd
