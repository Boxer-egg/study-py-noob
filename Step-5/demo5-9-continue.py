# demo5-9-continue.py

# 输出1——50，5的倍数。和5余数0，为5的倍数。

for item in range(51):
    if item % 5 != 0:
        continue
    print(item)
