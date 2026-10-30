# Your turn: give every player a level
# TODO 1: in __init__, add self.level = 1 under self.potions = 2
# TODO 2: add a method add_level(self) under drink_potion that adds 1 to
#         self.level and prints the new level
# TODO 3: call kai.add_level() at the bottom, then run it
# Run it: python3 starter.py on a Mac, python starter.py on Windows.
class Player:
    def __init__(self, name, hp=100):
        self.name = name
        self.hp = hp
        self.potions = 2

    def show(self):
        print(self.name, "has", self.hp, "HP")

    def drink_potion(self):
        self.potions -= 1
        self.hp += 20
        self.show()


kai = Player("Kai", 60)
kai.drink_potion()
kai.drink_potion()
print("Potions left:", kai.potions)
