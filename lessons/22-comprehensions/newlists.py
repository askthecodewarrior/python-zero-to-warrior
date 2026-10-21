# New lists from old ones
points = [12, -5, 30, 0, 8]
doubled = []
for p in points:
    doubled.append(p * 2)
print(doubled)

doubled = [p * 2 for p in points]
print(doubled)

positive = [p for p in points if p > 0]
print(positive)

party = ["mage", "rogue", "knight"]
print([hero.upper() for hero in party])
print([len(hero) for hero in party])
