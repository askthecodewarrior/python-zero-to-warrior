# Practice 3: raise your own error, then catch it
def check_level(level):
    if level < 1 or level > 10:
        raise ValueError("level must be 1 to 10")
    return level


try:
    print(check_level(4))
    print(check_level(12))
except ValueError as e:
    print("Error:", e)
