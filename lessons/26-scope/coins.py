# Assigning in a function makes a new local
coins = 100


def spend():
    coins = 40
    print("Inside:", coins)


spend()
print("Outside:", coins)
