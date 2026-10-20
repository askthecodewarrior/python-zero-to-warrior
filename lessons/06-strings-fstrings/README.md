# Lesson 06: Strings and f-strings in Python

Part of **Python: Zero to Warrior**, a free Python course for beginners.
Video: https://youtu.be/hxRDt4I6R8c · Full course: https://www.youtube.com/playlist?list=PLcsbg964FAwc

## What's in this lesson
- A string is text in quotes. `"Warrior"` and `'Warrior'` are the same string, as long as both ends match.
- Two kinds of quotes let you put one inside the other: `"It's my turn"` keeps the apostrophe as part of the text.
- `+` joins strings (concatenation) and adds no space for you: `player + " the Brave"`.
- `*` repeats a string: `"=" * 20` is a divider line of 20 equals signs.
- `len()` counts the characters in a string: every letter, number, space and symbol.
- An f-string has an `f` right before the opening quote. Python swaps each `{ }` for the value inside it:
  `f"{player} is level {level}"`. Numbers go straight in, with nothing to convert.
- The braces can hold an expression, any code that works out to a value: `f"New level: {level + 1}"`.
- `:.2f` inside the braces shows a number with two decimal places: `f"{price:.2f}"` shows `4.5` as `4.50`.

## Common mistakes
- Forgetting the `f`: `print("{player} is level {level}")` prints the braces and names as they are, with no error.
- An apostrophe inside single quotes: `print('It's my turn')` stops with
  `SyntaxError: unterminated string literal`, and none of the file runs. Use double quotes around text with an
  apostrophe.

## Files
- `solution.py`: the program from the video.
- `starter.py`: the "your turn" exercise, with TODOs to fill in.

## Run it
```
python3 solution.py      # Mac
python solution.py       # Windows
```

## Practice
1. Make `first = "Code"` and `last = "Warrior"`, then print them joined with a space between them, once with `+`
   and once with an f-string. Both lines should print `Code Warrior`.
2. Print `len("Hello, World!")`. Count the characters yourself first: does the comma count? The space? Run it and check.
3. A potion costs `2.5` gold and you buy `3`. Print `Total: 7.50 gold` with one f-string, doing the math inside the
   braces.
