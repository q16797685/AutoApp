#!/usr/bin/python
# coding:utf-8

"""
Created on 2017-07-17

@author: Wangchenyang

@回答婚姻史
"""

from time import sleep
import userdict
import random

question_fourty_three = ['11', '12', '13', '不记得了']


def answerMarital_history(self):

    # 婚姻史
    # 获取第40题，单选
    answer_fourty = self.driver.find_element_by_xpath(
        "//android.widget.TextView[contains(@resource-id,'item_tv1') and @text='2']")
    # log.recordLog(answer_fourty.text,answer_fourty.tag_name)
    answer_fourty.click()
    send_xz = self.driver.find_element_by_xpath(
        "//android.widget.Button[contains(@resource-id,'btn_send_xz')]")
    send_xz.click()
    sleep(3)

    # 获取第41题，单选
    answer_fourty_one = self.driver.find_element_by_xpath(
        "//android.widget.TextView[contains(@resource-id,'item_tv1') and @text='2']")
    # log.recordLog(answer_fourty_one.text,answer_fourty_one.tag_name)
    answer_fourty_one.click()
    send_xz.click()

    print 'gender', userdict.gender

    # 回答完问题分支
    if userdict.gender == 0:
        print '已完成'
        sleep(3)
    else:
        print '未完成'
        ran_char_fourty_three = random.choice(question_fourty_three)
        answer_fourty_three = self.driver.find_element_by_xpath(
            "//android.widget.EditText[contains(@resource-id,'et_answer')]")
        answer_fourty_three.send_keys(ran_char_fourty_three.decode('utf-8'))
        send_wb = self.driver.find_element_by_xpath("//android.widget.Button[contains(@resource-id,'btn_send_wb')]")
        send_wb.click()

        answer_fourty_four = self.driver.find_element_by_xpath(
            "//android.widget.TextView[contains(@resource-id,'item_tv1') and @text='2']")
        answer_fourty_four.click()
        send_xz.click()

        answer_fourty_five = self.driver.find_element_by_xpath(
            "//android.widget.TextView[contains(@resource-id,'item_tv1') and @text='2']")
        answer_fourty_five.click()
        send_xz.click()
        sleep(3)