def staff_info(id_counter=10000):
    name = input("Enter your name:")
    date = input("Enter your date:")
    staffID = input("Enter the staffID:")

    id_counter += 1
    requisition_ID = id_counter

    
    print_info = {
        "ID": requisition_ID,
        "Name": name,
        "date": date,
        "staffID": staffID
    }

    print("\nprinting staff Information:")
    print(f"ID: {print_info['ID']}")
    print(f"Name: {print_info['Name']}")
    print("Date: {print_info['Date']}")
    print("StaffID: {print_info['StaffID']}")

    return id_counter, print_info

new_id_counter, print_info = staff_info()

staff_info()


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


def display_requisitions(date,requisition_id,staff_id,name,total,status,approval_reference_number):
    total_amount = 0
    print("\nprinting requisitions:")
    print(f"ID: {print_info['ID']}")
    print(f"Name: {print_info['Name']}")
    print(f"Date: {print['Date']}")
    print(f"StaffID: {print_info['StaffID']}")
    print(f"The total price of items:{total_amount:.2f}")
    print(f"status:{status}:")
    print(f"approval refernce number:{requisition_id}")
    status = "pending"
    print(f"status{status}")

display_requisitions()    
