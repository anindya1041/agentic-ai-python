flavours = ["Ginger","Out of Stock","Lemon","Discontinued","Tulsi"]
for flavor in flavours:
    if flavor == "Out of Stock":
        continue
    if flavor == "Discontinued":
        break;
print(f"Discontinued item is found!")