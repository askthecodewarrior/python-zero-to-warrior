# Lesson 29: `if __name__ == '__main__'` in Python, Explained

Part of **Python: Zero to Warrior**, a free Python course for beginners.
Video: https://youtu.be/BFkkurtjXZI · Full course: https://www.youtube.com/playlist?list=PLcsbg964FAwc

## What's in this lesson
- **Importing a file runs all of it.** When `main.py` says `import helpers`, Python runs `helpers.py` once, from top to
  bottom. A `def` line just makes the function, but any other line really runs, so test lines at the bottom of a module
  print every time it's imported:
  ```python
  # My own module
  def greet(player):
      return f"Welcome, {player}!"


  # Quick test
  print("Testing greet")
  print(greet("Warrior"))
  ```
  ```python
  # Use my own module
  import helpers

  print(helpers.greet("Ana"))
  ```
  Running `main.py` prints `Testing greet`, `Welcome, Warrior!` and then `Welcome, Ana!`.
- **`__name__`** ("dunder name", short for double underscore name: two underscores before `name`, two after) is a
  variable Python sets for every file before it runs. You never have to make it yourself.
  - In the file you run, `__name__` is `"__main__"` (two underscores on each side).
  - In a file that gets imported, `__name__` is the module's own name, without the `.py`: `"helpers"`.
  - Add `print(__name__)` to the bottom of `helpers.py` to see it: `python3 helpers.py` prints `__main__`, and
    `python3 main.py` prints `helpers`.
- **The fix:** put the test lines under an `if` that checks `__name__`, so they only run when you run that file
  directly, and stay quiet when it's imported:
  ```python
  # My own module
  def greet(player):
      return f"Welcome, {player}!"


  if __name__ == "__main__":
      print("Testing greet")
      print(greet("Warrior"))
      print(__name__)
  ```
  Now `python3 helpers.py` still prints the three test lines, and `python3 main.py` only prints `Welcome, Ana!`.
- **The main() habit:** a lot of programs put the code that starts the program in a function called `main`, and the
  `if` at the bottom just calls it. The function's name is only a habit; it's a different thing from `"__main__"` in the
  quotes.
  ```python
  # Use my own module
  import helpers


  def main():
      print(helpers.greet("Ana"))


  if __name__ == "__main__":
      main()
  ```
- **The common mistake:** one underscore instead of two. `if _name_ == "__main__":` stops with
  `NameError: name '_name_' is not defined. Did you mean: '__name__'?`. And if the underscores are wrong around main,
  inside the quotes (`"main"` or `"_main_"`), there's no error at all: the test lines just never run.

## Files
- `helpers.py` (the fixed module) and `main.py` (lesson 28's main.py): the programs from the video. Keep them in the
  same folder, so `import helpers` finds `helpers.py`.
- `starter.py`: the "your turn" exercise, with TODOs.
- `solution.py`: one way to solve it.
- `tools.py` and `app.py`, `scores.py`, `game.py`: answers to practice problems 1, 2 and 3 (try them yourself first).

## Run it
```
python3 helpers.py      # Mac
python helpers.py       # Windows
python3 main.py         # Mac
python main.py          # Windows
```
The same goes for every other file.

## Practice
1. Predict, then run `app.py` (both files in the same folder):
   ```python
   # tools.py
   def double(n):
       return n * 2


   print("tools says", __name__)
   ```
   ```python
   # app.py
   import tools

   print("app says", __name__)
   print(tools.double(21))
   ```
   (`tools says tools`, then `app says __main__`, then `42`.) Then run `tools.py` by itself and predict again
   (`tools says __main__`).
2. Fix it: importing this module prints two test lines. Change it so they only run when you run `scores.py` itself.
   ```python
   def total(a, b):
       return a + b


   print("Testing total")
   print(total(2, 3))
   ```
   (`python3 scores.py` still prints `Testing total` and `5`; `import scores` prints nothing.)
3. Write `game.py`: import `helpers`, put an `input("Your name: ")` and a `print(helpers.greet(...))` with that name
   inside a function called `main()`, and call it under `if __name__ == "__main__":`. Typing `Warrior` should print
   `Welcome, Warrior!`.
