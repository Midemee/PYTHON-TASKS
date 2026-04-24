number = int(input("Enter a 3-digit number: "))

if number < 100 or number > 999:
    print("Invalid, please enter a valid 3-digit integer")

else:
	hundreds = number // 100
	tens = (number // 10) % 10
	units = number % 10

	sum = hundreds + tens + units

if sum == 0:
	print(number, "is divisible by the sum of its digits", sum)

else:
	print(number, "is not divisible by the sum of its digits", sum)

