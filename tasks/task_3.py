import contextlib
import io
from contextlib import redirect_stdout
from time import time
from typing import Callable
import inspect


class Decorator3:
    """This is a decorator class which will show the execution time of the
    functions which are decorated by this class and rank the functions
    based on the execution time and also dumps the output of each function
    to decorator_output.txt file"""
    execution_dict = {}

    def __init__(self, func: Callable) -> None:
        self.func = func
        self.trace_count = 0

    def __call__(self, *args, **kwargs) -> None:
        self.trace_count += 1
        start = time()

        self.f = io.StringIO()
        with contextlib.redirect_stdout(self.f):
            self.func(*args, **kwargs)

        self.total_time = time() - start
        Decorator3.execution_dict[f'{self.func.__name__}_{self.trace_count}'] = self.total_time

        with open('decorator_output.txt', 'a') as f:
            with redirect_stdout(f):
                print(f'Function "{self.func.__name__}" was executed {self.trace_count} times in {self.total_time}')
                print(f'Name:\t{self.func.__name__} ')
                print(f'Type:\t{type(self.func)} ')
                print(f'Sign:\t{inspect.signature(self.func)} ')
                print(f'Args:\tpositional: {args}, keywords: {kwargs}')
                print(f'Doc:\n{inspect.getdoc(self.func)}')
                print(f'Source:\n{inspect.getsource(self.func)} ')
                print(f'Output:\n{self.f.getvalue()}')
