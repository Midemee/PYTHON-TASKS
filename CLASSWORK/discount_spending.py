'''PSEUDOCODE
Declare variable discount initialise to zero
collect imput from user and store in a variable
if the user spending is greater than 1000 and less than or equal to 10000, apply 5k discount
if the user spending is greater than 10000 and less than or equal to 50000, apply 10k discount
if the user spending is greater than 50000, apply 20k discount
print out the rate'''

discount = 0
user_input = float(input("Enter the total spending amount: "))

if user_input >= 1000 and user_input <= 10000:
    discount = (5/100) * user_input
    discounted_price = user_input - discount
    print(f"The discounted price is = {discounted_price:.2f}")
    print(f"The discount is = {discount:.2f}")

elif user_input > 10000 and user_input <= 50000:
    discount = (10/100) * user_input
    discounted_price = user_input - discount
    print(f"The discounted price is = {discounted_price:.2f}")
    print(f"The discount is = {discount:.2f}")

elif user_input > 50000:
    discount = (20/100) * user_input
    discounted_price = user_input - discount
    print(f"The discounted price is = {discounted_price:.2f}")
    print(f"The discount is = {discount:.2f}")

else:
    print("Invalid input")


