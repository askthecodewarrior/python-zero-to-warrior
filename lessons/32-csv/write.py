import csv

rows = [["Warrior", 130], ["Ana", 110], ["Bo, Jr.", 90]]
with open("results.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "score"])
    writer.writerows(rows)
