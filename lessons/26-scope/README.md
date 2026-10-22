# Lesson 26: Variable Scope in Python (LEGB) Explained

Part of **Python: Zero to Warrior**, a free Python course for beginners.
Video: https://youtu.be/3QvZ0f1GMiI · Full course: https://www.youtube.com/playlist?list=PLcsbg964FAwc

## What's in this lesson
- **Scope** is where in your code a name can be seen and used.
- **Global and local:** a variable made at the top level of the file, outside every function, is a **global**
  variable, and a function can read it. A variable made inside a function is a **local** variable: it only exists in
  that function's frame, while that call runs.
  ```python
  gold = 100


  def open_chest():
      gems = 5
      print("Inside:", gold, gems)


  open_chest()                    # Inside: 100 5
  print("Outside:", gold, gems)   # NameError: name 'gems' is not defined
  ```
- **Assigning makes a new local.** Assigning to a name inside a function (giving it a value with an equals sign)
  makes that name local to the function, even when a global has the same name, so the global doesn't change:
  ```python
  coins = 100


  def spend():
      coins = 40
      print("Inside:", coins)


  spend()                    # Inside: 40
  print("Outside:", coins)   # Outside: 100
  ```
- **The common mistake:** reading a global and assigning it in the same function. `score += 1` is short for
  `score = score + 1`, which is an assignment, so `score` is local in the whole function, and Python stops with
  `UnboundLocalError: cannot access local variable 'score' where it is not associated with a value`.
- **The `global` keyword** tells Python that a name in this function means the global one:
  ```python
  score = 0


  def add_point():
      global score
      score += 1


  add_point()
  add_point()
  print("Score:", score)   # Score: 2
  ```
  It works, but most of the time the better habit is the one from lesson 24: pass the value in and return the new
  one, `score = add_point(score)`, so you can see what a function changes just by looking at the line that calls it.
- **LEGB:** every time you use a name, Python looks for it in this order and uses the first one it finds:
  **L**ocal (the function that's running), **E**nclosing (a function around it, when a function is defined inside
  another function), **G**lobal (the top level of the file) and **B**uilt-in (Python's own names, like `print` and
  `len`).
  ```python
  def outer():
      level = 3

      def inner():
          print("Level:", level)

      inner()


  outer()   # Level: 3  (inner has no level of its own, so Python finds outer's)
  ```
  If an inner function needs to assign to an enclosing variable, that's what the `nonlocal` keyword is for; you won't
  need it for a while.
- **Don't hide a built-in name.** Your own names are found before the built-in ones, so after `list = [1, 2]`,
  `list("abc")` stops with `TypeError: 'list' object is not callable`. Pick another name, like `numbers`.

## Files
- `chest.py`, `coins.py` and `score.py`: the programs from the video. (`chest.py` stops with the NameError on purpose.)
- `starter.py`: the "your turn" exercise, with TODOs.
- `solution.py`: one way to solve it.
- `lives.py` and `shout.py`: answers to practice problems 2 and 3 (try them yourself first).

## Run it
```
python3 coins.py      # Mac
python coins.py       # Windows
```
The same goes for every other file.

## Practice
1. Predict, then run:
   ```python
   hp = 10


   def heal():
       hp = 20
       print("Inside:", hp)


   heal()
   print("Outside:", hp)
   ```
   (`Inside: 20`, then `Outside: 10`: the `hp = 20` inside `heal` is a new local, so the global `hp` never changes.)
2. Fix it: this stops with an UnboundLocalError. Make it print `2` without using `global`.
   ```python
   lives = 3


   def lose_life():
       lives -= 1


   lose_life()
   print(lives)
   ```
3. Write a function `greet_loud(name)` with a function inside it, `shout()`, that prints the name in capital letters
   with an exclamation point. `greet_loud` calls `shout()` at the end. `greet_loud("Ana")` should print `ANA!`.
   (`shout` reads `name` from the enclosing function: the E in LEGB.)
