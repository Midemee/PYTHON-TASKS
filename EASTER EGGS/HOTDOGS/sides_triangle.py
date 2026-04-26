sideA = input("Enter one side of a triangle: ")
sideB = input("Enter second side of a triangle: ")
sideC = input("Enter third side ofa triangle: ")

if sideA + sideB > sideC && sideA + sideC > sideB && sideB + sideC > sideA:
    print("It's a valid triangle")
elif sideA == sideB  && sideB == sideC:
	print("It is an equilatorial triangle")
elif sideA == sideB && sideA == sideC || sideB == sideC:
	print("It is an isosceles triangle")
else:
	print("It's a scalene triangle")

