# Your turn: your own keyword arguments (one way to solve it)
def show_player(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(f"{key}: {value}")


show_player(name="Rex", level=7, weapon="bow")
