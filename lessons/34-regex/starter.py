# Your turn: dates with dashes
# TODO 1: change the date in the note to 10-31-2026
# TODO 2: change both / in the pattern to - so it still finds the date
# Run it: python3 starter.py on a Mac, python starter.py on Windows.
import re

note = "Boss fight on 10/31/2026 at 8 PM"
match = re.search(r"(\d+)/(\d+)/(\d+)", note)
if match:
    print("Month:", match.group(1))
    print("Day:", match.group(2))
    print("Year:", match.group(3))
