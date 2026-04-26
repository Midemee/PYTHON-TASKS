salary = float(input("Enter your salary: "))
rate = 0

if salary <= 50000:
    rate = 0.0

else if salary <= 150000:
	rate = 0.05

	else if salary <= 500000:
	rate = 0.075

else:
	rate = 0.10

double deduction = salary * rate
print("Deduction Rate: " + (rate * 100) + "%")
print("Social Insurance Deduction: " + deduction)

