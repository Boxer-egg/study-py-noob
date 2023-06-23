# demo5-8pswd-2.py

a = 0
while a < 3:
    pwd = input('请输入密码：')
    if pwd == '123':
        break
    else:
        print('不对')
        a += 1
else:
    print('再见')
