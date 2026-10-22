# Any number of arguments, packed in a tuple
def total(*args):
    print(args)
    return sum(args)


print(total(10, 25, 5))
print(total())
