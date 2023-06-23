# 5-5-sum.py

# 求偶数或奇数的和
add = int(input('你想要求偶数和还是奇数和？0（偶数）、1（奇数）'))
while add not in [0, 1]:
    add = int(input(print('只能输入‘0’[偶数]或者‘1’[奇数]哦')))
num = int(input('请输入最终数字： '))

print(sum(range(add, num+1, 2)))
