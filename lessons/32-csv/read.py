import csv

with open("players.csv", newline="") as f:
    reader = csv.reader(f)
    header = next(reader)
    print("Columns:", header)
    for row in reader:
        print(row)
