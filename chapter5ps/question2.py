# program to take 6 numbers from input and display the unique numbers.

set1 = set()
for i in range(6):
    num = int(input("Enter a number: "))
    set1.add(num)
print("The unique numbers are:", set1)