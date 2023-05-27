# 87747234
from typing import Generator, List, Tuple


class InputError(Exception):
    pass


def get_distance(n: int, numbers: List[int]) -> Generator[int, None, None]:
    distance = n
    for i in numbers:
        if i == 0:
            distance = 0
        else:
            distance += 1
        yield distance


def read_input() -> Tuple[int, List[int]]:
    try:
        n = int(input())
    except ValueError:
        raise InputError(
            'Ошибка! Было введено не число. Введите число в диапазоне от 1 до 10^6\n'
        )
    if not 1 <= n <= 10**6:
        raise InputError(
            'Ошибка! Число должно быть в диапазоне от 1 до 10^6\n'
        )
    numbers = input().strip().split()
    if len(numbers) != n:
        raise InputError(
            'Ошибка! Количество введенных символов [длина списка] не '
            'соответствует введенному ранее числу\n'
        )
    try:
        numbers = list(map(int, numbers))
    except ValueError:
        raise InputError('Ошибка! Вы ввели недопустимые символы [не числа]\n')
    if not any(number == 0 for number in numbers):
        raise InputError('Ошибка! Вы забыли ввести ноль\n')
    if any(number < 0 for number in numbers if number != 0):
        raise InputError('Ошибка! В списке присутствуют отрицательные числа\n')
    return n, numbers


if __name__ == '__main__':
    try:
        n, numbers = read_input()
        left_distance = get_distance(n, numbers)
        right_distance = reversed(tuple(get_distance(n, reversed(numbers))))
        print(*map(min, zip(left_distance, right_distance)))
    except InputError as e:
        print(e)
