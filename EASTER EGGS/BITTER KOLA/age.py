birth_year = int(input("Enter the birth year: "))
current_year = int(input("Enter the current year: "))
age = current_year - birth_year

if age >= 65:
    print("Eligible for discount")
else:
    print("Not eligible for discount")
