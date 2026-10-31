# Lesson 45: Iterators and Generators in Python (yield)

Part of **Python: Zero to Warrior**, a free Python course for beginners.
Video: https://youtu.be/x1fuXkqsY2w · Full course: https://www.youtube.com/playlist?list=PLcsbg964FAwc

## What's in this lesson
- **An iterable** is anything a `for` loop can go through: a list, a string, a tuple, a dictionary, a file. A number
  isn't one, which is why `for i in 5:` stops with `TypeError: 'int' object is not iterable` (lesson 15).
- **An iterator** hands you the items one at a time, and it remembers where it left off, like a bookmark.
  - `iter(potions)` gives you an iterator for the list.
  - `next(iterator)` hands you the next item.
  - When there's nothing left, `next()` stops with `StopIteration`.
- **iter() and next()** (`potions.py`):
  ```python
  # What a for loop does for you
  potions = ["heal", "mana", "speed"]
  iterator = iter(potions)
  print(next(iterator))
  print(next(iterator))
  print(next(iterator))
  print(next(iterator))
  ```
  It prints `heal`, `mana` and `speed`, and then the fourth `next()` has nothing left, so Python stops with a traceback
  whose last line is `StopIteration`.
- **What a for loop does for you.** `for potion in potions:` calls `iter(potions)` once at the start, calls `next()`
  before every pass and puts the value in `potion`, and when `next()` stops with `StopIteration`, the loop just ends,
  with no error. Looping over a file (`for line in f:`, lesson 31) works the same way: a file is an iterator too.
- **A generator** (`drops.py`): a function with `yield` in it is a **generator function**, and calling it gives you a
  **generator**, which is an iterator.
  ```python
  # A generator pauses at every yield
  def gold_drops(top):
      gold = 5
      while gold <= top:
          yield gold
          gold *= 2


  drops = gold_drops(40)
  print(next(drops))
  print(next(drops))
  for coins in drops:
      print("Loot:", coins)
  ```
  It prints `5`, `10`, `Loot: 20` and `Loot: 40`. `yield` is like `return` because it hands a value back, but instead of
  ending the function, it pauses it. The next time you ask for a value, it picks up on the line after the `yield`, with
  `gold` and `top` just the way it left them. `gold_drops(40)` on its own runs none of the function's code: it just
  hands you the generator. The `for` loop starts at 20 because the two `next()` calls already took 5 and 10. When
  `gold` doubles to 80, the `while` loop stops, the function is done, and that ends the `for` loop. (`gold *= 2` doubles
  `gold`, the way `+=` adds.)
- **A generator expression** (`memory.py`): a list comprehension (lesson 22) in parentheses instead of square brackets.
  ```python
  # A million numbers: a list vs a generator
  import sys

  big_list = [n * 2 for n in range(1_000_000)]
  big_gen = (n * 2 for n in range(1_000_000))
  print(sys.getsizeof(big_list))
  print(sys.getsizeof(big_gen))
  print(sum(big_gen))
  ```
  On Python 3.15.0 it prints `8448728`, `216` and `999999000000`. `sys.getsizeof` gives an object's size in bytes, and
  it only counts the object itself: the list is over eight million bytes without the numbers in it, and the generator
  is 216 bytes because it only ever has one number at a time. `sum` still gets all million numbers out of it. The
  underscores in `1_000_000` are only there to make it easier to read; Python ignores them.
- **Common mistake 1: using the same generator twice.** A generator hands out each value only once:
  ```python
  drops = gold_drops(40)
  print(list(drops))   # [5, 10, 20, 40]
  print(list(drops))   # []
  ```
  That's also why the second `list(half)` came back empty in lesson 43: `map()` and `filter()` hand you iterators too.
  If you need the values again, call `gold_drops(40)` again for a new generator, or keep the values in a list.
- **Common mistake 2: `len()` on a generator.** `len(drops)` stops with
  `TypeError: object of type 'generator' has no len()`, because a generator doesn't know how many values it'll make
  until it makes them. If you need the count, make it a list first: `len(list(drops))` is `4`.

## Files
- `potions.py`, `drops.py`, `memory.py`: the programs from the video.
- `starter.py`: the "your turn" exercise, with TODOs.
- `solution.py`: one way to solve it.
- `peek.py`, `squares.py`, `forever.py`: practice problems 1, 2 and 3 (`squares.py` and `forever.py` are one answer
  each: try them yourself first).

## Run it
```
python3 drops.py      # Mac
python drops.py       # Windows
```
The same goes for every other file.

## Your turn
In a new file called `triple.py`, write a generator function `triple(top)` that starts `n` at 1, and while
`n <= top`, yields `n` and then multiplies it by 3 (`n *= 3`). Then loop over `triple(100)` and print each number. It
prints `1`, `3`, `9`, `27` and `81`.

## Practice
1. Predict, then run `peek.py`: one `next()`, then `list()` on the same generator.
   ```python
   drops = gold_drops(100)
   print(next(drops))
   print(list(drops))
   ```
   (`5`, then `[10, 20, 40, 80]`: `next()` already took the 5, and the list gets everything that's left.)
2. Write `squares.py`: a generator expression that gives the square of every number from 1 to 5,
   `(n * n for n in range(1, 6))`, passed to `sum`. It prints `55`.
3. Write `forever.py`: a generator function `levels()` that starts `level` at 1 and, in a `while True:` loop (lesson
   16), yields `level` and adds 1. It never ends, and that's fine: it only makes the next level when you ask. Call
   `next()` on it three times, and it prints `1`, `2` and `3`.
