# demo5-11(3.4).py

# 三行四列的矩形


for i in range(1, 10):
    for j in range(1, 10):
        if j <= i:
            print(j, '*', i, '=', i*j, end='\t')
    print()
