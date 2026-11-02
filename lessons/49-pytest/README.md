# Lesson 49: Testing Python Code with pytest

Part of **Python: Zero to Warrior**, a free Python course for beginners. This is the last lesson before the projects at
the end of the course.
Video: https://youtu.be/KEYZvp3wN0k · Full course: https://www.youtube.com/playlist?list=PLcsbg964FAwc

## What's in this lesson
- **A test is code that checks your code.** It calls a function with values you picked and checks that what comes back
  is what you expected. Run your tests after every change, and they tell you if something broke.
- **`assert`** is the check inside every test. If what follows it is `True`, nothing happens; if it's `False`, Python
  stops with an `AssertionError`. On its own, that error doesn't tell you what the value was.
- **pytest** finds your tests and runs them. It looks in files whose names start with `test_` (or end with `_test.py`),
  and in those files it runs every function whose name starts with `test`. It prints a dot for each test that passed and
  an `F` for each test that failed. It doesn't come with Python, so install it in your project's virtual environment
  (lesson 48):
  ```
  pip install pytest            # with the venv on (Mac and Windows)
  uv add --dev pytest           # or, in a uv project (then: uv run pytest)
  ```
- **The function under test** (`shop.py`): 100 gold or more gets 10 gold off.
  ```python
  def total_cost(price, count):
      if count < 1:
          raise ValueError("count must be at least 1")
      cost = price * count
      if cost >= 100:
          cost -= 10
      return cost
  ```
- **The tests** (`test_shop.py`):
  ```python
  import pytest
  from shop import total_cost


  def test_small_order():
      assert total_cost(5, 4) == 20


  def test_exactly_100():
      assert total_cost(25, 4) == 90


  def test_zero_potions():
      with pytest.raises(ValueError):
          total_cost(20, 0)
  ```
  (The video's file has one more test, `test_big_order`.) `pytest -v` gives every test its own line, with `PASSED` or
  `FAILED`.
- **Find a bug with a test:** the video's `shop.py` started with `if cost > 100:`. The test for exactly 100 failed, and
  pytest showed why:
  ```
  E       assert 100 == 90
  E        +  where 100 = total_cost(25, 4)
  ```
  On the left is what the function gave back, on the right is what the test expected, and the `where` line says where
  the 100 came from. `>` left out exactly 100, so the fix is `>=`. A mistake like this, wrong by one value right at the
  edge, is called an **off-by-one error**, which is why it's worth testing the exact number where a rule changes.
- **`pytest.raises`** checks that code raises the error you expect (lesson 27). It's a `with` block, like the one you
  used to open files in lesson 31: the test passes only if the code under it raises that error.
- **`@pytest.mark.parametrize`** (a decorator, lesson 46) runs one test once for each set of values in a list.
- **The common mistakes:**
  - A test that pytest never runs: a function named `check_small_order` (not `test...`) or a file named
    `shop_tests.py` is ignored, and pytest says `collected 0 items` and `no tests ran`.
  - A test with no `assert`: `total_cost(25, 4) == 90` on its own works out the comparison and throws the answer away,
    so the test passes even with a bug. If a new test passes the first time, change the number it expects for a second
    and make sure it can fail.

## Files
- `shop.py` and `test_shop.py`: the code from the video (with the fix).
- `starter.py`: the "your turn" exercise, with a TODO. `solution.py`: one way to solve it.
- `damage.py` + `test_damage.py`: practice 1 (one of its tests fails on purpose).
- `vowels.py` + `test_vowels.py`: practice 2 (`test_vowels.py` is one answer: try it yourself first).
- `test_param.py`: practice 3 (one answer).

## Run it
With your venv on, in this folder:
```
pytest          # every test file here (Mac and Windows)
pytest -v       # one line per test
```
pytest runs a file you name even when its name doesn't start with `test_`: `pytest -v starter.py`.

## Your turn
Add a fifth test, `test_ten_potions`, that checks ten potions at 12 gold each: `total_cost(12, 10)` should be `110`.
Run `pytest -v starter.py`, and if it says `5 passed`, you've got it.

## Practice
1. `damage.py` has `after_hit(health, damage)`, which should never go below 0. Before you run `pytest test_damage.py`,
   predict what it prints. (`.F`: `test_big_hit` fails with `assert -5 == 0` and `where -5 = after_hit(10, 15)`. Fix
   `after_hit` with `max(health - damage, 0)` and run it again: `2 passed`.)
2. `vowels.py` has `count_vowels(word)`. Write `test_vowels.py` with three tests: a normal word, a word in capitals,
   and a word with no vowels. (One answer is in the folder: `"potion"` is 3, `"ELIXIR"` is 3, `"rhythm"` is 0.)
3. Put the four `total_cost` checks (5 and 4, 30 and 5, 25 and 4, 12 and 10) into one test with
   `@pytest.mark.parametrize`. `pytest -v test_param.py` shows four lines, each with its values in square brackets, and
   `4 passed`.
