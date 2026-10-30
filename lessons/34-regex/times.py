# Pull the hour and the minutes out of a time
import re

note = "Raid starts at 7:45 PM"
match = re.search(r"(\d+):(\d+)", note)
if match:
    print("Hour:", match.group(1))
    print("Minutes:", match.group(2))
    print("Minutes + 15:", int(match.group(2)) + 15)
