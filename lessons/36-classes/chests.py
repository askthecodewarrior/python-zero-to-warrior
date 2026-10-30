# Practice 1: predict the output, then run it
class Chest:
    def __init__(self, gold):
        self.gold = gold


left = Chest(50)
right = Chest(50)
left.gold = left.gold + 25
print(left.gold, right.gold)

right = left
right.gold = 0
print(left.gold, right.gold)
