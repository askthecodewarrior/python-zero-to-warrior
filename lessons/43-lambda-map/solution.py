# Your turn: sort and filter (one way to solve it)
weapons = ["sword", "bow", "crossbow", "mace"]
loot = [("sword", 120), ("bow", 75), ("mace", 40)]

print(sorted(loot, key=lambda item: item[1], reverse=True))

long_names = filter(lambda w: len(w) > 4, weapons)
print(list(long_names))
print([w for w in weapons if len(w) > 4])
