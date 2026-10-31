# Sort, map and filter with lambda
weapons = ["sword", "bow", "crossbow", "mace"]
print(sorted(weapons))
print(sorted(weapons, key=len))
print(sorted(weapons, key=len, reverse=True))

loot = [("sword", 120), ("bow", 75), ("mace", 40)]
print(sorted(loot, key=lambda item: item[1]))

half = map(lambda item: item[1] // 2, loot)
print(list(half))
print([item[1] // 2 for item in loot])

cheap = filter(lambda item: item[1] < 100, loot)
print(list(cheap))
print([item for item in loot if item[1] < 100])
