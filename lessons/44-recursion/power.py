# power(base, exp): base times itself, exp times
def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)


print(power(2, 10))
print(power(3, 4))
