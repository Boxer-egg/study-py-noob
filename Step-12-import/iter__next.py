# iter__next.py

class CountDown:
    def __init__(self, start):
        self.current = start #current保存了倒计时的当前值。

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0: #小于等于零时，抛出StopIteration
            raise StopIteration 
            '''
当Python在迭代一个对象（例如在for循环中）时，
它会持续调用该对象的__next__方法，直到__next__方法抛出StopIteration异常。
这个异常告诉Python：没有更多的元素可以迭代了，迭代可以结束了。
            '''
        else:
            self.current -= 1
            return self.current + 1  #返回减去1之前的值
#每次迭代都会返回一个比前一次小1的数，直到数到0为止。

# 创建一个倒数的迭代器
counter = CountDown(5)
'''
创建了一个CountDown类的新实例，并把5传递给了__init__方法的start参数。
然后，__init__方法把这个值赋给了实例变量self.current。
这样self.current在这个新创建的CountDown对象中就有了一个初始值5
'''

# 迭代倒数
for num in counter:
    print(num)

'''
每次调用__next__方法，
它先检查self.current是否小于或等于0。
如果是，那么就抛出StopIteration异常，结束迭代。
否则，就把self.current减去1，然后返回减去1之前的值。
这样，每次迭代都会返回一个比前一次小1的数，直到数到0为止。

'''