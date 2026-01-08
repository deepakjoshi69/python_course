# exception handling with else block

try:
    a = int(input("a = "))
    b = int(input("b = "))
except Exception as e:
    print(e)
else:   # else part will only exceute  if try part exceutes succesfully with an exception
    print(a+b)
# finally:
#     print("i am finally!")

print("Done!")