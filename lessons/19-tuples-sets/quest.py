# A player's position, and the loot they found
start = (3, 7)
print(start)
print(start[0])
x, y = start
print(x, y)

loot = {"gold", "gem", "gold", "key"}
print(loot)
print(len(loot))

loot.add("map")
loot.remove("key")
print(loot)
print("map" in loot)

drops = ["gold", "gem", "gold", "gold", "key"]
unique = set(drops)
print(unique)
