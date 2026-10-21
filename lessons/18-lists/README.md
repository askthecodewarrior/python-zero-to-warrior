# Lesson 18: Lists in Python for Beginners

Part of **Python: Zero to Warrior**, a free Python course for beginners.
Video: https://youtu.be/elXHWQzpTi4 · Full course: https://www.youtube.com/playlist?list=PLcsbg964FAwc

## What's in this lesson
- A **list** keeps a bunch of values, in order, in one variable. You write it with square brackets and commas:
  `inventory = ["sword", "shield", "potion"]`. Each value in a list is called an **item**. A list can hold numbers or
  a mix of types too, but most of the time every item is the same kind of thing.
- Every item has an **index**, just like the characters in a string (lesson 7): Python starts counting at 0, so
  `inventory[0]` is `"sword"` and `inventory[2]` is `"potion"`. Negative indexes count from the end: `inventory[-1]`
  is always the last item. Slices work too: `inventory[0:2]` gives you a new list, `['sword', 'shield']`.
- `len(inventory)` counts the items (3 here).
- When you print a list, Python usually shows its strings in single quotes: `['sword', 'shield', 'potion']`. It's the
  same list.
- Lists are **mutable**: you can change them after they're made (strings can't be changed, lesson 7).
  `inventory[1] = "gold shield"` puts a new item at index 1.
- Four list methods that change the list itself:
  - `inventory.append("rope")` adds an item to the end. Start with an empty list, `[]`, and append is how you add
    items one at a time;
  - `inventory.insert(0, "torch")` puts an item in at that index, and every item after it moves over one;
  - `inventory.remove("potion")` takes out the first item equal to that value (a ValueError if it isn't there);
  - `dropped = inventory.pop()` takes the last item off the end and hands it back.
  There are more, like `sort()`, which puts the items in order.
- `"sword" in inventory` is True when the value is in the list, and False when it isn't. It's handy before a
  `remove`.
- A `for` loop goes through a list one item at a time (lesson 15): `for item in inventory:`.
- The classic mistake: asking for an index that isn't there. A list of 3 items has indexes 0, 1 and 2, so
  `inventory[3]` stops with `IndexError: list index out of range`. The last index is always `len(inventory) - 1`, or
  just use `inventory[-1]`. An empty list has no items at all, so even index 0 gives you that error.

## Files
- `inventory.py`: the program from the video.
- `starter.py`: the "your turn" exercise, with TODOs.
- `solution.py`: one way to solve it.
- `count.py` and `safe_remove.py`: answers to practice problems 2 and 3 (try them yourself first).

## Run it
```
python3 inventory.py      # Mac
python inventory.py       # Windows
```
The same goes for every other file.

## Practice
1. Predict, then run: start with `inventory = ["sword", "shield", "potion"]`, then
   `inventory.insert(1, "map")`. What does `print(inventory[2])` show? (shield: everything from index 1 on moved over
   one.)
2. Count the items yourself: write a for loop that adds 1 to a `count` variable for every item, then print it next to
   `len(inventory)`. They should match.
3. Remove safely: before calling `inventory.remove(want)`, check `if want in inventory:`, and print a message when it
   isn't there instead of getting a ValueError.
