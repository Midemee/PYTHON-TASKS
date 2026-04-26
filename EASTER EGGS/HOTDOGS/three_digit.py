number = int(input("Enter a three-digit number: "))
stepOne = number / 100
stepTwo = (number / 10) % 10
stepThree = number % 10
sum = stepOne + stepTwo + stepThree
print(sum)

