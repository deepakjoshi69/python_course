# Write a python function to print multiplication table of a given number.

def print_table(n):
    for i in range(1, 11):
        print(f"{n} X {i} is {n*i}")

number = int(input("Enter a number : "))

print_table(number)