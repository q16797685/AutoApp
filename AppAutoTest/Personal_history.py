#!/usr/bin/python
# coding:utf-8

"""
Created on 2017-xx-xx

@author: Wangchenyang

@回答个人史
"""

from time import sleep


def answerPersonal_history(self):
    # 个人史
    # 获取第37题，单选
    answer_thirty_seven = self.driver.find_element_by_xpath(
        "//android.widget.TextView[contains(@resource-id,'item_tv1') and @text='2']")
    # log.recordLog(answer_thirty_seven.text,answer_thirty_seven.tag_name)
    answer_thirty_seven.click()
    send_xz = self.driver.find_element_by_xpath(
        "//android.widget.Button[contains(@resource-id,'btn_send_xz')]")
    send_xz.click()
    sleep(3)

    # 获取第38题，单选
    answer_thirty_eight = self.driver.find_element_by_xpath(
        "//android.widget.TextView[contains(@resource-id,'item_tv1') and @text='2']")
    # log.recordLog(answer_thirty_eight.text,answer_thirty_eight.tag_name)
    answer_thirty_eight.click()
    send_xz.click()
    sleep(3)
    print '完成个人史'
