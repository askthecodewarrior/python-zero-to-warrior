# Practice 3: a list of scores in a JSON file (one answer)
import json

try:
    with open("scores.json") as f:
        scores = json.load(f)
except FileNotFoundError:
    scores = []

score = int(input("Your score: "))
scores.append(score)
print("Scores so far:", scores)
print("Games played:", len(scores))

with open("scores.json", "w") as f:
    json.dump(scores, f)
