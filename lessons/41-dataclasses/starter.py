# Your turn: give Score a badges list
# TODO 1: on line 2, import field too
# TODO 2: under name, add a badges field (type list)
#         with a default of field(default_factory=list)
# TODO 3: at the bottom, add "speedrun" to ivy's badges,
#         then print ivy and print nova
# Run it: python3 starter.py on a Mac, python starter.py on Windows.
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
