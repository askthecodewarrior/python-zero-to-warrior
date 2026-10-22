# Read the high scores
with open("scores.txt", "r") as f:
    for line in f:
        print(line.strip())
