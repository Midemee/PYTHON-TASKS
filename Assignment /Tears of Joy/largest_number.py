largest = 0
while True:
    user_input = input("Enter: ");
    if user_input == "done":
        break
    number = int(user_input)
    if number > largest:
        largest = number

print(largest)



