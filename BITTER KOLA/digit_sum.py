number= int(input("Enter a 5-digit integer: "))
firstDigit = number / 10000
lastDigit = number % 10
sum = firstDigit + lastDigit
print("The sum is %d", sum)

