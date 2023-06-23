# 5-1-range.py

print('查看让range（）内单个数字10')
r = range(10)
print(r)
print(list(r))


print('查看让range（）内两个数字，199，210')
x = range(199, 210)
print(x)
print(list(x))

print('有开头、有结尾、有步长')
start = 200
a = 400
step = 5
y = range(start, a+1, step)
print(y)
print(list(y))


print(10 in y)
