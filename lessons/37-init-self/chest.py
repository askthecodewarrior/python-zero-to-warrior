# Practice 2 (one answer): a treasure chest with a default, and a method
# that calls another method through self
class Chest:
    def __init__(self, gold=0):
        self.gold = gold

    def show(self):
        print("The chest has", self.gold, "gold")

    def add(self, amount):
        self.gold += amount
        self.show()


small = Chest()
big = Chest(50)
small.add(10)
big.add(25)
small.show()
