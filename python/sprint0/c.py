from typing import List, Tuple


def moving_average(timeseries: List[int], K: int) -> List[float]:
    result = []  # Пустой массив.
    # Первый раз вычисляем значение честно и сохраняем результат.
    current_sum = sum(timeseries[0:K])
    result.append(current_sum / K)
    for i in range(len(timeseries) - K):
        current_sum -= timeseries[i]
        current_sum += timeseries[i + K]
        current_avg = current_sum / K
        result.append(current_avg)
    return result


def read_input() -> Tuple[List[int], int]:
    n = int(input())
    timeseries = list(map(int, input().strip().split()))
    K = int(input())
    return timeseries, K


timeseries, K = read_input()
print(" ".join(map(str, moving_average(timeseries, K))))
