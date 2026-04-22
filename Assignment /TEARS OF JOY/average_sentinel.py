'''
PSEUDOCODE
Declare variable count and initialise to zero
Declare total count and initialise to zero
collect number from user as store as float
while the user input not equal to inus one
    add userinput to total
    increase the count by one
    collect number from user as store as float
declare variable average
divide tota by count and assign to average
print out the count, total and average
'''

count = 0
total = 0
user_input = float(input("Enter a number: "))

while user_input != -1:
    total += user_input
    count += 1
    user_input = float(input("Enter a number: "))

average = total/count
print("Count = ",count)
print("Total = ", total)
print("Average = ", average)
