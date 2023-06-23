# demo7-2.py

student = {'章三': 100, '李四': 99, '王五': 98, '麻六': 59, '红七': 120}
keys = student.keys()
values = student.values()
items = student.items()

print(len(student))
print('输出keys（键） ：', student.keys())
print('输出values（值）：', student.values())
print('输出items（全部）：', student.items())

print(type(keys), list(keys))  # 将所有的keys组成的视图，转成列表
print(type(values), list(values))
print(type(items), list(items))
print(items)  # 元组（）

for i in student:
    print(i, student[i], student.get(i))
