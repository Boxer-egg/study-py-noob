# demo9-4.py
s = 'hello world'
print('h', s.isidentifier())
print('hello'.isidentifier())


s1 = {'1.': 11, '2.': '二二'}  # 11报错了 AttributeError  isnumeric只支持字符串

for key, value in s1.items():
    print(key, value)
    print(key.isnumeric(), str(value).isnumeric())

# str(value.isnumeric()) 尝试在 value 上执行 isnumeric()，然后将结果（布尔值）转换为字符串。

for s2 in range(3):
    print('输出', s2)
