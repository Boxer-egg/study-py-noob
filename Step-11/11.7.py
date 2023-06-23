class A:
    pass


class B:
    pass


class C(A, B):
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 创建C类的对象
x = C('jack', 20)
print(x.__dict__)  # 实例对象的属性字典，显示了所有的实例变量
print(x.name, x.age)  # 打印实例对象的name和age属性
print(C.__dict__)  # 类对象的属性字典，显示了类的所有属性，包括方法和类变量
print('++++++++++')
print('对象所属的类', C.__class__)  
# 显示类C的类型，结果应该是type，因为C是type类型的一个实例
print(C.__bases__)  # 父类类型的元组，显示类C所有直接父类组成的元组
print(C.__base__)  # 显示类C的第一个（主）父类
print('查看类的层次结构', C.__mro__)  
# 显示类C的方法解析顺序(Method Resolution Order)，这是Python解决多继承问题的方法
print('子类', A.__subclasses__())  # 显示类A的所有直接子类组成的列表
