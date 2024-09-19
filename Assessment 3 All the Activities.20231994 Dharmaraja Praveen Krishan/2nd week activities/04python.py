#item1 = 10
#item2 = 20
#item3 = 30
item1 = float(input("enter the price for item1:"))
item2 = float(input("enter the price for item2:"))
item3 = float(input("enter the price for item3:"))
sub_total = item1 + item2 + item3
sales_tax = sub_total * 0.15

total = sub_total + sales_tax

print(sub_total)
print(sales_tax)
print(total)