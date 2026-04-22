'''
PSEUDOCODE
Declare variable for computer choice 
assign random numbers from 1-100 to computer choice
declare variable attempts and assign to zero
while its running
get input from user 
increase the attempt by one
    if the user's guess is less than the computer's choice
        display message to go higher
    Otherwise if the user's guess is greater than the computer's choice
        display message to go lower
    othewise, display the message correct
    print out the numbers of attempts
    break the loop condition
'''

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
