# Lesson 39: Encapsulation and @property in Python

Part of **Python: Zero to Warrior**, a free Python course for beginners.
Video: https://youtu.be/TOA5WQWFN4Q · Full course: https://www.youtube.com/playlist?list=PLcsbg964FAwc

## What's in this lesson
- **Encapsulation** means an object keeps its data inside, and the rest of your program changes that data through the
  object's own code, so the object can make sure the data always makes sense. Like a thermostat on the wall: you press
  its buttons, you don't move its wires, and it won't go past its limits.
- **The problem.** With a plain attribute, nothing stops a bad value:
  ```python
  # Nothing stops a bad temperature
  class Thermostat:
      def __init__(self, temp):
          self.temp = temp


  home = Thermostat(72)
  home.temp = 500
  print("Heating to", home.temp)
  ```
  It prints `Heating to 500`.
- **One underscore is a sign, not a lock.** `self._temp` means "internal, please don't touch it from outside the
  class". It's a **convention** (an agreement between programmers): Python doesn't stop you, so `home._temp = 500`
  still works. Two underscores (`self.__temp`) make Python rename the attribute to `_Thermostat__temp` (**name
  mangling**). That makes it harder to touch by accident, but it's still not really private.
- **`@property` and a setter guard the value:**
  ```python
  # The thermostat checks every new temp
  class Thermostat:
      def __init__(self, temp):
          self.temp = temp

      @property
      def temp(self):
          return self._temp

      @temp.setter
      def temp(self, value):
          if value < 50 or value > 90:
              raise ValueError("temp must be 50 to 90")
          self._temp = value

      @property
      def celsius(self):
          return round((self._temp - 32) * 5 / 9, 1)


  home = Thermostat(72)
  home.temp = 68
  print(home.temp, home.celsius)
  try:
      home.temp = 500
  except ValueError as e:
      print("Error:", e)
  print(home.temp)
  ```
  It prints `68 20.0`, then `Error: temp must be 50 to 90`, then `68`: `raise` stopped the setter before
  `self._temp = value`, so 500 never got stored.
  - A line that starts with `@` is a **decorator**: it changes how the function under it works (decorators get their own
    lesson later in the course). `@property` turns `temp` into a **property**: `home.temp`, with no parentheses, runs
    the method and hands back `self._temp`.
  - `@temp.setter` runs whenever you write `home.temp = something`; `value` is the new temp. `raise` (lesson 27) stops
    it with your own message.
  - `__init__` says `self.temp = temp`, not `self._temp = temp`, so even a new thermostat goes through the setter.
  - `celsius` has no setter, so it's **read-only**: you can read it, but you can't set it. It's worked out from
    `_temp` every time you read it, so it always matches the temp.
- **The common mistakes:**
  - Setting a property that has no setter (`home.celsius = 20`) stops with
    `AttributeError: property 'celsius' of 'Thermostat' object has no setter`. Change the temp instead, or give the
    property a setter.
  - A setter that sets `self.temp` instead of `self._temp` runs itself again and again, about a thousand times, until
    Python stops it with `RecursionError: maximum recursion depth exceeded`. Inside the property and its setter, always
    use the underscore name.

## Files
- `plain.py`, `thermostat.py`: the programs from the video.
- `starter.py`: the "your turn" exercise, with TODOs.
- `solution.py`: one way to solve it (it prints `heat`, then `Error: mode must be heat, cool or off`).
- `predict.py`, `speaker.py`, `bug.py`: practice problems 1, 2 and 3 (`speaker.py` is one answer, and `bug_fixed.py` is
  `bug.py` fixed: try them yourself first).

## Run it
```
python3 thermostat.py       # Mac
python thermostat.py        # Windows
```
The same goes for every other file.

## Practice
1. Predict, then run `predict.py`: it prints `Start`, tries `Thermostat(95)` inside a `try`, then prints `End`.
   (`Start`, `Error: temp must be 50 to 90`, `End`: `__init__`'s `self.temp = temp` goes through the setter, so the
   object is never made and `Made it at` never prints.)
2. Write `speaker.py`: a `Speaker` class with a `volume` property whose setter only allows 0 to 100 (raise a
   `ValueError` with `volume must be 0 to 100` otherwise), and a read-only `is_muted` property that's `True` when the
   volume is 0. Make `Speaker(40)`, print the volume and `is_muted`, set the volume to 0 and print both again, then try
   150 inside a `try` and print the volume: `40 False`, `0 True`, `Error: volume must be 0 to 100`, `0`.
3. Fix `bug.py`. It has two bugs. The first run stops with `RecursionError: maximum recursion depth exceeded`. Fix that
   one, and the next run stops with `TypeError: 'str' object is not callable`. When both are fixed, it prints `60%`.
