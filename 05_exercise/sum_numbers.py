def sum_n(*numbers):
    total = 0
    for number in numbers:
        total += number

    return total


print(sum_n(90, 80, 70, 60, 50))
