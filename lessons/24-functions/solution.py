# Your turn: a function that returns (one way to solve it)
def total_cost(price, items):
    return price * items


cost = total_cost(12, 3)
print("Total:", cost)
print("Two orders:", total_cost(12, 3) + total_cost(5, 4))
