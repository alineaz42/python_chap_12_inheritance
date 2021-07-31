# video 9:50Hours
class A:
    company = "Google"

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("form parent class")

    def getInfo(self):
        print(
            f"Company name is {self.company} name is: {self.name} age: {self.age} ")


class B(A):
    company = "YouTube"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getAge(self):
        # name was called from Class A
        print(f"The age of:{self.name} is:{self.age} ")


person1 = A("Ali Neaz", 23)
person1.getInfo()
person2 = B("Shakil Ahamed", 24)

person2.getInfo()
