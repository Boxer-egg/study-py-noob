# demo8-3.py

s = {2, 2, 3, 3, 4, 5, 6}  # 元素不能重复
print(s, type(s))

ss = set(range(6))
print(ss, type(ss))

s3 = {2, 3}
print(s3.issubset(s))
print(s3.isdisjoint(s))


s2 = set('python')
print(s2, type(s2))
for i in s2:
    print(i, type(i))
# 集合只包含唯一的元素，而字典包含唯一的键和对应的值。

print(10 in s, 20 not in s)  # 集合的判断
s.add(2020)
print(s)
s.update({2323, 10, 1.1})
print(s)
s.remove(2323)
print(s)
s.pop()
print(s)

s2.pop()
print(s2)

s2.pop()
print(s2)
