# Lesson 40: Magic (Dunder) Methods in Python

Part of **Python: Zero to Warrior**, a free Python course for beginners.
Video: https://youtu.be/9kUBt8fBbKY · Full course: https://www.youtube.com/playlist?list=PLcsbg964FAwc

## What's in this lesson
- **A dunder method has two underscores on each side of its name** ("dunder" is short for double underscore), like
  `__init__` from lessons 36 to 39. You almost never call one yourself: Python calls it for you when you use a built-in
  function like `len()` or an operator like `==`, which is why they're also called **magic methods**.

  | You write | Python calls |
  |---|---|
  | `print(pack)` | `pack.__str__()` |
  | `len(pack)` | `pack.__len__()` |
  | `pack == other` | `pack.__eq__(other)` |
  | `pack + extra` | `pack.__add__(extra)` |

- **The problem (`before.py`):** with only `__init__`, `print(pack)` shows the class name and a memory address, like
  `<__main__.Backpack object at 0x102b88830>` (the address changes every run), and two backpacks that hold the same
  things aren't equal: `==` only checks whether both sides are the very same object.
- **The class with five dunder methods (`backpack.py`):**
  ```python
  # Python calls these dunder methods for you
  class Backpack:
      def __init__(self, items):
          self.items = items

      def __str__(self):
          return "Backpack: " + ", ".join(self.items)

      def __repr__(self):
          return f"Backpack({self.items})"

      def __len__(self):
          return len(self.items)

      def __eq__(self, other):
          return self.items == other.items

      def __add__(self, other):
          return Backpack(self.items + other.items)


  pack = Backpack(["sword", "rope"])
  extra = Backpack(["torch"])
  print(pack)                                # Backpack: sword, rope
  print([pack, extra])                       # [Backpack(['sword', 'rope']), Backpack(['torch'])]
  print(len(pack))                           # 2
  print(pack == Backpack(["sword", "rope"]))  # True
  print(pack + extra)                        # Backpack: sword, rope, torch
  ```
  - `__str__` is the text `print` shows. It has to **return** a string (`join` is from lesson 8).
  - `__repr__` ("representation") is the version for programmers: it looks like the code that made the object. A list
    shows its items with `__repr__`, and so does VS Code's debugger. Rule of thumb: `__str__` is for the people using
    your program, `__repr__` is for you when you're debugging. If you only write one, write `__repr__`, because `print`
    uses it when there's no `__str__`.
  - `__len__` is what `len()` calls, and it has to return a whole number.
  - `__eq__` is what `==` calls: `self` is the backpack on the left, `other` the one on the right. Now two backpacks
    are equal when they hold the same items in the same order.
  - `__add__` is what `+` calls. `+` on two lists makes one new list, so it returns a brand new backpack, and neither
    backpack changes.
  - Later in the course, dataclasses can write `__init__`, `__repr__` and `__eq__` for you.
- **The common mistakes:**
  - Printing inside `__str__` instead of returning the text: the text shows up once (the method printed it), then
    `TypeError: Backpack.__str__() must return a str, not NoneType`, because a function with no `return` hands back
    `None` (lesson 24). Return the text and let `print` do the printing.
  - One underscore on each side (`def _str_(self):`): no error, but `print(pack)` shows `Backpack(['sword', 'rope'])`,
    the `__repr__` version, because Python only looks for the exact name `__str__`. Count the underscores: two before
    the name, two after.

## Files
- `before.py`: the backpack with only `__init__` (the start of the video).
- `backpack.py`: the program from the video.
- `starter.py`: the "your turn" exercise, with TODOs.
- `solution.py`: one way to solve it.
- `gems.py`, `minutes.py`, `playlist.py`: practice problems 1, 2 and 3 (`minutes.py` and `playlist.py` are one answer
  each: try them yourself first).

## Run it
```
python3 backpack.py      # Mac
python backpack.py       # Windows
```
The same goes for every other file.

## Your turn
Add one more method under `__add__`, called `__lt__` ("less than": it's what `<` calls, and `sorted()` uses it to put
things in order), with `self` and `other`, that returns `len(self) < len(other)`. Then `print(extra < pack)`. It prints
`True`. (`solution.py` also prints `sorted([pack, extra])`: the backpack with fewer items comes first.)

## Practice
1. Predict, then run `gems.py`:
   ```python
   class Gem:
       def __init__(self, color):
           self.color = color

       def __repr__(self):
           return f"Gem('{self.color}')"


   red = Gem("red")
   print(red)
   print([red, Gem("blue")])
   print(red == Gem("red"))
   ```
   (`Gem('red')`: there's no `__str__`, so `print` uses `__repr__`. `[Gem('red'), Gem('blue')]`: a list always uses
   `__repr__`. `False`: there's no `__eq__`, so `==` asks whether they're the very same object, and they aren't.)
2. Write `minutes.py`: a `Minutes` class with an `amount`, a `__str__` that shows it like `90 min`, an `__add__` that
   returns a new `Minutes`, and an `__eq__`. With `warmup = Minutes(30)` and `workout = Minutes(60)`,
   `print(warmup + workout)` prints `90 min`, and `print(warmup + warmup == workout)` prints `True`.
3. Write `playlist.py`: a `Playlist` class with a `name` and a list of `songs`, a `__len__` that returns how many songs
   it has, and a `__str__` that uses `len(self)`. For `Playlist("Road trip", ["Highway", "Sunrise", "Home"])`,
   `print(len(trip))` prints `3` and `print(trip)` prints `Road trip: 3 songs`.
