number = int(input("Enter a number: "))
for count in range(1, 13):
    product = count * number
    print(f"{number:>2} * {count:>2} = {product:>3} ")
