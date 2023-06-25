#12 - 3 - open - file.py

import os

# 获取当前脚本的路径  约等于pwd
script_dir = os.path.dirname(os.path.abspath(__file__))
print(script_dir)
# 构造 abc.txt 的路径  类似字符串拼接
abc_path = os.path.join(script_dir, 'abc.txt')
print(abc_path)

file = open(abc_path, 'r')  # 打开并读取
print(file.readlines())  # 结果是个列表 加S就是读取所有。
file.close()


script_dir2 = os.path.dirname(os.path.abspath(__file__))
print('再次打印，看看写的对不对：', script_dir2)
ccc_path = os.path.join(script_dir2, 'ccc.txt')
print('再次打印，看看写的对不对：', ccc_path)
file = open(ccc_path, 'w')
file.write('helloword   \n成功啦～～～')
file.close()

file = open(ccc_path, 'a')
file.write('\n使用‘a’,(追加一条）')

