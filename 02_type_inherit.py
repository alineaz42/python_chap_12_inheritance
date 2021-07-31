# single inheritance
# multiple inheritance
# multilevel inheritance

# !1 single inheritance
# video 9:50Hours

class Employee:
    company = "Google"

    def __init__(self):
        print("Hello dear boy")

    def showDetails(self):
        # print("This is an employee")
        return "This is an employee"


class Programmer(Employee):
    language = "Python"
    company = "YouTube"

    def getLan(self):
        # print("The language is Python")
        return f"The language is {self.language}  "

    def showDetails(self):  # over writting of showDetails()
        print(f"This is a programmmer  and company is {self.company} ")


e = Employee()
p = Programmer()
p.showDetails()
# print(p.showDetails())
# # p.getLan()
# print(p.getLan())
# print(p.showDetails())
