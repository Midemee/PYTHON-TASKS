days = ("Enter number of days from today: ")
future = days % 7

if future == 0: 
    print("Monday")

elif future == 1:
    print("Tuesday")

elif future == 2:
    print("Wednesday")

elif future == 3:
    print("Thursday")

elif future == 4: 
    print("Friday")

elif future == 5:
    print("Saturday")

elif future == 6:
    print("Sunday")

else:
    print("Invalid")

