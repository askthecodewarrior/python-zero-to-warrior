# Practice 1: predict it, then run it
def gold_drops(top):
    gold = 5
    while gold <= top:
        yield gold
        gold *= 2


drops = gold_drops(100)
print(next(drops))
print(list(drops))
