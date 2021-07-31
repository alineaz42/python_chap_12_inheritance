

class Person:
    country = "Bd"
    company = "hululu"

    def takeBreath(slef):
        print("I am breathing from person")


class Employee(Person):
    # company = "Google"
    salary = 120

    def getSalary(self):
        print(f"Salary is {self.salary}")

    # def takeBreath(slef):
    #     print("I am an employee i am ....  from employee ")


class Programmer(Employee):
    # company = "Fiver"

    def getSalary(self):
        print("No salary to programmers")

    # def takeBreath(slef):
    #     print("I am a programmer luckily brathing")


p = Person()
e = Employee()
pr = Programmer()
# p.takeBreath()
e.takeBreath()
pr.takeBreath()
# print(pr.company)
print(pr.company)
print(pr.country)
