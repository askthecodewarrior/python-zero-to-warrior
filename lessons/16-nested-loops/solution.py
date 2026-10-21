# Every floor gets 4 rooms, but skip room 3 on every floor
for floor in range(1, 4):
    for room in range(1, 5):
        if room == 3:
            continue
        print("Floor", floor, "room", room)
