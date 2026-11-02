# Practice 2 (lesson 51), one answer: at least one of each kind
# A password generator with a window
import secrets
import string
import tkinter as tk
from tkinter import ttk


def generate():
    chars = ""
    if letters.get():
        chars += string.ascii_letters
    if digits.get():
        chars += string.digits
    if symbols.get():
        chars += string.punctuation
    if chars == "":
        status.set("Pick at least one kind of character.")
        return
    picks = []
    for kind, on in [(string.ascii_letters, letters.get()),
                     (string.digits, digits.get()),
                     (string.punctuation, symbols.get())]:
        if on:
            picks.append(secrets.choice(kind))
    while len(picks) < length.get():
        picks.append(secrets.choice(chars))
    secrets.SystemRandom().shuffle(picks)
    password = "".join(picks)
    result.set(password)
    status.set("")


def copy():
    root.clipboard_clear()
    root.clipboard_append(result.get())
    status.set("Copied. Paste it into a password manager.")


root = tk.Tk()
root.title("Password Generator")
frame = ttk.Frame(root, padding=20)
frame.grid()

length = tk.IntVar(value=16)
letters = tk.BooleanVar(value=True)
digits = tk.BooleanVar(value=True)
symbols = tk.BooleanVar(value=True)
result = tk.StringVar()
status = tk.StringVar()

label = ttk.Label(frame, text="Length")
label.grid(row=0, column=0, sticky="w")
spin = ttk.Spinbox(frame, from_=8, to=64, width=4)
spin.config(textvariable=length, state="readonly")
spin.grid(row=0, column=1, sticky="e")
box1 = ttk.Checkbutton(frame, text="Letters", variable=letters)
box1.grid(row=1, column=0, sticky="w")
box2 = ttk.Checkbutton(frame, text="Digits", variable=digits)
box2.grid(row=2, column=0, sticky="w")
box3 = ttk.Checkbutton(frame, text="Symbols", variable=symbols)
box3.grid(row=3, column=0, sticky="w")
entry = ttk.Entry(frame, textvariable=result, width=40)
entry.config(state="readonly", font="TkFixedFont")
entry.grid(row=4, column=0, columnspan=2, pady=10)
button = ttk.Button(frame, text="Generate", command=generate)
button.grid(row=5, column=0, sticky="w")
button2 = ttk.Button(frame, text="Copy", command=copy)
button2.grid(row=5, column=1, sticky="e")
note = ttk.Label(frame, textvariable=status)
note.grid(row=6, column=0, columnspan=2)

root.mainloop()
