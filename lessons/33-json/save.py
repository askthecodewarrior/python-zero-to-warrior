# Save the game
import json

player = {
    "name": "Warrior",
    "level": 5,
    "inventory": ["sword", "map"],
}

with open("save.json", "w") as f:
    json.dump(player, f, indent=2)
