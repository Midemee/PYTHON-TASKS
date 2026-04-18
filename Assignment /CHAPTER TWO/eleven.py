number = int (input('Enter a five digit number: '))

digit_one = number // 10000

digit_two = (number // 1000) % 10

digit_three = (number // 100) % 10

digit_four = (number // 10) % 10

digit_five = number % 10

print(digit_one,"\t", digit_two, "\t",  digit_three,"\t",  digit_four, "\t",   digit_five)

