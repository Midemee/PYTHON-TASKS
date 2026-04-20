'''PSEUDOCODE
Declare variable count and intialise to 1
Use the for loop to count 10 times
Multiply userInput by the count 
print out the result'''

number = int(input("Enter a number: "))
for count in range(1, 11):
    #print(number, "x" + count + " = " + (number * count))
    print(f'{number} x {count} = {number * count}')


