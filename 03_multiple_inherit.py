# multiple inheritance

class Employee:
    company = "Visa"
    eCode = 120


class Freelancer:
    company = "Fiverr"
    level = 0

    def upgraderLevel(self):
        self.level = self.level + 1


class Programmer(Employee, Freelancer):
    name = "Ali"


p = Programmer()
p.upgraderLevel()
print(p.upgraderLevel())  # not working why no idea
print(p.company)
