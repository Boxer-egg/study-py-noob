import prettytable as pt


# 显示坐席

# def show_ticket(row_num):
#     tb = pt.PrettyTable()
#     tb.field_name = ['行号', '座位1', '座位2', '座位3', '座位4', '座位5']
#     for i in range(row_num):
#         lst = [f"第{i+1}行:", "有票", "有票", "有票", "有票", "有票"]
#         tb.add_row(lst)
#     print(tb)


def order_ticket(row_num, row, column):
    tb = pt.PrettyTable()
    tb.field_name = ['行号', '座位1', '座位2', '座位3', '座位4', '座位5']
    for i in range(row_num):
        # 如果当前行是要标记的行
        if int(row) == i + 1:
            lst = [F"第{i+1}行:", "有票", "有票", "有票", "有票", "有票"]
            # 标记指定的座位为"已售出"
            lst[int(column)] = "已售"
            tb.add_row(lst)
        else:
            # 如果当前行不是要标记的行，就显示所有座位都有票
            lst = [F"第{i+1}行:", "有票", "有票", "有票", "有票", "有票"]
            tb.add_row(lst)
    print(tb)


order_ticket(row_num=8, column=3, row=7, )
#关键字参数
