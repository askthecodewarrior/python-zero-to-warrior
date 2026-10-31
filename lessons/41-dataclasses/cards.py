from dataclasses import dataclass


@dataclass(order=True)
class Card:
    rank: int
    suit: str


a = Card(10, "hearts")
b = Card(10, "spades")
c = Card(2, "spades")
print(a == b)
print(sorted([b, c, a]))
