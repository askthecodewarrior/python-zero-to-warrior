# Lesson 35: Build an Automatic File Organizer in Python

Part of **Python: Zero to Warrior**, a free Python course for beginners. ⭐ A project lesson.
Video: https://youtu.be/S8cFK4sdeLk · Full course: https://www.youtube.com/playlist?list=PLcsbg964FAwc

## Safety first
- These programs only ever work on a **test folder** called `messy_downloads`, inside the folder you run them from.
  `make_mess.py` makes it and fills it with empty test files, so you can make the mess again any time.
- `organizer.py` starts with `DRY_RUN = True`: it only **prints** what it would move. Read every line, and only when
  they all look right, set `DRY_RUN = False` and run it again.
- It never overwrites a file: if a folder already has a file with the same name, that file is skipped.
- If you ever point `FOLDER` at a real folder, make a backup first, and start with a dry run, every time.

## What's in this lesson
- Already in the course: `pathlib`'s `Path` and `exists()` (lesson 31), a dictionary and `get()` with a default
  (lesson 20), a `for` loop and `continue` (lessons 15 and 16), `if` / `elif` / `else` (lesson 11), f-strings (lesson
  06), functions (lessons 24 and 25) and `main()` under `if __name__ == "__main__":` (lesson 29).
- New, one line each:
  - `folder / name` joins two parts of a path: `Path("messy_downloads") / "cat.jpg"` is `messy_downloads/cat.jpg`;
  - `mkdir(exist_ok=True)` makes a folder, and it's fine if it's already there;
  - `touch()` makes an empty file;
  - `iterdir()` goes through every item in a folder, one `Path` at a time, and `sorted()` puts them in order by name;
  - `is_dir()` is `True` for a folder;
  - `.name` is the file's name without the folders in front of it, and `.suffix` is its extension with the dot
    (`".PNG"` for `logo.PNG`, `""` for a file with no extension);
  - `rename(target)` moves the file to its new path. On a Mac it would quietly replace a file that's already there, which
    is why the organizer checks `target.exists()` first.
- The organizer is three small functions under its settings (`FOLDER`, `DRY_RUN` and `TYPES`):
  - `folder_for(file)` gives the folder name for one file: `TYPES.get(file.suffix.lower(), "Other")`;
  - `organize(folder, dry_run)` skips folders, then for each file skips it, prints what it would do, or makes the
    folder and moves it;
  - `main()` checks that the test folder is there (`Can't find messy_downloads` if you run it from another folder, or
    before `make_mess.py`), then calls `organize()`.
- Two classic mistakes:
  - leaving out `.lower()`: `logo.PNG` has the suffix `.PNG`, which isn't the dictionary's `.png`, so it goes to `Other`;
  - leaving out the `mkdir()` line: `rename()` can't move a file into a folder that isn't there, so the first move
    stops with `FileNotFoundError: [Errno 2] No such file or directory`.

## Files
- `make_mess.py`: makes the test folder (run it first).
- `organizer.py`: the organizer from the video, as it is for the dry run (`DRY_RUN = True`).
- `starter.py`: the "your turn" exercise (a Videos folder), with TODOs.
- `solution.py`: one way to solve it (add `"movie.mp4"` to the names in `make_mess.py` too).
- `summary.py`, `numbered.py` and `hidden.py`: answers to the practice problems (try them yourself first).

## Run it
```
python3 make_mess.py     # Mac
python3 organizer.py
python make_mess.py      # Windows
python organizer.py
```
The same goes for every other file.

## Practice
1. Say how many files it moved: count them as you go, and print `Moved 8 files` at the end (or `Would move 8 files`
   on a dry run). (`summary.py` is one answer.)
2. Don't skip a file whose name is taken: give it a number instead, like `notes (1).txt`. A file's `.stem` is its name
   without the extension, so `f"{file.stem} ({n}){file.suffix}"` builds the new name; keep adding 1 to `n` while that
   name exists. (`numbered.py`.)
3. Leave hidden files alone. On a Mac, Finder can put a hidden `.DS_Store` file in a folder, and the organizer would
   move it to `Other`. Skip every file whose name starts with a dot. (`hidden.py`.)

## Checked on Python 3.15.0
Every file compiles and is PEP 8 clean (pycodestyle), and each one ran for real on a fresh test folder (the runs are in
the lesson's qa/companion-runs.txt): the organizer's dry run and real run, `starter.py`'s dry run, `solution.py`
moving `movie.mp4` to `Videos`, `summary.py` saying `Would move 8 files` and `Moved 8 files`, `numbered.py` moving a
second set of the same names as `backup (1).zip` and so on, and `hidden.py` leaving a `.DS_Store` where it was (while
`organizer.py` would have moved it to `Other`).
