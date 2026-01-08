#  Create a class ‘Employee’ and add salary and increment properties to it.
# Write a method ‘salaryAfterIncrement’ method with a @property decorator with a setter
# which changes the value of increment based on the salary

class Employee:
    salary = 56000
    increment = (11/100)
    @property
    def salary_increment(self):
        return self.salary + (self.salary * self.increment)
    
    @salary_increment.setter
    def salary_increment(self, increment):
        self.increment = increment

sal =  Employee()
print(sal.salary_increment)