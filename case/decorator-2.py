def add(func):
    def inner2():
        x = func()
        num = int(x) + 1
        print(f"单纯+1.现在数字为{num},下一步")
        return num
    return inner2  # 返回函数对象而不是结果

def cube(func):
    def inner2():
        x = func()
        num = int(x) ** 3
        print(f"现在经历了cube，数字为{num},下一步")
        return num
    return inner2  # 返回函数对象而不是结果

def square(func):
    def inner2():
        x = func()
        num = int(x) ** 2
        print(f"让数字相乘了:{num},下一步")
        return num
    return inner2  # 返回函数对象而不是结果



@add
@cube
@square
def test():
    print('尝试一下头顶三个帽子')
    return 2


test()
print("完事了")