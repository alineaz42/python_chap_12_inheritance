# video 10:40
class Employee:
    company = "Gas bd"
    salary = 5000
    salaryBonus = 500

    # property decorator
    # getter
    @property
    def totalSalary(self):
        return self.salary+self.salaryBonus

    # setter
    @totalSalary.setter
    def totalSalary(self, val):
        self.salaryBonus = val - self.salary


e = Employee()
e.totalSalary = 7000
print(e.salaryBonus)
print(e.salary)
print(e.totalSalary)
print(e.company)
