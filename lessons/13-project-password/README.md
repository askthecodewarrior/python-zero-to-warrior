# Lesson 13: Build a Password Strength Checker in Python

Part of **Python: Zero to Warrior**, a free Python course for beginners.
Video: https://youtu.be/FjSLsYbugJU · Full course: https://www.youtube.com/playlist?list=PLcsbg964FAwc

This is a learning project, not a real security tool. Don't use any password from the video or from this page:
they're on the internet now.

## What's in this lesson
- Plan the program as comments first, one per step, then build it one step at a time and run it after each step.
- `len(password)` counts every character in a string, spaces included.
- `password.lower()` gives you a lowercase copy, and the password itself stays the same. `==` is case sensitive
  (`"Password1!" == "password1!"` is False), so compare the lowercase copy when capitals shouldn't matter.
- A tiny blocklist: `common = lowered == "password" or lowered == "password1!"`. Each side of `or` is a full
  comparison on its own, and `common` ends up True or False.
- An `if` / `elif` / `else` chain checks from the top down and runs only the first block that's True, so the order of
  the checks is the order they win. `else` runs only when every check above it is False.
- `password.isdigit()` is True when every character is a digit.
- `input()` shows the password on the screen as you type it. That's fine for practice; a real login form usually
  hides it.
- Two common mistakes:
  - An `if` for every check instead of `elif`: Python tests every one, so `Password1!` prints
    `Weak: that's a common password` and then `OK: but 15 or more characters is better`.
  - Comparing `password` without `.lower()`: `Password1!` doesn't match `"password1!"` and gets OK.

## What makes a password strong (NIST)
The U.S. government's guidelines, NIST SP 800-63B-4 (2025):
- **Length matters most.** At least 15 characters when the password is the only thing protecting the account, and at
  least 8 when there's a second factor, like a code from an app on your phone.
- **No composition rules.** Forcing "a capital, a number and a symbol" makes people pick `password` → `Password1` →
  `Password1!`, NIST's own example. (`Password1!` has shown up in Have I Been Pwned's leaked password data 584,516
  times, checked October 19, 2026.)
- **Check a blocklist.** Compare the whole password against common and leaked passwords and easy guesses like the
  username or the site's name.
- A passphrase, a few random words with spaces, is an easy way to get a long password.

The numbers-only check in this program is a warning of my own, not a NIST rule: with only ten digits to pick from,
there are far fewer combinations to guess than with letters.

Sources: [NIST SP 800-63B-4](https://pages.nist.gov/800-63-4/sp800-63b.html) (sec. 3.1.1.2 and appendix A) ·
[Have I Been Pwned, Pwned Passwords](https://haveibeenpwned.com/Passwords)

## Files
- `solution.py`: the program from the video. Try `Password1!`, `5839201746381925` and `orbit pickle lantern`.
- `starter.py`: the "your turn" exercise (check the username too), with TODOs. It runs as it is; fill in the TODOs.
- `username_solution.py`: one way to do the your-turn exercise.

## Run it
```
python3 solution.py      # Mac
python solution.py       # Windows
```

## Practice
1. Your turn from the video: ask for a username before the password, and add an `elif` that rates the password weak
   when its lowercase copy matches the username in lowercase. With `pixel_knight` for both, you should see
   `Weak: it's the same as your username`.
2. `12345678` is one of the most common passwords there is, but the checker says `OK: but it's only numbers`. Add it
   to the blocklist. The line would be too long with a third `or`, so add a second line under it:
   `common = common or lowered == "12345678"`. Now it says `Weak: that's a common password`.
3. Predict first, then run it: what does the checker say for `Password1`, with no exclamation point? (It's 9
   characters, and it isn't on our two-password list, so you get `OK: but 15 or more characters is better`. A real
   blocklist would catch it.)
