# Your turn: a dictionary of your own (one way to solve it)
pet = {"name": "Biscuit", "age": 3, "food": "carrots"}
pet["age"] = 4
pet["toy"] = "ball"

for key, value in pet.items():
    print(f"{key}: {value}")
