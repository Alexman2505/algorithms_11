from typing import Tuple


def get_excessive_letter(shorter: str, longer: str) -> str:
    shorter = sorted(shorter)
    longer = sorted(longer)
    try:
        for i in range(len(longer)):
            if shorter[i] != longer[i]:
                return longer[i]
    except IndexError:
        return longer[-1]


def read_input() -> Tuple[str, str]:
    shorter = input().strip()
    longer = input().strip()
    return shorter, longer


shorter, longer = read_input()
print(get_excessive_letter(shorter, longer))
