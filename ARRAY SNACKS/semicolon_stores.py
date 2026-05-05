vat_rate = 0.075  

def get_customer_details():
    customer_name = input("Enter customer's name:")
    cashier_name = input("Enter cashier's name:")
    discount_rate = float(input("Enter discount rate"))

    return customer_name, cashier_name, discount_rate


def add_items():
    products = []
    quantities = []
    prices = []
    totals = []

    while True:
        product = input("\nEnter product's name: ")
        quantity = int(input("Enter the quantity: "))
        price = float(input("Enter the price: "))
        total = quantity * price

        products.append(product)
        quantities.append(quantity)
        prices.append(price)
        totals.append(total)

        user_choice = input("Add another item? (yes/no): ").lower()

        if user_choice == "no":
            break

    return products, quantities, prices, totals

  
def print_receipt(cashier_name, customer_name, products, quantities, prices, totals):

    print("SEMICOLON STORES")
    print("MAIN BRANCH")
    print("Location: 312, Herbert Macaulay way, sabo Yaba, Lagos")
    print("Tel: 03293828343")
    print(f"Cashier: {cashier_name}")
    print(f"Customer Name: {customer_name}")


def main():
    customer_name, cashier_name, discount_rate = get_customer_details()
    products, quantities, prices, totals = add_items()
    print_receipt(cashier_name, customer_name, products, quantities, prices, totals)

main()

