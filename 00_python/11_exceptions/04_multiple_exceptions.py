def process_order(item,quantity):
    try:
        price =  {"masala":20}[item]
        cost = price * int(quantity)
        print(f"total cost is {cost}")
    except KeyError:
        print("Sorry chai is not on Menu")
    except TypeError:
        print("Quantity must be in number")

process_order("ginger",2)
process_order("masala","two")