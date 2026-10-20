# Lesson 07: String Indexing and Slicing in Python

Part of **Python: Zero to Warrior**, a free Python course for beginners.
Video: https://youtu.be/DevbiX_KS3M · Full course: https://www.youtube.com/playlist?list=PLcsbg964FAwc

## What's in this lesson
- Every character in a string has a position number, its **index**. Python starts counting at 0, so in
  `hero = "Warrior"`, `hero[0]` is `W` and the last character, `hero[6]`, is the second `r`.
- Square brackets after the name get one character: `hero[4]` is `i`.
- **Negative indexes** count from the end: `hero[-1]` is always the last character, `hero[-2]` the one before it,
  back to `hero[-7]`, the `W`.
- `len(hero)` is 7, so the last index is `len(hero) - 1`, which is 6.
- A **slice** takes a piece: `hero[start:stop]` starts at `start` and stops *before* `stop`. `hero[0:3]` is `War`.
  Stop minus start is how many characters you get.
- Leave out the start and it starts at 0 (`hero[:3]` is `War`); leave out the stop and it goes to the end
  (`hero[3:]` is `rior`).
- A third number is the **step**, how far Python jumps each time: `hero[::2]` is `Wrir`, and a step of `-1` goes
  backwards, so `hero[::-1]` is `roirraW`.

## Common mistakes
- Using `len()` as an index: `hero[len(hero)]` stops with `IndexError: string index out of range`, because the
  indexes only go up to 6. Use `hero[len(hero) - 1]`, or just `hero[-1]`.
- Changing one letter: `hero[0] = "B"` stops with
  `TypeError: 'str' object does not support item assignment`. Strings are immutable (they can't be changed), so build
  a new one instead: `hero = "B" + hero[1:]` makes `Barrior`.

## Files
- `solution.py`: the program from the video.
- `starter.py`: the "your turn" exercise, with TODOs to fill in.

## Run it
```
python3 solution.py      # Mac
python solution.py       # Windows
```

## Practice
1. With `word = "Python"`, predict `word[2:5]`, `word[-3:]` and `word[::2]` before you run them. Use stop minus start
   to check how many characters each one should have.
2. Print `"racecar"[::-1]`, then `"warrior"[::-1]`. A word that reads the same backwards is a palindrome: which one
   is?
3. Make `code = "ABC-1234"` and print just the part after the dash with a slice, then just the part before it.
