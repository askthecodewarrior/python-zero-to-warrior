# Keep asking until the age is valid
while True:
    try:
        age = int(input("Age: "))
        if age < 0:
            raise ValueError("age can't be negative")
        break
    except ValueError as e:
        print("Try again:", e)

print("Your age is", age)
