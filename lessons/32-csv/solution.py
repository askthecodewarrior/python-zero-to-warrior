# Practice 1: the average score (one way to solve it)
import csv

total = 0
count = 0
with open("players.csv", newline="") as f:
    for row in csv.DictReader(f):
        total = total + int(row["score"])
        count = count + 1
print("Average:", total / count)
