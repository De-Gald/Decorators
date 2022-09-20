import contextlib
import io
from time import time
from typing import Callable
import inspect


def decorator_2(func: Callable) -> Callable:
    trace_count = 0

    def wrapper(*args, **kwargs) -> None:
        nonlocal trace_count
        trace_count += 1
        start = time()

        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            func(*args, **kwargs)

        print(f'Function "{func.__name__}" was executed {trace_count} times in {time() - start}')
        print(f'Name:\t{func.__name__} ')
        print(f'Type:\t{type(func)} ')
        print(f'Sign:\t{inspect.signature(func)} ')
        print(f'Args:\tpositional: {args}, keywords: {kwargs}')
        print(f'Doc:\n{inspect.getdoc(func)}')
        print(f'Source:\n{inspect.getsource(func)} ')
        print(f'Output:\n{f.getvalue()}')

    return wrapper
