def requisition_approval():
    total_amount = 0
    reference = "FN19001"
     

    while True:
        item_name = input("enter the item name(or type 'finish' to stop):")
        if item_name.lower()== "finish":
            break
        item_price = float(input("Enter the item price(or type'finish' to stop): "))
        try:
         total_amount += item_price
        except ValueError:
         print("Please Enter a valid number")
    print(f"The total price of items:{total_amount:.2f}")


    if total_amount < 500:
     status = 'approved'
     requisition_id = reference
     print(f"status:{status}:")
     print(f"approval refernce number:{requisition_id}")
    else:
       status = "pending"
       print(f"status{status}")


requisition_approval()       





