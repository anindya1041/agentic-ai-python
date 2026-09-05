device_status = "active"
temperature = 30

if device_status == "active":
    if temperature > 35:
        print("Temperature is too hot")
    else:
        print("Temperature is normal")
else:
    print("Device is offline")