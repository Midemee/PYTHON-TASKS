number_one = input("Enter a first integer: ")
number_two = input("Enter a second integer: ")

if numOne <= 0 or numTwo <= 0:
	print("Enter positive numbers only")

elif numTwo % numOne == 0:
	print(f"{number_one} is a factor of {number_two}")

else:
	print(f"{number_one} is not a factor of {number_two}")

