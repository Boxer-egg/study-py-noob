#11.9 - create - obj.py
# 117 __new__  __init__ 创建对象的过程

class Person(object):

    def __new__(cls, *args, **kwargs):  # __new__方法负责创建新的实例对象
        print('__new__被调用执行了.cls的值为：', id(cls))
        # 输出这个类的id，确认这个方法是由哪个类调用的
        obj = super().__new__(cls)  # 调用object的__new__方法来创建实例对象
        print('创建的对象的id为：', id(obj))
        # 输出新创建的实例对象的id，确认一个新的对象已经被创建
        return obj  # 返回新创建的实例对象


'''
至于你的问题"new也可以被赋值吗"，
我想你可能是想问在__new__方法中是否可以设置实例的属性。
答案是可以，但是通常不这么做。__new__方法主要用于控制对象的创建过程，
而__init__方法用于初始化新创建的实例。
通常，我们在__init__方法中设置实例的属性。

'''

    def __init__(self, name, age):  # __init__方法负责初始化实例对象
        print('__init__被调用了，self的值为', id(self))
        # 输出实例对象的id，确认这个方法是由哪个实例对象调用的
        self.name = name  # 设置实例对象的name属性
        self.age = age  # 设置实例对象的age属性


print('object这个对象的ID为：', id(object))  # 输出object类的id
print('Person这个对象的ID为：', id(Person))  # 输出Person类的id
print('----------------')
p1 = Person('ZhangSan', 22)  # 创建一个Person的实例对象p1
print('p1这个Person类的实例对象的ID', id(p1))  # 输出p1的id


'''
输出ID的目的是为了观察和验证__new__和__init__方法
调用的过程和对象的创建过程。通过比较ID，我们可以知道cls和Person是同一个对象，
self和obj是同一个对象，这就证明了__new__方法负责创建实例对象，
__init__方法负责初始化实例对象。

此外，通过对比p1的id和__new__方法创建的实例对象的id，
我们可以确认p1就是我们通过__new__方法创建的实例对象，
这就证明了Python创建实例对象的过程：先调用__new__方法创建实例对象，
再调用__init__方法初始化实例对象。'''


'''

object这个对象的ID为： 4309597304
Person这个对象的ID为： 5828227376
----------------
__new__被调用执行了.cls的值为： 5828227376
创建的对象的id为： 4303817616
__init__被调用了，self的值为 4303817616
p1这个Person类的实例对象的ID 4303817616

    首先，输出object类和Person类的id。这是为了展示object和Person是两个不同的对象。

    然后，创建一个Person的实例对象p1。在创建p1的过程中，
    首先会调用__new__方法创建一个新的实例对象。在__new__方法中，首先输出cls的id，
    然后调用object的__new__方法创建一个新的实例，然后输出新创建的实例的id，最后返回新创建的实例。

    在__new__方法返回新创建的实例后，会自动调用__init__方法初始化这个新创建的实例。
    在__init__方法中，首先输出self的id，然后设置实例对象的name和age属性。

    最后，输出p1的id，可以看到p1的id和__new__方法中创建的实例的id是相同的，
    这说明p1就是__new__方法创建的那个实例。

'''
