#11.4-inherit.py

#11.4-inherit.py

class Person(object):  # 定义一个Person的类，python3中，object可以不填写，Python 3 中所有类默认都继承自object。
    def __init__(self, name, age):  # 每一个类都有__init__方法。默认参数为self，代表实例本身。self.name和self.age是实例属性，每个实例各自拥有一份，每个实例的值可能不相等。
        self.name = name  # self.name是实例属性，name是方法的参数，这里将参数的值赋给实例属性。
        self.age = age
    def info(self):  # 定义一个实例方法info，该方法将在实例上调用。
        print(self.name, self.age)  # 方法的实现方式，为输出name和age的值。或者说输出self.name和.self.age的属性。

class Student(Person):  # 新建子类Student，父类为Person。
    def __init__(self, name, age, Stu_Num):  # 初始化子类自己的实例属性。
        super().__init__(name, age)  # 使用super调用父类的__init__方法，为继承自父类的属性赋值。
        self.Stu_Num = Stu_Num  # 子类新增的实例属性。
    def info(self):  # 在子类中重写父类的info方法。
        print(self.Stu_Num, end=",")  # 输出Student实例自身Stu_Num的值。end=','意味着在此行输出结束后不换行。
        super().info()  # 调用父类的info方法，输出继承自父类的属性。



class Teacher(Person):
	def __init__(self, name,age,YearOfTeacher): 
		super().__init__(name,age)
		self.YearOfTeacher = YearOfTeacher
	def info(self): #重写了父类(Person)的info方法
		print('教龄：',self.YearOfTeacher,end=",")
		super().info()

stu=Student('章三',20,'001')  # 创建一个Student类的实例，并提供必要的参数。
tc=Teacher('莉丝',41,12)

stu.info() # 调用Student实例的info方法，输出该实例的属性值。
tc.info()
abc.info()