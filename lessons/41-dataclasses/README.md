# Lesson 41: Dataclasses in Python

Part of **Python: Zero to Warrior**, a free Python course for beginners (the intermediate part).
Video: https://youtu.be/yotgiR69tAE · Full course: https://www.youtube.com/playlist?list=PLcsbg964FAwc

## What's in this lesson
- **A dataclass is a class that's mostly there to hold data**, like a high score: some points and a name. In lesson 40
  you wrote dunder methods like `__repr__` and `__eq__` by hand. With `@dataclass`, Python writes `__init__`, `__repr__`
  and `__eq__` for you, from the fields you list.
- **The import and the decorator:**
  ```python
  from dataclasses import dataclass


  @dataclass
  class Score:
      points: int
      name: str
  ```
  - `dataclasses` is a module that comes with Python, so there's nothing to install.
  - A line that starts with `@` is a **decorator** (like `@property` in lesson 39). `@dataclass` takes the class under it
    and writes those methods into it. Decorators get their own lesson later in the course.
  - `points: int` is a **field**: the name of a value and its type. The `: int` part is a **type hint**. It tells you and
    your editor what kind of value goes there, but Python doesn't check it when the program runs:
    `Score("lots", "Nova")` runs and stores the text. Type hints get their own lesson later in the course.
- **What @dataclass writes for you:**
  ```python
  nova = Score(120, "Nova")          # __init__: the fields in the order you listed them
  print(nova)                        # __repr__: Score(points=120, name='Nova')
  print(nova == Score(120, "Nova"))  # __eq__: True (a plain class says False here)
  ```
- **Sorting with order=True:** `@dataclass(order=True)` also writes the methods for `<`, `>`, `<=` and `>=`, so
  `sorted()` works. It compares the fields from the top down: points first, and the names only when two scores are tied.
  Without it, `sorted()` stops with `TypeError: '<' not supported between instances of 'Score' and 'Score'`.
  ```python
  for score in sorted([nova, rex, ivy]):
      print(score.points, score.name)    # 95 Rex, 120 Nova, 150 Ivy
  ```
- **Default values:** `name: str = "Guest"` lets you leave the name out: `Score(50)` is `Score(points=50, name='Guest')`.
- **frozen=True:** `@dataclass(frozen=True)` makes an object that can't be changed after it's made. Setting
  `nova.points = 200` stops with `dataclasses.FrozenInstanceError: cannot assign to field 'points'`.
- **The common mistakes:**
  - A default before a field without one (`points: int = 0`, then `name: str`) stops with
    `TypeError: non-default argument 'name' follows default argument 'points'`. It's the same rule as defaults in a
    function (lesson 25): move the fields with defaults to the bottom.
  - A list as a default (`badges: list = []`) stops with
    `ValueError: mutable default <class 'list'> for field badges is not allowed: use default_factory`. **Mutable** means
    it can be changed, and every Score would share that one list. The fix is
    `badges: list = field(default_factory=list)`, with `from dataclasses import dataclass, field`: dataclass calls `list`
    and makes a new empty list for every Score.

## Files
- `scores.py`: the program from the video.
- `starter.py`: the "your turn" exercise, with TODOs.
- `solution.py`: one way to solve it.
- `cards.py`, `books.py`, `point.py`: practice problems 1, 2 and 3 (`books.py` and `point.py` are one answer each: try
  them yourself first).

## Run it
```
python3 scores.py      # Mac
python scores.py       # Windows
```
The same goes for every other file.

## Your turn
Import `field` on line 2, add a `badges: list` field under `name` with a default of `field(default_factory=list)`,
then at the bottom add `"speedrun"` to ivy's badges with `ivy.badges.append("speedrun")` and print `ivy` and `nova`.
It prints `Score(points=150, name='Ivy', badges=['speedrun'])` and `Score(points=120, name='Nova', badges=[])`: each
Score got its own list.

## Practice
1. Predict, then run `cards.py`:
   ```python
   from dataclasses import dataclass


   @dataclass(order=True)
   class Card:
       rank: int
       suit: str


   a = Card(10, "hearts")
   b = Card(10, "spades")
   c = Card(2, "spades")
   print(a == b)
   print(sorted([b, c, a]))
   ```
   (`False`: `==` compares every field, and the suits are different. Then
   `[Card(rank=2, suit='spades'), Card(rank=10, suit='hearts'), Card(rank=10, suit='spades')]`: rank first, and the two
   10s are put in order by suit, because "hearts" comes before "spades".)
2. Write `books.py`: a `Book` dataclass with a `title`, a number of `pages`, and `read: bool = False`. Make two books,
   set `read` to `True` on the second one, and print both. With `Book("Dune", 412)` and `Book("Hatchet", 195)` it prints
   `Book(title='Dune', pages=412, read=False)` and `Book(title='Hatchet', pages=195, read=True)`.
3. Write `point.py`: a frozen `Point` dataclass with `x` and `y`. Try to change `x` inside a `try` block (lesson 27) and
   catch `FrozenInstanceError` (import it from `dataclasses` too), print the error, then print the point. With
   `Point(3, 4)` it prints `Can't move it: cannot assign to field 'x'` and `Point(x=3, y=4)`.
