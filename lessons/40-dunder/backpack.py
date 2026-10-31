# Python calls these dunder methods for you
class Backpack:
    def __init__(self, items):
        self.items = items

    def __str__(self):
        return "Backpack: " + ", ".join(self.items)

    def __repr__(self):
        return f"Backpack({self.items})"

    def __len__(self):
        return len(self.items)

    def __eq__(self, other):
        return self.items == other.items

    def __add__(self, other):
        return Backpack(self.items + other.items)


pack = Backpack(["sword", "rope"])
extra = Backpack(["torch"])
print(pack)
print([pack, extra])
print(len(pack))
print(pack == Backpack(["sword", "rope"]))
print(pack + extra)
