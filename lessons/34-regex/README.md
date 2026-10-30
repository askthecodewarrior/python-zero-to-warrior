# Lesson 34: Regular Expressions in Python (Regex Basics)

Part of **Python: Zero to Warrior**, a free Python course for beginners.
Video: https://youtu.be/deg54IFu_iY · Full course: https://www.youtube.com/playlist?list=PLcsbg964FAwc

## What's in this lesson
- **What a regular expression is:** a pattern that describes what the text looks like, instead of the exact text.
  The `in` operator (lesson 30) only finds text you already know, like `"555-1234" in text`. The pattern
  `\d+-\d+` (some digits, a dash, and some more digits) finds any phone number written that way.
- **The `re` module** comes with Python: `import re`.
- **Raw strings:** put an `r` in front of every pattern, `r"\d+-\d+"`. A backslash in a normal string is special to
  Python (`\n` is a new line, lesson 31), and the `r` tells Python to leave every backslash alone, so `re` gets `\d`
  exactly the way you typed it.
- **`re.search()`, `.group()`, `re.findall()` and `re.sub()`:**
  ```python
  # Find phone numbers in a message
  import re

  text = "Call 555-1234 or 555-9876 after 6 PM"
  match = re.search(r"\d+-\d+", text)
  print(match)
  print(match.group())

  numbers = re.findall(r"\d+-\d+", text)
  print(numbers)

  safe = re.sub(r"\d+-\d+", "XXX-XXXX", text)
  print(safe)
  ```
  prints
  ```
  <re.Match object; span=(5, 13), match='555-1234'>
  555-1234
  ['555-1234', '555-9876']
  Call XXX-XXXX or XXX-XXXX after 6 PM
  ```
  - `re.search(pattern, text)` finds the FIRST match anywhere in the text and gives back a match object (or `None`).
    `span=(5, 13)` is where the match starts and stops, the same numbers you'd use in a slice: `text[5:13]`.
  - `match.group()` gives you just the text that matched.
  - `re.findall(pattern, text)` gives you a list of every match. The `6` isn't in it: it has no dash after it.
  - `re.sub(pattern, new, text)` replaces every match and gives you back a new string (`text` doesn't change).
- **The pieces you'll use most:**

  | piece | matches |
  |---|---|
  | `\d` | a digit, 0 to 9 (in Python 3, digits from other alphabets match too) |
  | `\w` | a word character: a letter, a digit or `_` |
  | `\s` | a space, a tab or a new line |
  | `.` | any character but a new line |
  | `[aeiou]` | any one of the characters inside |
  | `+` | one or more of the piece before it |
  | `*` | zero or more of the piece before it |
  | `?` | zero or one: the piece before it is optional |
  | `^` | the start of the text |
  | `$` | the end of the text |

  `pieces.py` and `more_pieces.py` (from the video's slides) try them on `"Hit 3 orcs for 25 gold"`: `\d` finds
  `['3', '2', '5']` one digit at a time, `\d+` finds `['3', '25']`, `orcs?` finds `orc` and `orcs`, and `^\d+$`
  matches `"2026"` but not `"20x6"`.
- **Groups:** parentheses in a pattern make a group, numbered from 1, left to right.
  ```python
  # Pull the month, day and year out of a date
  import re

  note = "Boss fight on 10/31/2026 at 8 PM"
  match = re.search(r"(\d+)/(\d+)/(\d+)", note)
  if match:
      print("Month:", match.group(1))
      print("Day:", match.group(2))
      print("Year:", match.group(3))
  ```
  A group gives you back a string, so use `int()` to do math with it (lesson 05).
- **The common mistake:** `re.match()` only checks the very START of the text. `re.match(r"\d+-\d+", text)` gives
  back `None`, because the text starts with `Call`, and then `match.group()` stops the program with
  `AttributeError: 'NoneType' object has no attribute 'group'`. Use `re.search()` when the pattern could be anywhere,
  and check `if match:` before you call `.group()`, because `search()` gives back `None` too when nothing matches.
- **Leaving off the `r`:** Python 3.15 still runs the program, but it warns:
  `SyntaxWarning: "\d" is an invalid escape sequence. Such sequences will not work in the future. Did you mean "\\d"? A raw string is also an option.`

## Files
- `phones.py`, `dates.py`: the programs from the video.
- `pieces.py`, `more_pieces.py`: the pieces, from the video's slides.
- `starter.py`: the "your turn" exercise, with TODOs.
- `solution.py`: one way to solve it.
- `loot.py`, `tag.py`, `times.py`: practice problems 1, 2 and 3 (`tag.py` and `times.py` are one answer each: try
  them yourself first).

## Run it
```
python3 phones.py       # Mac
python phones.py        # Windows
```
The same goes for every other file.

## Practice
1. Predict, then run `loot.py`:
   ```python
   import re

   loot = "Level 7, 250 gold, 3 keys"
   print(re.findall(r"\d", loot))
   print(re.findall(r"\d+", loot))
   print(re.sub(r"\d+", "#", loot))
   ```
   (`['7', '2', '5', '0', '3']`, then `['7', '250', '3']`, then `Level #, # gold, # keys`.)
2. Write `tag.py`: ask for a player tag with `input()`, and use `re.search()` with `^\w+$` to print `Good tag` when it's
   only letters, digits and underscores, or `Letters, digits and _ only` when it isn't. `Warrior_7` is a good tag;
   `War rior!` isn't. Try it without the `^` and `$`: `War rior!` passes, because `\w+` finds `War` inside it.
3. Write `times.py`: pull the hour and the minutes out of `"Raid starts at 7:45 PM"` with two groups, print
   `Hour: 7` and `Minutes: 45`, then add 15 to the minutes with `int()` and print `Minutes + 15: 60`.
