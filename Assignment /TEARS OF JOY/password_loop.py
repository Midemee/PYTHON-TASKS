correct_password = "python123"
attempts = 0
while attempts < 3:
    password = input("Enter password: ")
    attempts += 1

    if password == correct_password:
        print("Access granted")
        break

else:
    print("Locked out")

