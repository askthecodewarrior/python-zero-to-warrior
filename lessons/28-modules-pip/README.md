# Lesson 28: Modules, import and pip in Python

Part of **Python: Zero to Warrior**, a free Python course for beginners.
Video: https://youtu.be/aH9NgQgVg9c · Full course: https://www.youtube.com/playlist?list=PLcsbg964FAwc

## What's in this lesson
- A **module** is a `.py` file of code you can reuse. Modules come from three places:
  1. **The standard library**, a big set of modules that comes with Python (`math`, `random`, `turtle` and more).
  2. **Your own files**: any `.py` file you write is a module too.
  3. **Packages** other people wrote and shared on **PyPI**, the Python Package Index (pypi.org), which you install
     with **pip**.
- `import math` loads a module, and the **dot** reaches inside it:
  ```python
  import math
  import random

  print(math.sqrt(81))                                 # 9.0 (sqrt always gives back a float)
  print(math.pi)                                       # 3.141592653589793
  print(random.randint(1, 6))                          # a whole number from 1 to 6
  print(random.choice(["sword", "shield", "potion"]))  # one item, picked at random
  ```
  The last two lines print something different on every run.
- `from math import sqrt` brings in just one name, so you can write `sqrt(81)` without `math.` in front. It's shorter,
  but `sqrt` on its own doesn't say where it came from, so most of the time `import math` is the clearer choice.
- **Your own module:** put `helpers.py` and `main.py` in the **same folder**. `main.py` says `import helpers` (the
  module's name, without `.py`), and Python runs `helpers.py` and gives `main.py` its functions:
  ```python
  # helpers.py
  def greet(name):
      return f"Welcome, {name}!"
  ```
  ```python
  # main.py
  import helpers

  print(helpers.greet("Ana"))   # Welcome, Ana!
  ```
- **The common mistake:** a typo in the module's name. `import helper` stops with
  `ModuleNotFoundError: No module named 'helper'. Did you mean: 'helpers'?` (Python 3.15). You get the same error when
  the two files are in different folders. And don't name a file of your own after a module that comes with Python,
  like `random.py`: then `import random` finds your file instead.
- **pip** comes with Python. `-m pip` runs the pip that belongs to that Python, so the package goes into the same
  Python that runs your programs:
  ```
  python3 -m pip install requests     # Mac
  python -m pip install requests      # Windows
  python3 -m pip list                 # see what's installed (Windows: python -m pip list)
  ```
  pip installs requests plus the packages it needs (its dependencies). If it says a new release of pip is available,
  that's fine to leave for now. Installing packages into a **virtual environment** (one per project) is the better
  habit, and it comes later in the course.
- **Using requests** (`todo.py`): `requests.get(url)` asks a website for data, and `.json()` turns the JSON it sends
  back into a Python dictionary. jsonplaceholder.typicode.com is a free practice site that sends back sample data:
  ```python
  import requests

  url = "https://jsonplaceholder.typicode.com/todos/1"
  response = requests.get(url)
  print(response.json())
  # {'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}
  ```

## Files
- `toolbox.py`, `helpers.py`, `main.py` and `todo.py`: the programs from the video (`todo.py` needs requests
  installed and an internet connection).
- `starter.py`: the "your turn" exercise, with TODOs.
- `solution.py`: one way to solve it.
- `predict.py`, `game_tools.py` with `play.py`, and `enemy.py`: answers to practice problems 1 to 3 (try them yourself
  first).

## Run it
```
python3 main.py      # Mac
python main.py       # Windows
```
The same goes for every other file.

## Practice
1. Predict, then run:
   ```python
   import math

   print(math.sqrt(49))
   print(int(math.sqrt(49)))
   ```
   (`7.0`, then `7`: `sqrt` gives back a float, and `int()` from lesson 5 turns it into a whole number.)
2. Make your own module: a file `game_tools.py` with a function `heal(hp)` that returns `hp + 10`, and a file
   `play.py` in the same folder that imports `game_tools` and prints `game_tools.heal(50)`. Running `play.py` should
   print `60`.
3. Use `from random import choice` to pick a random enemy from `["goblin", "orc", "dragon"]`, and print
   `A wild <enemy> appears!`. Run it a few times: the enemy changes.
