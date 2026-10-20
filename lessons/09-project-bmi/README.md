# Lesson 09: Build a BMI Calculator in Python (Beginner Project)

Part of **Python: Zero to Warrior**, a free Python course for beginners.
Video: https://youtu.be/PyFCH9R6Jak · Full course: https://www.youtube.com/playlist?list=PLcsbg964FAwc

## What's in this lesson
- Plan a program as comments first, one per step, then build it one step at a time and run it after each step.
- `float(input("Weight in kg: "))` asks a question and turns the answer into a number. Python runs it from the inside
  out: `input()` hands back a string, and `float()` turns it into a number. Use `float()`, not `int()`, when the user
  might type a decimal point (`int("1.75")` stops with a ValueError).
- The formula `weight / height ** 2`: `**` is the power operator, and Python does the power before the division, so
  it squares the height first.
- `f"{bmi:.1f}"` shows the number with one decimal place, rounded (22.857... shows as 22.9, not 22.8).
- Test with more than one set of values, including the ones a real user gets wrong (175 for the height, in
  centimeters, gives a BMI of 0.0).
- Two common mistakes:
  - Forgetting `float()`: `TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'`.
  - `weight / height * height`: `/` and `*` go left to right, so it gives back the weight (70.0). Use
    `height ** 2` or `(height * height)`.

## About BMI
BMI (body mass index) is weight in kilograms divided by height in meters, squared. The CDC's categories for adults
20 and older: less than 18.5 is underweight, 18.5 to less than 25 is healthy weight, 25 to less than 30 is
overweight, and 30 or greater is obesity. BMI is a screening measure, not a diagnosis: the CDC says to consider it
with other factors, and to talk with a health care provider if you have questions about yours.
Sources: CDC, [Adult BMI Categories](https://www.cdc.gov/bmi/adult-calculator/bmi-categories.html) and
[BMI Frequently Asked Questions](https://www.cdc.gov/bmi/faq/index.html).

## Files
- `solution.py`: the program from the video (type 70 and 1.75 when it asks).
- `starter.py`: the "your turn" exercise (ask for the height in centimeters), with TODOs to fill in. It asks for the
  weight and stops until you fill them in.

## Run it
```
python3 solution.py      # Mac
python solution.py       # Windows
```

## Practice
1. Your turn from the video: ask for the height in centimeters, then divide it by 100 to get meters. With 70 and 175
   you should see `Your BMI is 22.9`.
2. Make a pounds-and-inches version. The CDC's formula for U.S. units is `703 * weight / height ** 2`, with the weight
   in pounds and the height in inches. With 154 pounds and 69 inches you should see `Your BMI is 22.7`.
3. Predict first, then run it: type 55 and 1.7. The BMI is 19.031141868512112. Does `:.1f` show `19` or `19.0`?
