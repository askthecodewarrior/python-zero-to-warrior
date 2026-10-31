# Your turn, one answer: a log_calls decorator on add_up
import functools
import time


def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        seconds = time.perf_counter() - start
        print(f"{func.__name__}: {seconds:.2f} seconds")
        return result
    return wrapper


def log_calls(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Calling", func.__name__)
        return func(*args, **kwargs)
    return wrapper


@log_calls
def add_up(n):
    return sum(range(n))


print(add_up(10_000_000))
print(add_up.__name__)
