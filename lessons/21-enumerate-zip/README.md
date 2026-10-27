# Lesson 21: enumerate() and zip() in Python

Part of **Python: Zero to Warrior**, a free Python course for beginners.
Video: https://youtu.be/NHXHD0s-eH4 · Full course: https://www.youtube.com/playlist?list=PLcsbg964FAwc

## What's in this lesson
- **The long way:** `for i in range(len(shop)):` with `shop[i]` inside the loop gives you each index and its item. It
  works, but it's clunky.
- **`enumerate()`** does it for you. On every pass it hands you a **pair**, the index and the item, in a tuple
  (lesson 19): `(0, 'sword')`, `(1, 'shield')`, and so on. Put two names before `in` and the pair is **unpacked**:
  `for i, item in enumerate(shop):` puts the index in `i` and the item in `item`.
- **`start=1`** is a setting `enumerate()` has: `enumerate(shop, start=1)` counts 1, 2, 3, 4, the way a person
  numbers things. It only changes the numbers; the list doesn't change, and `shop[0]` is still `"sword"`.
- **`zip()`** walks two lists side by side: `for item, price in zip(shop, prices):` pairs the first item with the
  first price, the second with the second, and so on. Each pass is a pair again, a tuple, unpacked into two names.
- **zip stops at the shorter list, with no error.** `shop` has 4 items and `prices` has 3, so the loop prints 3 lines
  and the rope is left out. If you'd rather get an error when the lengths don't match, Python 3.10 and up has
  `zip(shop, prices, strict=True)`: it prints the 3 pairs, then stops with
  `ValueError: zip() argument 2 is shorter than argument 1`.
- **`dict(zip(keys, values))`** turns the pairs into a dictionary (lesson 20): `dict(zip(shop, prices))` is
  `{'sword': 50, 'shield': 30, 'potion': 10}`. `dict` is the name of Python's dictionary type.
- **The classic mistake:** one name before `in`, like `for item in enumerate(shop):`. There's no error, but `item`
  holds the whole tuple, so `print(item)` shows `(0, 'sword')`. The fix is two names: `for i, item in enumerate(shop):`.

## Files
- `shop.py`: the program from the video.
- `starter.py`: the "your turn" exercise, with TODOs.
- `solution.py`: one way to solve it.
- `even_items.py` and `price_lookup.py`: answers to practice problems 2 and 3 (try them yourself first).

## Run it
```
python3 shop.py      # Mac
python shop.py       # Windows
```
The same goes for every other file.

## Practice
1. Predict, then run: `colors = ["red", "green", "blue"]`, then `for n, c in enumerate(colors, start=10):` with
   `print(n, c)` inside. What prints? (10 red, 11 green, 12 blue: start can be any number.)
2. Every other item: loop over `shop = ["sword", "shield", "potion", "rope", "map"]` with `enumerate()`, and print only
   the items whose index is even (use `%` from lesson 04: `i % 2 == 0`). You should get sword, potion and map.
3. A price list: make `price_of = dict(zip(shop, prices))` from two lists, ask the user what they want to buy with
   `input()`, and print its price with `.get()` and a default (lesson 20), so an item the shop doesn't sell never
   crashes the program.
