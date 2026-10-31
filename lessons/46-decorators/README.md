# Lesson 46: Decorators in Python, Explained Visually

Part of **Python: Zero to Warrior**, a free Python course for beginners.
Video: https://youtu.be/DUGcAuBFEBc · Full course: https://www.youtube.com/playlist?list=PLcsbg964FAwc

## What's in this lesson
- **A decorator** is a function that takes a function and returns a **wrapper** around it: some code runs before the
  original, then the original runs, then some code runs after it, and the original function doesn't change. You've
  already used a few: `@property` (lesson 39) and `@dataclass` (lesson 41, which works on a class instead of a
  function). They're built on lesson 43's idea: a function is a value, so you can pass it to another function.
- **Building one** (`spells.py`):
  ```python
  # A decorator wraps a function in another one
  def announce(func):
      def wrapper():
          print("Casting...")
          func()
          print("Done!")
      return wrapper
  ```
  - `def wrapper():` inside `announce` is an **inner function**. Like any `def`, it only defines `wrapper`; nothing in
    it runs yet.
  - `return wrapper` has no parentheses: `announce` hands back the function itself, like `len` without its parentheses
    in lesson 43.
  - `wrapper` uses `func`, which belongs to `announce` (the enclosing scope, the E in LEGB, lesson 26). It keeps `func`
    even after `announce` is done. An inner function that remembers names from the function it was made in is a
    **closure**.
- **What it does to the name:**
  ```python
  def fireball():
      print("Fireball!")


  fireball = announce(fireball)
  fireball()                 # Casting...  Fireball!  Done!
  print(fireball.__name__)   # wrapper
  ```
  Python works out the right side first: `announce` makes a wrapper that holds on to the original as `func`, and then
  the name `fireball` moves over to the wrapper. Every function keeps its own name in `__name__` ("dunder name"), so it
  now says `wrapper`.
- **The @ line does the same thing:**
  ```python
  @announce
  def heal():
      print("Healing!")
  ```
  is just like writing `heal = announce(heal)` right after the `def`.
- **A practical decorator, a timer** (`timer.py`):
  ```python
  import functools
  import time


  def timer(func):
      @functools.wraps(func)
      def wrapper(*args, **kwargs):
          start = time.perf_counter()
          result = func(*args, **kwargs)
          seconds = time.perf_counter() - start
          print(f"{func.__name__}: {seconds:.2f} seconds")
          return result
      return wrapper
  ```
  - `*args, **kwargs` (lesson 25) let the wrapper take whatever arguments the original takes, and pass them all on.
  - `time.perf_counter()` is a clock made for timing things: read it before and after, and take the difference.
    `:.2f` (lesson 6) shows two decimal places. Your time is going to be different, and it changes every run.
  - `return result` hands the original's answer back to whoever called it.
  - `@functools.wraps(func)` copies the original's name (and its docstring, the description in triple quotes under a
    `def` line) onto the wrapper, so `add_up.__name__` is still `add_up`, not `wrapper`.
  - `10_000_000`: Python lets you put underscores in a number to make it easier to read.
- **The common mistakes:**
  - Forgetting `return wrapper`: the decorator hands back `None`, so the `@` line puts the name on `None`, and calling
    it stops with `TypeError: 'NoneType' object is not callable`.
  - Forgetting `return result` in the wrapper: the timer still prints its line, but `print(add_up(10_000_000))` shows
    `None` instead of the sum.

## Files
- `spells.py`, `timer.py`: the programs from the video.
- `starter.py`: the "your turn" exercise, with TODOs.
- `solution.py`: one way to solve it.
- `twice.py`, `shout.py`, `twice_wraps.py`: practice problems 1, 2 and 3 (`shout.py` and `twice_wraps.py` are one
  answer each: try them yourself first).

## Run it
```
python3 spells.py      # Mac
python spells.py       # Windows
```
The same goes for every other file.

## Your turn
Write a second decorator in `timer.py` called `log_calls`. Its wrapper takes `*args` and `**kwargs`, prints `Calling`
and the function's name, and then returns what the function returns. Put `@log_calls` on `add_up` in place of
`@timer`. It prints `Calling add_up`, then `49999995000000`, then `add_up`.

## Practice
1. Predict, then run `twice.py`:
   ```python
   def twice(func):
       def wrapper():
           func()
           func()
       return wrapper


   @twice
   def cheer():
       print("Huzzah!")


   cheer()
   print(cheer.__name__)
   ```
   (`Huzzah!` twice, because the wrapper calls the original two times, and then `wrapper`, because the name `cheer` is
   on the wrapper now.)
2. Write `shout.py`: a decorator `shout` whose wrapper takes `*args, **kwargs`, calls the function, and returns its
   result in capitals with `.upper()` (lesson 8). Put it on `def greet(name): return f"hello, {name}"`, written over two
   lines. `print(greet("Ana"))` prints `HELLO, ANA`, and `print(greet(name="Kai"))` prints `HELLO, KAI`.
3. Change `twice.py` so `print(cheer.__name__)` shows `cheer`. (Add `import functools` and `@functools.wraps(func)`
   above `def wrapper():`. It prints `Huzzah!`, `Huzzah!`, `cheer`.)
