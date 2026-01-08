# A file contains a word “Donkey” multiple times. You need to write a program
# which replace this word with ##### by updating the same file

with open("q3.txt","r") as file:
    content = file.read()

content = content.replace("Donkey","#####")

with open("q3.txt","w") as file:
    file.write(content)
