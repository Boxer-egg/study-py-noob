# test123.py


def fibonacci():
    a, b = 0, 1
    while True:  # 无限循环语句
        yield a  # 调用时，返回一个生成器对象。这个对象可以使用next()函数或者for循环来获取其返回的值。
        a, b = b, a + b


# 创建一个生成器对象
fib = fibonacci()

# 生成前5个斐波那契数
for i in range(5):
    print(next(fib)) #next不能后退

import time


class Timer:
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.time()
        print(f'Elapsed time: {self.end - self.start}')


# 使用自定义的上下文管理器
with Timer():
    for _ in range(9999999):
        pass
