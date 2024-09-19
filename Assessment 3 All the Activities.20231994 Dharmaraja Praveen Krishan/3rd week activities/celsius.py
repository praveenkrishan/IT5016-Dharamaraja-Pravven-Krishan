def celsius_to_faren(celsius):
    faren = celsius * 9 / 5 + 32
    return faren

celsius = float(input("enter the celsius:"))
print(celsius_to_faren(celsius))