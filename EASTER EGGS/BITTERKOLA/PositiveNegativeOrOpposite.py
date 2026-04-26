first_nmuber = int(input("Enter first integer: "))
second_number = int(input("Enter second integer: "))

if first_number > 0 and second_number > 0:
    print("Both positive. Sum:", first_number + second_number)
elif first_number < 0 and second_number < 0:
    print("Both negative. Product:", first_number * second_number)
else:
    # Opposite signs: Difference (Larger - Smaller)
    if first_number > second_number:
        print("Opposite signs. Difference:", first_number - second_number)
    else:
        print("Opposite signs. Difference:", second_number - first_number)
print()

