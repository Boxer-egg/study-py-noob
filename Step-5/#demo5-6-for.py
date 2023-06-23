# demo5-6-for.py


UserWrite = input('录入你想分解的词语： ')
for item in UserWrite:
    print(item)

for _ in range(3):
    print('人生苦短，我用Python')


a = int(input('假装录入100 :'))
sum1 = 0  # 用于储存偶数的和
for i in range(0, a+1, 2):
    sum1 += i
print('您假装录入的数字是{},从0到这个数字的偶数合为：{}'.format(a, sum1))
