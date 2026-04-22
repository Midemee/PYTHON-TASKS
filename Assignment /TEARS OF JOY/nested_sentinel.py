while True:
    name = input("Student: ")

    if name == "":
        print("Done")
        break

    total = 0
    count = 0
    score = float(input("Enter score: "))

    while score != -1:
        total += score
        count += 1
        score = float(input("Enter score: "))

    average = total/count
    print(f"{name} Average: {average}")
    
