loot = [("sword", 120), ("bow", 75), ("mace", 40)]
print(max(loot, key=lambda item: item[1]))
print(min(loot, key=lambda item: item[1]))
