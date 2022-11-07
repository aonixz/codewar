def sum_two_smallest_numbers(numbers):
    numbers.sort(reverse=True)
    low1 = numbers.pop()
    low2 = numbers.pop()
    return low1 + low2