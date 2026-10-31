# Your turn: write a log_calls decorator
# TODO 1: write def log_calls(func): with an inner wrapper(*args, **kwargs)
#         that prints "Calling" and func.__name__,
#         then returns func(*args, **kwargs)
# TODO 2: return wrapper from log_calls (and use @functools.wraps(func) on it)
# TODO 3: put @log_calls on add_up in place of @timer
# Run it: python3 starter.py on a Mac, python starter.py on Windows.
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


@timer
def add_up(n):
    return sum(range(n))


print(add_up(10_000_000))
print(add_up.__name__)
