# 4-7demoB.py

# 键盘录入两个整数，然后比较大小

num_a = int(input('请输入数字A： '))
num_b = int(input('请输入数字B： '))

print('使用条件表达式比较')
print(str(num_a)+'大于等于'+str(num_b) if num_a > num_b
      else str(num_a)+'小于'+str(num_b))
# print(str(num_a) + '大于等于' + str(num_b) if num_a >
#      num_b else str(num_a)+'小于' + str(num_b))
