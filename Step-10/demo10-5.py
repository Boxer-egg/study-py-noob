# demo10-5.py

def fun(a, b, c):
    print('a=', a)
    print('b=', b)
    print('c=', c)


fun(10, 20, 30)

fun(list[10], 1, 2)

list2 = [44, 55, 66]
fun(*list2)

dict1 = {'a': 111, 'b': 222, 'c': 333}
fun(**dict1)


def fun2(a, b, *, c, d):
    print('a=', a, 'b=', b, 'c=', c, 'd=', d)


fun2(10, 20, c='11', d=23.2)
