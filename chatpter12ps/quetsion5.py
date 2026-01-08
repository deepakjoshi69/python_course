# Store the multiplication tables generated in problem 3 in a file named Tables.txt.

from question3 import table

with open("Tables.txt","a") as file1:
    content = table()
    file1.write(f"{str(content)}\n")

# print(table())
