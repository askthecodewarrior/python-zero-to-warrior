# Lesson 48: Virtual Environments, pip and uv in Python

Part of **Python: Zero to Warrior**, a free Python course for beginners.
Video: https://youtu.be/h0Sacdy1Uyo · Full course: https://www.youtube.com/playlist?list=PLcsbg964FAwc

## What's in this lesson
- **The problem:** in lesson 28, `pip install requests` went into the one Python on your computer, which every project
  shares. If an older project needs `requests==2.31.0`, installing it uninstalls 2.34.2 for every project. And a
  program can "work on my machine" only because of something installed there months ago.
- **A virtual environment (venv)** is a folder inside your project with its own Python and its own packages. Python's
  `venv` module makes it, and most people name the folder `.venv`. Inside: `bin/` (`Scripts\` on Windows) with its own
  `python`, `pip` and the `activate` script, and `site-packages/`, where its packages go.
- **Make it and turn it on** (in your project's folder):

  | | Mac / Linux | Windows |
  |---|---|---|
  | make the venv | `python3 -m venv .venv` | `python -m venv .venv` |
  | turn it on (activate) | `source .venv/bin/activate` | `.venv\Scripts\activate` |
  | turn it off | `deactivate` | `deactivate` |

  Once it's on, `(.venv)` shows at the start of the terminal prompt (the line where you type), and `python3`/`python` and
  `pip` are the venv's. With the venv on, plain `pip` works; you don't need `python3 -m pip`.
  On Windows, if PowerShell says running scripts is disabled, run this once (it's in Python's venv docs), then activate
  again: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`
- **pip in a venv:**
  - A new venv starts with only pip: `pip list` shows `pip 26.2.1` and nothing else (your versions may be newer).
  - `pip install requests` installs requests and the four packages it needs into this venv only.
  - `pip freeze` lists what you installed, each with its exact version; `pip freeze > requirements.txt` saves that list
    into a file (the `>` sends the output into the file instead of printing it).
  - On another computer: make a venv, turn it on, then `pip install -r requirements.txt` (`-r` reads the list from the
    file), and pip installs the exact same versions.
  - Share `app.py` and `requirements.txt`, never `.venv` (it's big, and it only works on the computer that made it).
    Since Python 3.13, venv puts a `.gitignore` inside `.venv`, so Git leaves the folder out for you.
- **VS Code:** when a `.venv` folder appears in the folder you have open, VS Code picks it by itself, and the status bar
  shows `.venv (3.15.0)` when a Python file is open. That's the Python the Run button uses; if it shows something else,
  click it and pick the one with `.venv`. New terminals in VS Code usually turn the venv on for you.
- **The common mistake:** installing into the wrong Python. With the venv off (no `(.venv)` in the prompt),
  `python3 -m pip install requests` goes into the Python on your computer, and it still says it worked. Then, with the
  venv on, `python3 app.py` stops with `ModuleNotFoundError: No module named 'requests'`. The fix: turn the venv on
  first, check for `(.venv)`, then install.
- **uv** (optional, and a lot faster; the video used uv 0.13.6): install it once with the command for your system from
  https://docs.astral.sh/uv/getting-started/installation/, then:
  ```
  uv init quest-uv      # a new project folder, with pyproject.toml and a starter program in src/
  cd quest-uv
  uv add requests       # makes .venv, installs requests, writes uv.lock
  uv run quest-uv       # Hello from quest-uv!  (no activating needed)
  ```
  `pyproject.toml` lists `requests>=2.34.2` (2.34.2 or newer), and `uv.lock` records the exact version of every
  package; together they do the job of `requirements.txt`. uv keeps `uv.lock` up to date, so you don't edit it.

## Files
- `app.py`: the program from the video. With the venv on and requests installed, it prints `requests 2.34.2` (or your
  version).
- `requirements.txt`: the list `pip freeze` made in the video.
- `starter.py`: the "your turn" exercise, with TODOs.
- `solution.py`: one way to solve it. With pytest installed in the venv that's on, it prints `pytest 9.2.0` (or your
  version); with the venv off, `ModuleNotFoundError: No module named 'pytest'`.
- `which_python.py`: practice problem 2.

## Practice problems
1. **Rebuild it from the list.** Make a new folder, put `app.py` and `requirements.txt` in it, make a venv there, turn it
   on, and run `pip install -r requirements.txt`. Then run `app.py`. It should print the same version as before:
   `requests 2.34.2` with this file's list.
2. **Which Python is this?** Run `which_python.py` with the venv off, and then on. It prints `sys.prefix` (where the
   running Python lives) and whether that's a venv (`sys.prefix != sys.base_prefix`, the test Python's docs give).
   Venv off: `/Library/Frameworks/Python.framework/Versions/3.15` and `In a venv: False` on a Mac with python.org's
   Python. Venv on: the path of your `.venv` folder and `In a venv: True`.
3. **Two projects, two versions.** Make a second folder, `old-game`, copy `app.py` into it, make a venv there, turn it on,
   and run `pip install requests==2.31.0`. Run `app.py` in each folder with its own venv on: quest prints
   `requests 2.34.2` and old-game prints `requests 2.31.0`, on the same computer, at the same time.
