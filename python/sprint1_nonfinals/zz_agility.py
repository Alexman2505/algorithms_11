# 87757229
from typing import Tuple


class InputError(Exception):
    pass


def data_input() -> Tuple[int, str]:
    try:
        k = int(input())
    except ValueError:
        raise InputError(
            'Ошибка! Было введено не число. Введите число в диапазоне от 1 до 5\n'
        )
    if not 1 <= k <= 5:
        raise InputError('Ошибка! Число должно быть в диапазоне от 1 до 5\n')
    matrix = ''
    valid_chars = '123456789.'
    for _ in range(4):
        row = input()
        if len(row) != 4 or any(char not in valid_chars for char in row):
            raise InputError(
                'Ошибка! Каждая строка матрицы должна содержать 4 символа, '
                f'включая только {valid_chars}\n'
            )
        matrix += row
    return k, matrix


def calculations(
    k: int, matrix: str, valid_chars: str = '123456789.', players: int = 2
) -> int:
    return sum(
        0 < elem <= k * players
        for elem in [
            matrix.count(char) for char in valid_chars if char.isdigit()
        ]
    )


if __name__ == '__main__':
    try:
        k, matrix = data_input()
        print(calculations(k, matrix))
    except InputError as e:
        print(e)
