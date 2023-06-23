# demo7-3.py

itmes = [' apple', 'banana', 'pancake']
prices = [19, 22, 200]


a = {item: price for item, price in zip(itmes, prices)}


price2 = dict(zip(itmes, prices))


print(a,)
print(price2)


'''
假设你有两个列表，一个是商品名称，一个是价格，
但价格是字符串形式的，你想将价格转换为浮点数。
你可以使用字典推导式来实现这一点：
'''


items = ['apple', 'banana', 'pancake']
prices = ['1.99', '0.99', '2.99']

exp = {shangpin: float(jiage) for shangpin, jiage in zip(items, prices)}
print(exp)
