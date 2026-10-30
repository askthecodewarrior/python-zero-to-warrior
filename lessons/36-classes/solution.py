# Your turn: give Player a heal method (one way to solve it)
class Player:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def take_hit(self, damage):
        self.health -= damage

    def heal(self, amount):
        self.health += amount


hero = Player("Warrior", 100)
rival = Player("Shadow", 80)
print(hero.name, hero.health)
print(rival.name, rival.health)

hero.take_hit(30)
print(hero.name, hero.health)
print(rival.name, rival.health)

rival.heal(20)
print(rival.name, rival.health)
