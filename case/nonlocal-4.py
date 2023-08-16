# def funA():
#     x = 520

#     def funB():
#         x = 880
#         print("In funB, x =", x)
#     funB()
#     print("In funA, x =", x)


# funA()


def funA():
    x = 520

    def funB():
        nonlocal x  # Python 只会劝你从良，从不阻止你犯罪
        # 在内部修改外部函数作用域的值
        # 为了使 nonlocal 正常工作，嵌套函数中的变量名和它想要引用的外部函数中的变量名必须一致。
        x = 881
        print("In funB, x =", x)
    funB()
    print("In funA, x =", x)


funA()

str = 11
abc = 111
print(str, abc)

'''
视频编号：BV1c4411e77
funA 是一个外部函数，它有一个局部变量 x，其值为 520。
funB 是 funA 内部的一个嵌套函数。
在 funB 中，我们使用了 nonlocal x，这意味着我们想要引用并修改外部函数 funA 的局部变量 x，
而不是在 funB 中创建一个新的局部变量 x。
在 funB 中，我们修改了 x 的值为 881。
当我们调用 funB，它首先打印 x 的值，此时 x 的值为 881。
在 funB 调用后，funA 打印 x 的值。由于 funB 已经修改了 x 的值，所以此时 x 的值仍然是 881。
'''


'''
LEGB 规则是 Python 中用于命名空间查找的规则。
它代表 Local -> Enclosing -> Global -> Built-in，这是 Python 解释器在查找变量引用时的搜索顺序。

1. **Local (L)**:
    - 这是最内部的作用域。它包括局部名称，例如在函数内部定义的变量。如果在当前函数中找到了变量引用，搜索就会停止。

2. **Enclosing (E)**:
    - 这是嵌套函数的作用域。如果变量不在当前函数的局部作用域中，
    Python 会检查外部函数的局部作用域，从内到外。这就是 `nonlocal` 关键字的作用域。

3. **Global (G)**:
    - 如果变量既不在局部作用域，也不在嵌套函数的作用域中，Python 会在全局作用域中查找它。
    全局作用域包括在脚本顶层定义的变量和在脚本中使用 `global` 关键字声明的变量。

4. **Built-in (B)**:
    - 如果在上述所有作用域中都没有找到变量，Python 会在内置作用域中查找。
    这个作用域包括所有的内置函数和变量，例如 `print`、`len` 等。

这种查找顺序确保了局部作用域可以覆盖全局作用域，
嵌套函数的作用域可以覆盖包含它的函数的作用域，全局作用域可以覆盖内置作用域。

例如，如果你在函数内部有一个名为 `print` 的变量，它会覆盖内置的 `print` 函数，
只要你在该函数内部引用它。但在函数外部，`print` 仍然指的是内置的 `print` 函数。

LEGB 规则是理解 Python 作用域和命名空间查找的关键。
'''