def get_longest_word(line: str) -> str:
    lst = line.split()
    word = str(lst[0])
    for i in range(len(lst)):
        if len(lst[i]) > len(word):
            word = str(lst[i])
    return word


def read_input() -> str:
    _ = input()
    line = input().strip()
    return line


def print_result(result: str) -> None:
    print(result)
    print(len(result))


print_result(get_longest_word(read_input()))
