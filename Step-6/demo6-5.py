# demo6-5.py

list1 = [10, 20, 30, 'hello', 'python']
print(10 not in list1, 'hello' in list1, 'py'not in list1)


list2 = [list(range(0, 10, 2)), 3, 'hello']
# list(range())将range对象转换为列表
print(list2, 2 not in list2)

print(range(10, 2))


for i in range(0, 10, 3):  # 0,3,6,9
    i += 1      # # 0+1,3+1,6+1,9+1
    print(i)

print('列表元素的遍历')

for item in list2:
    print(item)
