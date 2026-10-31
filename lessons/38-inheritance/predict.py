# Practice 1: predict the output, then run it
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def describe(self):
        print(self.name, "costs", self.price, "gold")

    def use(self):
        print("You can't use the", self.name)


class Potion(Item):
    def use(self):
        print("You drink the", self.name)


rope = Item("rope", 3)
tonic = Potion("tonic", 10)
rope.use()
tonic.describe()
tonic.use()
print(isinstance(rope, Potion))
