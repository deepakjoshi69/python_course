import random

original = random.randint(1,101)
chance  = 1

guess = 0

while original!= guess:
    guess = int(input("Enter your guess ! "))
    if(original>guess):
        print("You entered smaller number! ")
    else:
        print("You entered bigger number!")
    
    chance += 1

print(f" your number is {guess} and computer number is {original} in {chance} chances.")