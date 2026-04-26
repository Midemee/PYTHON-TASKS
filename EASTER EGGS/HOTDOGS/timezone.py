hour = input("Enter current hour within 0-23: ")
if hour >= 7:
    print("Good Morning")
elif hour >= 12:
	print("Good Afternoon")
elif hour >= 4:
	print("Good Evening")
elif hour >= 10:
	print("Good Night")
else:
	print("Invalid hour")

