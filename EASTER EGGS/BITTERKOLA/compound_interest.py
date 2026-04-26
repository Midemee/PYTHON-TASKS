import math

balance= float(input("Enter initial bank balance: "))
rate= int(input("Enter annual interest rate: "))
rate = rate // 100;
year_one = balance * math.pow(1 * rate, 1)
year_two = balance * math.pow(1 * rate, 2)
year_three = balance * math.pow(1 * rate, 3)

print(f"Balance After:\nYear One: {year_one}\nYear Two: {year_two}\nYearThree: {year_three}")
