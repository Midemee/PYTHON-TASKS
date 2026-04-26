import math
number_one = input("Enter first number: ")
number_two = input("Enter second number: ")

if math.abs(number_one) < math.abs(number_two):
    print(f"{number_one} is close to zero")

elif math.abs(number_one) > math.abs(number_two):
    print(f"{number_two} is close to zero")
else:
	print("Both numbers are close to zero")

