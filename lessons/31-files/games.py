# Practice 2: count the games you've played
with open("games.txt", "a") as f:
    f.write("Game played\n")

with open("games.txt") as f:
    lines = f.readlines()

print("Games played:", len(lines))
