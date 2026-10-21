# Practice 3: remove an item only if it's there
inventory = ["torch", "sword", "gold shield"]
want = "potion"
if want in inventory:
    inventory.remove(want)
    print("Removed", want)
else:
    print("No", want, "to remove")
print(inventory)
