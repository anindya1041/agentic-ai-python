kettle_boiled = False

if kettle_boiled:
    print("Kettle Done! Time to make chai")

snack = input("please enter the snack").lower()
if snack=="cookie" or snack=="samosa":
    print(f"snack figure : {snack}")
else:
    print("sorry the snack is missing")