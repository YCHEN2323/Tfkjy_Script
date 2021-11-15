# -*- coding = utf-8 -*-
# @Time : 2021/11/11 11:39
# @Author : ChenY
# @File : getCookie.py
# @Software : PyCharm

import json
from time import sleep
from selenium import webdriver


# 获取cookie信息函数：免登录，120秒等待扫码时间，扫码成功后自动跳转
def getCookie():
    browser = webdriver.Chrome(r'E:\chromedriver.exe')  # 根据路径获得本地已下载驱动

    url = 'https://www.tfkjy.cn/#/login'     # 指定要打开的路径

    browser.get(url=url)        # 根据路径打开网页
    sleep(600)
    cookies = browser.get_cookies()     # 获取cookie信息
    # 将 cookies 写入文件
    with open("cookies.txt", "w") as f:
        json.dump(cookies, f)
        print('获取并存储cookie信息成功！')
    browser.close()


if __name__ == "__main__":
    getCookie()
