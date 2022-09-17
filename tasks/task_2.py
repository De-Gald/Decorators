from time import time
from typing import Callable
import inspect


def decorator_2(func: Callable) -> Callable:
    trace_count = 0

    def wrapper(*args, **kwargs) -> None:
        nonlocal trace_count
        trace_count += 1

        start = time()
        func(*args, **kwargs)

        print(f'Function "{func.__name__}" was executed {trace_count} times in {time() - start}')
        print(f'Source code of the function "{func.__name__}":\n{inspect.getsource(func)}')

    return wrapper
