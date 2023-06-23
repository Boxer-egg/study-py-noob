
class Student:
    native_pace='内蒙' #直接写在类里的变量，就是类属性
    
    def __init__(self,name,age):
        self.name=name # self.name 实体属性，进行赋值操作，将局部变量的name的值赋给实体属性。
        self.age=age

    #实例方法
    def eat(self):
        print('学生在吃饭')

    #静态方法
    @staticmethod
    def method():
        print('我使用了staticmethod进行修饰，所以我是静态方法')
    
    # 类方法
    @classmethod
    def cm(cls):
        print('我是类方法，使用了classmethod')


sut1=Student('张三',20)
print(sut1.name)
print(sut1.age)
print(sut1.eat)
sut1.eat()  #对象名.方法名（）
Student.eat(sut1) #同上一行
#类名.方法名(类的对象) ——》方法定义处的self
print('看ID',id(sut1.eat))

print('输出类属性：',Student.native_pace)
Student.native_pace='合肥'
print('输出类属性：',Student.native_pace)

Student.cm()
Student.method()

#print(id(stu1),type(sut1),sut1)
print(id(Student),type(Student),Student)
	
# def 类外定义的为函数，类内定义的叫方法

