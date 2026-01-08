# type() used to check the data type of a variable in Python.

a = 10
print(type(a))  # Output: <class 'int'>

# typecasting examples only if it can be validly converted

# int to float
a = 5 
b = float(a)
print(b)  # Output: 5.0    
print(type(b)) # Output: <class 'float'>

c = "10.7"
print(c)  # Output: 10.7
print(type(c)) # Output: <class 'str'>
d = float(c)
print(d)  # Output: 10.7    
print(type(d)) # Output: <class 'float'>

# x = "deepak"
# y = int(x)  # This will raise an error
# print(y)  # Output: ValueError: invalid literal for int() with base 10: 'deepak'