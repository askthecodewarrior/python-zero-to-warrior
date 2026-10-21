# Search the rooms, skip the trap
for room in range(1, 6):
    if room == 3:
        continue
    print("Searching room", room)

print("Done searching")
