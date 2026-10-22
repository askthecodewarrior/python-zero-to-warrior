# Practice 1: why is everything on one line?
with open("log.txt", "w") as f:
    f.write("Level 1 cleared")
    f.write("Level 2 cleared")

with open("log.txt") as f:
    print(f.read())
