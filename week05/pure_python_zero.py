f = open("scores.csv", "r", encoding="utf-8")
lines = f.readlines()
f.close()

header = lines[0].strip().split(",")
cat_idx = header.index("category")
score_idx = header.index("score")

count = 0
totals = {}
counts = {}

for line in lines[1:]:
    parts = line.strip().split(",")
    raw = parts[score_idx].strip()
    if raw == "":
        score = 0.0
    else:
        try:
            score = float(raw)
        except ValueError:
            continue

    category = parts[cat_idx]
    if category not in totals:
        totals[category] = 0.0
        counts[category] = 0
    totals[category] += score
    counts[category] += 1

    count = count + 1

print("사용한 행의 수:", count)
print(totals)
print(counts)

for c in sorted(totals.keys()):
    avg = totals[c] / counts[c]
    print(c, round(avg, 2))