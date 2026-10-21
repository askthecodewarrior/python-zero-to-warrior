# A game inventory, stored in a list
inventory = ["sword", "shield", "potion"]
print(inventory)
print(inventory[0])
print(inventory[-1])
print(len(inventory))

inventory[1] = "gold shield"
inventory.append("rope")
inventory.insert(0, "torch")
inventory.remove("potion")
dropped = inventory.pop()
print(inventory)
print("Dropped:", dropped)

if "sword" in inventory:
    print("Ready to fight!")

for item in inventory:
    print("You have a", item)
