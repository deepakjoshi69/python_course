# 1. Write a program to find the greatest of four numbers entered by the user.

list = []
for i in range(4):
    num = int(input("Enter a number: "))
    list.append(num)
greatest = max(list)
print("The greatest number is:", greatest)