# Lesson 30: Build Hangman in Python

Part of **Python: Zero to Warrior**, a free Python course for beginners. ⭐ A project lesson.
Video: https://youtu.be/tjAsTR-9hkk · Full course: https://www.youtube.com/playlist?list=PLcsbg964FAwc

## What's in this lesson
- Nothing new on its own, apart from `isalpha()`: `random.choice()` (lesson 28), a list and `append()` (lesson 18), a
  set with `set()`, `add()` and `in` (lesson 19), `while` loops and `break` (lessons 14 and 16), a `for` loop (lesson
  15), `join()` and `strip()` / `lower()` (lesson 08), `if` / `elif` / `else` and `or` / `not` (lessons 11 and 12),
  `def` and `return` (lessons 24 and 25), and `main()` under `if __name__ == "__main__":` (lesson 29).
- The program is four small functions, each starting with a comment from the plan:
  - `pick_word()` returns one word from the list, picked at random;
  - `show_word(word, guessed)` builds the board: each letter of the word if it's in the set of guesses, or `_` if it
    isn't, joined with spaces (`loop` with only `o` guessed is `_ o o _`);
  - `get_guess(guessed)` keeps asking until it gets one new letter: `strip()` and `lower()` clean what was typed,
    `len(guess) != 1 or not guess.isalpha()` turns away anything that isn't one letter, and `guess in guessed` turns
    away a repeat. `return guess` is the only way out of its `while True` loop;
  - `main()` plays: the board and the lives each turn, `break` when there are no blanks left, and one life gone for
    every letter that isn't in the word. After the loop, `if lives == 0:` shows the word.
- `isalpha()` works like `isdigit()` from lesson 08: it's `True` only when every character is a letter.
- `set()` makes an empty set. Empty curly braces `{}` make an empty dictionary (lesson 19).
- The word is random, so your games won't pick the same words as the video's.
- Two classic mistakes:
  - leaving out `.lower()`: a capital `O` isn't equal to `o`, so the game says `Not in the word.` and takes a life
    for a letter that's really there;
  - leaving out the `elif guess in guessed:` check: the same wrong letter costs a life every time it's typed.

## Files
- `hangman.py`: the game from the video.
- `starter.py`: the "your turn" exercise (three words of your own, and play again), with TODOs.
- `solution.py`: one way to solve it.
- `misses.py`, `levels.py` and `wholeword.py`: answers to the practice problems (try them yourself first).

## Run it
```
python3 hangman.py      # Mac
python hangman.py       # Windows
```
The same goes for every other file.

## Practice
1. Show the wrong letters next to the lives, like `Lives: 4   Wrong: e z`: keep them in a list, `append()` each miss,
   and `join()` the list in the board's line. (`misses.py` is one answer.)
2. Let the player pick a level: ask `Easy or hard?` before the game, give 8 lives for easy and 4 for hard, and ask
   again for anything else. A small function that returns the number works well. (`levels.py`.)
3. Let the player guess the whole word at once: if what they type is the word, they win right away; otherwise it has
   to be one new letter, as before. (`wholeword.py`.)

## Checked on Python 3.15.0
Every file compiles, is PEP 8 clean (pycodestyle), and was run with real input: `solution.py` played two games in a
row (a win, then six misses and `Out of lives!`) and stopped on `n`; `misses.py` showed `Wrong: e z`; `levels.py`
asked again after `medium` and gave 4 lives for `hard`; `wholeword.py` won on `loop` after one letter.
