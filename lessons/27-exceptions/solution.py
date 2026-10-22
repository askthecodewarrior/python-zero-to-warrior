# Your turn: a second check (one way to solve it)
while True:
    try:
        age = int(input("Age: "))
        if age < 0:
            raise ValueError("age can't be negative")
        if age > 150:
            raise ValueError("age can't be over 150")
        break
    except ValueError as e:
        print("Try again:", e)

print("Your age is", age)
