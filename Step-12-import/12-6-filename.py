#12 - 6 - filename.py

import os
path = os.getcwd()

i_need_file = os.path.dirname(os.path.abspath(__file__))
list1 = os.listdir(i_need_file)

# print(path)
#print('看大小：', os.path.getsize(path))
# 返回的是该目录元数据的大小，而不是其包含的所有文件和子目录的总大小。
# print(list1)

for FileName in list1:
    if FileName.endswith('.py'):
        print('列出py文件：', FileName)

list_files = os.walk(path)

for dirpath, dirname, filename in list_files:
    print(dirpath)
    print(dirname)
    print(filename)
    print('------------')
