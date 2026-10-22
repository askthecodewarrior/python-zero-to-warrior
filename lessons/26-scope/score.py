# The global keyword
score = 0


def add_point():
    global score
    score += 1


add_point()
add_point()
print("Score:", score)
