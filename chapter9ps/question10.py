# Write a program to wipe out the content of a file using python.
# method1: using open() function with 'w' mode

# with open("todelete.txt", "w") as file:
#     file.write("")
# print("The content of 'todelete.txt' has been wiped out.")

# Method 2

# with open("todelete.txt", "r+") as file:
#     file.truncate(0)
# print("The content of 'todelete.txt' has been wiped out.")

# method 3

with open("todelete.txt", "w") as file:
    pass
print("The content of 'todelete.txt' has been wiped out.")