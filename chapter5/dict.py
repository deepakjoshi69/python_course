# dictionary is a data structure that stores key-value pairs, allowing for efficient retrieval, insertion, and deletion of values based on their associated keys

dict = {
    "Deepak": 25,
    "Anjali": 22,   
    "Rohan": 28,
    "Priya": 24
}

# print(dict)
# print(type(dict))
# print(len(dict))
# print(dict["Rohan"]) # Accessing value using key
# print(dict.get("priya")) # shows None if key not found and also case sensitive
# print(dict.update({"Anjali": 23})) # updating value of existing key
# print(dict)
print(dict.items()) # returns all keys