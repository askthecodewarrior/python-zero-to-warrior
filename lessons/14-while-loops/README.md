# Lesson 14: While Loops in Python, Explained Visually

Part of **Python: Zero to Warrior**, a free Python course for beginners.
Video: https://youtu.be/kW5tmN6v-Ko · Full course: https://www.youtube.com/playlist?list=PLcsbg964FAwc

## What's in this lesson
- A **loop** runs a block of code over and over. A `while` loop is the word `while`, a condition, a colon, and an
  indented block, just like an `if`. The difference: at the end of the block, a `while` loop goes back up to the top
  and checks the condition again.
- The **condition** is checked at the top, before every pass. The block runs as long as it's True; the first time
  it's False, Python skips the block and carries on with the line after it. If it's False to begin with, the block
  never runs at all.
- One pass through the block is an **iteration**. A variable that counts the passes is a **counter**.
- `floor += 1` is the short way to write `floor = floor + 1`. `-=` takes away: `count -= 1`.
- A loop that keeps asking until the input is right: start `password` as an empty string `""`, so the condition is
  True the first time, and ask again inside the loop with `input()`. Capital letters matter: `"Dragon"` isn't
  `"dragon"`.
- The classic mistake: nothing inside the loop changes the variable in the condition, so the condition is True
  forever. That's an **infinite loop**. Stop it by clicking in the terminal and pressing **Control+C** (Control, not
  Command, on a Mac; Control+C on Windows too). Python stops with `KeyboardInterrupt`.

## Files
- `solution.py`: the tower program from the video (tower.py).
- `gate.py`: the password program from the video.
- `starter.py`: the "your turn" exercise (a countdown), with TODOs to fill in.
- `countdown_solution.py`: one way to solve it.
- `practice_solutions.py`: one way to do practice problems 2 and 3.

## Run it
```
python3 solution.py      # Mac
python solution.py       # Windows
```

## Practice
1. Predict, then run: in `solution.py`, change `floor = 1` to `floor = 4`. What prints, and why does the block never
   run?
2. Add a counter to `gate.py`: start `tries = 0` before the loop, add 1 to it inside the loop, and after the loop
   print how many tries it took (an f-string from lesson 6 works well).
3. Make a loop that keeps asking for a door number until it's 1, 2 or 3:
   `door = int(input("Pick a door (1-3): "))`. Hint: start `door` at 0, and keep looping while
   `door < 1 or door > 3` (`or` from lesson 12).
