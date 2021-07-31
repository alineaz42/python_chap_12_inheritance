class Employee:
    company = "Camel"
    salary = 1000
    location = "Dhaka"

    @classmethod
    def changeSalary(cls, sel):
        cls.salary = sel  # to change the class vars


e = Employee()
e.changeSalary(500)
print(e.salary)
print(Employee.salary)
