# A backpack with only __init__ so far
class Backpack:
    def __init__(self, items):
        self.items = items


pack = Backpack(["sword", "rope"])
print(pack)
print(pack == Backpack(["sword", "rope"]))
