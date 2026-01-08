# Write a recursive function to calculate the sum of first n natural numbers.

def sum_natural_numbers(n):
    if n == 0:
        return -1
    else:
        return n + sum_natural_numbers(n-1)
        
number = int(input("Enter a natural number: "))
print(sum_natural_numbers(number))