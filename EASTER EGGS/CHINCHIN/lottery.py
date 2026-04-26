import random

lottery = random.randint(0, 99)

choice = int(input("Enter two digits to pick lottery: "))

if choice == lottery:
    print("It's a match, You win!")
else:
    print("Wrong match, You lose!")
