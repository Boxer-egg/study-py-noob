# demo10-4.py

def fun1(*agrs):  # 可变的位置参数
    print(agrs)


fun1('abc')
fun1(10, 20, 30, [1, 2, 3])


def fun2(**kwargs):
    print(kwargs)


fun2(a=1, b=2, c=3)


def fun3(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")
# .items()字典方法，返回一个包含字典所有（键，值）对的迭代器。


fun3(name='Alice', age=25, country='Canada')
# 输出：name = Alice
#       age = 25
#       country = Canada

False
# 列表、元组、字典、集合和字符串都可以被用于创建迭代器：
'''
是一个可以记住遍历的位置的对象。迭代器对象从集合的第一个元素开始访问，
直到所有的元素被访问完结束。迭代器只能往前不会后退。
'''
my_tuple = ("apple", "banana", "cherry")
my_it = iter(my_tuple)

print(next(my_it))  # 输出：apple
print(next(my_it))  # 输出：banana
print(next(my_it))  # 输出：cherry
# print(next(my_it))  # 抛出 StopIteration 异常
