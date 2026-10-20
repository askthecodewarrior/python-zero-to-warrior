# Lesson 05: User Input and Type Casting in Python

Part of **Python: Zero to Warrior**, a free Python course for beginners.
Video: https://youtu.be/gHteuNjZAgk · Full course: https://www.youtube.com/playlist?list=PLcsbg964FAwc

## What's in this lesson
- `input("prompt")` shows the prompt, waits until the user types and hits Enter, and hands back what they typed.
- `input()` always gives you back a `str` (text), even when the user types a number. `type()` proves it.
- `+` between two strings joins them (that's called concatenation): `"5" + "5"` is `"55"`, while `5 + 5` is `10`.
- Casting changes a value's type: `int("5")` is `5`, `float("92.5")` is `92.5`, `str(10)` is `"10"`.
- The usual way to ask for a number is one line: `coins = int(input("Coins: "))`. Python works from the inside out.
- Two common errors:
  - `TypeError: can only concatenate str (not "int") to str` when you add a number to what `input()` gave you
    without converting it first.
  - `ValueError: invalid literal for int() with base 10: 'seven'` when the user types something `int()` can't read,
    like a word or `3.5`. Use `float()` if you need decimals.

## Files
- `solution.py`: the program from the video (type 5 and 5 when it asks).
- `starter.py`: the "your turn" exercise, with TODOs to fill in.

## Run it
```
python3 solution.py      # Mac
python solution.py       # Windows
```

## Practice
1. Ask for the player's name and their level, then print the name and the level plus 1. Convert the level first.
2. Ask for a price with `float(input(...))` and print it times 2. What happens if you use `int()` and type `4.99`?
3. Predict first, then run it: `x = input("Pick a number: ")` and `print(x * 2)`. Type 4. Now change it to
   `int(x) * 2`.
