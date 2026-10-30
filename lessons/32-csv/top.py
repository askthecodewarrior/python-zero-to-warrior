# Practice 3: save the players who scored 100 or more to top.csv
import csv

top = []
with open("players.csv", newline="") as f:
    for row in csv.DictReader(f):
        if int(row["score"]) >= 100:
            top.append([row["name"], row["score"]])

with open("top.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "score"])
    writer.writerows(top)
