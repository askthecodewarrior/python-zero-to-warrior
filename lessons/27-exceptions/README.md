# Lesson 27: Exception Handling in Python: try, except, finally

Part of **Python: Zero to Warrior**, a free Python course for beginners.
Video: https://youtu.be/tYip_eEqDJc · Full course: https://www.youtube.com/playlist?list=PLcsbg964FAwc

## What's in this lesson
- **A traceback** is Python's report of an **exception**, an error that happens while the program is running. Read it
  from the bottom up:
  ```
  Level: ten
  Traceback (most recent call last):
    File "/Users/warrior/Desktop/python-course/level.py", line 2, in <module>
      level = int(input("Level: "))
  ValueError: invalid literal for int() with base 10: 'ten'
  ```
  1. The last line: the error type (`ValueError`), then the message (`invalid literal for int() with base 10: 'ten'`).
  2. Above it: the line of code that failed, copied from your file.
  3. Above that: the file and the line number. `in <module>` means the main part of the file, not inside a function.
  4. The top line, `most recent call last`, means the newest step is at the bottom.
- **try / except:** put the line that can fail in a `try` block. If it raises the error named after `except`, Python
  skips the rest of the `try` block and runs the `except` block instead of crashing.
  ```python
  try:
      level = int(input("Level: "))
      print("The level after that is", level + 1)
  except ValueError:
      print("That's not a whole number.")
  print("The game keeps going.")
  ```
  Always name the error. An `except` with no name catches every error, even a typo in your own code, so it hides bugs.
- **More than one except:** Python checks them from the top down and runs the first one that matches.
- **else** runs only when nothing in the `try` block failed. **finally** always runs, whether something failed or not.
  ```python
  try:
      gold = int(input("Gold: "))
      players = int(input("Players: "))
      share = gold // players
  except ValueError:
      print("Please type whole numbers.")
  except ZeroDivisionError:
      print("You need at least one player.")
  else:
      print("Each player gets", share)
  finally:
      print("Done sharing.")
  ```
  100 and 4 prints `Each player gets 25`, then `Done sharing.`; `ten` prints `Please type whole numbers.`, then
  `Done sharing.`; 100 and 0 prints `You need at least one player.`, then `Done sharing.`
- **raise** makes your own error when a value is wrong for your program, with your own message:
  ```python
  def check_age(age):
      if age < 0:
          raise ValueError("age can't be negative")
      return age


  check_age(-5)
  ```
  The traceback's last line is `ValueError: age can't be negative`. It has two `File` lines, because the error happened
  inside a function: the bottom one (line 3, in `check_age`) is where it was raised, and the one above it (line 7) is
  the call that got there.
- **except ValueError as e** gives the error a name, `e`; `print(e)` prints its message. Together with a loop
  (`while True` and `break`, lessons 14 and 16), it keeps asking until the input is valid:
  ```python
  while True:
      try:
          age = int(input("Age: "))
          if age < 0:
              raise ValueError("age can't be negative")
          break
      except ValueError as e:
          print("Try again:", e)

  print("Your age is", age)
  ```
- **The common mistake:** catching the wrong error. `except TypeError:` around `int(input(...))` doesn't catch the
  `ValueError`, so the program still crashes. Read the traceback's last line and put that exact name after `except`.

## Files
- `level.py`, `safe_level.py`, `share.py` and `ask_age.py`: the programs from the video. `age.py` is the raise slide's
  program (it ends with a traceback on purpose).
- `starter.py`: the "your turn" exercise, with TODOs.
- `solution.py`: one way to solve it.
- `predict.py`, `lives.py` and `check_level.py`: answers to practice problems 1, 2 and 3 (try them yourself first).

## Run it
```
python3 safe_level.py      # Mac
python safe_level.py       # Windows
```
The same goes for every other file.

## Practice
1. Predict, then run:
   ```python
   try:
       print(int("12") + 1)
   except ValueError:
       print("Not a number")
   else:
       print("No errors")
   finally:
       print("Done")
   ```
   (`13`, `No errors`, then `Done`.) Now change `"12"` to `"twelve"` and predict again (`Not a number`, then `Done`:
   the `else` is skipped, the `finally` isn't).
2. Fix it: this still crashes with a `ZeroDivisionError` when you type 0. Make it print `You need at least one life.`
   ```python
   try:
       lives = int(input("Lives: "))
       print("Damage per life:", 100 // lives)
   except ValueError:
       print("Please type a whole number.")
   ```
3. Write a function `check_level(level)` that raises a `ValueError` with the message `level must be 1 to 10` when
   the level is under 1 or over 10, and returns the level otherwise. Call it with 4 and then 12 inside a `try`, and
   print the message with `except ValueError as e`. You should see `4`, then `Error: level must be 1 to 10`.
