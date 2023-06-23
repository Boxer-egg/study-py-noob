# P24 比较运算符
a, b = 20, 30

print('a>b吗？', a > b)  # false

print('a<=b吗？', a <= b)  # true

print('a!=b吗？', a != b)


"""一个等号（=）赋值运算符
两个等号（==），比较运算符

一个变量三部分组成：标识、类型、值
== 比较的是值
is  比较标识

"""

a, b = 10, 11

a = 10
b = 10

print(a == b)
print(a is b)


list1 = [11, 22, 33, 44]
list2 = [11, 22, 33, 44]

print('查看标识（ID）', id(list1), id(list2))

print('比较值：', list1 == list2)  # 值 value
print('比较标识', list1 is list2)  # 标识  id

print(a is not b)  # 比较a和b的标识（ID）是否相等

print(list2 is not list1)
