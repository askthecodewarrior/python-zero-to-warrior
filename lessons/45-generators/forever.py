# Practice 3: one answer (try it yourself first)
def levels():
    level = 1
    while True:
        yield level
        level += 1


climb = levels()
print(next(climb))
print(next(climb))
print(next(climb))
