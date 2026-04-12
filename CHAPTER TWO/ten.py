first_digit = int(input("Enter first digit: "))
second_digit = int(input("Enter second digit: "))
third_digit = int(input("Enter last digit: "))


total_sum = first_digit + second_digit + third_digit
average = total_sum / 3
product = first_digit * second_digit * third_digit


smallest = min(first_digit, second_digit, third_digit)
largest = max(first_digit, second_digit, third_digit)

print("Sum =",     total_sum)
print("Average = ", average)
print("Product = ", product)
print("Smallest = ", smallest)
print("Largest = ", largest)
