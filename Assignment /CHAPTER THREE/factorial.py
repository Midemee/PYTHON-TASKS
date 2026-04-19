number = int(input("Enter a non-negative integer: "))
factorial_number = 1

if number < 0:
    print("Negative numbers is invalid for factorial")
else:
    for count in range(1, number + 1):
        factorial_number *= count

    print("Factorial is: ", factorial_number)
