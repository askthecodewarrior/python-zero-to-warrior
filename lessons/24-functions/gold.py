# print shows a value, return hands it back
def show_total(gold, loot):
    print(gold + loot)


def get_total(gold, loot):
    return gold + loot


a = show_total(50, 25)
b = get_total(50, 25)
print("a is", a)
print("b is", b)
print(get_total(b, 10) * 2)
