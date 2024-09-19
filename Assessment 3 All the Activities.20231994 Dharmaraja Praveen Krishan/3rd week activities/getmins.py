def get_minutes(hours, minutes):
    total = hours * 60 + minutes
    return total

hours = float(input("enter the hours:"))
minutes = float(input("enter the minutes:"))


total_minutes = get_minutes(hours, minutes)
print(total_minutes)