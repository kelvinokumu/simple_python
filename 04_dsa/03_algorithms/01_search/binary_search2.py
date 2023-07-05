def binary_search(values, target):
    range_start = 0
    range_end = len(values) - 1
    while range_start < range_end:
        range_middle = (range_end + range_start) // 2
        value = values[range_middle]
        if value == target:
            return range_middle
        elif value < target:
            range_start = range_middle + 1
        else:
            range_end = range_middle - 1
    # Add your code here
    if values[range_start] != target:  # Instruction 2
        return -1  # Instruction 3
    return range_start


values = [1, 2, 4, 5, 8, 10, 13, 15, 17, 20, 23, 24, 25, 26, 30, 31, 32, 36, 37, 38, 41, 42, 43, 44, 45, 47, 50, 52, 54,
          55, 56, 57, 58, 59, 61, 62, 64, 66, 67, 69, 70, 73, 75, 76, 77, 78, 79, 80, 82, 83, 84, 85, 86, 87, 90, 91,
          92, 94, 95, 96, 97, 98, 99, 100]

print(binary_search(values, 1))
