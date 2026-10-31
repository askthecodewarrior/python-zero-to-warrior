# sum_digits(n): add up the digits of a whole number
def sum_digits(n):
    if n < 10:
        return n
    return n % 10 + sum_digits(n // 10)


print(sum_digits(2026))
print(sum_digits(7))
