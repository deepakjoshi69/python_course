def inches_to_cm(inches):
    return inches*2.54

inches = int(input("Enter inches : "))

cms = inches_to_cm(inches)

print(f"{inches}inches is {cms}cm")