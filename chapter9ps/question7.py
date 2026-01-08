# Write a program to find out the line number where python is present from ques 6.

with open("log.txt","r") as file:
    lines = file.readlines()
# print(lines)
lineno =1
for line in lines:
    if "python" in line:
        print(f"The word 'python' is present in the file at {lineno} Line")
        break
    lineno  += 1
else:
    print("python is not present in line!")