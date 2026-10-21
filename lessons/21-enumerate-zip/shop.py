# A shop's items, numbered and priced
shop = ["sword", "shield", "potion", "rope"]
for i, item in enumerate(shop):
    print(i, item)

for n, item in enumerate(shop, start=1):
    print(f"{n}. {item}")

prices = [50, 30, 10]
for item, price in zip(shop, prices):
    print(item, "costs", price)

print(dict(zip(shop, prices)))
