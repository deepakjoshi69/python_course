'''Write a program to print third, fifth and seventh element from a list using enumerate
function.'''

list = [1,2,3,4,5,6,7,7,8]

for index, item in enumerate(list):
    if(index+1 == 3 or index+1 == 5 or index+1 == 7):
        print(f"{item}")