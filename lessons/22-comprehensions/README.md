# Lesson 22: List Comprehensions in Python

Part of **Python: Zero to Warrior**, a free Python course for beginners.
Video: https://youtu.be/T1M2RgJ6zrs · Full course: https://www.youtube.com/playlist?list=PLcsbg964FAwc

## What's in this lesson
- **The long way:** to build a new list from an old one, you start with an empty list, loop over the old one, and
  `append` each new value (lessons 15 and 18). That's three lines for one list:
  ```python
  doubled = []
  for p in points:
      doubled.append(p * 2)
  ```
- **A list comprehension** builds the same list in one line, inside square brackets:
  `doubled = [p * 2 for p in points]`. The part you were appending (`p * 2`) goes first, then the `for` part, without
  its colon. The pattern is `[expression for item in list]`, where the **expression** is the code that gives you each
  new value. You don't need `append`: the comprehension builds the list for you.
- **A filter:** put an `if` at the very end to keep only some of the items:
  `positive = [p for p in points if p > 0]`. With `points = [12, -5, 30, 0, 8]` that's `[12, 30, 8]`: the `0` is left
  out too, because `0 > 0` is `False`. Use `p >= 0` to keep the zeros. The pattern is
  `[expression for item in list if condition]`.
- **Strings work the same way:** `[hero.upper() for hero in party]` gives every name in capital letters, and
  `[len(hero) for hero in party]` gives how many letters each name has. You can print a comprehension right away
  without saving it in a variable first.
- **The classic mistake:** putting the `if` in front, `[p if p > 0 for p in points]`. Python stops with
  `SyntaxError: expected 'else' after 'if' expression`, because an `if` up front does something different (it picks
  between two values, so it needs an `else`). For a filter, the `if` goes last.
- **When not to use one:** if a comprehension gets so long that you have to read it twice, a regular `for` loop is
  perfectly fine, and easier to read.
- **One more, for later:** curly braces make a *dictionary* comprehension, like
  `{item: price * 2 for item, price in gold.items()}` (lesson 20's `.items()`). The video sticks to lists.

## Files
- `newlists.py`: the program from the video.
- `starter.py`: the "your turn" exercise, with TODOs.
- `solution.py`: one way to solve it.
- `squares.py` and `prices.py`: answers to practice problems 2 and 3 (try them yourself first).

## Run it
```
python3 newlists.py      # Mac
python newlists.py       # Windows
```
The same goes for every other file.

## Practice
1. Predict, then run: `nums = [3, 8, 1, 6]`, then `print([n + 1 for n in nums if n > 2])`. What prints?
   (`[4, 9, 7]`: the filter keeps 3, 8 and 6, then the expression adds 1 to each.)
2. Squares: use `range(1, 11)` (lesson 15) and `**` (lesson 04) to make the squares of 1 to 10 in one line, then a
   second comprehension that keeps only the even ones (`% 2 == 0`). You should get `[4, 16, 36, 64, 100]`.
3. Half price: `prices = [40, 15, 120, 8]`. Write a loop with an `if` and `append` that halves (`// 2`) every price of
   20 or more, then write the same thing as one comprehension. Both print `[20, 60]`.
