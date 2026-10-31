# Practice 3: two bugs. Run it, read the error, fix it, run it again.
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def describe(self):
        print(self.name, "costs", self.price, "gold")


class Shield(Item):
    def __init__(self, name, price, armor):
        self.armor = armor

    def describe(self):
        super.describe()
        print("It blocks", self.armor)


wood = Shield("wooden shield", 8, 2)
wood.describe()
