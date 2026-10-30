# __init__ runs every time you make a player
class Player:
    def __init__(self, name, hp=100):
        self.name = name
        self.hp = hp
        self.potions = 2
        print("Made", self.name)


ana = Player("Ana")
kai = Player("Kai", 60)
print(ana.name, ana.hp, ana.potions)
print(kai.name, kai.hp, kai.potions)
