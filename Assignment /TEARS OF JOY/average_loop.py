'''
PSEUDOCODE
Declare variable and assign it to a list of numbers
declare total and initialise to zero
declare count and initialise to zero
loop through the list of numbers
in each iteration
add one to total
Increase count by one
Declare variable average 
divide total by count and assign it to average
print the result of average
'''

numbers = [4,8,15,16,23,42,10,5,4,7,20]
total = 0
count = 0

for number in numbers:
    total += number
    count += 1

average = total/count
print(average)
