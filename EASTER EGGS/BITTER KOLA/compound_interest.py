balance= float(input("Enter initial bank balance: "))
rate= int(input("Enter annual interest rate: "))
#rate = rate / 100;
year_one = balance * (1** (rate/100) * 1)
year_two = balance * (1** (rate/100) * 2)
year_three = balance * (1** (rate/100) * 3)

print(f"Balance After:\nYear One: {year_one}\nYear Two: {year_two}\nYearThree: {year_three}")
