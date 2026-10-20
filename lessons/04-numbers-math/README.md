# Lesson 04: Numbers and Math in Python

Part of **Python: Zero to Warrior**, a free Python course for beginners.
Video: https://youtu.be/ko_E0JQn6Dw · Full course: https://www.youtube.com/playlist?list=PLcsbg964FAwc

## What's in this lesson
- A whole number like `17` is an `int`. A number with a decimal point like `3.4` is a `float`.
- `+` adds, `-` subtracts, `*` multiplies and `/` divides. A single `/` always gives you a float: `10 / 5` is `2.0`.
- `//` is floor division: it divides, then rounds down to a whole number. `17 // 5` is `3` (three full bags of 5).
- `%` is the remainder (often called mod, short for modulo): `17 % 5` is `2` (two left over).
- `**` is power: `2 ** 3` is `2 * 2 * 2`, which is `8`.
- Order of operations: parentheses first, then `**`, then `* / // %`, then `+ -`. So `10 + 2 * 3` is `16`, and
  `(10 + 2) * 3` is `36`.
- Watch out: `^` is not power in Python (`2 ^ 3` prints `1`), and `0.1 + 0.2` prints `0.30000000000000004`
  because floats are stored in binary. `round(0.1 + 0.2, 2)` gives `0.3`.

## Files
- `solution.py`: the program from the video (`loot.py`).
- `starter.py`: the "your turn" exercise, with TODOs to fill in.

## Run it
```
python3 solution.py      # Mac
python solution.py       # Windows
```

## Practice
1. A quest takes 135 minutes. Use `//` and `%` with 60 to print it as hours and minutes. (You should get 2 hours
   and 15 minutes.)
2. Print `14 % 2` and `15 % 2`. What does `%` with 2 give you for even numbers, and for odd ones?
3. Predict first, then run it: `print(2 + 3 * 4 ** 2)` and `print((2 + 3) * 4 ** 2)`. Which part does Python work
   out first in each one?
