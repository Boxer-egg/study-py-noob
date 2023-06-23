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

# 浅拷贝是对原对象值的拷贝，地址还是一个指针指向原对象的地址。
# 深拷贝是对原对象地址的拷贝，创建了一个与原对象地址不同的对象。
# 修改原对象中的任何值，都不会改变深拷贝的对象的值。但浅拷贝会变。

# 赋值只是换名字，浅拷贝是弄一个一模一样的新对象
# 赋值操作是让变量指向这个值所在内存空间


# 赋值
lst1 = [1, 2, [3, 4]]
lst2 = lst1
lst2[0] = 10
print(lst1)  # 输出：[10, 2, [3, 4]]，lst1也被改变了

# 浅拷贝
import copy
lst1 = [1, 2, [3, 4]]
lst3 = copy.copy(lst1)
lst3[0] = 10
print(lst1)  # 输出：[1, 2, [3, 4]]，lst1没有被改变
print(lst3)


lst3[2][0] = 30
print(lst1)  # 输出：[1, 2, [30, 4]]，lst1的子列表被改变了
