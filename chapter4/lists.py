# list is a collection of elements of different data types, such as integers, strings, and floats.
# list = [1, "Deepak", 3.14, True]
list = [1, "Deepak", 3.14, True]
print(list) 
print(type(list))
print(len(list))  # Output: 4

# methods of list

# append() method adds an element to the end of the list.
list.append("New Element")
print(list)  # Output: [1, "Deepak", 3.14, True, "New Element"]
# print(list.sort())  # This will raise an error because the list contains different data types.  
print(list)  # Output: [1, "Deepak", True, "New Element"]
list1 = [5, 3, 8, 1, 5, 5 , 5]
print(list1.index(2))  # Output: 4