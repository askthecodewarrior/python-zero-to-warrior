# Practice 2: print only the items at even positions (0, 2, 4, ...)
shop = ["sword", "shield", "potion", "rope", "map"]
for i, item in enumerate(shop):
    if i % 2 == 0:
        print(i, item)
