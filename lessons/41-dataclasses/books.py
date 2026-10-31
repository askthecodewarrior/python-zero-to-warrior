from dataclasses import dataclass


@dataclass
class Book:
    title: str
    pages: int
    read: bool = False


first = Book("Dune", 412)
second = Book("Hatchet", 195)
second.read = True
print(first)
print(second)
