def to_binary(number: int) -> str:
    if number != 0:
        two = ''
        while number > 0:
            two = str(number % 2) + two
            number = number // 2
        return two
    return 0


def read_input() -> int:
    return int(input().strip())


print(to_binary(read_input()))
