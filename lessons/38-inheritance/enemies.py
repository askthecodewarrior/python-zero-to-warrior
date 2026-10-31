# A Goblin gets everything an Enemy has
class Enemy:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def attack(self):
        print(self.name, "hits for", self.damage)


class Goblin(Enemy):
    def steal(self):
        print(self.name, "steals a coin")


grub = Goblin("Grub", 5)
grub.attack()
grub.steal()
print(isinstance(grub, Enemy))
