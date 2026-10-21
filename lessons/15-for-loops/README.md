# Lesson 15: For Loops and range() in Python

Part of **Python: Zero to Warrior**, a free Python course for beginners.
Video: https://youtu.be/deqEZZd9DTU · Full course: https://www.youtube.com/playlist?list=PLcsbg964FAwc

## What's in this lesson
- A `for` loop goes through something one item at a time. `for letter in "GOLD":` runs its indented block four
  times, and `letter` (the loop variable) is `'G'`, then `'O'`, then `'L'`, then `'D'`.
- `range()` gives you numbers, one at a time. The stop number is never included:
  - `range(5)` gives 0, 1, 2, 3, 4 (it starts at 0, like a string's index);
  - `range(1, 6)` gives 1, 2, 3, 4, 5 (start, stop: the same rule as slicing);
  - `range(0, 10, 2)` gives 0, 2, 4, 6, 8, and `range(5, 0, -1)` gives 5, 4, 3, 2, 1 (the step is how much it counts by).
- An accumulator adds things up: start it at 0 **above** the loop, add to it inside (`gold += level`), and print it
  after. `range(1, 5)` stops before 5, so `gold.py` prints `Gold: 10`, not 15.
- for or while? Use `for` when you know how many times, or when you have something to go through (like a string).
  Use `while` when you don't know how many times (keep asking until the password is right).
- The classic mistake: `for i in 5:` stops with `TypeError: 'int' object is not iterable`. An iterable is something
  you can loop over, like a string or a range. The fix: `for i in range(5):`.
- **Boss level:** `circles.py` draws 36 circles with one loop. turtle is a drawing module that comes with Python;
  `pen.circle(100)` draws a circle with a radius of 100 and `pen.left(10)` turns 10 degrees, and 36 turns of 10 degrees
  make one full turn. At turtle's default speed the drawing takes a little over a minute. Close the window to end
  the program.

## Files
- `loops.py`: the first program from the video (a string, then `range(3)`).
- `gold.py`: the accumulator from the video.
- `circles.py`: the boss level.
- `starter.py`: the "your turn" exercise (add up 1 to 100), with TODOs to fill in.
- `solution.py`: one way to solve it.

## Run it
```
python3 loops.py      # Mac
python loops.py       # Windows
```
The same goes for `gold.py`, `circles.py` and `solution.py`.

## Practice
1. Predict, then run: what does `for n in range(10, 0, -3): print(n)` print? Then change the stop to -5. What
   changes, and why?
2. Count the capital letters in a word: start `count = 0`, loop over `"DraGOn"`, and add 1 to `count` when
   `letter.isupper()` is True. It should print 3.
3. Boss level, part 2: in `circles.py`, change the loop to `range(72)` and the turn to `pen.left(5)`. How many degrees
   is that in total? Then try `range(12)` with `pen.left(30)`. (Add `pen.speed(0)` before the loop if you don't want
   to wait: speed 0 is the fastest.)
