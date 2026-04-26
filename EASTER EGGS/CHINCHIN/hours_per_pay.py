wage = float(input("Enter your hourly wage: "))
hours = float(input("Enter your hours worked: "))
payment; = 0

if hours <= 40:
    payment = wage * hours
	print(payment)
else:
	payment = wage * hours * 1.5
	print(payment)

