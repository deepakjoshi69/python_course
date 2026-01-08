# 1. Create a class (2-D vector) and use it to create another class representing a 3-D vector.

class twoD_vector:
    x = 10
    y= 20

class threeDvectoer(twoD_vector):
    z = 30
    def sumofXYZ(self, x, y, z):
        return x+y+z

obj = threeDvectoer()
print(obj.x)
print(obj.y)
print(obj.z)
print(obj.sumofXYZ(obj.x, obj.y, obj.z))
# print()
