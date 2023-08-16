import prettytable as pt


# 显示坐席

def show_ticket(row_num):
    tb = pt.PrettyTable()
    tb.field_name = ['行号', '座位1', '座位2', '座位3', '座位4', '座位5']
    for i in range(row_num):
        lst = [f"第{i+1}行:", "有票", "有票", "有票", "有票", "有票"]
        tb.add_row(lst)
    print(tb)


def order_ticket(row_num, row, column):
    tb = pt.PrettyTable()
    tb.field_name = ['行号', '座位1', '座位2', '座位3', '座位4', '座位5']
    for i in range(row_num):
        lst = [F"第{i+1}行:", "有票", "有票", "有票", "有票", "有票"]
        lst = [int(column)]
        tb.add_row(lst)
    else:
        lst = [F"第{i+1}行:", "有票", "有票", "有票", "有票", "有票"]
        tb.add_row(lst)
    print(order_ticket(row_num, 1, 2))


show_ticket(13)
