age = int(input("Enter your age : "))

if(age >= 0):
    raise ValueError("You Entered a negavtive age or 0")

elif(age>=18):
    print("You can drive!")

else:
    print("You cannot drive!")