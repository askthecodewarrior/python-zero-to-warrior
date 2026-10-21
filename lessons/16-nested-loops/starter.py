# Your turn: every floor gets 4 rooms, but skip room 3 on every floor
# This is floors.py from the video. Change it:
# TODO 1: make the inner loop go through rooms 1 to 4.
#         (range stops BEFORE its stop number.)
# TODO 2: inside the inner loop, before the print, skip room 3
#         with an if and continue.
# Run it: you should get 9 lines, and no room 3 on any floor.
for floor in range(1, 4):
    for room in range(1, 3):
        print("Floor", floor, "room", room)
