"""apple = balls;
balls = apple.

This bug is a syntax error in declaring a variable"""

number_one = 5
number_two = 10

temp = number_one
number_one = number_two
number_two = temp

"""number_one, number_two = number_two, number_one"""

print(number_one, ",", number_two)


