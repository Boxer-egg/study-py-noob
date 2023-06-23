# demo6-8-update.py

list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(id(list1))
list1[2] = 100   # 一次修改一直值
print(id(list1), list1,)
list1[1:4] = [100, 200, 300]  # 一次修改范围值。

print(list1[::-1])  # 倒叙
print(id(list1), list1)
