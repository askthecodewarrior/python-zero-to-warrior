# A Boss adds to what an Enemy does
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
