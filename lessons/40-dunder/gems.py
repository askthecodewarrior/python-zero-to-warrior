# Practice 1: predict, then run. Gem has __repr__ but no __str__
class Gem:
    def __init__(self, color):
        self.color = color

    def __repr__(self):
        return f"Gem('{self.color}')"


red = Gem("red")
print(red)
print([red, Gem("blue")])
print(red == Gem("red"))
