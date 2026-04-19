principal_amount = float(input("Enter the principal amount: "))
annual_interest_rate = float(input("Enter the annual interest rate: "))
duration = int(input("Enter the duration in years: "))

monthly_rate = (annual_interest_rate / 100) / 12
number_of_payments = duration * 12

monthly_mortgage = principal_amount *(monthly_rate * (1 + monthly_rate) ** number_of_payments) / ((1 + monthly_rate) ** number_of_payments -1)

print("Monthly mortgage = ", round(monthly_mortgage,2))
print(f"Monthly mortgage = {monthly_mortgage:.2f}")



