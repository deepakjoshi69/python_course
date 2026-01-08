#  Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from
# ‘Pets’. Add a method ‘bark’ to class ‘Dog’.

class Animals:
    animal = "dog"

class Pets(Animals):
    pet = "domestic animal"

class Dog(Pets):
    def bark(self):
        return "Woof! Woof!"
    
    def animal_list(self):
        return f"Animal: {self.animal}, Pet: {self.pet}"

obj = Dog()
print(obj.bark())
print(obj.animal)
# print(obj.animal_list)
