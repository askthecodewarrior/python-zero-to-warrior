# Your turn, one way to solve it: an Archer that sets up through super()
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


class Archer(Enemy):
    def __init__(self, name, damage, arrows):
        super().__init__(name, damage)
        self.arrows = arrows


boss = Boss("Dragon", 10, 50)
print(boss.name, "has a shield of", boss.shield)
boss.attack()

bones = Archer("Bones", 3, 12)
bones.attack()
print(bones.arrows)
