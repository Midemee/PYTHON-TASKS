def maximum(number_one, number_two, number_three):
    largest = number_one
    if number_two > number_one:
        largest = number_two
    if number_three > number_two:
        largest = number_three
    return largest

print(maximum(29, 55, 32))

