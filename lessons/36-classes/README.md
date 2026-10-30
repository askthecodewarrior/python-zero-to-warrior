# Lesson 36: Classes and Objects in Python – OOP for Beginners

Part of **Python: Zero to Warrior**, a free Python course for beginners. This is the first lesson of the intermediate
part of the course.
Video: https://youtu.be/wbKxmU7zDA4 · Full course: https://www.youtube.com/playlist?list=PLcsbg964FAwc

## What's in this lesson
- **A class is a blueprint, and an object is one thing made from it.** The `Player` class says every player has a name
  and a health, and that a player can take a hit. `hero` and `rival` are two objects made from that one class, and each
  one has its own name and its own health. An object made from a class is also called an **instance** of that class.
  Writing programs around objects like this is called **object-oriented programming (OOP)**.
- **Why a class:** in lesson 20 a dictionary held a player's data, and in lesson 24 functions did things with data you
  passed in. A class keeps the data and the functions that use it together in one place.
- **The class:**
  ```python
  # A blueprint for a player in a game
  class Player:
      def __init__(self, name, health):
          self.name = name
          self.health = health

      def take_hit(self, damage):
          self.health -= damage
  ```
  - `class Player:` starts the class. A class name starts with a capital letter, and each word gets a capital with no
    underscore (`TreasureChest`). Python doesn't make you do that, but it's the style Python programmers use for the
    classes they write.
  - `__init__` ("dunder init": dunder is short for double underscore, like `__name__` in lesson 29) is a special method
    that Python runs for you every time you make a new object. It's where each object gets its starting data.
  - A **method** is a function that belongs to a class, so it starts with `def`.
  - `self` is the object the method is working on: the new object in `__init__`, and the object you called the method on
    in `take_hit`. Lesson 37 goes much deeper into `__init__` and `self`.
  - `self.name = name` makes an **attribute**: a variable that belongs to one object.
- **Making objects and using them:**
  ```python
  hero = Player("Warrior", 100)
  rival = Player("Shadow", 80)
  print(hero.name, hero.health)    # Warrior 100
  print(rival.name, rival.health)  # Shadow 80

  hero.take_hit(30)
  print(hero.name, hero.health)    # Warrior 70
  print(rival.name, rival.health)  # Shadow 80
  ```
  Calling the class like a function makes a new object; `"Warrior"` and `100` go to `name` and `health` in
  `__init__`, and you don't pass `self` (Python fills it in). The dot gets an attribute (`hero.health`) or calls a
  method (`hero.take_hit(30)`). Only hero's health changes, because each object keeps its own data.
- **The common mistakes:**
  - Printing the object itself: `print(hero)` prints something like `<__main__.Player object at 0x100e1c830>`, which
    is Python's default way to show an object (a Player from the file you ran, at an address in memory that changes
    every run). Print its attributes instead: `print(hero.name, hero.health)`.
  - Making an object without its values: `Player()` stops with
    `TypeError: Player.__init__() missing 2 required positional arguments: 'name' and 'health'`. It says 2, not 3,
    because Python passes `self` for you. Give it what `__init__` asks for: `Player("Warrior", 100)`.

## Files
- `players.py`: the program from the video.
- `starter.py`: the "your turn" exercise, with TODOs.
- `solution.py`: one way to solve it.
- `chests.py`, `pets.py`, `lamp.py`: practice problems 1, 2 and 3 (`pets.py` and `lamp.py` are one answer each: try them
  yourself first).

## Run it
```
python3 players.py      # Mac
python players.py       # Windows
```
The same goes for every other file.

## Your turn
Add a `heal` method under `take_hit`, with `self` and `amount`, that adds the amount to `self.health`. Then call
`rival.heal(20)` and print `rival.name` and `rival.health`. It prints `Shadow 100`.

## Practice
1. Predict, then run `chests.py`:
   ```python
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
   ```
   (`75 50`: two objects, each with its own gold. Then `0 0`: after `right = left`, both names point at the same object,
   like two name tags on one box (lesson 3), so changing it through one name changes what the other one sees.)
2. Write `pets.py`: a `Pet` class with a `name` and a `hunger` number, and a `feed(amount)` method that takes the amount
   off `hunger`. Make two pets, feed one of them, and print both. With `Pet("Mochi", 8)` fed 3 and `Pet("Rex", 5)` not
   fed, it prints `Mochi hunger: 5` and `Rex hunger: 5`.
3. Write `lamp.py`: a `Lamp` class with a `room`, an `on` attribute that starts as `False` (set it in `__init__`
   without a parameter), and a `toggle()` method that switches it with `not` (lesson 12). Toggle it twice and print it
   each time: `office lamp on: True`, then `office lamp on: False`.
