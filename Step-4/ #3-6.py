# 3-6.py
# 布尔运算

a, b = 1, 2
print('___and  并且__')
print(a == 1 and b == 2)  # t and t = ture
print(a == 1 and b > 2)

print(a != 1 and b != 2)  # F and F = false

print('__或者  or_')
print(a == 1 or b != 2)
# print(a != 1 or b != 2)

print('__不是  not|bool类型（整数）的操作数取反_')


t, f = True, False
t = True
f = False

print(not t)

print(not f)

print('---in和not in---')

s1 = 'helloworld'
print('w' in s1)
print('a' in s1)
print('e' not in s1)
print('E不在helloword里面', 'E' not in s1)
