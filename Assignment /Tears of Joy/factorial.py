count = 1;
factorial = 1;
number = int(input("Enter a number: "))
while count <= number:
    factorial *= count
    count += 1

print(factorial)
