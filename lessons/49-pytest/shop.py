# A potion shop: 100 gold or more gets 10 gold off
def total_cost(price, count):
    if count < 1:
        raise ValueError("count must be at least 1")
    cost = price * count
    if cost >= 100:
        cost -= 10
    return cost
