import csv

total = 0
with open("players.csv", newline="") as f:
    for row in csv.DictReader(f):
        print(row)
        total = total + int(row["score"])
print("Total:", total)
