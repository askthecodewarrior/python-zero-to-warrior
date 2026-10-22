# Catch the error instead of crashing
try:
    level = int(input("Level: "))
    print("The level after that is", level + 1)
except ValueError:
    print("That's not a whole number.")
print("The game keeps going.")
