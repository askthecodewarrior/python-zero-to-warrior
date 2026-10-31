# Your turn, one way to do it: a badges list for every Score
from dataclasses import dataclass, field


@dataclass(order=True)
class Score:
    points: int
    name: str
    badges: list = field(default_factory=list)


nova = Score(120, "Nova")
rex = Score(95, "Rex")
ivy = Score(150, "Ivy")
print(nova)
print(nova == Score(120, "Nova"))

for score in sorted([nova, rex, ivy]):
    print(score.points, score.name)

ivy.badges.append("speedrun")
print(ivy)
print(nova)
