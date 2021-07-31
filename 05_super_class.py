# super is called to call constructer

class Person:
    country = "Bd"
    company = "hululu"

    def __init__(self):
        print("Initalizing ther person \n")

    def takeBreath(slef):
        print("I am breathing from person super class")


class Employee(Person):
    company = "Google"
    salary = 120

    # def __init__(self):
    #     super().__init__()
    #     print("Init the person init")

    def getSalary(self):
        print(f"Salary is {self.salary}")

    def takeBreath(slef):
        super().takeBreath()
        print("I am an employee i am ....  from employee ")


class Programmer(Employee):
    company = "Fiver"

    def __init__(self):
        super().__init__()
        print("super from programmer")

    @staticmethod
    def getSalary(self):
        print("No salary to programmers")

    def takeBreath(slef):
        super().takeBreath()
        print("I am a programmer luckily brathing")


p = Person()
e = Employee()
pr = Programmer()
pr.takeBreath()
# pr.takeBreath()
# e.takeBreath()
# pr.getSalary()
