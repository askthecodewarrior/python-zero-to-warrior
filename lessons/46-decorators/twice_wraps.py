# Practice 3, one answer: twice with functools.wraps, so cheer keeps its name
import functools


def twice(func):
    @functools.wraps(func)
    def wrapper():
        func()
        func()
    return wrapper


@twice
def cheer():
    print("Huzzah!")


cheer()
print(cheer.__name__)
