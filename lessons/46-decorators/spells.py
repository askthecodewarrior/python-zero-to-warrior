# A decorator wraps a function in another one
def announce(func):
    def wrapper():
        print("Casting...")
        func()
        print("Done!")
    return wrapper


def fireball():
    print("Fireball!")


fireball = announce(fireball)
fireball()
print(fireball.__name__)


@announce
def heal():
    print("Healing!")


heal()
print(heal.__name__)
