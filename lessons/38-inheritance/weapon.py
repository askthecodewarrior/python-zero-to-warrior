# Practice 2, one answer: a Weapon is an Item with damage
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def describe(self):
        print(self.name, "costs", self.price, "gold")


class Weapon(Item):
    def __init__(self, name, price, damage):
        super().__init__(name, price)
        self.damage = damage

    def describe(self):
        super().describe()
        print("It hits for", self.damage)


axe = Weapon("axe", 25, 7)
axe.describe()
