# demo5-12-break3.py

for i in range(3):
    for j in range(10):
        if j % 4 == 0 and j != 0:  # range不写（1，10）。就要加 j!=0
            break
        print(j, end='\t')
    print()


print('''        j % 4==0  
	⬆️break（打断循环，只数到123就不数了），
    ⬇️continue（跳过当前，进入下一次，x为4的倍数时，跳过）''')
for i in range(3):
    for j in range(10):
        if j % 4 == 0 and j != 0:  # range不写（1，10）。就要加 j!=0
            continue
        print(j, end='\t')
    print()

'''
当j是4的倍数并且不等于0时，
⬆️break会导致内层循环提前结束，所以每次只打印出0, 1, 2, 3，
然后开始新的外层循环；

⬇️continue会跳过当前迭代的剩余部分，因此每当j是4的倍数并且不等于0时，
它不会被打印，而其他数字会正常打印。

'''
