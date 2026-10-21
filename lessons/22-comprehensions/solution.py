# Your turn: a list of words (one way to solve it)
words = ["axe", "dragon", "map", "castle", "orb"]

long_words = [word for word in words if len(word) > 3]
shout = [word.upper() for word in long_words]

print(long_words)
print(shout)
