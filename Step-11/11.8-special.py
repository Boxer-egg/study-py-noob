a = 100
b = 12
c = a + b

d = a.__add__(b)  # 使用内置类int的__add__方法进行加法操作


class Student:
    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        # 重写__add__这个特殊方法，让两个Student实例可以进行"+"操作，返回他们name的拼接
        return self.name + other.name

    def __len__(self):
        # 重写__len__这个特殊方法，使得len()函数可以返回Student实例的name属性的长度
        return len(self.name)


print(c, d)

stu1 = Student('zhangsan')
stu2 = Student('wangwu')

s = stu2 + stu1  # 实际上调用了stu2.__add__(stu1)，返回了两个实例的name属性的拼接
print(s)

s1 = stu1.__add__(stu2)  # 直接调用__add__方法，效果与上面一样
print(s1)

print(len(stu1))  # 调用了stu1的__len__方法，返回了stu1的name属性的长度
