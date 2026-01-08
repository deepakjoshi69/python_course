# . Write a python function to print first n lines of the following pattern:
# ***
# ** - for n = 3
# *

n =  int(input("Enter number : "))

for i in range(n,0,-1):
    print("*"*i)