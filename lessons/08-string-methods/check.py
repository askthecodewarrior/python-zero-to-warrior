# Check what the player typed
level = input("Level: ")
print(level.isdigit())
level = level.strip()
print(level.isdigit())
print(int(level) + 1)
