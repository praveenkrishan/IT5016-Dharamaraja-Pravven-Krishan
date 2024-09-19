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

    
def calculate_total_amount():
    total_amount = 0

    while True:
        price_input = input("enter the price of the item (or type finish to stop:)")

        if price_input.lower() == 'finish':
            break

        try:

            price = float(price_input)
            total_amount += price

        except ValueError:
            print("invalid input, enter a numerical value")

            print(f"the total amount is{total_amount: .2f}")

calculate_total_amount()          
            

def categorize_request(total_amount):
    if total_amount < 150:
        category = "Low"
        recommendation = "Proceed with standard processing."
    else:
        category = "High"
        recommendation = "Review for potential discounts."

    print(f"Request Summary:")
    print(f"Total Amount: ${total_amount:.2f}")
    print(f"Category: {category}")
    print(f"Recommendation: {recommendation}")

    categorize_request(total_amount)

def create_detailed_report (unique_id,user_name,Age,email,total_amount,catergory,reccomendations):
    new_id_counter, user_data = collect_user_data()
    category, recommendation=categorize_request(total_amount)
    



    