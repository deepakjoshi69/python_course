# using write() method to write to a file in Python
data = "This is some sample text to write to the file."
with open("File.txt", "w") as file:
    file.write(data)
    