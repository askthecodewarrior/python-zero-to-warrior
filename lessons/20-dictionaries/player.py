# A player's stats, stored by key
player = {"name": "Warrior", "level": 7, "gold": 50}
print(player)
print(player["gold"])

player["gold"] = 80
player["armor"] = "iron"
print(player)
print(len(player))

print(player.get("map", 0))
print("armor" in player)

del player["armor"]
gold = player.pop("gold")
print(player, gold)

for key, value in player.items():
    print(f"{key}: {value}")
