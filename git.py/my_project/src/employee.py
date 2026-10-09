class Employee:

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Salary:", self.salary)

employee1 = Employee("Vignesh", 25, 30000)
employee2 = Employee("Rahul" ,20, 45000 )

if employee1.name == "Vignesh":
    employee1.display()
    