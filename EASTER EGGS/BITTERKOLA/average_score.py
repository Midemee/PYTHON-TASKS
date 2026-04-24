first_score = float(input("Enter the first exam score: "))
second_score = float(input("Enter the second exam score: "))
third_score = float(input("Enter the third exam score: "))

average = (first_score + second_score + third_score) / 3

highest = average * 0.40
middle = average * 0.35
lowest = average * 0.25

print(f"Highest: {highest}\n Middle: {middle}\n Lowest: {lowest}")
