# -*- coding: utf-8 -*-
import os
import pickle
import time

import scrapy
from selenium import webdriver

from Spider.settings import BASE_DIR


def start_requests(self):
    # 使用selenium模拟登陆后拿到cookie交给scrapy的request使用
    # 通过selenium进行登陆
    # 从文件中读取cookies
    print("selenium")
    cookies = []
    if os.path.exists(BASE_DIR + "/cookies/echo.cookie"):
        cookies = pickle.load(open(BASE_DIR + "/cookies/echo.cookie", "rb"))
        pass
    if not cookies:
        browser = webdriver.Firefox(
            executable_path='D:/Workspace/DeveloperTools/SeleniumDrivers/firefox/geckodriver-v0.23.0-win64/geckodriver.exe')
        browser.get('http://www.app-echo.com/#/')
        time.sleep(3)
        browser.find_element_by_css_selector('.headerv3-login').click()
        browser.find_element_by_css_selector('.phone').send_keys('18126106725')
        browser.find_element_by_css_selector('.password').send_keys('Allen501983707')
        browser.find_element_by_css_selector('.login-btn').click()

        time.sleep(2)
        cookies = browser.get_cookies()
        # 写入cookies到文件
        pickle.dump(cookies, open(BASE_DIR + "/cookies/echo.cookie", "wb"))

    cookie_dict = {}
    for cookie in cookies:
        cookie_dict[cookie['name']] = cookie['value']
    for url in self.start_urls:
        yield scrapy.Request(url, dont_filter=True, headers=self.headers)
