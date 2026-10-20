# Lesson 11: if, elif, else in Python

Part of **Python: Zero to Warrior**, a free Python course for beginners.
Video: https://youtu.be/2kTmwvJC3Fk · Full course: https://www.youtube.com/playlist?list=PLcsbg964FAwc

## What's in this lesson
- An `if` statement is the word `if`, a condition, and a colon. A condition is anything that comes out `True` or
  `False`, and most of the time it's a comparison, like `health < 30`.
- The lines indented under it (4 spaces; VS Code adds them when you hit Enter after the colon) are a block. The block
  runs only when the condition is `True`. The first line back at the left edge isn't part of the `if`, so it runs every
  time.
- `else:` (no condition) runs when the condition is `False`. Python always takes exactly one of the two paths.
- `elif` is short for "else if". Python checks the conditions from the top down, runs the block under the first one
  that's `True`, and skips the rest of the chain. You get one `if`, as many `elif`s as you need, and at most one
  `else`.
- The order matters. With `>=`, put the biggest number first. With `<`, go from the smallest number up.
- Common mistakes (real Python 3.15 messages):
  - No colon: `SyntaxError: expected ':'`
  - No indent: `IndentationError: expected an indented block after 'if' statement on line 2`
  - `=` instead of `==`: `SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?`
  - Checks in the wrong order: no error at all, just the wrong answer (`health = 90` prints `Hurt`).

## Files
- `potion.py`: the first program from the video (`if` and `else`).
- `solution.py`: the second program from the video (`status.py`, the `elif` chain).
- `starter.py`: the "your turn" exercise (a loot drop), with TODOs to fill in.

## Run it
```
python3 solution.py      # Mac
python solution.py       # Windows
```
Each program asks for the health. Type a number and hit Enter.

## Practice
1. Add a "Full health" level to `solution.py` for 100 or more. Where does it have to go, and what happens to the old
   `if`? (Type 100, then 75: you should get `Full health`, then `Strong`.)
2. Go back to your BMI calculator from lesson 09 and replace the chart with an `if`, two `elif`s and an `else`, so it
   prints just the category: less than 18.5 is Underweight, less than 25 is Healthy weight, less than 30 is
   Overweight, and anything else is Obesity. (70 kg and 1.75 m should print `Healthy weight`; 95 and 1.8 should print
   `Overweight`.)
3. Predict first, then run it: in `solution.py`, what prints when you type `30`? What about `29`? (Hint: `>=` means
   "greater than or equal to".)
