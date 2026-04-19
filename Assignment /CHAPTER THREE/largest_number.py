largest_one = 0
largest_two = 0

for count in range(10):
    number = int(input("Enter a number: "))
    if number > largest_one:
        largest_two = largest_one
        largest_one = number
    elif number > largest_two:
        largest_two = number

print("The largest number is: ", largest_one)
print("The second largest number is: ", largest_two)
