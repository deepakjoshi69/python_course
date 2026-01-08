# Add a static method in problem 2, to greet the user with hello.

class Calculator:
    @staticmethod
    def greet():
        print("Hello there, I am a satitc method!")

    def square(self, number):
        return number*number
    
    def cube(self, number):
        return number*number*number
    
    def square_root(self, number):
        return number**0.5

number = int(input("Enter a number : "))

obj = Calculator()

obj.greet()
print(obj.square(number))
print(obj.cube(number))
print(obj.square_root(number))