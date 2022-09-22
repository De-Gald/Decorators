from time import time
from typing import Callable


def decorator_1(func: Callable) -> Callable:
    """Measures the execution time of a function
    :param func: Arbitrary Function"""
    trace_count = 0

    def wrapper(*args, **kwargs) -> None:
        nonlocal trace_count
        trace_count += 1

        start = time()
        func(*args, **kwargs)

        print(f'Function "{func.__name__}" was executed {trace_count} times in {time() - start}')

    return wrapper
