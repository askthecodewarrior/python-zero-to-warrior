# Lesson 51: Build a Password Generator GUI in Python (Tkinter)

Part of **Python: Zero to Warrior**, a free Python course for beginners. A project lesson: your first program with a
window you click on, built with Tkinter, which comes with Python.
Video: https://youtu.be/d8c4CmPlH6s · Full course: https://www.youtube.com/playlist?list=PLcsbg964FAwc

Don't use any password from the video: they're on the internet now. Run the program and make your own.

## What's in this lesson
- **Two rules for a password generator.**
  - **Length matters most** (lesson 13). NIST's password guidelines (SP 800-63B-4, 2025) say at least 15 characters
    when a password is the only thing protecting an account, at least 8 when there's a second step (like a code from
    an app), and sites should let you use at least 64. So the length box goes from 8 to 64 and starts at 16.
  - **Pick every character with `secrets`, not `random`.** The Python docs say `secrets` is for passwords, and that
    `random` is "completely unsuitable for cryptographic purposes" (lesson 17 said the same).
- **The window.** `root = tk.Tk()` makes the main window, `root.title(...)` sets its title, and `root.mainloop()` starts
  the event loop: the program waits for clicks and key presses and runs the code for each one, until you close the
  window. Nothing after `mainloop()` runs until then, so it's the last line. (turtle draws in a Tkinter window too:
  `turtle.done()` is its `mainloop()`.)
- **ttk** (`from tkinter import ttk`) is Tkinter's themed widgets, so the buttons and boxes look like your system's.
- **Widgets in a frame, laid out with `grid`.** A `ttk.Frame` with `padding=20` holds the widgets; `grid(row=...,
  column=...)` puts each one in a row and column (counting from 0), and `sticky="w"` / `"e"` pushes it to the left or
  the right of its spot. `columnspan=2` stretches the entry across both columns, and `pady=10` adds space above and
  below it.
- **Tkinter variables.** `tk.IntVar`, `tk.BooleanVar` and `tk.StringVar` can be tied to a widget (`textvariable=` or
  `variable=`): when the user changes the widget, the variable changes, and when your code calls `.set(...)`, the
  widget shows it. `.get()` reads it.
  - The `Spinbox` (`from_=8, to=64`; `from_` has an underscore because `from` is a Python keyword) is `readonly`, so
    only its arrows change it.
  - Each `Checkbutton` is tied to a `BooleanVar`.
  - The `Entry` is `readonly` (you can select and copy, not type) and uses `TkFixedFont`, Tk's fixed-width font.
- **`generate()`** adds `string.ascii_letters` (52 letters), `string.digits` (10) and `string.punctuation` (32 symbols)
  to `chars` for each box that's checked, then picks `length.get()` characters with `secrets.choice(chars)` and puts the
  password in `result`, which the entry shows. If no box is checked, it sets a message in `status` and returns before
  `secrets.choice` gets an empty string. (Without that check, `secrets.choice("")` raises `IndexError: Cannot choose
  from an empty sequence`; Tkinter prints it in the terminal and keeps the window open.)
- **`copy()`** uses `root.clipboard_clear()` and `root.clipboard_append(...)`. Anything on the clipboard can be read by
  other apps on your computer, so paste the password into your password manager right away, and don't leave it there.
- **`command=generate`, no parentheses.** The button needs the function itself, so it can call it on every click.
- **The common mistakes:**
  - `command=generate()` calls `generate` once while the button is made and gives the button `None`: the window opens
    with a password already in the box, and clicking Generate does nothing.
  - `random` instead of `secrets`: the passwords look random, but `random` is completely predictable once you know its
    starting point (its seed). `weak.py` sets the seed to 51 and prints `p1GJkp0o1Jq73zJ9` every single time.

## Files
- `passgen.py`: the program from the video.
- `starter.py`: the "your turn" exercise, with TODOs. `solution.py`: one way to solve it.
- `length_note.py`, `each_kind.py`: one answer each for practice problems 1 and 2 (try them yourself first).
- `weak.py`: the mistake from the video. Don't use it for passwords.

## Run it
```
python3 passgen.py      # Mac
python passgen.py       # Windows
```
The window opens and the terminal waits until you close it. On some Linux systems Tkinter is a separate package
(`python3-tk` on Debian and Ubuntu). Python's 3.15 release notes warn that macOS 27.0 can hang Tk apps when a menu
command opens a dialog; this app has no menus or dialogs.

## Your turn
Add a fourth check box, **No look-alikes**. When it's checked, take the characters that are easy to mix up (`0`, `O`,
`1`, `l` and `I`) out of `chars` before the loop picks anything. Test it with only Digits checked: you should never see a
0 or a 1. (`solution.py` is one answer: `chars = chars.replace(c, "")` for each of them, from lesson 8's string methods.)

## Practice problems
1. **Show the length.** After a password is made, make the message label say how many characters it has, like
   `16 characters`, with an f-string and `len()`. (`length_note.py`)
2. **At least one of each.** Some sites still want a letter, a digit and a symbol. With all three boxes checked and a
   length of 8, the video's program doesn't always give you all three (try it a few times). Change `generate()` so it
   picks one character from each checked kind first, fills the rest from `chars`, and then shuffles them with
   `secrets.SystemRandom().shuffle(...)`. (`each_kind.py`)
3. **A Clear button.** Add a third button that empties the password box and the message. Then think about it: should it
   clear the clipboard too?
