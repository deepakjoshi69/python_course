# 6. Write a program to calculate the factorial of a given number using for loop.

number = int(input("Enter a nummber : "))
factorial = 1
if number == 0 or number == 1:
    print("The factorial is 1")
else:
    for i in range(1,number+1):
        factorial = factorial*i
print(f"The factorial of {number}! is {factorial}.")


