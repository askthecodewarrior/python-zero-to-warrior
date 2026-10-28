# Lesson 31: Reading and Writing Files in Python

Part of **Python: Zero to Warrior**, a free Python course for beginners.
Video: https://youtu.be/zoHHC3qkeyk · Full course: https://www.youtube.com/playlist?list=PLcsbg964FAwc

## What's in this lesson
- **Why files:** everything a program keeps in variables is gone when it ends. A file stays on your disk, so the next
  run (or another program) can read it back.
- **`open()` takes a file name and a mode.** `with ... as f:` gives the open file a name, `f`, and when the indented
  block ends, Python closes the file for you, even if there's an error. That's why `with` is the normal way to open a
  file (without it, you'd have to call `f.close()` yourself).
  ```python
  # Save the high scores
  with open("scores.txt", "w") as f:
      f.write("Warrior 120\n")
      f.write("Ana 95\n")
      f.write("Bo 80\n")
  ```
  - `"w"` (write) creates the file if it isn't there, and **wipes it first** if it is.
  - `"r"` (read) is the default, so `open("scores.txt")` reads too.
  - `"a"` (append) keeps what's in the file and writes after it.
- **`write()` doesn't add a new line** the way `print()` does, so put `\n` at the end of each string yourself.
  Without it, every score lands on one line.
- **Where the file goes:** a file name on its own, like `"scores.txt"`, is a *relative path*: it's relative to the
  folder you run the program from. In VS Code's terminal, that's the folder you opened.
- **Reading it back:**
  ```python
  # Read the high scores
  with open("scores.txt", "r") as f:
      print(f.read())
  ```
  `f.read()` gives you the whole file as one string (print adds one more new line after the file's last `\n`, so you
  see an empty line at the end). Most of the time you go line by line:
  ```python
  # Read the high scores
  with open("scores.txt", "r") as f:
      for line in f:
          print(line.strip())
  ```
  Each `line` still ends with `\n`, and `strip()` takes it off. `f.readlines()` gives you all the lines in a list.
- **When the file isn't there,** `open()` for reading stops with
  `FileNotFoundError: [Errno 2] No such file or directory: 'scores.txt'`. Catch it with `try` / `except` (lesson 27):
  ```python
  # Read the high scores
  try:
      with open("scores.txt", "r") as f:
          for line in f:
              print(line.strip())
  except FileNotFoundError:
      print("No scores yet.")
  ```
- **The common mistake:** opening with `"w"` when you meant to add. `"w"` wipes the file as soon as it's opened, so the
  old scores are gone. Use `"a"`:
  ```python
  # Add a new score
  with open("scores.txt", "a") as f:
      f.write("Kai 150\n")
  ```
- **pathlib** (comes with Python) does the same jobs in one line each:
  ```python
  from pathlib import Path

  best = Path("best.txt")
  print(best.exists())          # False the first time
  best.write_text("Kai 150\n")  # opens, writes, closes (and wipes first, like "w")
  print(best.exists())          # True
  print(best.read_text())       # the whole file, like f.read()
  ```
- **Encoding:** Python 3.15 uses UTF-8 by default for `open()` on every system (PEP 686), so a name like Zoë reads back
  the same on Windows, a Mac or Linux. On older versions the default depended on your system (on Windows it usually
  wasn't UTF-8), so a lot of code writes `encoding="utf-8"`, and that's still fine to write:
  `open("scores.txt", "a", encoding="utf-8")`.

## Files
- `save.py`, `read.py`, `add.py`: the programs from the video. Run `save.py` first: it makes `scores.txt`.
- `starter.py`: the "your turn" exercise, with TODOs.
- `solution.py`: one way to solve it.
- `log.py`, `games.py`, `best.py`: practice problems 1, 2 and 3 (`best.py` is one answer to problem 3: try it
  yourself first).

## Run it
```
python3 save.py         # Mac
python save.py          # Windows
```
The same goes for every other file.

## Practice
1. Predict, then run `log.py`:
   ```python
   with open("log.txt", "w") as f:
       f.write("Level 1 cleared")
       f.write("Level 2 cleared")

   with open("log.txt") as f:
       print(f.read())
   ```
   (`Level 1 clearedLevel 2 cleared`, all on one line.) Fix it so each level is on its own line.
2. Write `games.py`: each time it runs, it adds `Game played` (and a `\n`) to `games.txt` with `"a"`, then reads the
   file back with `readlines()` and prints how many games you've played. Run it twice: `Games played: 1`, then
   `Games played: 2`. What would happen with `"w"`?
3. Write `best.py` with pathlib: ask for a score with `input()`, read the best score from `best.txt` if it
   `exists()` (`int()` of `read_text()`), and if the new score is higher, `write_text()` it and print
   `New best score!`. Typing 120, then 90, then 150 prints `New best score!`, `The best is still 120`,
   `New best score!`.
