# 4-3if.py
money = int(input('请输入你有多少钱：   '))
print('你有： ', money, '元人民币')
qvkuan = int(input('请输入你要取款多少元: '))

if qvkuan <= money:  # 条件表达式
    money = money - qvkuan
    print('请取款：', qvkuan, '剩余:  ', money)
else:
    print("您的余额不足，无法取款")
