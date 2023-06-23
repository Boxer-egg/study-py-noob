#11.4-re.py

# 我们将会讨论Python的面向对象编程的基础知识，包括类、实例、属性、方法、继承等概念。

class Person(object):  
# 这是我们的父类Person，所有的Person对象都会有两个属性：name和age。注意，在Python 3中，所有类都隐式地继承自object，因此这里的"(object)"可以省略。

    def __init__(self, name, age):  
    # 这是类的初始化方法。当我们创建一个新的Person对象时，Python会自动调用这个方法。self是对实例本身的引用，name和age是我们传入的参数。
        self.name = name  
        # 我们将参数name的值赋给实例属性self.name。这样，每个Person实例都会有自己的name属性，其值由我们在创建实例时指定。
        self.age = age  
        # 同理，我们将参数age的值赋给实例属性self.age。

    def info(self):  
    # 这是一个实例方法。它可以通过Person的实例来调用，输出实例的name和age属性。
        print(self.name, self.age)

class Student(Person):  
# 这是一个子类，它继承自Person类。这意味着Student类会自动获得Person类的所有属性和方法。我们可以添加或重写方法以定制子类的行为。

    def __init__(self, name, age, Stu_Num): 
    # 这是子类的初始化方法。注意，我们增加了一个新的参数Stu_Num。
        super().__init__(name, age)  
        # 使用super()函数调用父类的初始化方法，为name和age属性赋值。这样，我们就不需要直接复制父类的代码。
        self.Stu_Num = Stu_Num  
        # 新增的实例属性，只有Student类的实例才有。

    def info(self):  
    # 我们在子类中重写了info方法。当我们调用Student实例的info方法时，Python会运行这个版本，而不是父类中的版本。
        print(self.Stu_Num, end=",")  
        # 首先，我们输出Student实例的Stu_Num属性。
        super().info()  
        # 然后，我们使用super()函数调用父类的info方法，输出name和age属性。注意，这里没有重复父类的代码，而是直接使用了父类的方法。

# 下面，我们创建一个Student实例，并调用它的info方法。
stu = Student('章三', 20, '001')  
# 创建一个Student实例。注意，我们需要提供所有的参数，包括从Person类继承的name和age，以及Student类特有的Stu_Num。
stu.info()  
# 调用实例的info方法。它会先输出Stu_Num，然后输出name和age。


# 我们首先定义一个名为Person的类，这是一个基类（Base Class）或父类（Superclass）。
class Person(object):  
    # 这是类的初始化方法，它是一个特殊的方法，每当我们创建一个新的类实例时，它都会被自动调用。
    # 第一个参数self代表类的实例。name和age是我们要赋给每个实例的属性。每个实例都有自己的name和age属性，并且它们的值可能不相同。
    def __init__(self, name, age):  
        self.name = name  
        self.age = age

    # 这是一个实例方法，它用于输出Person实例的name和age属性。我们可以通过实例名称调用它，例如person.info()。
    def info(self):  
        print(self.name, self.age)  

# 现在我们定义一个新的类，名为Student。注意这个类的定义是在括号内指定了Person，这表示Student类是从Person类继承的。
class Student(Person): 
    # 在子类的初始化方法中，我们首先调用父类的初始化方法来设置name和age属性，然后设置子类特有的Stu_Num属性。
    def __init__(self, name, age, Stu_Num):  
        super().__init__(name, age)  
        self.Stu_Num = Stu_Num

    # 在子类中，我们重写（Override）了父类的info方法，这样当我们调用Student实例的info方法时，它将首先输出Stu_Num属性，然后输出继承自父类的name和age属性。
    def info(self):  
        print(self.Stu_Num, end=",")  
        super().info() 

# 创建一个Student类的实例，并通过参数提供所需的属性值。这个过程被称为实例化（Instantiation）。现在，stu就是一个Student类的实例（也是Person类的实例，因为Student是Person的子类）。
stu = Student('章三', 20, '001')  

# 调用stu实例的info方法，输出stu的属性值。首先输出Stu_Num属性，然后输出继承自父类的name和age属性。
stu.info()  

