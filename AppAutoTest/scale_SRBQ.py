#!/usr/bin/python
# coding:utf-8

"""
Created on 2017-06-29

@author: Wangchenyang

@功能：关怀回答量表
"""

from time import sleep
import random

SRBQ_Answer = ['几乎没有', '很少', '有时', '经常', '几乎总是']


def answerScale_SRBQ(self):
    """ 睡眠相关行为问卷SRBQ """
    # 获取随机答案字符串
    random_answer_1 = random.choice(SRBQ_Answer)
    # 获取第1题的元素
    getanswer_1 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_1 + "']")
    getanswer_1.click()
    sleep(1)

    random_answer_2 = random.choice(SRBQ_Answer)
    # 获取第2题的元素
    getanswer_2 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_2 + "']")
    getanswer_2.click()
    sleep(1)

    random_answer_3 = random.choice(SRBQ_Answer)
    # 获取第3题的元素
    getanswer_3 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_3 + "']")
    getanswer_3.click()
    sleep(1)

    random_answer_4 = random.choice(SRBQ_Answer)
    # 获取第4题的元素
    getanswer_4 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_4 + "']")
    getanswer_4.click()
    sleep(1)

    random_answer_5 = random.choice(SRBQ_Answer)
    # 获取第5题的元素
    getanswer_5 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_5 + "']")
    getanswer_5.click()
    sleep(1)

    random_answer_6 = random.choice(SRBQ_Answer)
    # 获取第6题的元素
    getanswer_6 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_6 + "']")
    getanswer_6.click()
    sleep(1)

    random_answer_7 = random.choice(SRBQ_Answer)
    # 获取第7题的元素
    getanswer_7 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_7 + "']")
    getanswer_7.click()
    sleep(1)

    random_answer_8 = random.choice(SRBQ_Answer)
    # 获取第8题的元素
    getanswer_8 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_8 + "']")
    getanswer_8.click()
    sleep(1)

    random_answer_9 = random.choice(SRBQ_Answer)
    # 获取第9题的元素
    getanswer_9 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_9 + "']")
    getanswer_9.click()
    sleep(1)

    random_answer_10 = random.choice(SRBQ_Answer)
    # 获取第10题的元素
    getanswer_10 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_10 + "']")
    getanswer_10.click()
    sleep(1)

    random_answer_11 = random.choice(SRBQ_Answer)
    # 获取第11题的元素
    getanswer_11 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_11 + "']")
    getanswer_11.click()
    sleep(1)

    random_answer_12 = random.choice(SRBQ_Answer)
    # 获取第12题的元素
    getanswer_12 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_12 + "']")
    getanswer_12.click()
    sleep(1)

    random_answer_13 = random.choice(SRBQ_Answer)
    # 获取第13题的元素
    getanswer_13 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_13 + "']")
    getanswer_13.click()
    sleep(1)

    random_answer_14 = random.choice(SRBQ_Answer)
    # 获取第14题的元素
    getanswer_14 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_14 + "']")
    getanswer_14.click()
    sleep(1)

    random_answer_15 = random.choice(SRBQ_Answer)
    # 获取第15题的元素
    getanswer_15 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_15 + "']")
    getanswer_15.click()
    sleep(1)

    random_answer_16 = random.choice(SRBQ_Answer)
    # 获取第16题的元素
    getanswer_16 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_16 + "']")
    getanswer_16.click()
    sleep(1)

    random_answer_17 = random.choice(SRBQ_Answer)
    # 获取第17题的元素
    getanswer_17 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_17 + "']")
    getanswer_17.click()
    sleep(1)

    random_answer_18 = random.choice(SRBQ_Answer)
    # 获取第18题的元素
    getanswer_18 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_18 + "']")
    getanswer_18.click()
    sleep(1)

    random_answer_19 = random.choice(SRBQ_Answer)
    # 获取第19题的元素
    getanswer_19 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_19 + "']")
    getanswer_19.click()
    sleep(1)

    random_answer_20 = random.choice(SRBQ_Answer)
    # 获取第20题的元素
    getanswer_20 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_20 + "']")
    getanswer_20.click()
    sleep(1)

    random_answer_21 = random.choice(SRBQ_Answer)
    # 获取第21题的元素
    getanswer_21 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_21 + "']")
    getanswer_21.click()
    sleep(1)

    random_answer_22 = random.choice(SRBQ_Answer)
    # 获取第22题的元素
    getanswer_22 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_22 + "']")
    getanswer_22.click()
    sleep(1)

    random_answer_23 = random.choice(SRBQ_Answer)
    # 获取第23题的元素
    getanswer_23 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_23 + "']")
    getanswer_23.click()
    sleep(1)

    random_answer_24 = random.choice(SRBQ_Answer)
    # 获取第24题的元素
    getanswer_24 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_24 + "']")
    getanswer_24.click()
    sleep(1)

    random_answer_25 = random.choice(SRBQ_Answer)
    # 获取第25题的元素
    getanswer_25 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_25 + "']")
    getanswer_25.click()
    sleep(1)

    random_answer_26 = random.choice(SRBQ_Answer)
    # 获取第26题的元素
    getanswer_26 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_26 + "']")
    getanswer_26.click()
    sleep(1)

    random_answer_27 = random.choice(SRBQ_Answer)
    # 获取第27题的元素
    getanswer_27 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_27 + "']")
    getanswer_27.click()
    sleep(1)

    random_answer_28 = random.choice(SRBQ_Answer)
    # 获取第28题的元素
    getanswer_28 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_28 + "']")
    getanswer_28.click()
    sleep(1)

    random_answer_29 = random.choice(SRBQ_Answer)
    # 获取第29题的元素
    getanswer_29 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_29 + "']")
    getanswer_29.click()
    sleep(1)

    random_answer_30 = random.choice(SRBQ_Answer)
    # 获取第30题的元素
    getanswer_30 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_30 + "']")
    getanswer_30.click()
    sleep(1)

    random_answer_31 = random.choice(SRBQ_Answer)
    # 获取第31题的元素
    getanswer_31 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_31 + "']")
    getanswer_31.click()
    sleep(1)

    random_answer_32 = random.choice(SRBQ_Answer)
    # 获取第32题的元素
    getanswer_32 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_32 + "']")
    getanswer_32.click()
    sleep(1)

    # 点击确认按钮
    clickComfirm = self.driver.find_element_by_xpath(
        "//android.widget.TextView[contains(@resource-id,'include_title_tv_save')]")
    clickComfirm.click()
    print 'you finish 睡眠相关行为问卷SRBQ scalc!'