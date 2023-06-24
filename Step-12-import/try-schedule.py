# try-schedule.py
import schedule
import time


def job1():
    print('调度器持续输出————嘿呀～')


schedule.every(3).seconds.do(job1)

while True:
    schedule.run_pending()
    time.sleep(1)
