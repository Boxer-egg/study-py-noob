import os

filename = 'student.txt'


def menu():
    print('========学生信息=======')
    print('========功能菜单=======')
    print('      1. 录入学生信息')
    print('      2. 查找学生信息')
    print('      3. 删除学生信息')
    print('      4. 修改学生信息')
    print('      5. 排序学生信息')
    print('      6. 统计学生总人数')
    print('      7. 显示所有学生信息')
    print('      0. 退出')


def insert():  # 插入数据的函数
    student_list = []  # 新建一个空列表，用于存放学生数据
    while True:  # 无限循环，只有在满足一定条件时通过break打断
        ID_num = int(input('请录入学生编号'))  # 获取学生编号，输入值会被转换为int类型
        if not ID_num:  # 如果编号输入不合法（例如空输入），则跳出循环
            break
        name = str(input('请录入学生姓名'))  # 获取学生姓名，输入值会被转换为str类型
        if not name:  # 如果姓名输入不合法（例如空输入），则跳出循环
            break

        try:  # 尝试执行下列代码
            # 获取Python分数，输入值会被转换为float类型
            Py_score = float(input('请录入Python分数'))
            Jar_score = float(input('请录入Java分数'))  # 获取Java分数，输入值会被转换为float类型
        except:  # 如果上述代码在执行过程中出现错误（例如输入的不是数字），则执行下面的代码
            print('输入无效，请重新输入')
            continue  # 跳过当前循环的剩余部分，直接开始下一次循环 while Ture
        student_info = {  # 创建一个新字典，用于存放单个学生的信息
            '学生编号': ID_num,
            '名字': name,
            'Python成绩': Py_score,
            'Java成绩': Jar_score
        }
        student_list.append(student_info)  # 将这个学生的信息添加到列表中
        answer = input('是否继续输入：y/n\n')  # 确认是否继续输入
        if answer == 'y':  # 如果用户输入'y'，则继续下一次循环
            continue  # 语句只影响它所在的最内层的循环，不影响外层循环
        else:  # 如果用户输入的不是'y'，则结束循环
            break

    save(student_list)  # 调用save函数，将学生信息列表保存到文件中
    print('学生信息录入完毕\n', student_list)
#


def save(lst):
    try:
        stu_txt = open(filename, 'a', encoding='utf-8')
        # 尝试以追加模式打开文件，如果文件已存在，新写入的内容会被添加到文件末尾
    except:  # 如果文件打开失败（例如文件不存在），则执行下面的代码
        stu_txt = open(filename, 'w', encoding='utf-8')
        # 以写入模式打开文件，如果文件已存在，它的内容会被清空，如果文件不存在，将创建新文件
    for item in lst:  # 遍历列表中的每一个元素（这里的元素指的是学生信息字典）
        stu_txt.write(str(item) + '\n')
        # 将字典转换为字符串并写入到文件中，每个字典后都会添加一个换行符，以便于后续读取
    stu_txt.close()  # 写入完成后，关闭文件以保存数据


'''
    for item in lst:这行代码的意思是，对列表lst中的每个元素进行迭代。
    在每次循环中，item变量都会被设置为列表中的一个元素。
    因为lst是一个包含学生信息字典的列表，所以每个item都是一个字典。

    stu_txt.write(str(item) + '\n')这行代码将item（学生信息字典）
    转换为字符串，并添加一个换行符。然后，这个字符串会被写入到打开的文件中。

    for循环会继续进行，直到lst中的所有元素都被处理完毕。
'''


def search():
    print('查找学生信息')

def delete():
    while True:  # 开始一个无限循环
        student_id = int(input('请输入要删除的学生的ID'))  # 录入学生ID，并转成int类型
        if student_id != '':  # 如果输入的学生ID不为空
            if os.path.exists(filename):  # 检查数据文件是否存在
                with open(filename, 'r', encoding='utf-8') as file:  
                # 以读模式打开数据文件，并将此动作命名为file
                    student_old = file.readlines()  # 读取文件中的所有行，每一行代表一个学生的数据
            else:   
                student_old = []  # 如果文件不存在，则设定student_old为一个空列表
            flag = False  # 初始化标记位，用于标记是否成功删除数据
            if student_old:  # 如果有旧的学生数据
                with open(filename, 'w', encoding='utf-8') as wf:  # 以写模式打开数据文件，准备写入新的学生数据
                    for item in student_old:  # 遍历每一个旧的学生数据
                        d = dict(eval(item))  # 将字符串类型的学生数据转换成字典类型
                        if int(d.get('学生编号')) != student_id:  # 如果该学生的编号与要删除的学生编号不匹配
                            wf.write(str(d) + '\n')  # 将该学生的数据写入到新的数据文件中
                        else:  # 如果该学生的编号与要删除的学生编号匹配
                            flag = True  # 标记为已找到并删除该学生数据
                    if flag:  # 如果已经删除了指定的学生数据
                        print(f'id为{student_id}的学生信息已经删除')  # 输出删除成功的消息
                    else:  # 如果没有找到指定的学生数据
                        print(f'没找到{student_id},的学生')  # 输出未找到的消息
            else:  # 如果没有任何旧的学生数据
                print('无学生信息')  # 输出没有学生数据的消息
                break  # 结束循环
            display()  # 调用显示学生列表函数，查看学生数据。
            answer = input('是否继续删除？y/n')  # 提示用户是否继续删除学生数据
            if answer == 'y':  # 如果用户输入的是'y'，则继续循环
                continue
            else:  # 如果用户输入的不是'y'，则结束循环
                break

"""

在这段代码中，其实并没有创建一个全新的文件，而是在原文件上进行了修改。这个过程是这样的：

1. 首先，程序读取所有的学生数据，保存在 `student_old` 这个列表里。

2. 然后，程序打开文件进行写入（'w'模式），这个动作会清空原来的文件。

3. 接下来，程序会遍历 `student_old` 列表中的每一行（也就是每一个学生的信息）。
对于每一个学生，程序检查其ID是否等于我们要删除的学生的ID。

4. 如果这个学生的ID不等于我们要删除的ID，那么程序就会把这个学生的信息写回到文件中。
因为这个学生的ID不等于我们要删除的ID，所以我们不想删除他，所以要把他的信息保留下来。

5. 如果这个学生的ID等于我们要删除的ID，那么程序就不会把他的信息写回到文件中。
因为这个学生的ID等于我们要删除的ID，所以我们想删除他，
所以我们不把他的信息写回文件，相当于把他的信息从文件中删除了。

6. 在遍历 `student_old` 列表的过程中，如果发现有学生的ID等于我们要删除的ID，
就把 `flag` 设置为 `True`。

7. 在遍历结束后，如果 `flag` 是 `True`，就表示我们找到了要删除的学生，
成功把他的信息从文件中删除了；如果 `flag` 是 `False`，就表示我们没有找到要删除的学生。

所以，当你输入一个不存在的学生ID时，程序没有找到要删除的学生，
所以就不会删除任何学生的信息，文件中的内容就不会有任何变化。
也就是说，虽然程序确实向文件中写入了数据，但是写入的数据实际上就是原来的数据，
没有任何变化，所以你看起来就像没有写入数据一样。

"""

def modify():
    pass


def sort():
    pass


def count():
    pass


def display():
    pass


def exit():
    pass


def main():
    actions = {
        1: insert,
        2: search,
        3: delete,
        4: modify,
        5: sort,
        6: count,
        7: display,
        0: exit
    }
    while True:
        menu()
        choice = int(input('请选择'))
        if choice in actions:
            if choice == 0:
                print('再见')
                break
            actions[choice]()
        else:
            print("无效的选项，请重新输入")


main()
