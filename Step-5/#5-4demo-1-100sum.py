# 5-4demo-1-100sum.py

# 1-100之间的偶数合

a = 0
sum = 0
while a < 101:  # a小于100时，停止循环
    sum += a    # sum=sum+a  a每次循环+2，sum没有改动
    a += 2      # a+2=a a每次自增2
    print('1~100的偶数合：', sum)   # 在循环内输出
