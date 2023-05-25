def get_distance(n: int, numbers: list[int]) -> int:
    distance = n
    for i in numbers:
        if i == 0:
            distance = 0
        else:
            distance += 1
        yield distance


def read_input() -> tuple[int, list[int]]:
    n = int(input())
    numbers = list(map(int, input().strip().split()))
    return n, numbers


if __name__ == '__main__':
    try:
        n, numbers = read_input()
        left_distance = get_distance(n, numbers)
        right_distance = reversed(tuple(get_distance(n, reversed(numbers))))
        print(*map(min, zip(left_distance, right_distance)))
    except ValueError:
        print('Ошибка, потому что были введены не числа')
# тут не хватает нескольких проверок
