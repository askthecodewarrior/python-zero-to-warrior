# Lesson 33: JSON in Python for Beginners

Part of **Python: Zero to Warrior**, a free Python course for beginners.
Video: https://youtu.be/mRaBRO8A_24 · Full course: https://www.youtube.com/playlist?list=PLcsbg964FAwc

## What's in this lesson
- **What JSON is:** JSON (JavaScript Object Notation) is a text format for data. It looks almost like Python's
  dictionaries and lists, and just about every language can read and write it. A lot of web APIs send their data as
  JSON (lesson 28's `response.json()` turned it into a dictionary), a lot of settings files are JSON, and it's a common
  way for a program to save its data, like a game's save file.
- **Save with `json.dump()`:** it takes your data and an open file, and writes the data into the file as JSON.
  ```python
  # Save the game
  import json

  player = {
      "name": "Warrior",
      "level": 5,
      "inventory": ["sword", "map"],
  }

  with open("save.json", "w") as f:
      json.dump(player, f, indent=2)
  ```
  Without `indent=2`, the whole file is one line:
  `{"name": "Warrior", "level": 5, "inventory": ["sword", "map"]}`. With it, each item gets its own line, pushed in by
  two spaces, so a person can read it (and change it by hand).
- **Load with `json.load()`:** it reads the JSON in the file and gives you back a Python dictionary.
  ```python
  # Load the game and add a level
  import json

  with open("save.json") as f:
      player = json.load(f)

  player["level"] += 1
  print(player["name"], "is now level", player["level"])
  print("Inventory:", player["inventory"])

  with open("save.json", "w") as f:
      json.dump(player, f, indent=2)
  ```
  Each run adds one to the level and saves it back: `Warrior is now level 6`, then `Warrior is now level 7`. Unlike a
  CSV file (lesson 32), where every value comes back as a string, JSON gives you back real numbers and real lists, so
  `+= 1` works without `int()`.
- **JSON is stricter than Python:**

  | Python | JSON |
  |---|---|
  | `"text"` or `'text'` | `"text"` only (double quotes) |
  | `True`, `False`, `None` | `true`, `false`, `null` |
  | a comma after the last item is fine | no comma after the last item |
  | a tuple `(3, 4)` | an array `[3, 4]` (it comes back as a list) |

- **`json.dumps()` and `json.loads()`** do the same thing with a string instead of a file (the `s` means string):
  ```python
  import json

  text = json.dumps({"hp": 30, "alive": True, "pet": None})
  print(text)        # {"hp": 30, "alive": true, "pet": null}
  print(type(text))  # <class 'str'>

  data = json.loads(text)
  print(data)        # {'hp': 30, 'alive': True, 'pet': None}
  print(type(data))  # <class 'dict'>
  ```
- **The common mistake:** typing a JSON file by hand like a Python dictionary, with single quotes or a comma after the
  last pair. `json.load()` stops with a `json.JSONDecodeError`, and the last line of the traceback says what's wrong and
  where: `Expecting property name enclosed in double quotes: line 1 column 2 (char 1)`, or
  `Illegal trailing comma before end of object: line 4 column 32 (char 68)`. The lines in the middle of the traceback
  come from inside the json module. If a file might be broken, catch it with `try` / `except json.JSONDecodeError:`
  (lesson 27).

## Files
- `save.py`, `level_up.py`: the programs from the video. Run `save.py` first: it makes `save.json`.
- `strings.py`: `json.dumps()` and `json.loads()`, from the video's slide.
- `starter.py`: the "your turn" exercise, with TODOs.
- `solution.py`: one way to solve it.
- `tuple.py`, `settings.py`, `scores.py`: practice problems 1, 2 and 3 (`settings.py` and `scores.py` are one answer
  each: try them yourself first).

## Run it
```
python3 save.py         # Mac
python save.py          # Windows
```
The same goes for every other file.

## Practice
1. Predict, then run `tuple.py`:
   ```python
   import json

   spot = {"x": 3, "pos": (3, 4), "alive": False}
   text = json.dumps(spot)
   print(text)

   back = json.loads(text)
   print(back)
   print(type(back["pos"]))
   ```
   (`{"x": 3, "pos": [3, 4], "alive": false}`, then `{'x': 3, 'pos': [3, 4], 'alive': False}` and `<class 'list'>`:
   JSON has no tuples, so the tuple comes back as a list.)
2. Write `settings.py`: load `settings.json` if it's there (catch `FileNotFoundError` and start with
   `{"sound": True, "volume": 7}`), switch `"sound"` with `not`, print `Sound: on` or `Sound: off`, and save it back
   with `indent=2`. Run it twice: `Sound: off`, then `Sound: on`. Open `settings.json` and look for `true`.
3. Write `scores.py`: keep a list of scores in `scores.json`. Load the list (or start with `[]` if the file isn't
   there), ask for a score with `input()`, add it with `append()`, print the list and how many games you've played with
   `len()`, then save it. Typing 120, then 90 prints `Scores so far: [120]` and `Games played: 1`, then
   `Scores so far: [120, 90]` and `Games played: 2`.
