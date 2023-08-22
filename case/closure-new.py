def funcA():
    x = 123

    def funB():
        print(x)
    funB()  # 在 A 中调用 B。


funcA()


def funcA1():
    x = 299

    def funB1():
        print(x)
    return funB1  # 在 A 中调用 B。


funcA1()()  # 通过 funcA1调用 funB1
funny = funcA1()
funny()


def power(exp):
    def exp_of(base):
        return base ** exp
    return exp_of


square = power(2)
cube = power(3)


print(square(4))
print(cube(5))


'''

您的理解大体是对的，但有几点需要纠正和补充。首先，让我从代码开始。

闭包是一个函数对象，它记住了某些外部的变量，即使在外部函数已经结束执行后。
在这个例子中，`power`函数是一个外部函数，而`exp_of`是一个内部函数。

1. **`power(2)`调用**：
   当您调用`power(2)`时，外部函数`power`执行，并把`2`赋值给了`exp`。
   在`power`函数的体内，定义了内部函数`exp_of`，但此时它**并没有执行**。`power`函数执行完毕后返回了内部函数`exp_of`（注意，这里返回的是函数本身，不是函数的执行结果）。

2. **`square = power(2)`**:
   这里，`square`现在是一个指向`exp_of`函数的引用，并且`exp_of`函数"记住"了`exp`的值为`2`。

3. **执行`square(4)`**:
   当您调用`square(4)`时，实际上是在调用`exp_of(4)`。
   此时，`exp_of`使用它"记住"的`exp`值（即`2`）和传入的参数`base`值（即`4`），然后计算`4 ** 2`。
   注意，两个星号`**`表示的是幂运算，不是乘法。因此，`4 ** 2`等于`4`的`2`次方，即`16`。

4. **关于闭包**：
   闭包的关键是，即使外部函数（在这里是`power`）已经完成执行并返回了，
   内部函数（在这里是`exp_of`）仍然能够访问外部函数的局部变量（在这里是`exp`）。
   这就是为什么当您调用`square(4)`时，即使`power`函数已经完成执行，`exp_of`仍然可以访问`exp`的值。

总结：

- `power`函数被调用并返回了内部函数`exp_of`。
- 内部函数`exp_of`记住了`exp`的值。
- `square(4)`实际上调用了`exp_of(4)`，并使用了它记住的`exp`值。


'''


'''
您的理解是正确的，但为了更清晰，让我们详细地描述一下这个过程。

1. **执行`square = power(2)`**:

    当您调用`power(2)`时，`power`函数开始执行。这时，`exp`变量被赋值为`2`。
    然后，在`power`函数内部，您定义了一个内部函数`exp_of`。

    最后，`power`函数的最后一行是`return exp_of`。这意味着`power`函数返回了`exp_of`这个函数对象
    （并不是`exp_of`的调用结果，只是这个函数对象本身）。

    一旦`power`函数执行完毕并返回了结果，该函数的执行上下文（execution context）就已经结束了。
    然而，由于Python的闭包特性，`exp_of`这个内部函数依然"记住"了它能访问的外部变量`exp`的值。

    当您写`square = power(2)`，您实际上是将`exp_of`这个函数对象赋值给了`square`变量。

2. **调用`square(4)`**:

    当您执行`square(4)`时，您实际上是在调用`exp_of(4)`，
    因为`square`现在就是指向`exp_of`的一个引用。
    这时，它使用了之前"记住"的`exp`的值（即`2`）来执行`base ** exp`的计算。

    此时，您没有再次调用`power`函数。`square(4)`直接调用的是`exp_of`函数。

因此，您的理解是正确的：在执行`square = power(2)`后，`power`函数的执行上下文已经结束，
但由于闭包的特性，`exp_of`依然能记住`exp`的值。
当您调用`square(4)`时，您直接调用了`exp_of`，而不是通过`power`。
'''
