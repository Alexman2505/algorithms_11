# 87704819
from typing import Tuple


class InputError(Exception):
    pass


def data_input() -> Tuple[int, str]:
    k = int(input())
    if not 1 <= k <= 5:
        raise InputError(
            'Ошибка! Значение k должно быть в диапазоне от 1 до 5.'
        )
    k *= 2
    matrix = ''
    valid_chars = set('123456789.')  # Допустимые символы
    for _ in range(4):
        row = input()
        if len(row) != 4 or any(char not in valid_chars for char in row):
            raise InputError(
                'Ошибка! Каждая строка матрицы должна содержать 4 символа, '
                'включая только числа от 1 до 9 или точки ".".'
            )
        matrix += row
    return k, matrix


def calculations() -> int:
    k, matrix = data_input()
    numbers = []
    scores: int = 0
    for i in range(1, 10):
        count = matrix.count(str(i))
        numbers.append(count)
    for elem in numbers:
        if elem == 0:
            continue
        if elem <= k:
            scores += 1
    return scores


if __name__ == '__main__':
    result = calculations()
    print(result)
