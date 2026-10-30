# Lesson 32: Working with CSV Files in Python

Part of **Python: Zero to Warrior**, a free Python course for beginners.
Video: https://youtu.be/BN2kWNKueeo · Full course: https://www.youtube.com/playlist?list=PLcsbg964FAwc

## What's in this lesson
- **A CSV file** (comma separated values) is plain text: one row on each line, a comma between the values, and usually
  a header row on top that names the columns. Excel and Google Sheets open it too, with each value in its own cell.
  `players.csv`:
  ```
  name,level,score
  Warrior,5,120
  Ana,3,95
  "Bo, Jr.",2,80
  Kai,6,150
  ```
  Bo's name has a comma in it, so the whole name is in double quotes: that comma is part of the name, not a
  separator.
- **Why not just `split(",")`?** `split.py` reads each line, strips the `\n` off and splits it at every comma. It works
  until a value has a comma in it: Bo's row comes out as four values, with the quotes still in them:
  `['"Bo', ' Jr."', '2', '80']`.
- **The csv module** comes with Python. `csv.reader` gives you one row at a time, as a list of strings, and it knows
  the rules for quotes and commas (`read.py`):
  ```python
  import csv

  with open("players.csv", newline="") as f:
      reader = csv.reader(f)
      header = next(reader)
      print("Columns:", header)
      for row in reader:
          print(row)
  ```
  `next(reader)` takes the first row, the header, so the loop starts on the first player. Bo's row is now
  `['Bo, Jr.', '2', '80']`.
- **`newline=""`:** the csv docs say to open a CSV file with `newline=""`, for reading and for writing, because the csv
  module does its own line-ending handling. When you write without it, Windows adds an extra `\r` to every row, and
  you get a blank line between rows.
- **`csv.DictReader`** gives you each row as a dictionary, keyed by the header, so you write `row["score"]` instead of
  remembering it's the third column (`total.py`).
- **Every value comes back as a string**, numbers too: `'120'`, not `120`. Adding it to a number stops with
  `TypeError: unsupported operand type(s) for +: 'int' and 'str'`. Convert first, with `int()` (or `float()` for
  decimals), just like `input()` in lesson 5:
  ```python
  total = total + int(row["score"])
  ```
- **Writing:** `csv.writer` with `writerow()` (one row) and `writerows()` (a list of rows), and `open(..., "w",
  newline="")` (`write.py`). The writer turns numbers into text and puts quotes around a value that has a comma in it,
  on its own. It ends every row with `\r\n`, which is why VS Code says CRLF for `results.csv`.
- **`csv.DictWriter`** writes dictionaries: give it the column names with `fieldnames`, `writeheader()` writes the
  header row, and `writerow()` takes one dictionary (`write_dict.py`; it writes `results.csv` too, so it replaces what
  `write.py` wrote).

## Run the files
Put `players.csv` in the same folder, then on a Mac: `python3 split.py`, `python3 read.py`, `python3 total.py`,
`python3 write.py`. On Windows, type `python` instead of `python3`.

## Your turn (from the video)
Add a row to the end of `players.csv` with your own name, a level and a score (no spaces after the commas), then run
`total.py` again. Your score is in the total.

## Practice
1. **The average score.** Finish `starter.py`: add each score to `total` (with `int()`), count the rows, and print
   `Average:` and `total / count`. With the video's four players it prints `Average: 111.25`. (`solution.py` is one
   way to do it.)
2. **Who's level 4 or higher?** Write `levels.py`: read `players.csv` with `csv.DictReader` and print only the players
   whose level is 4 or more, like `Warrior is level 5` and `Kai is level 6`. (Remember: `row["level"]` is a string.)
3. **Save the top players.** Write `top.py`: read `players.csv`, keep the name and score of every player who scored
   100 or more, and write them to `top.csv` with `csv.writer`, a header row of `name,score`, and `newline=""`. Open
   `top.csv`: it has `name,score`, `Warrior,120` and `Kai,150`.
