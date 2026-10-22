# Practice 3: the average of any number of scores
def average(*scores):
    if len(scores) == 0:
        return 0
    return sum(scores) / len(scores)


print(average(80, 90, 100))
print(average(75, 85))
print(average())
