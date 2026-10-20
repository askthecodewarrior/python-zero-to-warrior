# Lesson 10: Booleans and Comparison Operators in Python

Part of **Python: Zero to Warrior**, a free Python course for beginners.
Video: https://youtu.be/0hbbBDLEQdg · Full course: https://www.youtube.com/playlist?list=PLcsbg964FAwc

## What's in this lesson
- A **bool** (boolean) has only two values: `True` and `False`. They start with a capital letter and don't go in
  quotes. `type(7 == 7)` is `<class 'bool'>`.
- A **comparison** asks Python a question about two values, and the answer is always a bool.
- The six **comparison operators**:

  | Operator | It asks | Example | Result |
  |---|---|---|---|
  | `==` | equal to? | `7 == 10` | `False` |
  | `!=` | not equal to? | `7 != 10` | `True` |
  | `<` | less than? | `7 < 10` | `True` |
  | `>` | greater than? | `7 > 10` | `False` |
  | `<=` | less than or equal to? | `7 <= 7` | `True` |
  | `>=` | greater than or equal to? | `7 >= 7` | `True` |

- One `=` **stores** a value (`level = 7`). Two, `==`, **ask** if two values are equal (`level == 7`).
- You can store a comparison: `ready = level >= boss_level`. Python works out the right side first.
- Comparing strings is **case sensitive**: `"warrior" == "Warrior"` is `False`.
- A string is never equal to a number: `"5" == 5` is `False`. `input()` always gives you a string, so convert it
  first: `int("5") == 5` is `True`.
- `bool()` turns any value into `True` or `False`.
  - **Falsy** (turns into `False`): `0`, `0.0`, `""` (an empty string), and `False` itself. There are a few more,
    but they use things later in the course.
  - **Truthy** (turns into `True`): the rest of what we tried: `7`, `-1`, `"warrior"`, even `" "` (just a space).
  - `bool("False")` is `True`: in quotes, `"False"` is a string with five letters in it, and it isn't empty.

## Common mistakes
- One equals sign where you meant two: `print(level = 7)` stops with
  `TypeError: print() got an unexpected keyword argument 'level'`. Use `print(level == 7)`.
- Lowercase `true` or `false`: `NameError: name 'true' is not defined. Did you mean: 'True'?`

## Files
- `solution.py`: `compare.py` from the video.
- `truthy.py`: the second program from the video.
- `starter.py`: the two "your turn" exercises, with TODOs to fill in.

## Run it
```
python3 solution.py      # Mac
python solution.py       # Windows
```

## Practice
1. Predict first, then run: `print(10 >= 10)`, `print(10 > 10)` and `print("Apple" == "apple")`.
2. Ask for the player's age with `int(input("Age: "))`, then print whether it's 13 or more with `print(age >= 13)`.
   Run it twice: type `12`, then `13`.
3. Ask for a name with `name = input("Name: ")`, then `print(bool(name))`. Run it once with your name, and once
   where you just hit Enter. Why does the second run print `False`?
