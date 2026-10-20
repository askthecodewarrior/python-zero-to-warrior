# Lesson 01: Get Python and VS Code (Windows & Mac)

Part of **Python: Zero to Warrior**, a free Python course for beginners.
Video: https://youtu.be/m3Dtbd4LWW4 · Full course: https://www.youtube.com/playlist?list=PLcsbg964FAwc

This lesson doesn't click through the installers, because they keep changing. These are the official pages, which
stay up to date. Get the newest version: it was Python 3.15 when the video was recorded, and a newer number is fine.

## What you need
| Piece | Its job | Where to get it |
|---|---|---|
| Python | reads your code and runs it | https://www.python.org/downloads/ (Windows: **Download Python install manager**; Mac: **Download Python 3.x**) |
| VS Code | the editor where you write your code | https://code.visualstudio.com/download |
| The Python extension, by Microsoft | lets VS Code understand and run Python | in VS Code: the **Extensions** icon, search **Python**, install the one by **Microsoft** (https://marketplace.visualstudio.com/items?itemName=ms-python.python) |

The install steps, from Python's own documentation:
- Windows: https://docs.python.org/3/using/windows.html
- Mac: https://docs.python.org/3/using/mac.html

## Check that it worked
1. Open VS Code and click the **Extensions** icon. Under **Installed** you should see **Python** by Microsoft (with
   Pylance and Python Debugger, which it installs for you). Click it: **Disable** and **Uninstall** buttons mean it's
   installed and turned on.
2. Open a terminal in VS Code: **Terminal → New Terminal**, or **Control + `** (backtick, the key above Tab) on
   Windows and Mac. If VS Code asks whether you trust the authors of the files in your folder, it's your own folder,
   so trust it.
3. Type the version check and hit enter:
   ```
   python3 --version     # Mac
   python --version      # Windows
   ```
   You should see a version number, `Python 3.15.0` or newer. If you get an error instead, close VS Code, open it
   again, and try once more; if that doesn't fix it, go back to the install page for your computer.

If you see the version number, you have everything you need for this course.

## Practice
No code in this lesson. Your one job: get the version number to show up in VS Code's terminal, then reply to the
pinned comment with "Day 1 ✅".
