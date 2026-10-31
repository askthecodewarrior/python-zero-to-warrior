# Lesson 42: Build a Bank Account System in Python (OOP Project)

Part of **Python: Zero to Warrior**, a free Python course for beginners. This is the project at the end of the
object-oriented lessons (36 to 41), and it uses something from each of them.
Video: https://youtu.be/VsQk_mNyl1c · Full course: https://www.youtube.com/playlist?list=PLcsbg964FAwc

This is a teaching project. Real banking software needs a lot more than this, like security, a database and a lot of
testing. The people in it (Zoe, Ava and Ben) are made up.

## What's in this lesson
- **Money in whole cents.** Floats can't store most decimal fractions exactly (`print(0.1 + 0.2)` prints
  `0.30000000000000004`, lesson 4), so every amount is a whole number of cents in an int: $50.00 is `5000`, and $12.50
  is `1250`. The program only turns cents into dollars when it prints them.
- **`account.py`: a Transaction and an Account.**
  - `Transaction` is a dataclass (lesson 41) with a `kind` and the `cents`, so Python writes its `__init__` and its
    `__repr__`, and it prints as `Transaction(kind='deposit', cents=5000)`.
  - `Account.__init__` sets the `owner`, `_balance = 0` and an empty `history` list. The underscore is lesson 39's
    convention: the account's own data, so other code should leave it alone. Python doesn't stop anyone from writing
    `_balance`; the underscore is a promise, not a lock. The list is made in `__init__`, so every account gets its own.
  - `balance` is a `@property` with no setter (lesson 39): other code can read `zoe.balance`, and `zoe.balance = 100`
    is an `AttributeError` (`property 'balance' of 'Account' object has no setter`).
  - `deposit()` and `withdraw()` check the amount first and `raise ValueError(...)` (lesson 27) for an amount that
    isn't positive, or for more money than the account has. A failed check stops the method before the balance or the
    history changes. Without the positive check, `withdraw(-5000)` would add $50.
  - `__str__` (lesson 40) is what `print` shows: `f"{self.owner}: ${self._balance / 100:.2f}"`, with lesson 6's
    `:.2f` for two decimal places.
  - The test at the bottom is inside `if __name__ == "__main__":` (lesson 29), so it runs when you run account.py, and
    not when bank.py imports it.
- **`bank.py`: a SavingsAccount and a Bank.**
  - `from account import Account` (lesson 28) uses the class from your own file.
  - `class SavingsAccount(Account):` inherits everything (lesson 38). Its `__init__` calls `super().__init__(owner)`
    for the owner, the balance and the history, then adds `self.rate`. `add_interest()` works out
    `self.balance * self.rate // 100` (lesson 4's floor division keeps it whole cents) and deposits it, so interest gets
    checked and shows up in the history. A tiny balance can round down to 0 interest, and `deposit()` refuses 0, so it
    only deposits when the interest is more than 0.
  - `Bank` keeps every account in a dictionary (lesson 20) under its owner's name. `transfer()` withdraws first and then
    deposits, so if there isn't enough money, the withdraw raises its `ValueError`, the deposit never runs, and nothing
    moves. (A name that isn't in the bank still raises a `KeyError` on the receiver after the money is out: see the
    practice ideas below.)
  - `try` / `except ValueError as e` around the transfer that's too big prints `Transfer failed: not enough money`, and
    the program keeps going.
- **The common mistakes:**
  - Deposit first, then withdraw, in `transfer()`. It still says the transfer failed, but the deposit already happened,
    so money shows up out of nowhere: Ava ends with `$120.00` instead of `$30.00`. Take the money out first.
  - Parentheses after a property: `print(zoe.balance())` stops with `TypeError: 'int' object is not callable`, because
    `zoe.balance` is already the number. Write `zoe.balance`.

## Files
- `account.py`, `bank.py`: the programs from the video. Keep them in the same folder.
- `starter.py`: the "your turn" exercise, with TODOs. `solution.py`: one way to solve it.
- `predict.py`, `checking.py`, `statement.py`: practice problems 1, 2 and 3 (`checking.py` and `statement.py` are one
  answer each: try them yourself first).
- `menu.py`: a bonus text menu for one account, with `while True`, `input()` and `try` / `except` (lessons 5, 14,
  16 and 27).

## Run it
```
python3 account.py      # Mac
python account.py       # Windows
```
The same goes for every other file. Every file here imports from account.py, so run them from this folder.

## Your turn
Give `Bank` a method called `total` that adds up the balance of every account and returns it (in cents). Then print it
at the bottom in dollars. `solution.py` prints `Total: $50.40`: Ava's $30.00 plus Ben's $20.40.

## Practice
1. Predict, then run `predict.py`:
   ```python
   kim = Account("Kim")
   kim.deposit(2000)
   try:
       kim.deposit(0)
   except ValueError as e:
       print("Error:", e)
   try:
       kim.withdraw(-500)
   except ValueError as e:
       print("Error:", e)
   print(kim)
   print(len(kim.history))
   ```
   (`Error: amount must be positive` twice, then `Kim: $20.00` and `1`: both bad amounts were stopped before they got
   near the balance or the history.)
2. Write `checking.py`: a `CheckingAccount(Account)` with a `fee` in cents, whose `withdraw()` checks the amount is
   positive, then calls `super().withdraw(cents + self.fee)` (lesson 38's `super().method()`). With a fee of 150, a
   $100.00 deposit and a $20.00 withdrawal, it prints `Sam: $78.50`; then withdrawing $79.00 fails with
   `not enough money`, because the fee makes it $80.50.
3. Write `statement.py`: a `statement(account)` function that prints each transaction as `+$40.00` for a deposit or
   `-$15.75` for a withdrawal, then the account line. Deposits of 4000 and 250 and a withdrawal of 1575 print `+$40.00`,
   `-$15.75`, `+$2.50` and `Lee: $26.75`.

More ideas: make `transfer()` check that both names are in `self.accounts` before it touches any money, or give
`menu.py` a second account and a transfer choice.
