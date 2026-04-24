number = int(input("Enter a five-digit number: "))

if number <10000 and number > 99999:
    print("Please enter a 5-digit number!")

first_step = number % 10
second_step = number / 10
print(number)
