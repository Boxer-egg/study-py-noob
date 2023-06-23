# demo9-2.py

s = 'hello,python'
ss = s.title()
print(s, ss)
print(ss.center(22, '*'))
print(ss.ljust(25, "!"))
print(ss.rjust(25, "!"))
print(ss.zfill(19))


aa = [1, 2, 3, 4, 5]
squares = [number ** 2 for number in aa]
print(squares)

nb = [1, 2, 3, 5]
a = [shuzi ** 2 for shuzi in nb]
print(a)


s4 = '''
https://www.bilibili.com/video/
BV1wD4y1o7AS?p=80&spm_id_from=pageDriver&vd_source
=ff66893fb81121d2b498f13bea2023e9
'''
parts = s4.split('/')

# 使用列表推导式中的 'for' 循环来解包嵌套列表
parts = [subpart for part in parts for subpart in part]
print(parts)
