#11.6.py

class Animal(object):
	def eat(self):
		print('动物要吃东西')

class Dog(Animal):
    def __init__(self, name):
        self.name = name
    def eat(self):
    	print(f'{self.name}狗吃肉')
 
class Cat(Animal):
	def eat(self):
		print('猫吃鱼')
		
class Person(object):
	def eat(self):
		print('人吃五谷杂粮')

def fun11(Obj):
	Obj.eat()
 
fun11(Dog('二哈，')) 
fun11(Cat())
fun11(Person())
fun11(Animal())

'''
多态的主要用途是提高代码的灵活性和可重用性。
你可以写出只依赖对象接口（也就是对象的方法和属性）
而不依赖对象实际类型的代码，这样的代码可以对多种不同类型的对象工作。
这让你可以编写更一般的、可重用的函数和类，因为它们能处理任何具有正确接口的对象，
而不仅仅是某个特定类型的对象。

多态的需要源于软件设计的一些基本原则，
如 "开放封闭原则"（软件实体应该对扩展开放，对修改封闭）。
如果你的代码是多态的，那么你可以添加新的对象类型，
而不必修改使用这些对象的代码。只要新类型满足原有的接口要求
（即它有正确的方法和属性），原有的代码就可以不作修改地使用新类型的对象。

'''
	