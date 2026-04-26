def calculate_wage(successful_deliveries):
    base_pay = 5000

    if successful_deliveries >= 70:
        amount_per_parcel = 500
    elif successful_deliveries >= 60:
        amount_per_parcel = 250
    elif successful_deliveries >= 50:
        amount_per_parcel = 200
    else:
        amount_per_parcel = 160

    return (successful_deliveries * amount_per_parcel) + base_pay
