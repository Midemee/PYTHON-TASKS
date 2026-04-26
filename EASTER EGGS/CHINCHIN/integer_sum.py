number = int(input("Enter a number witin 0-1000: "))
sum = 0

if number < 0 || number > 1000:
    print("Invalid number! Enter number within 0-1000")

else:
	while number > 0):
	    remainder = number % 10
	    sum = sum + remainder
	    number = number // 10

print("The sum is: {sum}")

