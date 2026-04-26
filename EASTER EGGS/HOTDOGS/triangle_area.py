import math

x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))
x3 = float(input("Enter x3: "))
y3 = float(input("Enter y3: "))

side1 = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
side2 = math.sqrt(math.pow(x3 - x2, 2) + math.pow(y3 - y2, 2))
side3 = math.sqrt(math.pow(x3 - x1, 2) + math.pow(y3 - y1, 2))
side = (side1 + side2 + side3) /2
area = math.sqrt(side * (side - side1) * (side - side2) * (side - side3))
print(f"The area of the triangle is: {area:.2f}")

