def make_powered_list(numbers):
    def make_power(number): return numbers ** 2

    return map(make_power, numbers)

    new_numbers = []
    for number in numbers:
        new_numbers.append(number ** 2)
    return new_numbers
