# Methods read and change the player
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
