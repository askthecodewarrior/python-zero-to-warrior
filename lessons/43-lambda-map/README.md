# Lesson 43: lambda, map, filter and sorted in Python

Part of **Python: Zero to Warrior**, a free Python course for beginners.
Video: https://youtu.be/TRZD3FNuSX0 · Full course: https://www.youtube.com/playlist?list=PLcsbg964FAwc

## What's in this lesson
- **A function is a value**, the same way a number or a string is. `len("crossbow")` calls the function and gives back
  `8`; `len` on its own, with no parentheses, is the function itself (`print(len)` prints `<built-in function len>`).
  So you can hand a function to another function, and that one calls it for you. `sorted`, `map` and `filter` all work
  that way, and so do decorators, later in the course.
- **sorted() and key=:**
  ```python
  weapons = ["sword", "bow", "crossbow", "mace"]
  print(sorted(weapons))                          # ['bow', 'crossbow', 'mace', 'sword']
  print(sorted(weapons, key=len))                 # ['bow', 'mace', 'sword', 'crossbow']
  print(sorted(weapons, key=len, reverse=True))   # ['crossbow', 'sword', 'mace', 'bow']
  ```
  `sorted` gives you back a new list in order and leaves `weapons` as it was. For lowercase words like these the order
  is alphabetical (capital letters sort before every lowercase letter: see practice 1). `key` is a keyword argument
  (lesson 25): sorted calls that function on every item and sorts by what comes back. There are no parentheses after
  `len`, because you're handing the function to sorted, not calling it. `reverse=True` flips the order.
  Lists also have a sort method: `weapons.sort()` changes the list itself and gives back `None`.
- **lambda: a tiny function with no name.** These two do the same thing:
  ```python
  def price(item):
      return item[1]

  lambda item: item[1]
  ```
  A lambda is the word `lambda`, the parameter, a colon, and one expression, which it hands back for you (no `def`, no
  name, no `return`). Use one for a short key or rule you need in one place. Anything with statements in it (a loop, an
  if block), or anything you'll use again, gets a `def` with a name.
  ```python
  loot = [("sword", 120), ("bow", 75), ("mace", 40)]
  print(sorted(loot, key=lambda item: item[1]))   # [('mace', 40), ('bow', 75), ('sword', 120)]
  ```
  Without the key, sorted compares the tuples by their first item, the name: `[('bow', 75), ('mace', 40), ('sword', 120)]`.
- **map() and filter():** both take a function and a list. `map` calls the function on every item and keeps every
  result (new values: `loot` doesn't change); `filter` keeps only the items where the function gives back `True`.
  ```python
  half = map(lambda item: item[1] // 2, loot)
  print(list(half))                         # [60, 37, 20]
  print([item[1] // 2 for item in loot])    # [60, 37, 20]

  cheap = filter(lambda item: item[1] < 100, loot)
  print(list(cheap))                                # [('bow', 75), ('mace', 40)]
  print([item for item in loot if item[1] < 100])   # [('bow', 75), ('mace', 40)]
  ```
  In Python 3, `map` and `filter` hand you a map object and a filter object, not a list: they work out each value only
  when something asks for it, so `list()` collects them. Under each one is the list comprehension (lesson 22) that does
  the same job. map and filter read best when you already have a function with a name (`map(int, prices)` in practice
  2); when you'd need a lambda anyway, the comprehension is usually the clearer choice.
- **The common mistakes:**
  - Printing the map object itself: `print(half)` prints something like `<map object at 0x102c56d40>` (the address
    changes every run). Wrap it in `list()`. And a map object hands out its values only once, so a second `list(half)`
    gives `[]`. Lesson 45 (generators) shows why.
  - Putting `return` inside a lambda: `key=lambda item: return item[1]` stops with `SyntaxError: invalid syntax`, the
    arrows under `return`. A lambda holds one expression and hands it back for you, so take `return` out.

## Files
- `armory.py`: the program from the video.
- `starter.py`: the "your turn" exercise, with TODOs.
- `solution.py`: one way to solve it.
- `predict.py`, `numbers.py`, `richest.py`: practice problems 1, 2 and 3 (`numbers.py` and `richest.py` are one answer
  each: try them yourself first).

## Run it
```
python3 armory.py      # Mac
python armory.py       # Windows
```
The same goes for every other file.

## Your turn
Sort `loot` by price with the most expensive first (the same lambda, plus `reverse=True`). Then use `filter` and a
lambda to keep only the weapons with more than 4 letters, and write that same filter as a list comprehension. The sort
puts `('sword', 120)` first, and both of the other two print `['sword', 'crossbow']`.

## Practice
1. Predict, then run `predict.py`:
   ```python
   names = ["Zed", "amy", "Bo"]
   print(sorted(names))
   print(sorted(names, key=str.lower))
   ```
   (`['Bo', 'Zed', 'amy']`: capital letters sort before lowercase ones. Then `['amy', 'Bo', 'Zed']`: `str.lower` is a
   function too (no parentheses), so sorted compares the lowercase copies and keeps the names as they were.)
2. Write `numbers.py`: text from a file or `input()` comes in as strings. Turn `["40", "75", "120"]` into numbers with
   `map(int, ...)` (`int` is the function you hand over), print the list and its `sum()`, then do the same with a
   comprehension. It prints `[40, 75, 120]`, `235` and `[40, 75, 120]`.
3. Write `richest.py`: `max()` and `min()` take a `key` the same way `sorted` does. Use them with the lambda from the
   video to print the most expensive and the cheapest item in `loot`: `('sword', 120)` and `('mace', 40)`.
