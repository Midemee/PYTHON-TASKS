principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate %: "))
time = float(input("Enter the time (in years): "))

SI = (principal * rate * time)/ 100
A = principal + SI

print("Simple Interest = ", SI)
print("Total Amount = ", A)
