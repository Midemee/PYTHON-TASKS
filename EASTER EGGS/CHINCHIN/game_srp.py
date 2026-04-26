import random

game = random.randint(0, 2)

choice = int(input("Enter 0 for Scissors, 1 for Rock, 2 for Paper: "))

if game == 0:
    result = "Scissors"
elif game == 1:
    result = "Paper"
else:
    result = "Rock"

if game == 0 and choice == 0:
    print("Scissors")
elif game == 1 and choice == 1:
    print("Paper")
elif game == 2 and choice == 2:
    print("Rock")
else:
    print("You lose!")
