#  Write a class “Calculator” capable of finding square, cube and square root of a
# number.

class Calculator:
    def square(self, number):
        return number*number
    
    def cube(self, number):
        return number*number*number
    
    def square_root(self, number):
        return number**0.5

number = int(input("Enter a number : "))

obj = Calculator()

print(obj.square(number))
print(obj.cube(number))
print(obj.square_root(number))