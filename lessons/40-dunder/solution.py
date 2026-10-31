# Your turn, one way to do it: __lt__ is what < calls, and sorted() uses it too
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

    def __lt__(self, other):
        return len(self) < len(other)


pack = Backpack(["sword", "rope"])
extra = Backpack(["torch"])
print(extra < pack)
print(sorted([pack, extra]))
