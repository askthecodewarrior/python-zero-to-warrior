# Text from a file or input() comes in as strings
prices = ["40", "75", "120"]
numbers = list(map(int, prices))
print(numbers)
print(sum(numbers))
print([int(p) for p in prices])
