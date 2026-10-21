# Lesson 16: break, continue and Nested Loops in Python

Part of **Python: Zero to Warrior**, a free Python course for beginners.
Video: https://youtu.be/r-jLt0vIu-M · Full course: https://www.youtube.com/playlist?list=PLcsbg964FAwc

## What's in this lesson
- `break` stops a loop right away, and Python jumps to the first line after the loop. `gate2.py` is the password
  gate from lesson 14 written with `while True:`. The condition is always True, so the loop only ends when the
  password is `dragon` and `break` runs. "Wrong password" never prints on that pass, because `break` has already left
  the loop.
- `continue` skips the rest of one pass, and the loop goes on with the next one. In `rooms.py`, room 3 is a trap:
  `if room == 3: continue` skips its print, so you get rooms 1, 2, 4 and 5, then `Done searching`.
- The same loop with `break` instead of `continue` stops at room 3 and prints only rooms 1 and 2. Both work the same
  way in a `while` loop.
- VS Code tip: when you hit Enter after `break` or `continue`, the Python extension moves the cursor back out one
  level for you, because nothing after them in that block would ever run.
- A **nested loop** is a loop inside another loop. For every pass of the outer loop, the inner loop runs all the way
  through, like a clock's minute hand going all the way around before the hour hand moves one. `floors.py` prints
  `Floor 1 room 1`, `Floor 1 room 2`, then floor 2's rooms, then floor 3's: six lines, three floors times two rooms.
- The classic mistake: `break` only stops the loop it's in. A `break` in the inner loop stops that floor's rooms, and
  the outer loop just moves on to the next floor. To stop the outer loop, put the `if` and the `break` in the outer
  loop.
- **Boss level:** `grid.py` draws a 5 by 5 grid of dots with turtle. The outer loop goes up the rows, the inner loop
  goes across the columns:
  - `pen.penup()` lifts the pen, so the turtle moves without drawing a line;
  - `pen.goto(x, y)` moves the turtle to a spot: x is how far across, y is how far up, and (0, 0) is the middle of the
    window. `col * 100 - 200` gives -200, -100, 0, 100, 200, so the dots are 100 apart and centered;
  - `pen.dot(size)` draws a filled dot. `10 + row * 10 + col * 10` makes the dots bigger as they go up and to the
    right (10 at the bottom left, 90 at the top right).
  The dot line runs 25 times: 5 columns for each of the 5 rows. At turtle's default speed it takes about 6 seconds.
  Close the window to end the program.

## Files
- `gate2.py`: `while True` and `break` (it asks for a password; the right one is `dragon`).
- `rooms.py`: `continue` skips room 3.
- `floors.py`: the nested loop from the video.
- `grid.py`: the boss level.
- `starter.py`: the "your turn" exercise (4 rooms on every floor, skip room 3), with TODOs.
- `solution.py`: one way to solve it.
- `times.py` and `checker.py`: answers to practice problems 2 and 3 (try them yourself first).

## Run it
```
python3 floors.py      # Mac
python floors.py       # Windows
```
The same goes for every other file.

## Practice
1. Predict, then run: in `rooms.py`, change `continue` to `break`. Which rooms get searched now, and does
   `Done searching` still print?
2. A times table: write nested loops where `row` and `col` both go from 1 to 3, and print
   `row, "x", col, "=", row * col`. You should get 9 lines, from `1 x 1 = 1` to `3 x 3 = 9`.
3. Boss level, part 2: in `grid.py`, make a checkerboard. Inside the inner loop, before `goto`, skip the dot with
   `continue` when `(row + col) % 2 == 1` (remember `%` from lesson 4: it's the remainder). How many dots are left?
   (13: run `checker.py` to check.)
