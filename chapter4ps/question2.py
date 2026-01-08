# program to store marks of 6 student and display in stored order.

marks = []
for i in range(4):
    mark = int(input("Enter the marks of student : "))
    marks.append(mark)
marks.sort()
print(marks)