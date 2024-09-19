def requisitions_total():
    total_amount = 0



    while True:
        item_name = input("enter the item name(or type 'finish' to stop): ")
        if item_name.lower()== "finish":
            break
        item_price = float(input("Enter the item price(or type'finish' to stop): "))
        try:
         total_amount += item_price
        except ValueError:
         print("Please Enter a valid number")
    print(f"The total price of items:{total_amount:.2f}")


requisitions_total()              

        
