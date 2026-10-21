# Practice 2: the squares of 1 to 10, and only the even ones
squares = [n ** 2 for n in range(1, 11)]
even_squares = [s for s in squares if s % 2 == 0]

print(squares)
print(even_squares)
