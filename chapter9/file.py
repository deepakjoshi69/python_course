# this chaper is about file input and output in Python.

# with open("File.txt") as file:
#     content = file.read()
#     print(content)

file = open("File.txt")
content = file.read()
print(content)
file.close()