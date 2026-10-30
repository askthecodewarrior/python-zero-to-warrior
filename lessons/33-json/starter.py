# Your turn: add an item to the inventory, then level up
# TODO 1: add a third item to the inventory list on line 8, like "shield"
#         (each item in double quotes, with a comma between them)
# TODO 2: run this file, then run level_up.py
# Run it: python3 starter.py on a Mac, python starter.py on Windows.
import json

player = {
    "name": "Warrior",
    "level": 5,
    "inventory": ["sword", "map"],
}

with open("save.json", "w") as f:
    json.dump(player, f, indent=2)
