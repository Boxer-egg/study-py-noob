# demo5-10-else.py
a = 0
while a < 3:
    pwd = input('请录入密码：  ')
    if pwd == '123':
        print('duile')
        break
    else:
        print('再来一次')
    a += 1
else:
    print('meijihuile')
