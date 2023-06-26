#12 - 5 - os.py

import os
import subprocess

#os.system('open /Applications/MWeb\ Pro.app')

#os.system('open /System/Applications/Calculator.app')
#subprocess.run(['open', '/Applications/Drafts.appf'])
print(os.getcwd())

need_dir = os.path.dirname(os.path.abspath(__file__))
print(need_dir)
i_need_new_dir = os.path.join(need_dir, 'test-dir/a/b')
print(i_need_new_dir)


lst1 = os.listdir(need_dir)
lst2 = os.listdir('./Step-12-import')

print(lst1)

print('手动写目录 \n', lst2)

os.makedirs(i_need_new_dir, exist_ok=True)

# exist_ok=True 如果目标目录已经存在，os.makedirs不会抛出异常，而是直接返回。

# os.chdir() 修改工作目录

print('让我看看：',os.path.split(i_need_new_dir))



'''

`os`模块：
- `os.mkdir(path)`: 创建一个目录
- `os.makedirs(path)`: 递归地创建目录
- `os.rmdir(path)`: 删除一个目录
- `os.removedirs(path)`: 递归地删除目录
- `os.rename(src, dst)`: 重命名或移动一个文件或目录
- `os.listdir(path)`: 列出指定目录下的所有文件和子目录
- `os.getcwd()`: 获取当前工作目录的路径
- `os.chdir(path)`: 改变当前工作目录
- `os.environ`: 一个字典，包含所有环境变量

`os.path`模块：
- `os.path.join(path1, path2, ...)`: 将一个或多个路径组合成一个路径
- `os.path.split(path)`: 将路径分割成目录和文件名两部分
- `os.path.dirname(path)`: 获取路径的目录部分
- `os.path.basename(path)`: 获取路径的文件名部分
- `os.path.exists(path)`: 判断一个路径是否存在
- `os.path.isfile(path)`: 判断路径是否为一个存在的文件
- `os.path.isdir(path)`: 判断路径是否为一个存在的目录
- `os.path.abspath(path)`: 获取路径的绝对路径
- `os.path.getsize(path)`: 获取文件的大小



'''