# Practice 3: a price list from two lists, and a safe lookup
shop = ["sword", "shield", "potion"]
prices = [50, 30, 10]
price_of = dict(zip(shop, prices))

item = input("What do you want to buy? ")
print(item, "costs", price_of.get(item, "nothing, we don't sell it"))
