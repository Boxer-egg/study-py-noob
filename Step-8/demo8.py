# coding：gbk utf=8
name = '张三'
age = 20

print(type(name), type(age)),
print('我叫'+name+',今年' + str(age))

print('---str()将其他类型转换成str---')
a = 10
b = 19.22
c = False
print(type(a), type(b), type(c))
print(str(a), str(b), type(a), type(b), type(str(a)))

"""str()函数不会改变原变量的类型或值，
  它只是返回一个新的字符串，这个字符串的内容和原变量的值相同。
  也就是说，即使你使用了str(a)和str(b)，变量a和b本身的类型和值都不会改变。
  因此，当你打印type(a)和type(b)时，仍然会显示它们的原始类型，
  分别是<class 'int'>和<class 'float'>。
  如果你想改变变量a和b的类型，你需要将str()函数的返回值赋值给它们，像这样
  """

print('---int()将其他类型转换成int---')


f2 = 10.1
s3 = '77.72'
ff = True
s33 = 'hello'

print(int(f2), type(int(f2)), int(ff), type(int(ff)))


print('--float(),将其他类型转换成float-----')
ac = True
ii = 98
print(float(ii), type(float(ii)), float(ac), type(float(ac)))
