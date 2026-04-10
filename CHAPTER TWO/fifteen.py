a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a <=b and a<= c:
    smallest = a
    if b <= c:
        middle = b
        largest = c
    else:
        middle = c
        largest = b

print(smallest, middle, largest)
