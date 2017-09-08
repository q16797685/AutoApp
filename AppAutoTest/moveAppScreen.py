#!/usr/bin/python
# coding:utf-8

"""
Created on 2017-xx-xx

@author: Wangchenyang

@功能：移动手机屏幕
"""

from time import sleep


def getSize(self):
    """获取APP当前窗口大小"""
    x = self.driver.get_window_size()['width']
    y = self.driver.get_window_size()['height']
    return (x, y)


# T值越大，移动越慢，T参数越小，移动越快
def swipeUp(self, t):   # 屏幕向下移动
    sleep(3)
    l = getSize(self)
    x1 = int(l[0] * 0.5)
    y1 = int(l[1] * 0.7)
    y2 = int(l[1] * 0.5)
    self.driver.swipe(x1, y1, x1, y2, t)


def swipeDown(self, t):    # 屏幕向上移动
    sleep(3)
    l = getSize(self)
    x1 = int(l[0] * 0.5)
    y1 = int(l[1] * 0.25)
    y2 = int(l[1] * 0.75)
    self.driver.swipe(x1, y1, x1, y2, t)
