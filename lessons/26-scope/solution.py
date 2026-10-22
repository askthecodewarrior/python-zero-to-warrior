# Return the new score instead of using global
score = 0


def add_point(score):
    return score + 1


score = add_point(score)
score = add_point(score)
print("Score:", score)
