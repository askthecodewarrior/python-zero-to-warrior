# Lesson 38: Inheritance and super() in Python

Part of **Python: Zero to Warrior**, a free Python course for beginners.
Video: https://youtu.be/UdCqwnVQ3Bc · Full course: https://www.youtube.com/playlist?list=PLcsbg964FAwc

## What's in this lesson
- **Inheritance means writing shared code once.** A goblin and a boss are both enemies: both need a name and the
  damage they do, and both attack. Put that in a **parent class** (also called a base class or a superclass), and make
  each kind of enemy a **child class** (also called a subclass) that gets everything the parent has. A good check is
  to say it out loud: "a goblin is an enemy".
- **`class Goblin(Enemy):`** The class in the parentheses is the parent. Goblin has no `__init__` and no `attack()`
  of its own, so Python looks in Goblin first, doesn't find them, and uses Enemy's. Goblin adds a new method, `steal()`,
  that only goblins have, and it can still use `self.name`, because Enemy's `__init__` set it.
  ```python
  # A Goblin gets everything an Enemy has
  class Enemy:
      def __init__(self, name, damage):
          self.name = name
          self.damage = damage

      def attack(self):
          print(self.name, "hits for", self.damage)


  class Goblin(Enemy):
      def steal(self):
          print(self.name, "steals a coin")


  grub = Goblin("Grub", 5)
  grub.attack()
  grub.steal()
  print(isinstance(grub, Enemy))
  ```
  It prints `Grub hits for 5`, `Grub steals a coin` and `True`: `isinstance()` checks whether an object belongs to a
  class, and an object of a child class counts. It only goes one way: a plain `Enemy` doesn't get `steal()`.
- **`super().__init__(...)` reuses the parent's setup.** As soon as a child class has its own `__init__`, Python runs
  that one instead of the parent's, so the parent's `__init__` doesn't run unless you call it. `super()` is how a child
  class calls its parent's methods. Don't pass `self` to it: Python passes it for you.
- **Overriding, and extending with `super().method()`.** A method in the child with the same name as one in the parent
  **overrides** it: on a boss, Python finds Boss's `attack()` first. With no `super()` line, it replaces the parent's
  method; with `super().attack()` in it, it runs the parent's version and then adds to it.
  ```python
  # A Boss adds to what an Enemy does
  class Enemy:
      def __init__(self, name, damage):
          self.name = name
          self.damage = damage

      def attack(self):
          print(self.name, "hits for", self.damage)


  class Boss(Enemy):
      def __init__(self, name, damage, shield):
          super().__init__(name, damage)
          self.shield = shield

      def attack(self):
          super().attack()
          print(self.name, "breathes fire")


  boss = Boss("Dragon", 10, 50)
  print(boss.name, "has a shield of", boss.shield)
  boss.attack()
  ```
  `Dragon has a shield of 50`, then `Dragon hits for 10` (Enemy's attack, run by `super().attack()`) and
  `Dragon breathes fire` (the line Boss added). Take the `super().attack()` line out, and the dragon only breathes fire.
- **The common mistakes:**
  - A child `__init__` with no `super().__init__(...)` line: making the object works, but the first time something
    uses a parent attribute, Python stops with `AttributeError: 'Boss' object has no attribute 'name'`. Nothing ran
    Enemy's `__init__`, so the name and the damage were never set.
  - `self` passed to `super().__init__(self, name, damage)`: Python already passes `self`, so Enemy's `__init__` gets
    four arguments and stops with `TypeError: Enemy.__init__() takes 3 positional arguments but 4 were given`.
- A class can have more than one parent, but you won't need that for a while.

## Files
- `enemies.py`, `boss.py`: the programs from the video.
- `starter.py`: the "your turn" exercise, with TODOs.
- `solution.py`: one way to solve it (its last two lines print `Bones hits for 3` and `12`).
- `predict.py`, `weapon.py`, `bug.py`: practice problems 1, 2 and 3 (`weapon.py` is one answer, and `bug_fixed.py` is
  `bug.py` fixed: try them yourself first).

## Run it
```
python3 boss.py       # Mac
python boss.py        # Windows
```
The same goes for every other file.

## Practice
1. Predict, then run `predict.py`: an `Item` class with `describe()` and `use()`, and a `Potion(Item)` that overrides
   only `use()`. (`You can't use the rope`, `tonic costs 10 gold`, `You drink the tonic`, `False`: the potion uses the
   parent's `describe()`, its own `use()`, and a plain `Item` isn't a `Potion`.)
2. Write a `Weapon(Item)` class whose `__init__` takes `name`, `price` and `damage`, sets the first two with
   `super().__init__`, and whose `describe()` calls `super().describe()` and then prints `It hits for` and the damage.
   `Weapon("axe", 25, 7).describe()` should print `axe costs 25 gold`, then `It hits for 7`.
3. Fix `bug.py`. It has two bugs. The first run stops with
   `AttributeError: type object 'super' has no attribute 'describe'`. Fix that one, and the next run stops with
   `AttributeError: 'Shield' object has no attribute 'name'`. When both are fixed, it prints
   `wooden shield costs 8 gold`, then `It blocks 2`.
