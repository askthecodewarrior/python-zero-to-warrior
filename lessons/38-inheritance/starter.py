# Your turn: an Archer class
# TODO 1: under the Boss class, add class Archer(Enemy): with its own
#         __init__(self, name, damage, arrows)
# TODO 2: in it, call super().__init__(name, damage), then set self.arrows
# TODO 3: at the bottom, make Archer("Bones", 3, 12), call its attack(),
#         and print its arrows
# Run it: python3 starter.py on a Mac, python starter.py on Windows.
class Enemy:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def attack(self):
        print(self.name, "hits for", self.damage)


class Boss(Enemy):
    def __init__(self, name, damage, shield):
        super().__init__(name, damage)
        self.shield = shield

    def attack(self):
        super().attack()
        print(self.name, "breathes fire")


boss = Boss("Dragon", 10, 50)
print(boss.name, "has a shield of", boss.shield)
boss.attack()
