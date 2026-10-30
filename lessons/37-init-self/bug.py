# Practice 3: this file has two bugs. Run it, read the error, fix it, and
# run it again until it prints the right thing.
class Player:
    def __init__(self, name, hp=100):
        self.name = name
        self.hp = hp

    def show():
        print(self.name, "has", self.hp, "HP")

    def take_damage(self, amount):
        hp -= amount
        self.show()


ana = Player("Ana")
ana.show()
ana.take_damage(15)
