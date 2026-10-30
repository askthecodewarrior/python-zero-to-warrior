# Practice 2 (one answer): a Pet class with a feed method
class Pet:
    def __init__(self, name, hunger):
        self.name = name
        self.hunger = hunger

    def feed(self, amount):
        self.hunger -= amount


cat = Pet("Mochi", 8)
dog = Pet("Rex", 5)
cat.feed(3)
print(cat.name, "hunger:", cat.hunger)
print(dog.name, "hunger:", dog.hunger)
