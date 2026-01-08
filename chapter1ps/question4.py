import os

path = input("Enter the file path: ")

if os.path.exists(path):
    print("The file exists.")
    for items in os.listdir(path):
        print(items)
else:
    print("The file does not exist.")