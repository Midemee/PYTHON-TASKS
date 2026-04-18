'''Modify the script of Fig. 3.3 to validate its inputs. For any
input, if the value entered is other than 1 or 2, keep looping until the user enters a correct value. Use one counter to keep track of the number of passes, then calculate the number
of failures after all the user’s inputs have been received.'''

passes = 0
failures = 0

for student in range(10):
    result = int(input("Enter result (1=pass, 2=fail): "))

    while result != 1 and result != 2:
        result = int(input("Enter result (1=pass, 2=fail): "))

    if result == 1:
        passes +=1
    else:
        failures +=1

print("Passed =", passes)
print("Failed =", failures)

if passes > 8:
    print("Bonus to the instructor!")
