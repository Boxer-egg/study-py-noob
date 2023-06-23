#11.5-object.py

class Student3(object):
	def __init__(self, name,age):
		self.name = name
		self.age = age
	def __str__(self): #重写父类的方法
		return '叫我{0}，今年{1}'.format(self.name,self.age)


stu=Student3('刘奶奶',80)
# print(dir(stu))
print(stu)  #默认调用__str__()这样的方法。
print(stu.name,'今年',stu.age)