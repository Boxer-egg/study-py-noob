# demo7-1.py
# 创建字典

scores = {'章三': 40, 'lisi': 50, '我': '想要更多'}  # 新建字典方法1
print(scores)
print(type(scores))

student = dict(name='jack', age=20, name2='rose', age2=22)  # 新建字典方法2
print(student)


dd = {}  # 空字典
ff = dict()  # 空字典
print(dd, ff)


# 获取字典中的元素
print('指定键（我），查看值：', scores['我'])
print('指定键（lisi），查看值：', scores.get('lisi'))
print('指定键（不存在），查看值：', scores.get('你瞅啥'))  # None
print('指定键（不存在，但输出默认），查看值：', scores.get('你瞅啥', '瞅你咋地'))  # 瞅你咋地

print('我' in scores)     # 判断值，是否存在字典内
print('我' not in scores)


del scores['我']  # 删除指定键值对
scores.clear()  # 清空字典
print(scores)

scores['陈六子'] = 59  # 新增元素
print(scores)
scores['陈六子'] = 61  # 新增元素
print(scores)


print(len(student))
print('输出keys（键） ：', student.keys())
print('输出values（值）：', student.values())
print('输出items（全部）：', student.items())
