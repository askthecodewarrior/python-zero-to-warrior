# Practice 3, fixed: self back in the def line, and self. in front of hp
class Player:
    def __init__(self, name, hp=100):
        self.name = name
        self.hp = hp

    def show(self):
        print(self.name, "has", self.hp, "HP")

    def take_damage(self, amount):
        self.hp -= amount
        self.show()


ana = Player("Ana")
ana.show()
ana.take_damage(15)
