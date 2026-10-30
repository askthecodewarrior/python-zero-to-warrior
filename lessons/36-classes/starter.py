# Your turn: give Player a heal method
# TODO 1: under take_hit, add a method called heal, with self and amount,
#         that adds the amount to self.health
# TODO 2: at the bottom, call rival.heal(20),
#         then print rival.name and rival.health
# Run it: python3 starter.py on a Mac, python starter.py on Windows.
class Player:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def take_hit(self, damage):
        self.health -= damage


hero = Player("Warrior", 100)
rival = Player("Shadow", 80)
print(hero.name, hero.health)
print(rival.name, rival.health)

hero.take_hit(30)
print(hero.name, hero.health)
print(rival.name, rival.health)
