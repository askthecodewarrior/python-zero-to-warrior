# Your turn: give Backpack a __lt__ method, so < works
# TODO 1: under __add__, add a method called __lt__
#         (two underscores on each side), with self and other,
#         that returns len(self) < len(other)
# TODO 2: at the bottom, print(extra < pack)
# Run it: python3 starter.py on a Mac, python starter.py on Windows.
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
