# 4-5ifelif.py
'''
多分枝结构，多选一执行
90-100 a
80-89 b
70-79 c
60-69 d
59以下 e
大于100  小于0  非法数字

'''

num = int(input('请输入分数： '))

if num >= 90 and num < 100:  # 90 <= num < 100:
    print('你的成绩是A')
elif num >= 80 and num < 89:
    print('你的成绩是B')
elif num >= 70 and num < 79:
    print('你的成绩是C')
elif num >= 60 and num < 69:
    print('你的成绩是D')
elif num < 59 and num > 0:
    print('你的成绩是E，没及格还要继续努力啊～')
else:
    print('老师不说别的，你是天才')
