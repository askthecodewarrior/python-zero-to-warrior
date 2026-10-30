# Practice 1: the average score
import csv

total = 0
count = 0
with open("players.csv", newline="") as f:
    for row in csv.DictReader(f):
        # TODO 1: add this row's score to total (it's a string: use int())
        # TODO 2: add 1 to count
        pass
# TODO 3: print "Average:" and total divided by count
# Run it: python3 starter.py on a Mac, python starter.py on Windows.
