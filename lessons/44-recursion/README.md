# Lesson 44: Recursion in Python, Explained Visually

Part of **Python: Zero to Warrior**, a free Python course for beginners.
Video: https://youtu.be/I6PlI7P5-J8 · Full course: https://www.youtube.com/playlist?list=PLcsbg964FAwc

## What's in this lesson
- **Recursion** is when a function solves a problem by calling itself on a smaller piece of that same problem. A
  function that does that is a **recursive function**.
- **Every recursive function needs two parts:**
  - a **base case**, where it stops calling itself;
  - a **recursive step**, where it calls itself with something smaller, so every call gets one step closer to the base
    case.
- **A countdown that calls itself** (`countdown.py`):
  ```python
  # A function that calls itself
  def countdown(n):
      if n == 0:
          print("Go!")
          return
      print(n)
      countdown(n - 1)


  countdown(3)
  ```
  It prints `3`, `2`, `1`, `Go!`. `if n == 0:` is the base case, and `return` on its own just ends the function.
  `countdown(n - 1)` is the recursive step: the same function with a number that's one smaller.
- **A value comes back** (`factorial.py`): 3 factorial is 3 × 2 × 1.
  ```python
  # 3 factorial is 3 * 2 * 1
  def factorial(n):
      if n == 1:
          return 1
      return n * factorial(n - 1)


  print(factorial(3))
  ```
  It prints `6`, and `factorial` runs three times. Each call gets its own **frame** on the **call stack** (lesson 24),
  with its own `n`: `factorial(3)` waits for `factorial(2)`, which waits for `factorial(1)`. That one is the base case
  and returns 1, then the answers come back one at a time: 2 × 1 is 2, and 3 × 2 is 6.
- **The common mistake: no base case.** Take the `if` block out of `countdown` and it never stops: it prints 3, 2, 1,
  0, -1 and on down to -995, then Python stops it with `RecursionError: maximum recursion depth exceeded`. Python only
  lets calls stack up about 1,000 deep. The fix is the base case, and making sure every call moves toward it.
- **Recursion or a loop?** Recursion fits things shaped like a tree, where each piece holds smaller pieces of the same
  kind (folders inside folders, a branch that splits into smaller branches). For something that just counts or
  repeats, a loop is usually simpler. The countdown as a `while` loop (lesson 14) prints the same four lines:
  ```python
  n = 3
  while n > 0:
      print(n)
      n -= 1
  print("Go!")
  ```
- **The boss level** (`tree.py`): a fractal tree with turtle. `branch(length)` stops when `length < 15` (the base case),
  draws a line, turns left 30 degrees and draws a smaller tree (`branch(length * 0.7)`), turns right 60 and draws
  another, then turns back and goes `backward(length)`, so the turtle ends where that branch started. `pen.speed(0)` is
  turtle's fastest speed (the tree draws in about 8 seconds), and `pen.teleport(0, -220)` moves the turtle without
  drawing a line.

## Files
- `countdown.py`, `factorial.py`, `tree.py`: the programs from the video.
- `starter.py`: the "your turn" exercise, with TODOs.
- `solution.py`: one way to solve it.
- `order.py`, `power.py`, `digits.py`: practice problems 1, 2 and 3 (`power.py` and `digits.py` are one answer each:
  try them yourself first).

## Run it
```
python3 countdown.py      # Mac
python countdown.py       # Windows
```
The same goes for every other file.

## Your turn
In a new file called `total.py`, write a recursive function `total(n)` that adds up every number from 1 to n. The base
case is `if n == 0: return 0`, and the recursive step is `return n + total(n - 1)`. Then `print(total(100))`. It prints
`5050`, the same answer as the for loop in lesson 15.

## Practice
1. Predict, then run `order.py`: it's `countdown` with `print(n)` moved under the recursive call.
   ```python
   def countdown(n):
       if n == 0:
           print("Go!")
           return
       countdown(n - 1)
       print(n)


   countdown(3)
   ```
   (`Go!`, `1`, `2`, `3`: each call prints only after the call it made has come back, so the deepest call, the base
   case, prints first, and `countdown(3)` prints last.)
2. Write `power.py`: `power(base, exp)` multiplies `base` by itself `exp` times. The base case is `exp == 0`, which
   returns 1. `power(2, 10)` prints `1024` and `power(3, 4)` prints `81`.
3. Write `digits.py`: `sum_digits(n)` adds up the digits of a whole number, using `% 10` for the last digit and `// 10`
   for the rest (lesson 4). The base case is a number under 10, which is its own sum. `sum_digits(2026)` prints `10`.
