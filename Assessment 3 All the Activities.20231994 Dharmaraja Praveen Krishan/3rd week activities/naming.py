def function3(name):
    first = name[0]
    end = name[len(name) - 1]
    combined = end + first
    return combined.upper()

name = input("enter the name")
print(function3(name))