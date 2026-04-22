'''PSEUDOCODE
Declare variable count and intialise to 1
Use the for loop to count 10 times
Multiply userInput by the count 
print out the result'''

for count in range(10):
    if count != 0:
        
        print(count, end="|   ")
    else:
        print(f"{"":>5}", end="")
    for number in range(1, 10):
        if count != 0:
            print(f"{count * number:>2}", end=" ")
        else:
            print(f"{number:>2}", end=" ")
            if number == 9:
                print("\n-----------------------------------", end="")
    print()

