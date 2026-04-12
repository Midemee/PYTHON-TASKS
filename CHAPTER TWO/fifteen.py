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

elif b <= a and b<= c:
    smallest = b
    if a <= c:
        middle = a
        largest = c
    else: 
        middle = c
        largest = a

else: 
    smallest = c
    if a <= b:
        middle = a
        largest = b
    else: 
        middle = b
        largest = a

print("Smallest =" , smallest, "Middle = ", middle, "Largest = ", largest)

