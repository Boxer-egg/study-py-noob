# 5-5sum-jisuan.py

import pdb
# 从1到任意一个数的偶数合
head = 0
end = int(input('请输入到任意一个数，计算从0到他的偶数和'))
step = 2
sum2 = 0
# pdb.set_trace()

sum1 = range(head, end+1, step)
print('共计需要计算这些数字：', list(sum1))


sum2 = 0
while head <= end:
    # 在自增的head大于用户输入的数字时，结束.|当 head 的值小于或等于用户输入的 end
    sum2 += head  # sum2每次增加head
    head += step		# 0每次自增步长2
print(sum2)
