# operators in python

# Arithmetic Operators
x = 10
y = 5
print(x + y) # Addition: 15
# -,*,/,//,%,**
print(10//2)
print(2**3)
print(10%3)
print(5/2)
print(y+1)

# Comparison Operators return boolean values

a = 10
b = 10
print(a == b) # Equal: True
# print(a === b)  there is no === operator in python

print(5<3) # Less than: False
print(5>3) # Less than: False

# assignment operators

c = 20
c += 5  # Equivalent to c = c + 5
print(c)  # Output: 25
c *= 2  # Equivalent to c = c * 2
print(c)  # Output: 50
c -= 10  # Equivalent to c = c - 10
print(c)  # Output: 40

# Logical Operators
p = True
q = False
print(p and q)  # Logical AND: False
print(p or q)   # Logical OR: True  
print(not p)    # Logical NOT: False

# and, or, not
print(True and False)
print(True and True)
print(True or True)
print(True or False)
print(not(False))