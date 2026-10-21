# Practice 3: the same discount, as a loop and as a comprehension
prices = [40, 15, 120, 8]

sale = []
for price in prices:
    if price >= 20:
        sale.append(price // 2)
print(sale)

sale = [price // 2 for price in prices if price >= 20]
print(sale)
