# demo6-7-remove.py

list1 = [1, 2, 3, 4, 5, 6, 2]
print('原始列表', list1)
list1.remove(2)
print('remove2列表', list1)

list1.pop(1)
print('pop1删除第二位', list1)
list1.pop()
print('pop()最后一位', list1)


new_list1 = list1[1:3]  # 0,1,2,3, 不包括3
print('切片后[1,3]', new_list1)
list1.clear()
print(list1)
del new_list1
# print(new_list1)  #is not defined
