# demo10-1.py
def calc(a, b):  # 形式参数，形参
    c = a+b
    return c


a = calc(10, 20)  # 实际参数的值，实参。实参是函数的调用处
print(a)


def greet(*names):
    for name in names:
        print("Hello, " + name + "!")


greet("Alice", "Bob", "Charlie")
