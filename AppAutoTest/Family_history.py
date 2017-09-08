#!/usr/bin/python
# coding:utf-8

"""Created on 2017-7-17

@author: Wangchenyang

@回答家族史
"""

from time import sleep


def answerFamily_history(self):

    # 家族史
    # 获取第39题，单选
    answer_thirty_nine = self.driver.find_element_by_xpath(
        "//android.widget.TextView[contains(@resource-id,'item_tv1') and @text='2']")
    answer_thirty_nine.click()
    send_xz = self.driver.find_element_by_xpath("//android.widget.Button[contains(@resource-id,'btn_send_xz')]")
    send_xz.click()
    sleep(3)
    print '完成家族史'
