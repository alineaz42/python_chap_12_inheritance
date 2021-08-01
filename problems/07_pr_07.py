# did not complete this problem

class Vector:
    def __init__(self, vec):
        self.vec = vec

    def __str__(self):
        str1 = ""
        index = 0
        for i in self.vec:
            str1 = f"{i}a{index}"
            index += 1
        return str1[:-1]

    def __add__(self, vec2):
        newList = []
        for i in range(len(self.vec)):
            newList.append(self.vec[i]+vec2.vec[i])
        return Vector(newList)

    def __len__(self):
        return len(self.vec)


v1 = Vector([1, 2, 3])
v2 = Vector([5, 6, 7])
print(v1+v2)
print(len(v1))
