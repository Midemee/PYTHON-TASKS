number_one = input("Enter first integer: ")
number_two = input("Enter second integer: ")
number_three = input("Enter third integer: ")

highest = 0
lowest = 0

if number_one > number_two and number_one > number_three:
    highest = number_one

elif number_two > number_one and number_two > number_three: 
    highest = number_two

elif number_three > number_two and num_three > number_two:
    highest = number_three

elif number_one < number_two and number_one < number_three:
	lowest = number_one

elif number_two < number_one and number_two < number_three:
	highest = number_two

elif number_three < number_one and number_three < number_two:
    lowest = number_three

print("Highest : ", highest, "Lowest : ", lowest)

