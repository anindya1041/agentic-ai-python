def calculate_bill(cups,price_per_cups):
    return cups*price_per_cups
my_bill = calculate_bill(3,15)
print(my_bill)
print("Order for Table 2: ", calculate_bill(2,50))