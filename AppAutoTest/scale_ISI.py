#!/usr/bin/python
# coding:utf-8

"""
Created on 2017-06-29

@author: Wangchenyang

@功能：失眠严重指数ISI
"""

from time import sleep
import random


ISI_Answer = ['无', '轻度', '中度', '重度', '极重度']
answer_four = ['非常满意', '满意', '不太满意', '不满意', '非常不满意']


def answerScale_ISI(self):
    """ 失眠严重指数ISI """
    # 获取随机答案字符串
    random_answer_1 = random.choice(ISI_Answer)
    # 获取第1题的元素
    getanswer_1 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_1 + "']")
    getanswer_1.click()
    sleep(1)

    random_answer_2 = random.choice(ISI_Answer)
    # 获取第2题的元素
    getanswer_2 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_2 + "']")
    getanswer_2.click()
    sleep(1)

    random_answer_3 = random.choice(ISI_Answer)
    # 获取第3题的元素
    getanswer_3 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_3 + "']")
    getanswer_3.click()
    sleep(1)

    random_answer_4 = random.choice(answer_four)
    # 获取第4题的元素
    getanswer_4 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_4 + "']")
    getanswer_4.click()
    sleep(1)

    random_answer_5 = random.choice(ISI_Answer)
    # 获取第4题的元素
    getanswer_5 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_5 + "']")
    getanswer_5.click()
    sleep(1)

    random_answer_6 = random.choice(ISI_Answer)
    # 获取第4题的元素
    getanswer_6 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_6 + "']")
    getanswer_6.click()
    sleep(1)

    random_answer_7 = random.choice(ISI_Answer)
    # 获取第4题的元素
    getanswer_7 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_7 + "']")
    getanswer_7.click()
    sleep(1)

    # 点击确认按钮
    clickComfirm = self.driver.find_element_by_xpath(
        "//android.widget.TextView[contains(@resource-id,'include_title_tv_save')]")
    clickComfirm.click()
    print 'you finish 失眠严重指数ISI scalc!'