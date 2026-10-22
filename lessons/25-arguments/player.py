# Any number of keyword arguments, in a dictionary
def show_player(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(f"{key}: {value}")


show_player(name="Ana", level=3, gold=50)
