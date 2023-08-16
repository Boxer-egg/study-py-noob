# List Comprehensions（列表推导式）
# 这是一种简洁的创建列表的方法。例如，如果我们想要创建一个包含前10个数字平方的列表，可以使用列表推导式来完成：

# for i in range(5):  # 这会执行5次，从0到4
#     print("这是第", i + 1, "次循环")

squares = [x**2 for x in range(1, 11)]
print(squares)


# 拆解
squared = []   # 初始化一个空列表

for x in range(1, 11):  # 这是外层循环，遍历从1到10的数字
    squared_value = x**2  # 计算x的平方值
    squared.append(squared_value)  # 将平方值添加到列表中

print(squared)  # 打印结果列表


# Enumerate函数:
# 当您在for循环中需要同时迭代列表的索引和值时，enumerate非常有用
names = ["Alice", "Bob", "Charlie"]
for index, name in enumerate(names):
    print(f"索引 {index} 的名字是 {name}")

# Break和Continue:

# break: 可以提前退出循环。
# continue: 跳过当前迭代，继续下一个迭代

for i in range(5):
    if i == 3:
        break
    print(i)


# else 与循环:
# else 可以与 for 和 while 循环一起使用。当循环正常结束（没有遇到break）时，会执行 else 部分。
for i in range(5):
    print(i)
else:
    print("循环正常结束")


'''



对于初学者，理解列表推导式与传统的 `for` 循环之间的关系是很有帮助的。

**是否应该使用列表推导式？**

1. **简洁性**：列表推导式提供了一种简洁的方式来创建列表，特别是当你需要基于一个现有的列表或范围来创建一个新列表时。

2. **可读性**：对于简单的操作，列表推导式通常更易读。但是，对于更复杂的逻辑，尤其是当你有多个循环或条件语句时，传统的 `for` 循环可能更加清晰。

3. **性能**：列表推导式在某些情况下可能比等效的 `for` 循环稍微快一点，但这个差异通常可以忽略不计。重要的是选择使你的代码更加清晰和可维护的方法。

**建议**：

- 当你需要简单地转换一个列表或范围的元素（例如，计算每个元素的平方）时，可以考虑使用列表推导式。
  
- 如果你的逻辑开始变得复杂或难以阅读，那么使用传统的 `for` 循环可能是更好的选择。
  
- Python 还提供了集合推导式、字典推导式等，它们的工作方式与列表推导式相似，但用于创建集合或字典。

例如，集合推导式：

```python
unique_squares = {x**2 for x in range(-4, 5)}
```

字典推导式：

```python
squared_dict = {x: x**2 for x in range(1, 6)}
```

最后，最重要的是理解代码的工作原理。随着你对Python的深入了解，你会更好地判断在哪里使用哪种结构。
'''
