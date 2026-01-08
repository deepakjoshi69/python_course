# Write a program to find out whether a student has passed or failed if it requires a
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
# take marks as an input from the user

list = []
for i in range(3):
    marks = int(input(f"Enter marks for subject {i+1} from 100 : "))
    list.append(marks)
total = sum(list)
if(total/3>=40 and list[0]>=33 and list[1]>=33 and list[2]>=33):
    print("The student has passed")
else:
    print("The student has failed")
