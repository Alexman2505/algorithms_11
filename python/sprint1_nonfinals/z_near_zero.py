# 87704141
from typing import List, Tuple


class InputError(Exception):
    pass


class LengthMismatchError(Exception):
    pass


class ZeroNotFoundError(Exception):
    pass


def get_distance(n: int, numbers: List[int]) -> int:
    distance = n
    for i in numbers:
        if i == 0:
            distance = 0
        else:
            distance += 1
        yield distance


def read_input() -> Tuple[int, List[int]]:
    n = int(input())
    if not 1 <= n <= 10**6:
        raise InputError(
            'Ошибка! Значение n должно быть в диапазоне от 1 до 10^6'
        )
    numbers = list(map(int, input().strip().split()))
    if len(numbers) != n:
        raise LengthMismatchError(
            'Ошибка! Длина списка не соответствует введенному ранее числу'
        )
    if 0 not in numbers:
        raise ZeroNotFoundError('Ошибка! Нет нуля в введенном списке')
    return n, numbers


if __name__ == '__main__':
    n, numbers = read_input()
    left_distance = get_distance(n, numbers)
    right_distance = reversed(tuple(get_distance(n, reversed(numbers))))
    print(*map(min, zip(left_distance, right_distance)))
