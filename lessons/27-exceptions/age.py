def check_age(age):
    if age < 0:
        raise ValueError("age can't be negative")
    return age


check_age(-5)
