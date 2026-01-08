# program to create an empty dictionary and add 4 values to it given by user.

dict = {}
for i in range(4):
    name = input("Enter your name : ")
    fav_lang = input("Enter your favorite programming language : ")
    dict.update({name: fav_lang})
print("The dictionary is :", dict)