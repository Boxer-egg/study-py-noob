# demo6-6-add.py

list1abc = [1, 2, 3, 4, 5]
print('打印list1：', list1abc, '查看ID:', id(list1abc))
list1abc.append(100)
print(list1abc, id(list1abc))


list2abc = ['h', 'e', 'l', 'l', 'o']
list1abc.append(list2abc)
print(list1abc, 'append把列表当作一个元素插进去')
list1abc.extend(list2abc)
print(list1abc, 'extend将列表内元素插入进去')


print('任意位置添加，例如，索引1的位置，添加‘ABC’')
list1abc.insert(1, 'ABC')
print(list1abc)

list3 = [True, False, 'hello']
print(list3)
list1abc[1::] = list3
print(list1abc, '只留第一位，后面加上列表list3')
