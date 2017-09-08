#!/usr/bin/python
# coding:utf-8

"""
Created on 2017-xx-xx

@author: Wangchenyang

@功能：公共方法
"""

from time import sleep
from appium import webdriver
import json

slc_answer = ['无', '轻度', '中度', '偏重', '严重']


def openApp(self):
    """ 启动App """
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '4.4.2'
    desired_caps['deviceName'] = 'Android Emulator'
    desired_caps['appPackage'] = 'com.fulcruminfo.patient'
    desired_caps['appActivity'] = 'com.fulcurum.patient.view.splash.Splash'
    desired_caps["unicodeKeyboard"] = "True"  # Appium输入中文
    desired_caps["resetKeyboard"] = "True"  # Appium输入中文

    self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    try:
        while True:
            source = self.driver.page_source

    except Exception,e:
        print e
    finally:
        self.driver.quit()
