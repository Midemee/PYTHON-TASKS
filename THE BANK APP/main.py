from pybank import *

message = """1. Register
2. Login
3. Calculate Balance
4. Apply Interest
5. Summary
6. Exit : """

while True:
    user_input = input(message)
    match user_input:
        case "1":
            email = input("Enter email: ")
            password = input("Enter password: ")
            if validate_email(email) and is_strong_password(password):
                print("Registration successful")
            else:
                print("Registration failed")
                
        case "2":
            email = input("Enter email: ")
            password = input("Enter password: ")
            if validate_email(email) and is_strong_password(password):
                print("Login successful")
            else:
                print("Login failed")
                
        case "3":
            transactions = []
            amount = float(input("Enter amount or 0 to stop: "))
            while amount != 0:
                transactions.append(amount)
                amount = float(input("Enter amount or 0 to stop: "))
            total_transactions = calculate_balance(transactions)
            print("Your balance is ", total_transactions)

        case "4":
            compound_interest = []
            balance =  int(input("enter balance:   "))      
            rate = int(input("enter rate:  "))
            years = int(input("enter year:   "))   
            if rate < 0 and years < 1:
                print("invalid input")
            elif rate > 0 and years >= 1:
                compound_interest = balance * (1 + rate) ** years
            print("your yearly interest is", compound_interest )
                
        case "5":
            transactions = []
            for amount in transactions:
                if transaction[0] == "credit":
                    total_credits += transaction[0]
                else:
                    total_debits += transaction[0]
                
                transaction_count += 1
        
                net_balance = total_credits - total_debits
    
                print ("total_credits", total_credits)
                print("total_debits",total_debits)
                print("net_balance", net_balance)
                print("transaction_count", transaction_count)
                
        case "6":
                print("shut down....")
                break
