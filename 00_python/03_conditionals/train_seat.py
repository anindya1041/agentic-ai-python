seat_type = input("Please Enter seat type :").lower()
match seat_type:
    case("lower"):
        print(f"seat type : {seat_type}")
    case("upper"):
       print(f"seat type : {seat_type}")
    case _:
        print(f"Not a valid input")

