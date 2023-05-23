from typing import List, Tuple


def zipper(a: List[int], b: List[int]) -> List[int]:
    c = []
    while a:
        c.append(a[0])
        a.pop(0)
        c.append(b[0])
        b.pop(0)
    return c


def read_input() -> Tuple[List[int], List[int]]:
    n = int(input())
    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))
    return a, b


a, b = read_input()
print(" ".join(map(str, zipper(a, b))))
