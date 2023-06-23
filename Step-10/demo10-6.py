# demo10-6.py

def fun1(num):
    if num == 1:     # 基本情况
        return 1
    else:             # 递归情况
        res = num*fun1(num-1)    # 先递推，再回归
        return res


print(fun1(6))

'''
基本情况（base case）：这是函数将返回一个结果而不再递归的情况。
在设计递归函数时，必须有一个或多个基本情况来避免无限递归。
递归情况（recursive case）：这是函数进行递归调用的情况。在这种情况下，
函数通常会把问题分解成更小的问题，然后递归地求解这些更小的问题。这个过程被称为“递推”。
'''

# 6的阶乘。 6*（6-1）


def factorial_for(n):    # 定义一个函数，命名为：factorial_for，可录入参数：n
    result = 1           # result 取值为1，既阶乘最后都是乘到1
    for i in range(1, n + 1):  # 建立range循环，循环生成数据赋值i，从1开始，生成到n+1，但不包含n+1
        result *= i  # result=result*i 每一次将i的值带入计算，。每次循环的i赋值时，计算公式
    return result  # 最后将返回循环完成的result的值


print(factorial_for(5))  # 输出: 120


def factorial_for(n):
    # 定义一个名为"factorial_for"的函数，它接受一个参数n，代表我们要计算阶乘的数。
    result = 1
# 初始化一个变量result，将它设置为1。这是因为阶乘运算是乘法运算，开始时我们需要一个乘法的单位元素，就是1。

    for i in range(1, n + 1):
        # 对于每一个在1到n（包括n）的整数i，我们都会执行以下的操作。这个循环会依次处理这些数。
        result *= i
# 我们将result与i相乘，然后把结果存回result。这就实现了阶乘的计算过程，因为阶乘就是将一系列的数相乘。

    return result
# 我们返回result，这就是n的阶乘。


print(factorial_for(5))
# 我们调用这个函数来计算5的阶乘，并将结果打印出来。应该得到的结果是120，因为5的阶乘就是120。
