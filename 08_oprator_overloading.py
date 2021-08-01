class Number:
    def __init__(self, num):
        self.num = num

    def __add__(self, num2):
        print("Let's add")
        return self.num+num2.num

    def __mul__(self, num2):
        print("Lets multiply")
        return self.num*num2.num


# search for overloading google
n1 = Number(4)
n2 = Number(6)
sum = n1+n2
mul = n1*n2
print(sum)
print(mul)


'''
Operator Magic Method
+ __add__(self,other)
- _sub__(self,other)
* __mul__(self,other)
/ __truediv__(self,other)
// __floordiv__(self,other)
% __mod__(self,other)
** __pow__(self,other)
>> __rshift__(self,other)
<< __lshift__(self,other)
& __and__(self,other)
| __or__(self,other)
^ __xor__(self,other)
///
Operator	Magic Method
<	__LT__(SELF, OTHER)
>	__GT__(SELF, OTHER)
<=	__LE__(SELF, OTHER)
>=	__GE__(SELF, OTHER)
==	__EQ__(SELF, OTHER)
!=	__NE__(SELF, OTHER)
///
Operator	Magic Method
–	__NEG__(SELF, OTHER)
+	__POS__(SELF, OTHER)
~	__INVERT__(SELF, OTHER)
'''
