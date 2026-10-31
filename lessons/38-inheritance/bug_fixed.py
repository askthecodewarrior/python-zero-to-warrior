# Practice 3, fixed: super() has its parentheses, and
# Shield's __init__ calls super().__init__
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def describe(self):
        print(self.name, "costs", self.price, "gold")


class Shield(Item):
    def __init__(self, name, price, armor):
        super().__init__(name, price)
        self.armor = armor

    def describe(self):
        super().describe()
        print("It blocks", self.armor)


wood = Shield("wooden shield", 8, 2)
wood.describe()
