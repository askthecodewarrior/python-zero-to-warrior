# Lesson 03: Variables and Data Types in Python

Part of **Python: Zero to Warrior**, a free Python course for beginners.
Video: https://youtu.be/lWtvoZPPpoI · Full course: https://www.youtube.com/playlist?list=PLcsbg964FAwc

## What's in this lesson
- A variable is a name tag on a value: `name = value`. The `=` means "put this name on that value", not "equals".
- The four basic data types: `str` (text, in quotes), `int` (a whole number), `float` (a number with a decimal point)
  and `bool` (`True` or `False`, with a capital letter).
- `type()` tells you a value's type. `print()` can show several things separated by commas, with a space between each.
- Variables can change: `level = level + 1` works out the right side first, then moves the name tag.
- Variable names use snake_case: lowercase words joined with underscores.

## Files
- `solution.py`: the program from the video.
- `starter.py`: the "your turn" exercise, with TODOs to fill in.

## Run it
```
python3 solution.py      # Mac
python solution.py       # Windows
```

## Practice
1. Make a variable `coins = 50`, then give the player 25 more coins with `coins = coins + 25`. Print it.
2. What does `print(type("42"))` show? Why isn't it `int`? Run it and check.
3. Make the mistakes on purpose: print a variable name in quotes, then misspell one. Read what Python tells you.
