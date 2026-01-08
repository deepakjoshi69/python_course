try:
    a = int(input("Enter a number : "))
    b = int(input("Enter another number : "))

    c = a/b
except ZeroDivisionError:
    print("DIvision by zero is not allowed in pyhton!")

except ValueError:
    print("You entered wrong type value, please enterd an integer!")

except Exception as e:
    print(e)

print(c)