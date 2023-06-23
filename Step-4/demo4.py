# demo4  赋值运算符，运算顺序从左到右

a = b = c = 20

print(a, id(a), type(a))
print(b, id(b))

print('--支持参数赋值-')

a = 20
print(a)
a += 30  # a = a+30
print(a)
a *= 2  # a= a*2
print(a)

a /= 3
print(a)
a //= 2
print(a)

print('---解包赋值---')

a, b, c = (20, 30, 40)
print(a, b, c)

print('---交换两个变量---')

a, b = 20, 14.11

print('交换前：', a, b)
a, b = b, a*2
print('交换后：', a, b)
