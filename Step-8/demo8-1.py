# demo8-1.py


list1 = [100, 200, 11, 99]  # 可变序列
print(id(list1))
list1.append(1212)
print(id(list1), list1)

s = 'hello'  # 不可变序列
print(id(s))
s += ',word'
print(id(s))
print(s)

t = ('hello', 'Python', 'nihao', 110)
print(t)
t2 = tuple(('he', 'gazi', 123))
print(t2)
t3 = (1,)  # 元组中，只有一个元素，逗号不能省略
print(t3, type(t3))
t4 = 'hh', '123', 'ab'
print(t3, type(t4))

list1 = []
list2 = list()

dict1 = {}
dict2 = dict()

t5 = ()  # 空元组不用逗号了
t6 = tuple()

print(list1, list2, dict1, dict2, t5)
