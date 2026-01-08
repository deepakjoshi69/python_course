# Write a program to find the sum of first n natural numbers using while loop.

number1 = int(input("Enter first natural number : "))
sum = 0
i = 1
while i < number1+1:
    sum = sum+i
    i += 1
print(f"The sum of {number1} natural number is : {sum}")