# Your turn: two lists of your own (one way to solve it)
names = ["Ana", "Ben", "Cy"]
scores = [90, 75, 82]

for n, name in enumerate(names, start=1):
    print(f"{n}. {name}")

for name, score in zip(names, scores):
    print(name, "scored", score)
