# Practice 2: the players at level 4 or higher
import csv

with open("players.csv", newline="") as f:
    for row in csv.DictReader(f):
        if int(row["level"]) >= 4:
            print(row["name"], "is level", row["level"])
