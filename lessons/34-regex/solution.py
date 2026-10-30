# Your turn: dates with dashes (one way to solve it)
import re

note = "Boss fight on 10-31-2026 at 8 PM"
match = re.search(r"(\d+)-(\d+)-(\d+)", note)
if match:
    print("Month:", match.group(1))
    print("Day:", match.group(2))
    print("Year:", match.group(3))
