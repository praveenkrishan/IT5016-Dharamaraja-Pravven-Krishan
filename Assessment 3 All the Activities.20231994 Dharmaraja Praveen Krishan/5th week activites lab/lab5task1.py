def collect_user_data(id_counter=5000):
    name = input("Enter your name:")
    age = input("Enter your age:")
    email = input("Enter the email:")

    id_counter += 1
    unique_id = id_counter

    
    user_info = {
        "ID": unique_id,
        "Name": name,
        "Age": age,
        "Email": email
    }

    print("\nUser Information:")
    print(f"ID: {user_info['ID']}")
    print(f"Name: {user_info['Name']}")
    print(f"Age: {user_info['Age']}")
    print(f"Email: {user_info['Email']}")

    return id_counter, user_info

new_id_counter, user_data = collect_user_data()
