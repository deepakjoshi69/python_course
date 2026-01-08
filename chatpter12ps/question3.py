# 3. Write a list comprehension to print a list which contains the multiplication table of a
# user entered number.
def table():
    try:
        number = int(input("Enter a number : "))
    except ValueError:
        print("Enter a Number!")
    except Exception as e:
        print(e)
    else:
        list = [number*i for i in range(1,11)]
        return list


