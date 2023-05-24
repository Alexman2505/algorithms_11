def check_parity(a: int, b: int, c: int) -> bool:
    if not a and not b and not c:
        return True
    if a and b and c:
        if (a % 2 and b % 2 and c % 2) or (
            not a % 2 and not b % 2 and not c % 2
        ):
            return True
        return False
    if a and b:
        if (a % 2 and b % 2) or (not a % 2 and not b % 2):
            return True
        return False
    if b and c:
        if (b % 2 and c % 2) or (not b % 2 and not c % 2):
            return True
        return False
    if a and c:
        if (a % 2 and c % 2) or (not a % 2 and not c % 2):
            return True
        return False


def print_result(result: bool) -> None:
    if result:
        print("WIN")
    else:
        print("FAIL")


a, b, c = map(int, input().strip().split())
print_result(check_parity(a, b, c))
