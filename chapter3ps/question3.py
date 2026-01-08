# program to find double space in a string 

name = "Hii  there, My name is  Deepak Joshi"
for i in range(len(name)-1):
    if name[i] == " " and name[i+1] == " ":
        print(f"Double space found at index {i}")