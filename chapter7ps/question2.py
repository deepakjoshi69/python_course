# 2. Write a program to greet all the person names stored in a list ‘l’ and which starts
# with S.
# l = ["Harry", "Soham", "Sachin", "Rahul"]

l = ["Harry", "Soham", "Sachin", "Rahul"]

for i in l:
    if(i[0].lower()=='s'):
        print(f"Good morning, {i}")

