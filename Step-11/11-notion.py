#11 - notion.py

class Computer():  # 定义了一个类，类名为Computer
    maker = "M88ultra"  # 这是一个类属性，它是类的一部分，所有的类实例都可以访问

    def __init__(self, cpu, ram):  # 这是一个特殊的方法，称为构造方法
        # self代表类的实例，cpu和ram是传入的参数
        # 下面的语句定义了两个实例属性，它们是类实例的一部分，每个实例都有自己的cpu和ram属性
        self.cpu = cpu
        self.ram = ram

    def run(self, program):  # 这是一个实例方法，只有类的实例才能调用
        print(f"Running {program} on {self.cpu} with {self.ram}GB RAM")


def greet():  # 这是一个函数，它不属于任何类，可以在程序的任何地方调用
    print("Hello, world!")


# 创建了一个Computer类的实例，my_computer就是一个实例对象
my_computer = Computer("Ryzen 99 Max", 32)

my_computer.run("Python")  # 调用实例的方法
print('Computer类的cpu实例属性：', my_computer.cpu)  # 访问实例的属性

greet()  # 调用函数


'''
这段代码定义了一个类（Computer），类中包含一个类属性（maker）、
两个实例属性（cpu和ram）、一个构造方法（__init__）和一个实例方法（run）。
然后，我们创建了这个类的一个实例（my_computer），
并通过这个实例调用了实例方法和访问了实例属性。最后，我们调用了一个函数（greet）。
'''
