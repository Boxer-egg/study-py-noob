# demo9-5.py
s = 'hello,Python'
print(s.replace('Python', 'JavaSripte'))

s1 = 'hello,Python,Python,Python'
print(s1.replace('Python', 'JavaSripte', 2))

list1 = ['hello', 'python', 'Java']
print('.||.'.join(list1))


t = ('hello', 'python', 'java')
print('--'.join(t))
print('python'.join('***'))
'''
.join() 方法将 '***' 的每个字符（即，每个 '*'）连接成一个字符串，
并在每个字符之间插入 'python'。所以，结果是 '*python*python*'。
'''
print('python'.join('**')
      )  # 'python'.join('**') 的结果是 '*python*'，因为在两个 '*' 之间插入了 'python'。
print('python'.join('*'))  # 没地方插入python


print('*'.join('python'))


print(ord('王'))
print(chr(29579))
