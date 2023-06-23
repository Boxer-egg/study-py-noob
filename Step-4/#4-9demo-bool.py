# 4-9demo-bool.py
# 通过对象的布尔值快速判断
age = int(input('请输入你的年龄： '))

if age and 120 > age > 0:
    print('图灵验证通过，您是人类，您的年龄为：', age)

else:
    print("录入非法")
