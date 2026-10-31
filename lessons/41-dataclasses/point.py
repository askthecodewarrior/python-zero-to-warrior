from dataclasses import dataclass, FrozenInstanceError


@dataclass(frozen=True)
class Point:
    x: int
    y: int


home = Point(3, 4)
try:
    home.x = 10
except FrozenInstanceError as e:
    print("Can't move it:", e)
print(home)
