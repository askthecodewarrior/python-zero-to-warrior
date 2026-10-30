# Load the game and add a level
import json

with open("save.json") as f:
    player = json.load(f)

player["level"] += 1
print(player["name"], "is now level", player["level"])
print("Inventory:", player["inventory"])

with open("save.json", "w") as f:
    json.dump(player, f, indent=2)
