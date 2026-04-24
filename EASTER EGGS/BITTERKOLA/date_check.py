day = int(input("Enter a day as an integer: "))
month = int(input("Enter month as an integer: "))
year = int(input("Enter year as an integer: "))

if day < 1 and day > 31: 
    print("Invalid")

elif month < 1 and month > 12:
    print("Invalid")

elif year < 1 and year > 365:
    print("Invalid")

else: 
    print("Valid")

