total_sum = 0
product = 1
for count in range(4):
    number = int(input("Enter a number: "))

    total_sum += number
    product *= number

#smallest = min(number)
#largest = max(number)

average = total_sum / 4

print("Sum =",     total_sum)
print("Average = ", average)
print("Product = ", product)
#print("Smallest = ", smallest)
#print("Largest = ", largest)

    
