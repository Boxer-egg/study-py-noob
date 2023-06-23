# demo5-7-for2.py
'''
算出水仙花数：
153 = 1*1*1 + 5*5*5 + 3*3*3 =1 + 125 + 27
'''
found = False  # 这是一个标志变量，用来跟踪我们是否找到了至少一个水仙花数

for i in range(99, 1000):  # 将要计算水仙花数的范围用“i”定义出来。
    # print(i)  # 此时打印，则每一行：i=99,i=100,i=101,i=102 …………
    sum1 = 0  # 用于计算拆分数字立方的和
    for i2 in str(i):
        '''因为用了两个tab,
        所以本次新写的for循环，嵌套在了第一个for循环里面。
        此for循环的意思是：将用i定义出来的数字拆分，循环是在字符串形式的'i'中的每一个字符之间进行迭代。
        例如i定义了123，则i2位拆分成i2=1换行、i2=2换行、i2=3换行'''
    # print(i2)  # i=99,i2=9,i2=9;i=100,i2=1,i2=0,i2=0;i=153,i2=1,i2=5,i2=3
        sum1 += (int(i2)**3)
    '''本行公式为：sum1=i2**3+i2**3(i的数字被拆分成单个数字成为i2，并计算i2的立方相加)
        假设i=123，则sum1的计算为：sum1=1**3+2**3+3**3=1+8+27=36
        需要注意的是，这个操作不是一次性完成的，而是在每一次循环中，都会将当前位的立方加到 sum1 上。'''
    if i == sum1:   # 根据上一行的假设i=123,此行判断为：123!=36,则不打印(i),如果 i的数值等于sum1的数值，则打印i的数值。
        print(i)
        found = True  # 如果我们找到了一个水仙花数，就把标志变量设置为 True
if not found:  # 如果在循环结束后，我们还没有找到任何水仙花数，就打印 "没有水仙花数"
	'''
如果found = True，那么not found就是False，所以不会执行print("没有水仙花数")这条语句。
	'''
    print('没有水仙花数')








found = False  
for i in range(99, 1000):     
    sum1 = 0 
    for i2 in str(i):
        sum1 += (int(i2)**3)
    if i == sum1:
        print(i)
        found = True 
if not found: 
    print('没有水仙花数')





for item in range (100, 1000) :
	ge=  item%10
	shi=item//10%10
	bai=item//100
# print (bai, shi, ge)
if ge**3+shi**3+bai**3==item
print (item)
