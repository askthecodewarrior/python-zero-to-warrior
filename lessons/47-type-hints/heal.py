# Practice 1: hints on a function that heals a player
def heal(health: int, potion: int, cap: int) -> int:
    return min(health + potion, cap)


print(heal(70, 20, 100))
print(heal(95, 20, 100))
