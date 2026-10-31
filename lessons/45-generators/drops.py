# A generator pauses at every yield
def gold_drops(top):
    gold = 5
    while gold <= top:
        yield gold
        gold *= 2


drops = gold_drops(40)
print(next(drops))
print(next(drops))
for coins in drops:
    print("Loot:", coins)
