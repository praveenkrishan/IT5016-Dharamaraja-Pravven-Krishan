def function2(name1,name2):
    len1 = len(name1)
    len2 = len(name2)
    shorter_length = min(name1,name2)
    return shorter_length

name1 = (input("enter name1"))
name2 = (input("enter name2"))

print(function2(name1,name2))