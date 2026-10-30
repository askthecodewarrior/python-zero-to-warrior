# Lesson 37: __init__, self and Methods in Python

Part of **Python: Zero to Warrior**, a free Python course for beginners.
Video: https://youtu.be/AOWp2xl9P4c · Full course: https://www.youtube.com/playlist?list=PLcsbg964FAwc

## What's in this lesson
- **`__init__` runs every time you make an object.** "init" is short for initialize: its job is to set up each new
  object. People call it "dunder init", because of the two underscores on each side (like `__name__` in lesson 29).
  When you write `Player("Ana")`, Python makes a brand new empty object, runs `__init__` with `self` as that new object
  and `name` as `"Ana"`, and hands the object back.
  ```python
  # __init__ runs every time you make a player
  class Player:
      def __init__(self, name, hp=100):
          self.name = name
          self.hp = hp
          self.potions = 2
          print("Made", self.name)


  ana = Player("Ana")
  kai = Player("Kai", 60)
  print(ana.name, ana.hp, ana.potions)
  print(kai.name, kai.hp, kai.potions)
  ```
  It prints `Made Ana` and `Made Kai` first, because `__init__` runs right on lines 10 and 11, then `Ana 100 2` (Ana
  got the default) and `Kai 60 2`.
- **Defaults and attributes.** `hp=100` is a default value (lesson 25): leave it out and the player starts with 100.
  `self.name = name` stores the value on the object as an **attribute**. `self.potions = 2` doesn't come from a
  parameter at all: every player starts with two. `name` on its own is just a parameter, and it's gone when
  `__init__` finishes (lesson 26), so `self.name` is how the object keeps it.
- **Instance vs class attributes.** Attributes you set with `self` are **instance attributes**: each object gets its
  own. A variable inside the class but outside any method is a **class attribute**, shared by every object.
- **Methods read and change the object, and can call each other through `self`:**
  ```python
  # Methods read and change the player
  class Player:
      def __init__(self, name, hp=100):
          self.name = name
          self.hp = hp
          self.potions = 2

      def show(self):
          print(self.name, "has", self.hp, "HP")

      def drink_potion(self):
          self.potions -= 1
          self.hp += 20
          self.show()


  kai = Player("Kai", 60)
  kai.drink_potion()
  kai.drink_potion()
  print("Potions left:", kai.potions)
  ```
  `Kai has 80 HP`, `Kai has 100 HP`, `Potions left: 0`: the object keeps its data from one call to the next.
- **What `self` is.** `self` is the object in front of the dot. `kai.drink_potion()` is the same call as
  `Player.drink_potion(kai)`: Python finds the method in the class and passes the object in as the first argument.
  That's why `self` always comes first in the `def` line, and why you don't pass it yourself when you call a method
  with a dot.
- **The common mistakes:**
  - `self` left out of the `def` line (`def show():`): calling `kai.show()` stops with
    `TypeError: Player.show() takes 0 positional arguments but 1 was given`. The one that was given is the object.
  - `self.` left off an attribute inside a method (`print(name, "has", hp, "HP")`): Python stops with
    `NameError: name 'name' is not defined. Did you mean: 'self.name'?`

## Files
- `player.py`, `battle.py`: the programs from the video.
- `starter.py`: the "your turn" exercise, with TODOs.
- `solution.py`: one way to solve it (its last line prints `Kai is now level 2`).
- `order.py`, `chest.py`, `bug.py`: practice problems 1, 2 and 3 (`chest.py` is one answer, and `bug_fixed.py` is
  `bug.py` fixed: try them yourself first).

## Run it
```
python3 battle.py       # Mac
python battle.py        # Windows
```
The same goes for every other file.

## Practice
1. Predict, then run `order.py`: a class whose `__init__` prints, then `print("Start")`, two players, and
   `print("End")`. (`Start`, `Made Ana`, `Made Kai`, `End`: each `__init__` runs on the line that makes its player.)
2. Write `chest.py`: a `Chest` class whose `__init__` takes `gold` with a default of 0, a `show()` method that prints
   `The chest has 10 gold`, and an `add(self, amount)` method that adds to `self.gold` and then calls `self.show()`.
   Make `Chest()` and `Chest(50)`, add 10 to the first and 25 to the second, then show the first again:
   `The chest has 10 gold`, `The chest has 75 gold`, `The chest has 10 gold`.
3. Fix `bug.py`. It has two bugs. The first run stops with
   `TypeError: Player.show() takes 0 positional arguments but 1 was given`. Fix that one, and the next run stops with
   `UnboundLocalError: cannot access local variable 'hp' where it is not associated with a value`. When both are fixed,
   it prints `Ana has 100 HP`, then `Ana has 85 HP`.
