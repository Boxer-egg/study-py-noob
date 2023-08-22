class Car(object):  # 定义一个父类，表示车
    def __init__(self, type, no):
        self.type = type  # 车的类型
        self.no = no  # 车牌号

    def start(self):  # 车的启动方法
        pass

    def stop(self):  # 车的停止方法
        pass


class Taxi(Car):  # 定义一个子类，表示出租车，继承自Car类
    def __init__(self, type, no, company):
        super().__init__(type, no)  # 调用父类的初始化方法，设置车的类型和车牌号
        self.company = company  # 出租车公司

    def start(self):  # 重写start方法
        print('乘客您好～～')
        print(f'我是{self.company}出租车公司，我的车牌是{self.no}')
        print('请问您要去哪里？')

    def stop(self):
        print('目的地到了，请您付费下车')


class FamilyCar(Car):  # 定义一个子类，表示家用车，继承自Car类
    def __init__(self, type, no, name):
        super().__init__(type, no)  # 调用父类的初始化方法，设置车的类型和车牌号
        self.name = name  # 车主的名字

    def start(self):
        print(f'我是{self.name}，我的汽车我做主。')

    def stop(self):
        print('目的地到了，我们去玩吧～～')


if __name__ == "__main__":
    taixi = Taxi('沃尔沃', '蒙D', '野马')  # 创建一个出租车实例
    taixi.start()  # 启动出租车
    taixi.stop()  # 停止出租车
    print('-' * 30)
    family_car = FamilyCar('还是沃尔沃', '蒙D', '小王')  # 创建一个家用车实例
    family_car.start()  # 启动家用车
    family_car.stop()  # 停止家用车

'''

一、`if __name__ == "__main__":` 
是一种常见的 Python 代码片段，用于测试模块是否被直接运行
。Python 有两种方式使用 .py 文件，一种是直接运行它，另一种是导入它作为模块。当你直接运行一个 .py 文件时，Python 解释器将把特殊的变量 `__name__` 设为 `"__main__"`，因此 `if __name__ == "__main__":` 将判断当前脚本是否被直接运行。
如果是，它将执行冒号后面的代码。

二、`__init__` 是一个特殊的方法，被称为类的构造器或初始化方法。
当你创建类的新实例时，`__init__` 方法将自动被调用。
你可以在 `__init__` 方法中设定实例的属性或执行其他初始化操作。

三、在子类中定义的方法会覆盖父类中相同名称的方法，这被称为方法覆写或方法重载。
如果你在子类中调用一个覆写的方法，它将执行子类中定义的版本，而不是父类中的版本。
如果你想在子类的方法中调用父类的版本，可以使用 `super().method()` 这样的语法。

'''
