from typing import List


def factorize(number: int) -> List[int]:
    lst = []
    d = 2
    while d * d <= number:
        if number % d == 0:
            lst.append(d)
            number = number // d
        else:
            d += 1
    if number > 1:
        lst.append(number)
    return lst


result = factorize(int(input()))
print(" ".join(map(str, result)))
