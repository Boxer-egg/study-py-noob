# 4-4ifelse.py 双分支结构
"""
录入整数，编写程序，判断是基数还是偶数
"""

a = int(input("请输入数字： "))
b = a % 2
print(type(b))
if b == 1:
    print('你输入的是奇数')
else:
    print("偶数啦")

'''

a = int(input("请输入数字： "))
if a % 2 == 1:
    print('你输入的是奇数')
else:
    print("偶数啦")

'''
