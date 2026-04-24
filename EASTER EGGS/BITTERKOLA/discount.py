price = int(input("Enter the price: "))
discount = int(input("Enter the discount percentage: "))
discount_amount = (discount / 100) * price
final_price = price - discount_amount
print(f"Final price: {final_price:.2f} Discount Price: {discount_amount:.2f}")

