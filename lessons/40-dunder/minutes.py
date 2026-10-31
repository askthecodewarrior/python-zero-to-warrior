# Practice 2, one answer: Minutes with __str__, __add__ and __eq__
class Minutes:
    def __init__(self, amount):
        self.amount = amount

    def __str__(self):
        return f"{self.amount} min"

    def __add__(self, other):
        return Minutes(self.amount + other.amount)

    def __eq__(self, other):
        return self.amount == other.amount


warmup = Minutes(30)
workout = Minutes(60)
print(warmup + workout)
print(warmup + warmup == workout)
