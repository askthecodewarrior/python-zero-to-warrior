# Practice 3: count each drop with a dictionary
drops = ["gold", "gem", "gold", "gold", "key"]
counts = {}
for drop in drops:
    counts[drop] = counts.get(drop, 0) + 1
print(counts)
