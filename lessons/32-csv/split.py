with open("players.csv") as f:
    for line in f:
        print(line.strip().split(","))
