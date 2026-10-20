# Lesson 08: String Methods in Python (isdigit, isupper, split, join)

Part of **Python: Zero to Warrior**, a free Python course for beginners.
Video: https://youtu.be/ghfy07d_L3o · Full course: https://www.youtube.com/playlist?list=PLcsbg964FAwc

## What's in this lesson
- A **method** is a function that belongs to a value. You call it with a dot, its name and a pair of parentheses:
  `player.upper()`. The parentheses are what run it.
- `upper()` and `lower()` give you the text in all capitals or all lowercase.
- `replace(old, new)` swaps one part of a string for another: `"Warrior".replace("rior", "lock")` is `"Warlock"`.
- `isupper()` asks "are all the letters capitals?" and `isdigit()` asks "is every character a digit, 0 to 9?".
  Both give back a **bool**, `True` or `False`.
  - `isupper()` only looks at letters: `"LEVEL 7".isupper()` is `True`. It needs at least one capital, though, so a
    string with no letters, like `"42"`, gives `False`.
  - `isdigit()` needs every character to be a digit: `"42 gold"`, `"7.5"` and `"-7"` are all `False`, and so is an
    empty string `""` (what you get if someone just hits Enter).
- `strip()` takes the spaces off the start and the end of a string. `int()` copes with those spaces, but `isdigit()`
  doesn't, so strip what someone typed before you check it.
- `split(",")` cuts a string at every comma and gives you a **list** of the pieces, in order:
  `['sword', 'shield', 'potion']`. With empty parentheses, `split()` cuts at the spaces.
- `"-".join(items)` glues a list back into one string, with the glue between the pieces: `sword-shield-potion`.

## Common mistakes
- Calling a method without saving the result: `name.upper()` on its own line changes nothing, because strings are
  **immutable** (they can't be changed). Save the new string: `name = name.upper()`.
- Forgetting the parentheses: `print(name.upper)` prints something like
  `<built-in method upper of str object at 0x1010db480>` (the number is different every run) instead of `WARRIOR`.

## Files
- `solution.py`: `methods.py` from the video.
- `check.py`: the second program from the video (type a level with a couple of spaces in front of it).
- `starter.py`: the two "your turn" exercises, with TODOs to fill in.

## Run it
```
python3 solution.py      # Mac
python solution.py       # Windows
```

## Practice
1. Ask for a chat message with `input()`, then print it in lowercase and print whether it was all capitals with
   `isupper()`. Run it twice: type `GG EZ`, then `gg ez`. (The first says `True`, the second `False`.)
2. Make `date = "2026-10-18"`. Split it on the dashes and print the list, then join it back with `"/"` so it prints
   `2026/10/18`.
3. Predict first, then run: `print("7".isdigit())`, `print("-7".isdigit())` and `print("007".isdigit())`. Which one
   says `False`, and why?
