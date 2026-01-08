#  Write a program to make a copy of a text file “this. txt”

with open("this.txt", "r") as source_file:
    content = source_file.read()

with open("to.txt", "w") as dest_file:
    dest_file.write(content)    

print("File copied successfully 'this.txt' to 'to.txt'")