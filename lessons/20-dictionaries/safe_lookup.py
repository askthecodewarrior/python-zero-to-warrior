# Practice 2: look up a key safely
player = {"name": "Warrior", "level": 7, "gold": 50}
item = input("What do you want to check? ")
print(item, "->", player.get(item, "not found"))
