# Lesson 25: Default and Keyword Arguments, *args and **kwargs

Part of **Python: Zero to Warrior**, a free Python course for beginners.
Video: https://youtu.be/kriHkpx6kMA · Full course: https://www.youtube.com/playlist?list=PLcsbg964FAwc

## What's in this lesson
- **Default values:** an equals sign on a parameter gives it a **default value**, the value it uses when the call
  doesn't pass one.
  ```python
  def greet(name, greeting="Hello"):
      print(f"{greeting}, {name}!")


  greet("Ana")              # Hello, Ana!
  greet("Kai", "Welcome")   # Welcome, Kai!
  ```
  Parameters with defaults go after the ones without, or Python stops with a `SyntaxError`.
- **Positional arguments** match the parameters by position: the first argument goes to the first parameter, the
  second to the second.
- **Keyword arguments** name the parameter in the call, so the order doesn't matter:
  ```python
  greet(greeting="Hi", name="Zed")   # Hi, Zed!
  greet("Mia", greeting="Hey")       # Hey, Mia!
  ```
  You can mix the two, as long as the positional ones come first. You've used one before: `start=1` in `enumerate`.
- **`*args`:** a star in front of a parameter packs all the positional arguments in the call, however many there are,
  into one **tuple**. `args` is just the name most people use; the star does the work. `sum()` is a built-in function
  that adds up the numbers in a tuple or a list.
  ```python
  def total(*args):
      print(args)
      return sum(args)


  print(total(10, 25, 5))   # (10, 25, 5), then 40
  print(total())            # (), then 0
  ```
- **`**kwargs`:** two stars pack any number of keyword arguments into a **dictionary**, where each keyword is a key
  holding the value you gave it. (In math, like `2 ** 3`, `**` is still the power operator from lesson 04.)
  ```python
  def show_player(**kwargs):
      print(kwargs)
      for key, value in kwargs.items():
          print(f"{key}: {value}")


  show_player(name="Ana", level=3, gold=50)
  # {'name': 'Ana', 'level': 3, 'gold': 50}, then one line per key
  ```
- **print uses all of these.** `help(print)` starts with `print(*objects, sep=' ', end='\n', file=None, flush=False)`:
  any number of values, then two default values you can change by keyword:
  ```python
  print("Ana", "Kai", "Zed", sep=", ")   # Ana, Kai, Zed
  print("Loading", end="...")
  print("done")                          # Loading...done (on one line)
  ```
- **The common mistake:** a positional argument after a keyword argument.
  `greet(greeting="Hey", "Mia")` stops with `SyntaxError: positional argument follows keyword argument`, and because
  it's a SyntaxError, none of the file runs. The fix: `greet("Mia", greeting="Hey")`.

## Files
- `welcome.py`, `total.py` and `player.py`: the programs from the video.
- `starter.py`: the "your turn" exercise, with TODOs.
- `solution.py`: one way to solve it.
- `hero.py` and `average.py`: answers to practice problems 2 and 3 (try them yourself first).

## Run it
```
python3 welcome.py      # Mac
python welcome.py       # Windows
```
The same goes for every other file.

## Practice
1. Predict, then run:
   ```python
   def power_up(level, boost=1):
       return level + boost


   print(power_up(5))
   print(power_up(5, 3))
   print(power_up(boost=10, level=2))
   ```
   (`6`, `8`, then `12`: the first call uses the default, the second replaces it, and the third names both.)
2. Fix it: this stops with a SyntaxError before anything prints. Make it print `Kai carries a bow`.
   ```python
   def make_hero(name, weapon="sword"):
       print(f"{name} carries a {weapon}")


   make_hero(weapon="bow", "Kai")
   ```
3. Write a function `average(*scores)` that returns the average of any number of scores: `sum(scores)` divided by
   `len(scores)`. `print(average(80, 90, 100))` should print `90.0`. Bonus: make `average()` with no scores return `0`
   instead of crashing (hint: an `if` on `len(scores) == 0`).
