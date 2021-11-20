# -*- coding = utf-8 -*-
# @Time : 2021/11/11 11:32
# @Author : ChenY
# @File : __init__.py.py
# @Software : PyCharm

import random
import schedule
import time
import os
import json
from time import sleep
from selenium import webdriver
import datetime

# 定义一个字典，存储本次运行总计已读新闻数
# all_count:总阅读数
# single_count:单次内容统计数
count_list = {'all_count': 0, "single_count": 0}
# 定义一个列表，存储不同内容页面的class标签，供页面随机跳转选择使用
page_list = ['党史教育', '科学百科',
             '健康生活', '科技前沿',
             '军事科技', '实用技术', '天文地理']


# 根据cookie免登录
def setUp(root, cookie_name):

    browser = webdriver.Chrome(r'E:\chromedriver.exe')  # 指定驱动
    url = "https://www.tfkjy.cn/popularscience" \
          "/kpResource/kp-source-new.html"    # 天府科技云登录链接
    # 访问网站，清空旧cookies信息
    browser.get(url)
    browser.delete_all_cookies()

    # 加载 cookies信息
    with open(root + "/" + cookie_name, "r") as f:
        cookies = json.load(f)
        for cookie in cookies:
            browser.add_cookie(cookie)

    # 验证是否登录成功
    browser.get(url)
    Time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print("-------"
          + Time
          + ":---------cookie登录已成功！当前登录用户为："
          + cookie_name
          + "---------------")
    try:
        # 登录成功后尝试进行阅读
        ContentRandomSelect(browser)
    except Exception as e:
        # 抛出异常并关闭驱动，不然驱动会越来越多，占内存
        print(e)
        count_list["single_count"] = 0
        count_list["all_count"] = 0
        browser.quit()


# 到达指定页面，进行网页关键控制信息抓取，自动阅读
def AutoStart(browser):
    # 临时计数器归零
    count = 0
    # 获取当前列表页的句柄
    handle = browser.current_window_handle
    sleep(2)
    # 获取内容列表
    lists = browser.find_elements_by_class_name("kp-recommend-top-title")
    # 循环点击并查看
    for lsz in lists:
        sleep(2)
        lsz.click()
        # 一个页面停留12秒
        for i in range(11):
            sleep(1)
        # 该页面一篇阅读已完成，计数器+1
        count += 1
        # 获取该篇文章标题
        title = lsz.text
        print(str(count) + ".已阅读" + '->《' + str(title) + '》')
        # 如果已阅读10条，那么将10条加入到总阅读数中，打印总数
        # 将读取新闻数加到总读取数中
        count_list["all_count"] += 1
        # 将本次读完的10篇文章加入单次内容条数内
        count_list["single_count"] += 1
        # # 跳转到科普苑主页
        # browser.switch_to_window(handle)
        sleep(1)
        if count == len(lists):
            # 跳转到下一页面
            browser.switch_to_window(handle)
            sleep(2)
            browser.find_element_by_xpath('//a[@class="next"]').click()
            Time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            # 打印总计的浏览数
            print(Time
                  + ":目前已浏览总计"
                  + str(count_list["all_count"])
                  + "篇文章")
            AutoStart(browser)
        # 如果单次内容条数大于50，则
        elif count_list["single_count"] >= 50:
            # 将单次内容统计条数置零
            count_list["single_count"] = 0
            # 跳转到科普苑主页
            browser.switch_to_window(handle)
            break


# 控制内容主页面的随机跳转
def ContentRandomSelect(browser):
    # 总计2次内容大类的跳转,每类内容读50条
    for i in range(2):
        # 根据给定列表内容进行跳转
        sleep(10)
        target_title = page_list[random.randint(0, 6)]
        page = browser.find_element_by_xpath(
            "//div[@class='li drag-item' and text()='"
            + target_title
            + "']")
        page.click()
        print("第"
              + str(i+1)
              + "次随机切换内容！当前阅读内容为 --> "
              + str(target_title))
        # 执行该类内容的自动阅读
        sleep(3)
        AutoStart(browser)
        # 如果总计条数大于等于100，则退出当前账号，切换下一条账号
        if count_list["all_count"] >= 100:
            Time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(Time + "：当前账号阅读条数已达到100，已自动退出账号")
            count_list["single_count"] = 0
            count_list["all_count"] = 0
            browser.quit()
            continue


# 循环获取cookie文件
def GetFiles():
    cookie_dir = "./cookies"
    for root, dirs, file in os.walk(cookie_dir, topdown=False):
        for f in file:
            sleep(2)
            setUp(root, f)
            sleep(30)


# 这是定时函数
def ScheduleRun(start_time, second_time):
    schedule.every().day.at(start_time).do(GetFiles)
    schedule.every().day.at(second_time).do(GetFiles)
    while True:         # 通过循环暴力查看时间，保证执行
        schedule.run_pending()
        time.sleep(0.5)


# 主函数入口
if __name__ == "__main__":
    # 设定定时任务的时间
    times1 = "02:20"
    times2 = "05:20"
    ScheduleRun(times1, times2)
    # GetFiles()
