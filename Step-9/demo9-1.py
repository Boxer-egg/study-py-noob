# demo9-1.py

s = 'hello,hello'

print(s.index('lo'))
print(s.rindex('lo'))
print(s.find('lo'))
print(s.rfind('lo'))


# 大小写转换

s1 = 'hello,python abc'
s2 = 'HELlo,PYHTon,ABC'
print('全大全小:', s1.upper(), s1.lower())

print(' switch:', s1.swapcase(), s2.swapcase())
print('title:', s1.title(), s2.title())
print('cap:', s1.capitalize(), s2.capitalize())
