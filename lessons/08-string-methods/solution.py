# String methods: tools built into every string
player = "Warrior"
print(player.upper())
print(player.lower())
print(player.replace("rior", "lock"))

print(player.isupper())
print("42".isdigit())
print("LEVEL 7".isupper())
print("7.5".isdigit())

loot = "sword,shield,potion"
items = loot.split(",")
print(items)
print("-".join(items))
