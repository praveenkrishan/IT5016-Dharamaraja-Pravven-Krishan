def shopping_lists():
    print("welcome to the shooping list program!")
    shopping_lists =[] #it is ist that store calues
    total_price = 0
    while True:
       item = input("enter the name of the item(or type 'done'to finish):")
       if item.lower() == "done":
           break
       try:
         price = float(input("enter the price of item '{item}':"))
         shopping_lists.append((item,price))
         total_cost  += price

       except ValueError:
         print("Invalid input. please enter a numeric value for the price")
    return shopping_lists,total_price

def main():
   print("welcome to the shopping list program")
   shopping_lists,total_price = shopping_lists()

   if not shopping_lists:
      print("no items were entered")
   else:
      print("\nshopping list:")
      for item, price in shopping_lists:
        print(f"{item},${price:.2f}")
      print(f"\ntotal price:${total_price:.2f}")

main()       





    


