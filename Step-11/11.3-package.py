#11.3-package.py

class Car(object):
	"""docstring for Car"""
	def __init__(self, brand):
		self.brand = brand
	def start():
		print('汽车已启动～')


car=Car('沃尔沃')
Car.start()
print(car.brand)

print('____')

class Student1():
	def __init__(self, name,age):
		self.name = name
		self.__age = age #不在外部引用
	def show(self):
		print(self.name,self.__age)

stu1=Student1('章三',20)
stu1.show()
print(stu1.name)
#print(stu1.age)
print(dir(stu1))
print('______')
print(stu1._Student1__age) #靠自觉

