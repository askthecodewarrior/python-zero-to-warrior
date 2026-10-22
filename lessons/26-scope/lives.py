# Practice 2: lose_life returns the new count, so no global is needed
lives = 3


def lose_life(lives):
    return lives - 1


lives = lose_life(lives)
print(lives)
