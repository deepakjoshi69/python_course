# Exception handiling is used to prevent from  program crash by tellig whats the error is inside except block

try:
    number = int(input("Enter a number: "))
except Exception as e:
    print(e)

print("program will not crash it will continue!")
