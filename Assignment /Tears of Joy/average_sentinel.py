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
