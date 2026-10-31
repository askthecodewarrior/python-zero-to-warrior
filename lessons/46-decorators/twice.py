# Practice 1: predict, then run
def twice(func):
    def wrapper():
        func()
        func()
    return wrapper


@twice
def cheer():
    print("Huzzah!")


cheer()
print(cheer.__name__)
