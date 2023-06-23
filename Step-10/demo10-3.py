# demo10-3.py


def fun1():
    print('hello,fun1')
    # return 'hello'


print(fun1())
# Python函数默认返回None，如果没有在函数中指定返回值。


def fun2():
    return 'hello'

#abc = fun2()
#print('abc', abc)


print('fun2', fun2())


def fun3():
    return '12', '22'


print(fun3(), '返回的是元组')


print('__带有返回的新代码__')


def fun(*num2):
    odd2 = []  # 奇数
    even2 = []  # 偶数
    for i in num2:
        if i % 2 == 1:
            odd2.append(i)
        else:
            even2.append(i)
    print('奇数列表：', odd2, '偶数列表：', even2)
    return odd2, even2


odd2_nums, even2_nums = fun(1, 2, 3, 11, 12, 10)

print(odd2_nums)


def fun123(a=None, b=10):
    return(a, b)


print()
print(fun123(b=100))
fun123(100, 222)
print(fun123(0, 1))
