number_one = float(input("Enter first numerator: "))
denominator_one = float(input("Enter first denominator: "))
number_two + float(input("Enter second numerator: "))
denominator_two = float(input("Enter second denominator : "))

resultOne = numOne/DenOne
resultTwo = numTwo/DenTwo

add = resultOne + resultTwo
subtract = resultOne - resultTwo
product = resultOne * resultTwo

print(f"Sum: {add:.2f}\nDifference: {subtract:.2f}\nProduct: {product:.2f}\n")

if resultOne == 0:
    print("Quotient is not divisible by zero")

else:
	quotient = resultOne / resultTwo
	print(f"Quotient: {quotient:.2f}")

