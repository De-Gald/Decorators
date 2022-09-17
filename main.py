import numpy as np
import math

from tasks import *


@Decorator4
def print_pascal_triangle(n: int) -> None:
    """
    Calculating pascal triangle
    :param n: size of a pascal triangle
    """
    matrix = np.zeros((n, n + 1))
    matrix[0, 1] = 1
    for i in range(1, n):
        for j in range(1, i + 2):
            matrix[i, j] = matrix[i - 1, j] + matrix[i - 1, j - 1]
    pascal_triangle = list(map(lambda row: list(filter(lambda el: el != 0, row)), np.delete(matrix, 0, 1).astype(int)))

    [print(*row) for row in pascal_triangle]


@Decorator4
def solve_quadratic_equation(a: float, b: float, c: float) -> None:
    """
    Solving quadratic equation ax^2 + bx + c given a, b, c params
    :param a: coefficient before x^2
    :param b: coefficient before x
    :param c: free coefficient
    """
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        print(f"Equation  {a}x^2 + {b}x + {c} doesn't have real solutions!!!")
        return

    sqrt_of_discriminant = math.sqrt(discriminant)

    print(f'Solutions of the {a}x^2 + {b}x + {c} are: ', list(map(
        lambda sqrt_of_discriminant_with_sign: (-b + sqrt_of_discriminant_with_sign) / (2 * a),
        [sqrt_of_discriminant, -sqrt_of_discriminant]
    )))


if __name__ == '__main__':
    print_pascal_triangle(3)
    solve_quadratic_equation(1, 5, 4)
    print_pascal_triangle(5)
    solve_quadratic_equation('', 4, 5)

    ranking = sorted(Decorator4.execution_dict.items(), key=lambda el: el[1])
    print(f'\n{"PROGRAM":27s} | RANK |  TIME ELAPSED')
    for idx, (name, time) in enumerate(ranking):
        print(f'{name:31s} {str(idx + 1):5s} {time}')
