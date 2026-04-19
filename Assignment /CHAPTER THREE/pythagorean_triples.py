side_one = 0
side_two = 0

for side in range(1, 21):
    side_one = int(input("Enter a number for side one: "))
    side_two = int(input("Enter a number for side two: "))
    sides = side_one * side_one + side_two * side_two
    print(sides)

