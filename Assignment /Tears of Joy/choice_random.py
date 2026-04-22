import random

computer_choice = random.randint(1,100)
attempts = 0

while True:
    guess = int(input("Guess: "))
    attempts += 1

    if guess < computer_choice:
        print("Higher")

    elif guess > computer_choice:
        print("Lower")
    else:
        print("Correct!", attempts)
        break
