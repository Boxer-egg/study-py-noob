# 5-3demowhileSum.py

# 0~4之间的累加和

"""
1.初始化变量
2.条件判断
3.条件执行题(循环体)
4.改变变量
"""
import time
b = 0
sum = 0
while b < 5:
    sum += b
    print(b)
    b += 1


print(sum)
"""
b  b<5 sum   sum+b=sum
0  Ture 0    0
1  Ture  1    0+1
2  Ture  3     1+2
3  Ture  6     3+3 
4  Ture  10    6+4
5  False 


"""
