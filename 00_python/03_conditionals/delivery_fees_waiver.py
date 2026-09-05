order_amount = int(input("Enter the amount"))
delivery_fees = 0 if order_amount > 300 else 30
print(f"Delivery fee is :{delivery_fees}")
