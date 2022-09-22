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

        self.total_time = time() - start
        Decorator4.execution_dict[f'{self.func.__name__}_{self.trace_count}'] = self.total_time

        with open('decorator_output.txt', 'a') as f:
            with redirect_stdout(f):
                print(f'Function "{self.func.__name__}" was executed {self.trace_count} times in {self.total_time}')
                print(f'Name:\t{self.func.__name__} ')
                print(f'Type:\t{type(self.func)} ')
                print(f'Sign:\t{inspect.signature(self.func)} ')
                print(f'Args:\tpositional: {args}, keywords: {kwargs}')
                print(f'Doc:\n{inspect.getdoc(self.func)}')
                print(f'Source:\n{inspect.getsource(self.func)} ')
                print('Output:')
                try:
                    self.func(*args, **kwargs)
                except Exception as e:
                    logging.error(repr(e))
                print()


def decorator_4(func: Callable) -> Callable:
    """This is a Decorator function 4 using a function which executes the function "func"
    and then writes down the functions name, type, sign,
    Args, Doc, Source, Output
    :param func: It is a Function which is decorated with this decorator_4 function
    """
    trace_count = 0

    def wrapper(*args, **kwargs):
        nonlocal trace_count
        trace_count += 1
        start = time()

        total_time = time() - start
        global execution_dict
        execution_dict[f'{func.__name__}_{trace_count}'] = total_time

        with open('decorator_output.txt', 'a') as f:
            with redirect_stdout(f):
                print(f'Function "{func.__name__}" was executed {trace_count} times in {total_time}')
                print(f'Name:\t{func.__name__} ')
                print(f'Type:\t{type(func)} ')
                print(f'Sign:\t{inspect.signature(func)} ')
                print(f'Args:\tpositional: {args}, keywords: {kwargs}')
                print(f'Doc:\n{inspect.getdoc(func)}')
                print(f'Source:\n{inspect.getsource(func)} ')
                print('Output:')
                try:
                    func(*args, **kwargs)
                except Exception as e:
                    logging.error(repr(e))
                print()

    return wrapper
