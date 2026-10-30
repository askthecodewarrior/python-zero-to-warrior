# Your turn, one way to solve it: a level that starts at 1, and add_level()
class Player:
    def __init__(self, name, hp=100):
        self.name = name
        self.hp = hp
        self.potions = 2
        self.level = 1

    def show(self):
        print(self.name, "has", self.hp, "HP")

    def drink_potion(self):
        self.potions -= 1
        self.hp += 20
        self.show()

    def add_level(self):
        self.level += 1
        print(self.name, "is now level", self.level)


kai = Player("Kai", 60)
kai.drink_potion()
kai.drink_potion()
print("Potions left:", kai.potions)
kai.add_level()
