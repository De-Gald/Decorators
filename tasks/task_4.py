import logging
from contextlib import redirect_stdout
from time import time
from typing import Callable
import inspect

logging.basicConfig(
    format="%(asctime)s %(message)s",
    handlers=[logging.FileHandler("task_1.logs")]
)

execution_dict = {}


class Decorator4:
    execution_dict = {}

    def __init__(self, func: Callable) -> None:
        self.func = func
        self.trace_count = 0

    def __call__(self, *args, **kwargs) -> None:
        self.trace_count += 1
        start = time()

        try:
            self.func(*args, **kwargs)
        except Exception as e:
            logging.error(repr(e))

        self.total_time = time() - start
        Decorator4.execution_dict[f'{self.func.__name__}_{self.trace_count}'] = self.total_time

        with open('decorator_output.txt', 'a') as f:
            with redirect_stdout(f):
                print(f'Function "{self.func.__name__}" was executed {self.trace_count} times in {self.total_time}')
                print(f'Source code of the function "{self.func.__name__}":\n{inspect.getsource(self.func)}')


def decorator_4(func: Callable) -> Callable:
    trace_count = 0

    def wrapper(*args, **kwargs):
        nonlocal trace_count
        trace_count += 1
        start = time()

        try:
            func(*args, **kwargs)
        except Exception as e:
            logging.error(repr(e))

        total_time = time() - start
        global execution_dict
        execution_dict[f'{func.__name__}_{trace_count}'] = total_time

        with open('decorator_output.txt', 'a') as f:
            with redirect_stdout(f):
                print(f'Function "{func.__name__}" was executed {trace_count} times in {total_time}')
                print(f'Source code of the function "{func.__name__}":\n{inspect.getsource(func)}')

    return wrapper
