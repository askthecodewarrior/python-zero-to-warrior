# Lesson 24: Functions in Python (def, parameters, return)

Part of **Python: Zero to Warrior**, a free Python course for beginners.
Video: https://youtu.be/Q3UN-akWPZ4 · Full course: https://www.youtube.com/playlist?list=PLcsbg964FAwc

## What's in this lesson
- **Why functions:** when the same lines show up again and again, you write them once, give them a name, and run them
  by name whenever you need them. Change the message, and you change it in one place. Programmers call that
  "don't repeat yourself".
- **Making one:** `def`, the function's name, parentheses, and a colon, then the **body**: the indented lines under
  the `def`, which are the code the function runs.
  ```python
  def greet(name):
      print(f"Welcome, {name}!")
      print("Your quest starts now.")
  ```
- **A def doesn't run the body.** Python reads it, remembers the name `greet`, and moves on. A file with only the
  `def` in it prints nothing. The body runs when you **call** the function: its name with parentheses after it,
  `greet("Ana")`.
- **Parameter and argument:** the name inside the parentheses on the `def` line (`name`) is a **parameter**, a
  variable that waits for a value. The value you put in the parentheses when you call it (`"Ana"`) is an
  **argument**. The argument fills in the parameter.
- **The call stack:** each call gets its own **frame**, a box that holds that call's own variables (its parameters
  with the arguments' values, in the same order). The frame goes on top of the main program's when the function is
  called, and goes away when the function is done.
- **print against return:** `print` only shows a value on the screen. `return` hands the value back to the line that
  called the function, so you can save it in a variable or use it in an expression:
  ```python
  a = show_total(50, 25)   # prints 75, then a is None
  b = get_total(50, 25)    # prints nothing, and b is 75
  print(get_total(b, 10) * 2)   # 170
  ```
  A function that doesn't have a `return` hands back `None`, Python's way of saying there's no value at all.
- **Two common mistakes:**
  - Calling a function above its `def`: Python runs a file from the top down, so it stops with
    `NameError: name 'greet' is not defined`. Keep the `def` above the code that calls it.
  - Forgetting `return`: the body works out the answer and throws it away, so you get `None`. If a function gives you
    `None`, check that it has a `return`.
- **Style:** Python's style guide (PEP 8) puts two empty lines before and after a function at the top level of a file.

## Files
- `greet.py` and `gold.py`: the programs from the video.
- `starter.py`: the "your turn" exercise, with TODOs.
- `solution.py`: one way to solve it.
- `area.py` and `even.py`: answers to practice problems 2 and 3 (try them yourself first).

## Run it
```
python3 gold.py      # Mac
python gold.py       # Windows
```
The same goes for every other file.

## Practice
1. Predict, then run:
   ```python
   def shout(word):
       print(word.upper())


   x = shout("hi")
   print(x)
   ```
   (`HI`, then `None`: the body prints `HI`, and there's no `return`, so `x` is `None`.)
2. Fix it: this prints `None` instead of `12`. Find the missing word.
   ```python
   def area(width, height):
       width * height


   print(area(3, 4))
   ```
3. Write a function `is_even(n)` that returns `True` when `n` is even and `False` when it's odd (hint: `n % 2 == 0`
   from lessons 04 and 10). `print(is_even(4))` should print `True`, and `print(is_even(7))` should print `False`.
