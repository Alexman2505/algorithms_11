def is_palindrome(line: str) -> bool:
    word = "".join(char for char in line if char.isalpha()).lower()
    return word == word[::-1]


print(is_palindrome(input().strip()))
