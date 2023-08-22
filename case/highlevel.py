import time 

def logger(msg):
    def time_master(func):
        def call_func():
            start = time.time()
            func()  #这里给形参加括号，说明准备引入的是个函数
            stop=time.time()
            print(f"共计耗时{(start-stop):.2f}秒")
        return call_func
    return time_master

def funA():
    print()


def funB():
    print()
