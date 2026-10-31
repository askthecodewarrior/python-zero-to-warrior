# Your turn: a triple generator (one way to do it)
def triple(top):
    n = 1
    while n <= top:
        yield n
        n *= 3


for n in triple(100):
    print(n)
