# 11.10 - copy.py

class CPU():
    pass


class DISK():
    pass


class Computer():
    def __init__(self, CPU, DISK):
        self.CPU = CPU
        self.DISK = DISK


# 1、变量赋值
cpu1 = CPU()
cpu2 = cpu1
print(cpu1, id(cpu1))
print(cpu2, id(cpu2))

print('2.类的浅拷贝')

disk = DISK()  # 创建硬盘类的对象
computer = Computer(disk, cpu1)  # 创建计算机类的对象

import copy
computer2 = copy.copy(computer)
print(computer, computer.CPU, computer.DISK)
#<__main__.Computer object at 0x101015e90>
# <__main__.DISK object at 0x101015e50> <__main__.CPU object at 0x101015e10>
print(computer2, computer2.CPU, computer2.DISK)
#<__main__.Computer object at 0x100f76790>
#<__main__.DISK object at 0x101015e50> <__main__.CPU object at 0x101015e10>

# 浅拷贝会有两种类型
# 1. 引用类型：原对象的数据改变后，浅拷贝的新对象数据也会改变
# 2. 非应用类型：原对象的数据改变后，浅拷贝的新对象数据**不会改变**。同理，新对象的数据改变后，原对象的数据**也不会改变**。

# 深拷贝创建了一个与原对象完全独立的新对象，新对象的所有字段（无论是引用类型还是非引用类型）都是原对象的一份拷贝，所以新对象和原对象完全不共享任何数据。


# 赋值只是换名字，浅拷贝复制了新对象。新对象和原对象共享了引用类型的数据。
# 赋值操作是让变量指向这个值所在内存空间


'''
引用类型：

列表（list）
字典（dict）
集合（set）
类和对象
元组（tuple）（虽然元组本身是不可变的，但它可以包含可变的引用类型，如列表）
函数
模块
非引用类型（也被称为基本类型或值类型）：

整数（int）
浮点数（float）
布尔值（bool）
字符串（str）
None

需要注意的是，虽然字符串看起来像引用类型（因为它们可以是任意长度，并且有一些类似引用类型的行为），
但在Python中，字符串实际上是不可变的，所以它们被视为非引用类型。
当你修改一个字符串时，Python实际上是创建了一个新的字符串。

同时，虽然元组（tuple）是一个引用类型，但由于它的不可变性，
它在很多情况下的行为更像非引用类型。
例如，当你对一个元组进行浅拷贝时，由于元组本身是不可变的，
所以你不能在新的元组上进行任何修改，这与非引用类型的行为相同。
然而，如果元组中包含了可变的引用类型（如列表），
那么这部分数据在浅拷贝中仍然是共享的。
'''

# 赋值
lst1 = [1, 2, [3, 4]]
lst2 = lst1
lst2[0] = 10
print(lst1)  # 输出：[10, 2, [3, 4]]，lst1也被改变了

# 浅拷贝

lst1 = [1, 2, [3, 4]]
lst3 = copy.copy(lst1)
lst3[0] = 10
print(lst1)  # 输出：[1, 2, [3, 4]]，lst1没有被改变
print(lst3)


lst3[2][0] = 30
print(lst1)  # 输出：[1, 2, [30, 4]]，lst1的子列表被改变了

print('深拷贝')
computer3 = copy.deepcopy(computer)
print(computer3, computer3.CPU, computer3.DISK)
print(computer, computer.CPU, computer.DISK)

#值都不相同
