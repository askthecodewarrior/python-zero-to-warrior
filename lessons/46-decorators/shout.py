# Practice 2, one answer: a decorator that hands back the result in capitals
import functools


def shout(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper


@shout
def greet(name):
    return f"hello, {name}"


print(greet("Ana"))
print(greet(name="Kai"))
