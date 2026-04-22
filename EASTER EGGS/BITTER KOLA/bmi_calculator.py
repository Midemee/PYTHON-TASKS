weight = float(input("Enter the weight in kg: "))
height = float(input("Enter the height in kg: "))
bmi = weight / (height * height)
print("BMI: {bmi:.2f}")

if bmi < 18.5:
    print("Group: Underweight")
elif bmi <= 24.9:
    print("Group: Overweight")
else:
    print("Group: Obese")
