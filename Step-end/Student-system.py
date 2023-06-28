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


def insert():
    student_list = []  # 移动到循环之外
    while True:
        ID_num = int(input('请录入学生编号'))
        if not ID_num:
            break
        name = str(input('请录入学生姓名'))
        if not name:
            break

        try:
            Py_score = float(input('请录入Python分数'))
            Jar_score = float(input('请录入Java分数'))
        except:
            print('输入无效，请重新输入')
            continue
        student_info = {  # 使用不同的变量名
            '学生编号': ID_num,
            '名字': name,
            'Python成绩': Py_score,
            'Java成绩': Jar_score
        }
        student_list.append(student_info)  # 添加到列表
        answer = input('是否继续输入：y/n\n')
        if answer == 'y':
            continue
        else:
            break

    save(student_list)
    print('学生信息录入完毕')


def save(lst):
    try:
        stu_txt = open(filename, 'a', encoding='utf-8')  # 使用正确的编码
    except:
        stu_txt = open(filename, 'w', encoding='utf-8')  # 使用正确的编码
    for item in lst:
        stu_txt.write(str(item) + '\n')
    stu_txt.close()


def search():
    print('查找学生信息')


def delete():
    pass


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
