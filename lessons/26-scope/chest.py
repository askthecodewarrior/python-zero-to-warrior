# Global and local names
gold = 100


def open_chest():
    gems = 5
    print("Inside:", gold, gems)


open_chest()
print("Outside:", gold, gems)
