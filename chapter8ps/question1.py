# 1. Write a program using functions to find greatest of three numbers.

def max_three(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
num3 = int(input("Enter third number : "))

max_number = max_three(num1, num2, num3)

print(f"The max from {num1}, {num2} and {num3} is {max_number}")