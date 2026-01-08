# Attempt problem 1 using while loop
# print table of a number entered by user

number = int(input("Enter the number : "))
i=1
while(i<=10):
    print(f"{number} X {i} = {number*i}")
    i += 1