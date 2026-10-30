# Your turn: add an item to the inventory (one way to solve it)
import json

player = {
    "name": "Warrior",
    "level": 5,
    "inventory": ["sword", "map", "shield"],
}

with open("save.json", "w") as f:
    json.dump(player, f, indent=2)
