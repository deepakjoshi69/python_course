# now we can merge two dictionary

dict1 = { "a" : 1, "b":2 }
dict2 = { "b" : 3, "c":4 }
dict3 = { "b" : 4, "d":6 }

merge =  dict1 | dict2 | dict3

print(merge)

# now we can also open multiple file together

with (open("file.txt") as f1, open("file2.txt") as f2 ):
    pass

# before we used to open like this 

with open("file.txt") as file:
    pass