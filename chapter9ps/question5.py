words = ["Donkey","Elephant","Tiger","Lion","Giraffe"]

with open("q3.txt","r") as file:
    content = file.read()
    
for word in words:
    content = content.replace(word,"#"*len(word))

with open("q3.txt","w") as file:
    file.write(content)
