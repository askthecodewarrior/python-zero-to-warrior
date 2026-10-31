# A high score on the leaderboard
from dataclasses import dataclass


@dataclass(order=True)
class Score:
    points: int
    name: str


nova = Score(120, "Nova")
rex = Score(95, "Rex")
ivy = Score(150, "Ivy")
print(nova)
print(nova == Score(120, "Nova"))

for score in sorted([nova, rex, ivy]):
    print(score.points, score.name)
