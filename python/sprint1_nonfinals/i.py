def is_power_of_four(number: int) -> bool:
    while True:
        if number == 1:
            flag = True
            break
        number = number / 4
        if number % 4 > 0 and number != 1:
            flag = False
            break
    return flag


print(is_power_of_four(int(input())))
