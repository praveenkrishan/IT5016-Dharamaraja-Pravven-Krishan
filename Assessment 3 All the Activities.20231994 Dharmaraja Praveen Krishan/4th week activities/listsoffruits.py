"""
lists_demo
"""
#append
my_lists = [1, 2, 3, 'apple', 'lemon']
my_lists.append(6)
print(my_lists)

#insert
my_lists.insert(1, 20)
print(my_lists)
print()

#pop
poped_element = my_lists.pop()
print(my_lists)
print()

#sort
my_lists.sort(key=str)
print(my_lists)
print()