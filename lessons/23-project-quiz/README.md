# Lesson 23: Build a Quiz Game in Python

Part of **Python: Zero to Warrior**, a free Python course for beginners. ⭐ A project lesson.
Video: https://youtu.be/dVZiCewTwaQ · Full course: https://www.youtube.com/playlist?list=PLcsbg964FAwc

## What's in this lesson
- Nothing new on its own: a list (lesson 18), dictionaries (lesson 20), a for loop with `enumerate(..., start=1)`
  (lessons 15 and 21), `input()` (lesson 05), `strip()` and `lower()` (lesson 08), `if` / `else` (lesson 11), `+=`
  (lesson 14) and f-strings (lesson 06).
- The one new combination is **dictionaries inside a list**. Each question is a dictionary with two keys, `"text"`
  and `"answer"`, and the list holds all of them in order. Inside square brackets, Python lets you put each item on its
  own line, and a comma after the last item is fine (it makes adding a question easier).
- In VS Code, typing `[` puts the closing `]` in for you, and Enter between them moves the `]` down to its own line.
  If your editor didn't add it, type it yourself after the last question.
- On each pass of `for n, question in enumerate(questions, start=1):`, `n` counts from 1 and `question` is one
  dictionary, so `question["text"]` is the question to ask and `question["answer"]` is its answer.
- `input()` always gives you a string, so a number answer is stored as a string too: `"3"`, in quotes.
- `reply.strip().lower()` takes the spaces off both ends, then makes every letter lowercase (each method hands back a
  new string, so `lower()` works on what `strip()` gave back). That's why every answer in the list is lowercase.
- `len(questions)` counts the dictionaries, so "Question 1 of 3" and "out of 3" change by themselves when you add a
  question.
- Two classic mistakes:
  - comparing the reply as it was typed (`if reply == question["answer"]:`): `Float` with a capital F, or a space
    before the word, isn't equal to `float`, so the game says `Wrong! The answer was float`;
  - leaving out `score += 1`: every right answer says `Correct!`, but the end says `You scored 0 out of 3`.

## Files
- `quiz.py`: the game from the video.
- `starter.py`: the "your turn" exercise (a fourth question, and "Perfect score!"), with TODOs.
- `solution.py`: one way to solve it.
- `answers.py` and `twotries.py`: answers to practice problems 2 and 3 (try them yourself first).

## Run it
```
python3 quiz.py      # Mac
python quiz.py       # Windows
```
The same goes for every other file.

## Practice
1. Add two more questions of your own, one with a word answer and one with a number answer. Remember the quotes
   around the number, and keep both answers lowercase.
2. Let a question have more than one right answer: give each dictionary an `"answers"` key holding a list, like
   `["for", "while"]` for "Name a loop keyword", and check the reply with `in` instead of `==`. (`answers.py` is one
   answer.)
3. Give the player a second try: when the first reply is wrong, ask once more with `input()` before showing the
   answer, and still add 1 to the score if the second try is right. (`twotries.py`.)

## Checked on Python 3.15.0
Every file compiles, is PEP 8 clean (pycodestyle), and was run with real answers: `solution.py` says
`Question 1 of 4` and `You scored 4 out of 4`, then `Perfect score!`; `answers.py` accepts `While` and `three`;
`twotries.py` gives `3` a second chance after `3.5`.
