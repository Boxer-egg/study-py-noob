import time


def logger(msg):
    def time_master3(func):
        def call_func():
            start = time.time()
            func()
            stop = time.time()
            print(f"[{msg}]一共耗费了{(stop-start):.3f}")
        return call_func
    return time_master3


@logger(msg="A")
def funA():
    time.sleep(1)
    print("正在调用 A ……")


@logger(msg="B")
def funB():
    time.sleep(1)
    print("正在调用 B ……")


funA()
funB()

# funA() = logger(msg="A")  # 得到 time_master 的引用。
# funA() = logger(msg="A")(funA)  # 得到 call_func 的引用。
