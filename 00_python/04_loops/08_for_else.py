staff = [("Amit",16),("Zara",17),("Raj",15)]

for name,age in staff:
    if age>= 18:
        print(f"{name} is eligble to manage staff")
        break
    else:
        print("No one is eligble")
