# types is like we can define variable with specific type

number: int = 10 # defining variable with int type

name: str = "Python" # defining variable with str type

print(f"Number: {number}\n{type(number)}\nName: {name}\n{type(name)}")

# we can also define function with specific type

def show(number1: int, number2: int) -> int:
    return number1 + number2

print(show(5, 10))

# implementing types in tuple dict union list

from typing import Tuple, List

list1 : List[int] = [1,2,3,4,4]

tuple1 : Tuple[int, str] = ("Deepak",16,15, "hii")

print(list1)
print(tuple1)