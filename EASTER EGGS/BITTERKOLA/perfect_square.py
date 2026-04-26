import math
number = input("Enter positive integer: ")

if number < 0:
    print("Please Enter positive integer")
else:
    squareRoot = math.sqrt(number)

if squareRoot * squareRoot == number:
	print("It is a perfect square")

else:
	print("It is not a perfect square")

