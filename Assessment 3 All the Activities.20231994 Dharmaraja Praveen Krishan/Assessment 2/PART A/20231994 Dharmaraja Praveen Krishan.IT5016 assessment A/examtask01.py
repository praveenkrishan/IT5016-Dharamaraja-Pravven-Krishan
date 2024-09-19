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
    print(f"Date: {print_info['Date']}")
    print(f"StaffID: {print_info['StaffID']}")

    return id_counter, print_info

new_id_counter, print_info = staff_info()

staff_info()


