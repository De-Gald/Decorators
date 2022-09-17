from contextlib import redirect_stdout
from time import time
from typing import Callable
import inspect


class Decorator3:
    execution_dict = {}

    def __init__(self, func: Callable) -> None:
        self.func = func
        self.trace_count = 0

    def __call__(self, *args, **kwargs) -> None:
        self.trace_count += 1

        start = time()
        self.func(*args, **kwargs)
        self.total_time = time() - start

        Decorator3.execution_dict[f'{self.func.__name__}_{self.trace_count}'] = self.total_time

        with open('decorator_output.txt', 'a') as f:
            with redirect_stdout(f):
                print(f'Function "{self.func.__name__}" was executed {self.trace_count} times in {self.total_time}')
                print(f'Source code of the function "{self.func.__name__}":\n{inspect.getsource(self.func)}')
