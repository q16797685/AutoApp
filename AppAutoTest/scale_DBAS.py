#!/usr/bin/python
# coding:utf-8

"""
Created on 2017-06-29

@author: Wangchenyang

@功能：回答睡眠相关信念与态度量表DBAS
"""

from time import sleep
import random


DBAS_Answer = ['非常同意', '同意', '一般', '不同意', '非常不同意']


def answerScale_DBAS(self):
    """ 睡眠相关信念与态度量表DBAS """
    # 获取随机答案字符串
    random_answer_1 = random.choice(DBAS_Answer)
    # 获取第1题的元素
    getanswer_1 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_1 + "']")
    getanswer_1.click()
    sleep(1)

    random_answer_2 = random.choice(DBAS_Answer)
    # 获取第2题的元素
    getanswer_2 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_2 + "']")
    getanswer_2.click()
    sleep(1)

    random_answer_3 = random.choice(DBAS_Answer)
    # 获取第3题的元素
    getanswer_3 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_3 + "']")
    getanswer_3.click()
    sleep(1)

    random_answer_4 = random.choice(DBAS_Answer)
    # 获取第4题的元素
    getanswer_4 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_4 + "']")
    getanswer_4.click()
    sleep(1)

    random_answer_5 = random.choice(DBAS_Answer)
    # 获取第4题的元素
    getanswer_5 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_5 + "']")
    getanswer_5.click()
    sleep(1)

    random_answer_6 = random.choice(DBAS_Answer)
    # 获取第4题的元素
    getanswer_6 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_6 + "']")
    getanswer_6.click()
    sleep(1)

    random_answer_7 = random.choice(DBAS_Answer)
    # 获取第4题的元素
    getanswer_7 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_7 + "']")
    getanswer_7.click()
    sleep(1)

    random_answer_8 = random.choice(DBAS_Answer)
    # 获取第4题的元素
    getanswer_8 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_8 + "']")
    getanswer_8.click()
    sleep(1)

    random_answer_9 = random.choice(DBAS_Answer)
    # 获取第4题的元素
    getanswer_9 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_9 + "']")
    getanswer_9.click()
    sleep(1)

    random_answer_10 = random.choice(DBAS_Answer)
    # 获取第4题的元素
    getanswer_10 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_10 + "']")
    getanswer_10.click()
    sleep(1)

    random_answer_11 = random.choice(DBAS_Answer)
    # 获取第4题的元素
    getanswer_11 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_11 + "']")
    getanswer_11.click()
    sleep(1)

    random_answer_12 = random.choice(DBAS_Answer)
    # 获取第4题的元素
    getanswer_12 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_12 + "']")
    getanswer_12.click()
    sleep(1)

    random_answer_13 = random.choice(DBAS_Answer)
    # 获取第4题的元素
    getanswer_13 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_13 + "']")
    getanswer_13.click()
    sleep(1)

    random_answer_14 = random.choice(DBAS_Answer)
    # 获取第4题的元素
    getanswer_14 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_14 + "']")
    getanswer_14.click()
    sleep(1)

    random_answer_15 = random.choice(DBAS_Answer)
    # 获取第4题的元素
    getanswer_15 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_15 + "']")
    getanswer_15.click()
    sleep(1)

    random_answer_16 = random.choice(DBAS_Answer)
    # 获取第4题的元素
    getanswer_16 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_16 + "']")
    getanswer_16.click()
    sleep(1)

    random_answer_17 = random.choice(DBAS_Answer)
    # 获取第4题的元素
    getanswer_17 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_17 + "']")
    getanswer_17.click()
    sleep(1)

    random_answer_18 = random.choice(DBAS_Answer)
    # 获取第4题的元素
    getanswer_18 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_18 + "']")
    getanswer_18.click()
    sleep(1)

    random_answer_19 = random.choice(DBAS_Answer)
    # 获取第4题的元素
    getanswer_19 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_19 + "']")
    getanswer_19.click()
    sleep(1)

    random_answer_20 = random.choice(DBAS_Answer)
    # 获取第4题的元素
    getanswer_20 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_20 + "']")
    getanswer_20.click()
    sleep(1)

    random_answer_21 = random.choice(DBAS_Answer)
    # 获取第4题的元素
    getanswer_21 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_21 + "']")
    getanswer_21.click()
    sleep(1)

    random_answer_22 = random.choice(DBAS_Answer)
    # 获取第4题的元素
    getanswer_22 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_22 + "']")
    getanswer_22.click()
    sleep(1)

    random_answer_23 = random.choice(DBAS_Answer)
    # 获取第4题的元素
    getanswer_23 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_23 + "']")
    getanswer_23.click()
    sleep(1)

    random_answer_24 = random.choice(DBAS_Answer)
    # 获取第4题的元素
    getanswer_24 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_24 + "']")
    getanswer_24.click()
    sleep(1)

    random_answer_25 = random.choice(DBAS_Answer)
    # 获取第4题的元素
    getanswer_25 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_25 + "']")
    getanswer_25.click()
    sleep(1)

    random_answer_26 = random.choice(DBAS_Answer)
    # 获取第4题的元素
    getanswer_26 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_26 + "']")
    getanswer_26.click()
    sleep(1)

    random_answer_27 = random.choice(DBAS_Answer)
    # 获取第4题的元素
    getanswer_27 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_27 + "']")
    getanswer_27.click()
    sleep(1)

    random_answer_28 = random.choice(DBAS_Answer)
    # 获取第4题的元素
    getanswer_28 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_28 + "']")
    getanswer_28.click()
    sleep(1)

    random_answer_29 = random.choice(DBAS_Answer)
    # 获取第4题的元素
    getanswer_29 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_29 + "']")
    getanswer_29.click()
    sleep(1)

    random_answer_30 = random.choice(DBAS_Answer)
    # 获取第4题的元素
    getanswer_30 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_30 + "']")
    getanswer_30.click()
    sleep(1)

    random_answer_31 = random.choice(DBAS_Answer)
    # 获取第4题的元素
    getanswer_31 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_31 + "']")
    getanswer_31.click()
    sleep(1)

    # 点击确认按钮
    clickComfirm = self.driver.find_element_by_xpath(
        "//android.widget.TextView[contains(@resource-id,'include_title_tv_save')]")
    clickComfirm.click()
    print 'you finish 睡眠相关信念与态度量表DBAS scalc!'