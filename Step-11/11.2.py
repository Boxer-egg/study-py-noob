#11.2.py

class Student:
	def __init__(self, name,age):
		self.name = name
		self.age = age
	def eat(self):
		print(self,name+'在吃饭')

stu1=Student('章三',20)
stu2=Student('王武',17)
stu1.eat
print(stu1.name)

stu2.gender='女'
print('stu2.gender:',stu2.gender)

def show():
	print('定义在类之外的，称为函数')
stu1.show=show
stu1.show()
		


