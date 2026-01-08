# Write a program to find whether a given username contains less than 10
# characters or not.

name = input("Enter your username: ")
if len(name) < 10:
    print("Username contains less than 10 characters")
else:
    print("Username contains 10 or more characters")