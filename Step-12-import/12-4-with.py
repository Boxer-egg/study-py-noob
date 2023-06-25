# 12 - 4 - with.py

import os
script_dir = os.path.dirname(os.path.abspath(__file__))
print(script_dir)
png_path1 = os.path.join(script_dir, 'jieping.png')
print(png_path1)
copy2jieping = os.path.join(script_dir, 'copy2jieping.png')
print(copy2jieping)


with open(png_path1, 'rb') as src_file:  # 二进制模式，打开源文件。with语句会在执行完毕后自动调用file.close()
    #print('看看二进制文件：', src_file.read())  #不要打印，太多了。
    with open(copy2jieping, 'wb') as target_file:  # 二进制模式，写入文件
        target_file.write(src_file.read())  # 写入打开的二进制文件到target_file目录的文件内
print(src_file)  # src_file是一个文件对象，表示你的程序和打开的文件之间的连接。

'''
open(copy2jieping, 'wb')
这行代码的含义是，如果copy2jieping.png文件不存在，那么就创建一个新文件；
如果文件已经存在，那么就会清空这个文件的内容，准备写入新的内容。
这就是'wb'模式的行为：它既可以用于新建文件，也可以用于清空并覆写已经存在的文件。
'''
