# Lesson 19: Tuples and Sets in Python

Part of **Python: Zero to Warrior**, a free Python course for beginners.
Video: https://youtu.be/BgshQ1qkBpA · Full course: https://www.youtube.com/playlist?list=PLcsbg964FAwc

## What's in this lesson
- A **tuple** is a lot like a list (lesson 18): it keeps its items in order, and every item has an index. You write it
  with parentheses and commas: `start = (3, 7)`. So `start[0]` is `3` and `start[1]` is `7`.
- A tuple is **immutable**, just like a string (lesson 7): once it's made, you can't add, remove or change its items.
  `start[0] = 5` stops with `TypeError: 'tuple' object does not support item assignment`. If the value really changes,
  make a new tuple and put the name on it: `start = (5, 7)`.
- Use a tuple for values that belong together and shouldn't change, like a position on a map, or a date.
- **Unpacking** puts each item of a tuple in its own variable: `x, y = start` makes `x` 3 and `y` 7, and `start` still
  holds both. The number of variables before the `=` has to match the number of items, or you get a `ValueError`.
- A **set** keeps each value only once. You write it with curly braces: `loot = {"gold", "gem", "gold", "key"}` holds
  three items, because the second `"gold"` is dropped, so `len(loot)` is 3.
- A set has **no order**, so it has no index: `loot[0]` stops with `TypeError: 'set' object is not subscriptable`.
  When you print a set, the order may not match the order you typed, and it can be different on your computer (or
  from one run to the next, for strings). That's normal.
- Sets can change: `loot.add("map")` puts an item in (a set has no `append`, because there's no end to add to), and
  `loot.remove("key")` takes one out. `"map" in loot` is True when the value is in the set, just like `in` with a list.
- Turn a list into a set to get rid of duplicates: `unique = set(drops)`. If you need a list again, `list(unique)`
  gives you one, but the order might not be the same.
- Which one? A **list** for items that change (an inventory), a **tuple** for values that belong together and don't
  change (a position, a date), a **set** when you don't want duplicates and only care whether something is in there.
- The classic mistake: `{}` on its own is an empty **dictionary** (a different type that stores pairs of values), not
  an empty set, so `loot = {}` then `loot.add("gold")` stops with `AttributeError: 'dict' object has no attribute
  'add'`. For an empty set, use `loot = set()`.

## Files
- `quest.py`: the program from the video.
- `starter.py`: the "your turn" exercise, with TODOs.
- `solution.py`: one way to solve it.
- `unpack.py` and `unique.py`: answers to practice problems 2 and 3 (try them yourself first).

## Run it
```
python3 quest.py      # Mac
python quest.py       # Windows
```
The same goes for every other file. Your sets may print their items in a different order from the video's: a set
has no order.

## Practice
1. Predict, then run: `colors = {"red", "blue", "red", "green", "blue"}`. What does `print(len(colors))` show? (3:
   each color is kept once.)
2. Unpack three items: make `player = ("Warrior", 7, 92.5)`, unpack it into `name, level, health`, and print a line
   that says the player's name and level.
3. Count the unique visitors: start with a list of names where some names come more than once, turn it into a set,
   print the number of visits and the number of unique visitors, and check whether one name is `in` the set.
