def update_order():
    chai_type = "Elaichi"
    def Kitchen():
        nonlocal chai_type
        chai_type = "Kesar"
    Kitchen()
    print("After Kitchen update",chai_type)
update_order()
