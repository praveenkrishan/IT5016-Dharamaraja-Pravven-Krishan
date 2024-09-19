def calculate_total_amount():
    total_amount = 0

    while True:
        price_input = input("enter the price of the item (or type 'finish' to stop:)")

        if price_input.lower() == 'finish':
            break

        try:

            price = float(price_input)
            total_amount += price

        except ValueError:
            print("invalid input, enter a numerical value")

            print(f"the total amount is{total_amount: .2f}")

calculate_total_amount()            