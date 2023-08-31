def fibIter(n):
    a = 1
    b = 1
    c = 1
    while n > 2:
        c = a + b
        a = b
        b = c
        n -= 1
    return c


def fibIter1(n):
    if n <= 0:
        return "n should be a positive integer"
    a, b = 1, 1
    for _ in range(n-2):
        a, b = b, a + b
    return b


'''
下划线 _ 通常用作“不关心这个变量”的占位符。
当你在循环中不打算使用到该变量时，可以使用下划线。这样做可以提高代码的可读性。
'''

print(f"老师写的：{fibIter1(6)}")

print(fibIter(6))
