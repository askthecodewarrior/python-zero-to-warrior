# Lesson 12: and, or, not: Logical Operators in Python

Part of **Python: Zero to Warrior**, a free Python course for beginners.
Video: https://youtu.be/LcZRRMNBfQ8 · Full course: https://www.youtube.com/playlist?list=PLcsbg964FAwc

## What's in this lesson
- The three logical operators join True/False checks:
  - `and` is True only when **both** sides are True: `has_key and level >= 5`.
  - `or` is True when **at least one** side is True: `has_key or level >= 5`.
  - `not` flips one value: `not stunned` is True when `stunned` is False.
- The truth table: `and` is True in one row only (True and True); `or` is False in one row only (False or False).
- Inside an `if`, the whole condition has to work out True for the indented block to run.
- Order: Python does `not` first, then `and`, then `or`, the way it does multiplication before addition.
  `True or False and False` is `True`; `(True or False) and False` is `False`. When you mix `and` and `or`, use
  parentheses so nobody has to remember the order.
- The classic mistake: `if answer == "y" or "yes":` is always True, because `"yes"` on its own is a non-empty
  string, and a non-empty string is truthy. Write a full check on each side: `answer == "y" or answer == "yes"`.

## Files
- `solution.py`: the program from the video (door.py).
- `dungeon.py`: the dungeon program from the video, with the fix.
- `starter.py`: the "your turn" exercise (a treasure chest), with TODOs to fill in.
- `chest_solution.py`: one way to solve it.

## Run it
```
python3 solution.py      # Mac
python solution.py       # Windows
```

## Practice
1. Predict, then run: `print(not True or True)` and `print(not (True or True))`. Why are they different?
2. Run `dungeon.py` and type `Yes` with a capital Y. It says you stay outside. Fix it so `Y`, `y`, `YES` and `yes`
   all let you in. (Hint: `.lower()` from the string methods lesson.)
3. Python lets you write `level >= 1 and level <= 10` as `1 <= level <= 10`. Set `level = 7`, print both, and check
   they match. Then try a level of 12.
