# -*- coding = utf-8 -*-
# @Time : 2021/11/17 22:10
# @Author : ChenY
# @File : TEST.py
# @Software : PyCharm
# 这是定时函数
import schedule
import time
import datetime
from time import sleep


def Do():
    for i in range(70):
        Time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(str(Time) + "-->" + str(i))
        sleep(1)


def schedule_do(start_time, second_time):
    schedule.every().day.at(start_time).do(Do)
    schedule.every().day.at(second_time).do(Do)
    while True:         # 通过循环暴力查看时间，保证执行
        schedule.run_pending()
        time.sleep(0.5)
        # Time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # print(str(Time) + "正在等待执行")


# 主函数入口
if __name__ == "__main__":
    # 设定定时任务的时间
    times1 = "22:20"
    times2 = "22:30"
    schedule_do(times1, times2)
