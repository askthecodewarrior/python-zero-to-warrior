# Lesson 17: Build a Number Guessing Game in Python

Part of **Python: Zero to Warrior**, a free Python course for beginners. ⭐ A project lesson.
Video: https://youtu.be/AkgssX26DSE · Full course: https://www.youtube.com/playlist?list=PLcsbg964FAwc

## What's in this lesson
- The **random module** comes with Python. `import random` loads it (the same way `import turtle` did in lessons 15
  and 16), and `random.randint(a, b)` gives you a random whole number from `a` to `b`, **both ends included**:
  `random.randint(1, 6)` can give you 1, 2, 3, 4, 5 or 6. That's different from `range(1, 6)`, which stops at 5.
- `random` is fine for games. For passwords or anything to do with security, the Python docs say to use the
  `secrets` module instead.
- `dice.py` rolls a six-sided die. Run it a few times: you get a different number each time (and your numbers will be
  different from the video's).
- `guess.py` is the game, built in three steps, with the plan written as comments first:
  1. pick a secret number with `random.randint(1, 100)` and say so;
  2. a `while True:` loop that asks for a guess, turns it into a whole number with `int(input(...))`, counts it with
     `tries += 1`, and says `Too low!` or `Too high!`. When it's neither, the guess is right, and `else: break` leaves
     the loop;
  3. after the loop, an f-string says how many tries it took. Python only gets to that line after `break`.
- Strategy: guess the middle of what's left every time, and 1 to 100 never takes more than 7 guesses.
- If the player types a word, like `fifty`, `int()` stops the program with a `ValueError`. Catching that (with `try`
  and `except`) comes later in the course.
- Two classic mistakes:
  - leaving out `int()`: the guess is a string, and `guess < secret` stops with
    `TypeError: '<' not supported between instances of 'str' and 'int'`;
  - putting `secret = random.randint(1, 100)` inside the loop: the secret changes on every guess, so the hints
    don't add up. Pick it once, before the loop.

## Files
- `dice.py`: roll a die with `random.randint(1, 6)`.
- `guess.py`: the game from the video.
- `starter.py`: the "your turn" exercise (say "1 try", not "1 tries"), with TODOs.
- `solution.py`: one way to solve it.
- `limit.py` and `twodice.py`: answers to practice problems 2 and 3 (try them yourself first).

## Run it
```
python3 guess.py      # Mac
python guess.py       # Windows
```
The same goes for every other file.

## Practice
1. Make the game go from 1 to 1000: change the `randint` line and the message. If you always guess the middle, what's
   the most guesses you'll ever need now? (10.)
2. Give the player 7 tries. Use `while tries < 7:` instead of `while True:`, print the "You got it" message inside the
   `else` before `break`, and after the loop, if the last guess wasn't the secret (`!=`), print
   `Out of tries! It was` and the secret. (`limit.py` is one answer.)
3. Roll two dice: two `randint` calls, then print both and their total. Run it a few times. What's the smallest total
   you can get, and the largest? (`twodice.py`.)
