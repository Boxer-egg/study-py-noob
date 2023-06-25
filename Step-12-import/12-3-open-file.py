#12 - 3 - open - file.py

import os

# 获取当前脚本的路径  约等于pwd
script_dir = os.path.dirname(os.path.abspath(__file__))
print(script_dir)
# 构造 abc.txt 的路径  类似字符串拼接
abc_path = os.path.join(script_dir, 'abc.txt')
print(abc_path)

file = open(abc_path, 'r')  # 打开并读取
print('read和readlines的区别:', file.read(10))
file.seek(0)   # 将文件指针移动到文件的开头
print(file.readlines())  # 结果是个列表 加S就是读取所有。
# 这个方法会读取文件中的所有行，然后将文件指针移动到文件的末尾。
file.close()


print('---')
script_dir2 = os.path.dirname(os.path.abspath(__file__))
print('再次打印，看看写的对不对：', script_dir2)
ccc_path = os.path.join(script_dir2, 'ccc.txt')
print('再次打印，看看写的对不对：', ccc_path)
file = open(ccc_path, 'w')
file.write('helloword   \n成功啦～～～')
file.close()

file = open(ccc_path, 'a')
file.write('\n使用‘a’,(追加一条）')
