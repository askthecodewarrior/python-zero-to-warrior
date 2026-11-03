# Lesson 53: Build a Port Scanner in Python (Ethical Hacking Basics)

Part of **Python: Zero to Warrior**, a free Python course for beginners. This project builds a small port scanner with
Python's `socket` module, and it only ever scans **your own computer**.
Video: https://youtu.be/h6bPSd0sERU · Full course: https://www.youtube.com/playlist?list=PLcsbg964FAwc

## Read this first: permission
- **Only scan computers you own, or ones you have written permission to test.** A port scan you weren't asked for can
  look like the start of an attack to the people who run that network.
- Without permission, a scan can get your internet service shut off, get you fired or expelled, and in some places it
  can be a crime. (A 17-year-old in Finland was convicted for port scanning a bank.) Source: the Nmap project's guide to
  the legal issues, <https://nmap.org/book/legal-issues.html>.
- Professional penetration testers get permission **in writing** before they start, and it spells out exactly what
  they're allowed to test. That's what ethical hacking is: testing for weaknesses with permission, so they can be fixed.
- Every program here checks **localhost (127.0.0.1)** only, the loopback address: a connection to it never leaves your
  machine. `scanner.py` refuses any other host on purpose. Don't change that. School, work and public Wi-Fi networks
  are not yours to scan.

## Before you start: a test server (so there's an open port to find)
Python comes with a tiny web server. Start it in a terminal in your python-course folder, bound to your own computer:
```
python3 -m http.server 8000 --bind 127.0.0.1      # Mac
python -m http.server 8000 --bind 127.0.0.1       # Windows
```
It prints `Serving HTTP on 127.0.0.1 port 8000 (http://127.0.0.1:8000/) ...` and keeps running. Keep the
`--bind 127.0.0.1`: without it, the server listens on every network your computer is on, so other people on the same
Wi-Fi might be able to open the files in that folder. (Python's docs say this server isn't meant to run a real website.)
Then open a **second** terminal (in VS Code, the + button in the terminal panel) for the scanner.

**When you're done, stop the server:** click that terminal (in VS Code, the first one in the list on the right), click
inside it, and press Control+C. It prints `Keyboard interrupt received, exiting.` and port 8000 is closed again.

## What's in this lesson
- **A port** is a number from 0 to 65535 that says which program on a computer gets a connection (the IP address says
  which computer). Some are well known: 22 SSH, 80 HTTP, 443 HTTPS. A port is **open** when a program is listening on
  it, and **closed** when nothing is, so the computer refuses the connection.
- **The warning comes first**, in the comment at the top of `scanner.py`.
- `ALLOWED` is a set (lesson 19) of the only two hosts the scanner accepts, `"127.0.0.1"` and `"localhost"`. `PORTS` is a
  dictionary (lesson 20) of seven ports and a name for each.
- `is_open(host, port)`:
  - `socket.socket(socket.AF_INET, socket.SOCK_STREAM)` makes an IPv4, TCP socket, and `with` closes it for you
    (like `with open` in lesson 31).
  - `s.settimeout(0.5)` (all one word) waits half a second at most. On your own computer a closed port answers right
    away, but out on a network a computer can just not answer at all.
  - `s.connect_ex((host, port))` takes ONE argument, a `(host, port)` tuple, so it has two sets of parentheses. It gives
    back `0` if it connected, and an error number if it didn't (61 on a Mac, "connection refused"; Windows uses other
    numbers). `connect()` would raise an exception instead (lesson 27). `== 0` turns the number into `True` (open) or
    `False` (closed).
- `scan(host)`: **the guard comes first.** If the host isn't in `ALLOWED`, it prints why and returns before any socket
  exists, so nothing is ever sent to another computer. Then it loops over `PORTS.items()`.
- `main()` asks for the host and uses `.strip().lower()` (lesson 08), so `" LocalHost "` still matches. The
  `if __name__ == "__main__":` check is lesson 29.
- **The common mistakes:**
  - Leaving off `== 0`: `is_open` returns the raw number, and every port comes out backwards, because `0` (open) is falsy
    and `61` (closed) is truthy (lesson 10).
  - `s.connect_ex(host, port)`: two arguments instead of one tuple, so Python stops with
    `TypeError: socket.connect_ex() takes exactly one argument (2 given)`.

## Files
- `scanner.py`: the program from the video.
- `starter.py`: the "your turn" exercise, with TODOs. `solution.py`: one way to solve it.
- `predict.py`, `one_port.py`, `only_open.py`: practice problems 1, 2 and 3 (`one_port.py` and `only_open.py` are one
  answer each: try them yourself first). They all check 127.0.0.1 only.

## Run it
```
python3 scanner.py      # Mac
python scanner.py       # Windows
```
Type `localhost` at `Host to scan:`. With the test server running, port 8000 says open. Your list might show other
ports open too, depending on what's running on your computer (in the video, 3306 is open because MySQL is running on
that Mac), and finding out what's listening on your own machine is what a scanner is for. Type any other host and it
refuses:
```
Host to scan: 192.168.1.1
Refusing to scan 192.168.1.1: localhost only.
Scanning without permission can be illegal.
```

## Your turn
Make `scan()` count the open ports: set `open_count = 0` before the loop, add 1 to it each time a port is open, and
after the loop print how many were open. `solution.py` does it; on the video's computer it printed
`2 of 7 ports are open` (yours depends on what's running on your computer).

## Practice
1. Predict, then run `predict.py` (no network needed: the numbers are the ones `connect_ex()` really gave back in the
   video):
   ```python
   results = {22: 61, 3306: 0, 8000: 0, 8080: 61}

   for port, code in results.items():
       print(port, code == 0, bool(code))
   ```
   It prints:
   ```
   22 False True
   3306 True False
   8000 True False
   8080 False True
   ```
   `code == 0` is True for the open ports, and `bool(code)` is the backwards answer from the first common mistake.
2. Write `one_port.py`: ask for a port number with `input()` and `int()` (lesson 05), check just that one port on
   `"127.0.0.1"`, and print whether it's open. With the test server running, `8000` gives `Port 8000 is open` and
   `8080` gives `Port 8080 is closed`.
3. Write `only_open.py`: check the same seven ports on 127.0.0.1 and print only the open ones, with their names, or
   `No open ports found` if none are. On the video's computer it printed `3306 (MySQL)` and `8000 (HTTP dev server)`.

Every file was run on Python 3.15.0 with the test server running on 127.0.0.1:8000.
