# demo6-9sort.py
list1 = [1, 2, 33, 4, 55, 12, 0]
print('原始列表', list1, id(list1))
print(list1.sort())
list1.sort()
print(list1, id(list1))


list2 = sorted(list1)  # sorted()函数 新建
print(list2, id(list2))

list1.sort(reverse=True)  # True 是降序
print(list1)


list3 = sorted(list1, reverse=False)
print(list3, '生序排序，默认行为')
list3 = sorted(list1, reverse=True)
print(list3, '降序排序')
