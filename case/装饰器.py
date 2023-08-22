import time
def myfun():
    print("正在调用myfun函数。。")

def repaot(fun):
    print("要开始了~~")
    fun()
    print("调用完成。")

repaot(myfun)
#要开始了~~
#正在调用myfun函数。。
#调用完成。


        

def time_master(func):
    print("一个函数为另一个函数的参数：~start~")
    start=time.time()
    func()
    stop = time.time()
    print(f"共计执行:{(stop-start):.3f}秒")

def myfun1():
    time.sleep(1)
    print("咆哮~")
time_master(myfun1)

#新写一个
print("---"*20)
time.sleep(2)

def time_master1(func):
    '''
    1.装饰器本质上是一个函数，它接受一个函数作为参数，并返回一个函数。
    这个返回的函数通常是对输入函数进行了一些增强或修改的版本。
    2.装饰器允许您在不修改原始函数代码的情况下为其添加额外的功能。

    '''
    def call_func():
        print("新写的，开始执行~")
        start =time.time()
        func()
        stop=time.time()
        print(f"结束了。。。")
        print(f"共计执行{(stop-start):.3f}秒")
    return call_func


@time_master1  #myfun2 = time_master1(myfun2)
def myfun2():
    print("开始执行和结束中间插入一下,并等1S。")
    time.sleep(1)


myfun2()
    

# test=time_master1(myfun2)
# test()
# test() = myfun2()  不加@的情况下。
# 调用 myfun2时，不是直接调用，而是将myfun2 这个函数，作为参数，放到上面的装饰器里面。然后调用装饰器


'''





3. **装饰器的参数和返回值**：

    在您的`time_master1`装饰器中，您传入了一个`func`参数，这是您想要增强的函数。
    您返回了一个新函数`call_func`，它在调用时首先执行一些额外的代码，
    然后调用原始的`func`函数，之后再执行其他一些代码。

4. **注意事项**：

    您的装饰器目前仅适用于不接受任何参数的函数。如果您希望装饰器能够处理带有参数的函数，
    您需要修改装饰器的内部函数以使其能够接受并传递参数。这通常是通过使用`*args`和`**kwargs`完成的。


    def time_master1(func):
        def call_func(*args, **kwargs):
            # ... original code ...
            func(*args, **kwargs)
            # ... original code ...
        return call_func
'''