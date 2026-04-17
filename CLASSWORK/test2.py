'''product = 7
while product <= 1000:
    product = product * 7
    print(product)'''

'''total = 0
for number in range(10):
    total = total + number
    print(total)'''

#For loop with a list
#definite repetition
'''total = 0
for number in ([2, -3, 0, 17, 9]):
    total += number
    print(total)

for character in 'Programming':
    print(character, end = ' ')

total = 0
grade_counter = 0
grades = [98, 76, 71, 87, 83, 90, 57, 79, 82, 94]

for grade in grades:
    total += grade
    grade_counter += 1
    
average = total / grade_counter
print(f'The class average is {average}')

number_one = 7
number_two = 5
product = number_one * number_two
print(f'{number_one} * {number_two} = {product}')
print(f'{number_one} * {number_two} = {number_one * number_two}')

#Exam grade to test iteration and selection statement 
passes = 0
failures = 0

for student in range (10):
    result = int(input("Enter the each result (1=pass, 2=fail): "))
    if result == 1:
        passes += 1
    else:
        failures += 1

print('passed: ', passes)
print('failed: ', failures)

if passes > 8:
    print("Bonus to the instructor")

for number in range(1, 6):
    user_input = int(input("Enter a number: "))
    if user_input % 2 == 0:
        print(user_input, "is even")
    else:
        print(f"{user_input} is odd")'''

principal_amount = 1000
rate = 5

for year in range (1, 11):
    amount = principal_amount * (1 + rate)** year
    print(f"{amount:.2f}")
    
