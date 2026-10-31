# Lesson 47: Type Hints in Python

Part of **Python: Zero to Warrior**, a free Python course for beginners.
Video: https://youtu.be/WVT75jHRM40 · Full course: https://www.youtube.com/playlist?list=PLcsbg964FAwc

## What's in this lesson
- **A type hint is a label that says what type a value is supposed to be.** In lesson 41 you wrote `points: int` in a
  dataclass. This lesson is about where hints go and what they're for.
  ```python
  level: int = 3                                    # on a variable: a colon and the type
  def add_bonus(damage: int, bonus: int) -> int:    # on each parameter, and -> for the return value
  ```
- **Python doesn't check hints when it runs.** It keeps them, but it runs the code either way:
  ```python
  print(add_bonus(10, 5))      # 15
  print(add_bonus("10", "5"))  # 105: + joins the two strings, and nothing stops it
  ```
  The hints are for you, for your editor, and for **type checkers** (tools that read your code and tell you where the
  types don't match).
- **Turn on type checking in VS Code.** Out of the box, the Python extension doesn't check types at all, so nothing is
  underlined. Open Settings (Command comma on a Mac, Control comma on Windows), search for `type checking`, and set
  **Python › Analysis: Type Checking Mode** to `basic`. Now VS Code underlines a mismatch in red before you run anything.
  Put the mouse on the squiggle to read the message, which comes from **Pylance** (the part of the Python extension that
  checks your code). If Pylance ever pops up a message recommending type checking, its Yes button opens this same setting.
  Shown with VS Code 1.143 and Pylance 2026.4.
- **Say what's inside, with square brackets:**
  ```python
  hits: list[int] = [12, 7, 30]                       # a list of ints
  bag: dict[str, int] = {"potion": 3, "arrow": 20}    # str keys, int values
  spot: tuple[int, int] = (4, 9)                      # exactly two ints
  ```
- **A value that might not be there:** `int | None` means an int, or `None` (Python 3.10 and newer; older code writes
  `Optional[int]`, from the `typing` module, which means the same thing).
  ```python
  def count(bag: dict[str, int], item: str) -> int | None:
      return bag.get(item)

  print(count(bag, "arrow"), count(bag, "rope"))  # 20 None
  ```
- **The common mistake:** a return hint that forgets `None`. With `-> int`, VS Code underlines `bag.get(item)`:
  `Type "int | None" is not assignable to return type "int"`, because `get` gives back `None` when the key isn't there
  (lesson 20). The fix is `-> int | None`.
- **Checking a whole project:** command-line type checkers like `mypy` check every file at once. Lesson 48 shows how to
  install tools like that properly. On this lesson's `hints.py` it finds the same two problems:
  `hints.py:7: error: Argument 1 to "add_bonus" has incompatible type "str"; expected "int"  [arg-type]` (and the same
  for argument 2).

## Files
- `hints.py`: the program from the video. Line 7 is the deliberate mistake, left in so you can see the squiggle.
- `starter.py`: the "your turn" exercise, with TODOs.
- `solution.py`: one way to solve it.
- `heal.py`, `party.py`, `find.py`: practice problems 1, 2 and 3 (one answer each: try them yourself first).

Run any of them with `python3 hints.py` on a Mac, or `python hints.py` on Windows.

## Practice problems
1. **Heal a player.** Write `heal(health, potion, cap)` that adds the potion to the health but never goes past the cap
   (`min()` helps), and give every parameter and the return value a hint. `heal(70, 20, 100)` gives `90`, and
   `heal(95, 20, 100)` gives `100`. Answer: `heal.py`.
2. **A party and its gold.** Make `party`, a list of names, and `gold`, a dictionary from each name to their gold, both
   with hints (`list[str]` and `dict[str, int]`). Then write `total_gold(names, purse)` with hints that adds up the gold
   for those names. With Rook 40, Ivy 25 and Max 10, it gives `75`. Answer: `party.py`.
3. **Maybe not in the party.** Write `find_spot(party, name)` that returns where the name is in the list, or `None` when
   it isn't there, and give it the hint `-> int | None`. `find_spot(party, "Ivy")` gives `1`, and
   `find_spot(party, "Zed")` gives `None`. Then change the hint to `-> int` and read what VS Code says. Answer: `find.py`.

Every output above is a real run on Python 3.15.0.
