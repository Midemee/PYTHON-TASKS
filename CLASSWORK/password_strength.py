'''PSEUDOCODE
Declare variable for password to zero
collect password from user and store in a variable
if the user password is less than 8 
It is very weak
else, if the user password is strictly equal to 8 
It is weak
else, if the user password is greater than 8 or less than or equal to 16
It is strong
else if the user password is greater than 16
It is very strong
else, display invalid password'''


password = input("Enter your password: ")
password_length = len(password)

if password_length < 8:
    print("Very weak")

elif password_length == 8:
    print("Weak")

elif password_length > 8 and password_length <= 16:
    print("Strong")

else:
    print("Very Strong")


