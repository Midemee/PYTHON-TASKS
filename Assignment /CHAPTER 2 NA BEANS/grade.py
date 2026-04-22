mark = int(input("Enter your mark 0-10: "))

if mark >= 90 and mark <= 100:
    print("Grade A")
elif mark >= 80 and mark <= 89:
    print("Grade B")
elif mark >= 70 and mark <= 79:
    print("Grade C")
elif mark >= 60 and mark <= 69:
    print("Grade D")
elif mark >= 0 and mark < 60:
    print("Grade F")
else:
    print("Invalid input")
