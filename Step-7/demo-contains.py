# demo-contains.py

list1 = [10, 20, 30, 'hello', 'python']

contains_py = any('py' in str(item) for item in list1)
print(not contains_py)


"""
当然可以。让我们一步一步地解析 `'py' in item for item in list1`。

这是一个列表推导式的一部分，它在每个元素`item`上执行一个操作，
然后将结果存储在一个新的列表中。这个操作是检查字符串 `'py'` 是否在 `item` 中。

- `'py' in item`：这是一个布尔表达式，会检查字符串 `'py'` 是否是 `item` 的一部分。
如果 `'py'` 在 `item` 中，这个表达式就会返回 `True`，否则返回 `False`。

- `for item in list1`：这是一个循环，会遍历 `list1` 中的每个元素，并将每个元素的值赋给 `item`。

所以 `'py' in item for item in list1` 将会为 `list1` 中的每个元素执行 `'py' in item` 这个操作，
并返回一个新的布尔值列表。例如，如果 `list1` 是 `['apple', 'banana', 'cherry', 'python']`，
那么结果将会是 `[False, False, False, True]`，因为只有 'python' 这个字符串中包含了 'py'。

注意，这个表达式并不会直接产生一个列表，它其实是一个生成器表达式。
你可以将它传递给如 `any`、`all` 这样的函数，也可以使用 `list()` 函数将其转换成一个真正的列表。
例如 `list('py' in item for item in list1)` 会返回一个真正的列表 `[False, False, False, True]`。



"""
