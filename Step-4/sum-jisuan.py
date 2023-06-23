# sum-jisuan.py
import pdb

# 从1到任意一个数的偶数合
start = 0
end = int(input('请输入到任意一个数，计算从0到他的偶数和：'))
step = 2

# pdb.set_trace()

numbers = range(start, end+1, step)
print('共计需要计算这些数字：', list(numbers))

total = 0  # 用于储存偶数的和
for number in numbers:
    total += number

print('从0到{}的偶数和是：{}'.format(end, total))
