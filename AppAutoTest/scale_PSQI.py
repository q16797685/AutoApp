#!/usr/bin/python
# coding:utf-8

"""
Created on 2017-07-06

@author: Wangchenyang

@功能：匹兹堡睡眠质量指数问卷PSQI
"""

from time import sleep
import random
import moveAppScreen

PSQI_Answer = ['无', '小于1次每周', '1次2次每周', '大于3次每周']
fifteen_Answer = ['很好', '较好', '较差', '很差']
eighteen_Answer = ['没有困难', '有一点困难', '比较困难', '非常困难']
twenty_Answer = ['没有', '偶尔有', '有时有', '经常有']
twenty_one_Answer = ['没有', '有，但不在一个房间', '同一房间，但不同床', '同床']


def answerScale_PSQI(self):
    """ 匹兹堡睡眠质量指数问卷PSQI """
    # 获取随机答案字符串
    # 获取第1题的元素
    getanswer_1 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout/android.widget.TextView"
        "[contains(@resource-id,'tv_question_title') and @text='1.近一个月，晚上上床睡觉通常时间 请点选']")
    getanswer_1.click()
    windows_size = moveAppScreen.getSize(self)
    print windows_size
    moveAppScreen.swipeUp(self, 800)
    click_button = self.driver.find_element_by_xpath("//android.widget.Button[contains(@resource-id,'button1')]")
    click_button.click()
    sleep(1)

    # 获取第2题的元素
    getanswer_2 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.TextView"
        "[contains(@resource-id,'tv_question_title') and @text='2.近一个月，从上床到入睡通常需要时间 请点选']")
    getanswer_2.click()
    choose_two = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout/android.widget.LinearLayout"
        "/android.widget.RelativeLayout[2][contains(@resource-id,'lay_2')]")
    choose_two.click()
    choose_four = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout/android.widget.LinearLayout[3]"
        "/android.widget.RelativeLayout[contains(@resource-id,'lay_4')]")
    choose_four.click()
    choose_ok = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[3]/android.widget.RelativeLayout[contains(@resource-id,'lay_ok')]")
    choose_ok.click()
    sleep(1)

    # 获取第3题的元素
    getanswer_3 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[3]/android.widget.TextView"
        "[contains(@resource-id,'tv_question_title') and @text='3.近一个月，通常起床时间 请点选']")
    getanswer_3.click()
    click_button.click()
    sleep(1)

    # 获取第4题的元素
    getanswer_4 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[4]/android.widget.TextView"
        "[contains(@resource-id,'tv_question_title') and @text='4.近一个月，每夜通常实际睡眠时间（不等于卧床时间） 请点选']")
    getanswer_4.click()
    click_button.click()
    sleep(1)

    random_answer_5 = random.choice(PSQI_Answer)
    # 获取第4题的元素
    print random_answer_5
    getanswer_5 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[5]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_5 + "']")
    print getanswer_5
    getanswer_5.click()
    sleep(1)

    random_answer_6 = random.choice(PSQI_Answer)
    # 获取第4题的元素
    getanswer_6 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_6 + "']")
    getanswer_6.click()
    sleep(1)

    random_answer_7 = random.choice(PSQI_Answer)
    # 获取第4题的元素
    getanswer_7 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_7 + "']")
    getanswer_7.click()
    sleep(1)

    random_answer_8 = random.choice(PSQI_Answer)
    # 获取第4题的元素
    getanswer_8 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_8 + "']")
    getanswer_8.click()
    sleep(1)

    random_answer_9 = random.choice(PSQI_Answer)
    # 获取第4题的元素
    getanswer_9 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_9 + "']")
    getanswer_9.click()
    sleep(1)

    random_answer_10 = random.choice(PSQI_Answer)
    # 获取第4题的元素
    getanswer_10 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_10 + "']")
    getanswer_10.click()
    sleep(1)

    random_answer_11 = random.choice(PSQI_Answer)
    # 获取第4题的元素
    getanswer_11 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_11 + "']")
    getanswer_11.click()
    sleep(1)

    random_answer_12 = random.choice(PSQI_Answer)
    # 获取第4题的元素
    getanswer_12 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_12 + "']")
    getanswer_12.click()
    sleep(1)

    random_answer_13 = random.choice(PSQI_Answer)
    # 获取第4题的元素
    getanswer_13 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_13 + "']")
    getanswer_13.click()
    sleep(1)

    random_answer_14 = random.choice(PSQI_Answer)
    # 获取第4题的元素
    getanswer_14 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_14 + "']")
    getanswer_14.click()
    sleep(1)

    random_answer_15 = random.choice(fifteen_Answer)
    # 获取第4题的元素
    getanswer_15 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_15 + "']")
    getanswer_15.click()
    sleep(1)

    random_answer_16 = random.choice(PSQI_Answer)
    # 获取第4题的元素
    getanswer_16 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_16 + "']")
    getanswer_16.click()
    sleep(1)

    random_answer_17 = random.choice(PSQI_Answer)
    # 获取第4题的元素
    getanswer_17 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_17 + "']")
    getanswer_17.click()
    sleep(1)

    random_answer_18 = random.choice(eighteen_Answer)
    # 获取第4题的元素
    getanswer_18 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_18 + "']")
    getanswer_18.click()
    sleep(1)

    random_answer_19 = random.choice(PSQI_Answer)
    # 获取第4题的元素
    getanswer_19 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_19 + "']")
    getanswer_19.click()
    sleep(1)

    random_answer_20 = random.choice(twenty_Answer)
    # 获取第4题的元素
    getanswer_20 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_20 + "']")
    getanswer_20.click()
    sleep(1)

    random_answer_21 = random.choice(twenty_one_Answer)
    # 获取第4题的元素
    getanswer_21 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_21 + "']")
    getanswer_21.click()
    sleep(1)

    random_answer_22 = random.choice(PSQI_Answer)
    # 获取第4题的元素
    getanswer_22 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_22 + "']")
    getanswer_22.click()
    sleep(1)

    random_answer_23 = random.choice(PSQI_Answer)
    # 获取第4题的元素
    getanswer_23 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_23 + "']")
    getanswer_23.click()
    sleep(1)

    random_answer_24 = random.choice(PSQI_Answer)
    # 获取第4题的元素
    getanswer_24 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_24 + "']")
    getanswer_24.click()
    sleep(1)

    random_answer_25 = random.choice(PSQI_Answer)
    # 获取第4题的元素
    getanswer_25 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_25 + "']")
    getanswer_25.click()
    sleep(1)

    random_answer_26 = random.choice(PSQI_Answer)
    # 获取第4题的元素
    getanswer_26 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[3]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_26 + "']")
    getanswer_26.click()
    sleep(1)

    # 点击确认按钮
    clickComfirm = self.driver.find_element_by_xpath(
        "//android.widget.TextView[contains(@resource-id,'include_title_tv_save')]")
    clickComfirm.click()
    print 'you finish 匹兹堡睡眠质量指数问卷PSQI scalc!'