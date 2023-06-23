# demo6-3-index.py

lst = ['hello', 'world', '98']
print(lst.index('hello'), lst.index('98'))

print(lst.index('98', 1, 3))

print(lst.index('hello', 1, 3))  # ValueError: 'hello' is not in list
