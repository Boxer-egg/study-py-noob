在面向对象的编程中，多态性（Polymorphism）是指一个接口或者类具有多种不同的实现方式。这意味着，一个基类的实例在不同情况下可以表现为一个或多个派生类的实例。多态性允许我们对一个类的对象进行方法调用，而不必了解对象的具体类型。

在 Python 中，我们可以通过方法重写（Method Overriding）和鸭子类型（Duck Typing）来实现多态性。下面就分别给出两个例子。

首先，通过方法重写实现多态：

```python
class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"

# 这个函数接受一个Animal类型的对象
# 但实际上我们会传入Animal的子类（Dog或Cat）
def make_sound(animal):
    print(animal.sound())

dog = Dog()
cat = Cat()

make_sound(dog)  # 输出 "Woof!"
make_sound(cat)  # 输出 "Meow!"
```

在上面的例子中，`make_sound`函数接受一个Animal类型的对象作为参数，然后调用其`sound`方法。由于Dog和Cat类都覆盖了父类的`sound`方法，因此这两个子类在调用`sound`方法时表现出了多态性。

其次，通过鸭子类型实现多态：

```python
class Dog:
    def sound(self):
        return "Woof!"

class Cat:
    def sound(self):
        return "Meow!"

# 这个函数接受一个有sound方法的对象
def make_sound(animal):
    print(animal.sound())

dog = Dog()
cat = Cat()

make_sound(dog)  # 输出 "Woof!"
make_sound(cat)  # 输出 "Meow!"
```

在这个例子中，`make_sound`函数并不关心传入的对象具体是什么类型，只关心这个对象是否有`sound`方法。这就是鸭子类型的思想：如果它走起路来像鸭子，叫起来也像鸭子，那么它就是鸭子。即：对象的类型不是由继承定义的，而是由其行为（它具有哪些方法）定义的。
