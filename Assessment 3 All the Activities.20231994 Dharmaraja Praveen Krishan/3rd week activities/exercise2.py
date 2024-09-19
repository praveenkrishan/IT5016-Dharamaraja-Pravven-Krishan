def functionBMI(weight,height):
    height_in_centimers = height / 100
    BMI = weight / height_in_centimers ** 2
   
    return BMI

weight = float(input("enter the weight"))
height = float(input("enter the height"))

print(functionBMI(weight,height))