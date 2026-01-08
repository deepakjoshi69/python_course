# Create a class “Programmer” for storing information of few programmers
# working at Microsoft.

class Programmer:
    company = "Microsoft"

    def __init__(self, name, salary, language):
        self.name = name
        self.salary = salary
        self.language = language

employee1 = Programmer("Deepak", 100000, "Python")
print(employee1.name, employee1.salary, employee1.language, employee1.company)
employee2 = Programmer("Derik", 100000, "Java")
print(employee2.name, employee2.salary, employee2.language, employee2.company)
employee3 = Programmer("Guarv", 100000, "Python")
print(employee3.name, employee3.salary, employee3.language, employee3.company)