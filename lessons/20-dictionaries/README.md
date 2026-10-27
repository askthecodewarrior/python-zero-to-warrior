# Lesson 20: Dictionaries in Python, Explained Visually

Part of **Python: Zero to Warrior**, a free Python course for beginners.
Video: https://youtu.be/zTur9wm55Wg · Full course: https://www.youtube.com/playlist?list=PLcsbg964FAwc

## What's in this lesson
- A **dictionary** stores each value under a name called a **key**. You write it with curly braces, and inside go
  **pairs**: a key, a colon, then its value, with a comma between pairs:
  `player = {"name": "Warrior", "level": 7, "gold": 50}`. Think of a row of lockers: the key is the label on the
  door, the value is what's inside.
- **Get a value by its key** in square brackets: `player["gold"]` is `50`. A list uses a number (an index); a
  dictionary uses the key.
- **Change and add** with the same kind of line. `player["gold"] = 80` changes gold, because `"gold"` is already a key.
  `player["armor"] = "iron"` adds a new pair, because `"armor"` isn't a key yet. So `len(player)` is 4, not 5:
  `len()` counts the pairs.
- **Order:** since Python 3.7, a dictionary keeps the order you put things in, so a new key goes at the end.
- **Each key only once.** A value can be any type (a string, a number, even a list). `{}` on its own is an empty
  dictionary (lesson 19).
- **The classic mistake:** asking for a key that isn't there. `player["map"]` stops with `KeyError: 'map'`. Keys care
  about capital letters, so `player["Gold"]` is a KeyError too.
- **The fix:** `player.get("map")` gives `None` (Python's way of saying there's no value) instead of an error, and
  `player.get("map", 0)` gives `0`. The **default** (the 0) is what you get when that key is missing;
  `player.get("gold", 0)` still gives the real gold.
- **`in` checks the keys:** `"armor" in player` is True. `"iron" in player` is False, even though `"iron"` is a value.
  (To look for a value, use `"iron" in player.values()`.)
- **Remove a pair:** `del player["armor"]` deletes the key and its value. `gold = player.pop("gold")` takes it out too,
  and hands you the value. A dictionary's `pop` needs the key (a list's `pop()` didn't).
- **Loop over it:** `for key, value in player.items():` gives you each key and its value, one pair at a time.
  `player.keys()` (or just `player`) gives you the keys, and `player.values()` gives you the values.

## Files
- `player.py`: the program from the video.
- `starter.py`: the "your turn" exercise, with TODOs.
- `solution.py`: one way to solve it.
- `safe_lookup.py` and `count_loot.py`: answers to practice problems 2 and 3 (try them yourself first).

## Run it
```
python3 player.py      # Mac
python player.py       # Windows
```
The same goes for every other file.

## Practice
1. Predict, then run: `scores = {"Ann": 90, "Bo": 75}`, then `scores["Bo"] = 80` and `scores["Cy"] = 70`. What does
   `print(len(scores))` show? (3: Bo was already a key, so only Cy is new.)
2. Look up a key safely: ask the user for a key with `input()`, and print its value from `player` with `.get()` and a
   default of `"not found"`, so a key that isn't there never crashes the program.
3. Count things with a dictionary: start with `drops = ["gold", "gem", "gold", "gold", "key"]` and an empty
   dictionary `counts = {}`. Loop over the list, and for each drop, set `counts[drop]` to `counts.get(drop, 0) + 1`.
   Print `counts`. (You should get `{'gold': 3, 'gem': 1, 'key': 1}`.)
