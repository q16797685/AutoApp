#!/usr/bin/python
# coding:utf-8

"""
Created on 2017-07-05

@author: Wangchenyang

@功能：回答量表抑郁自评量表SDS
"""

from time import sleep
import random

scalc_answer = ['绝大部分或全部时间', '少部分时间', '相当多时间', '绝大部分或全部时间']


def answerScalc_SDS(self):
    """ 抑郁自评表SDS """
    # 获取随机答案字符串
    random_answer_one = random.choice(scalc_answer)
    # 获取第1题的元素
    getanswer_one = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_one + "']")
    getanswer_one.click()
    sleep(2)

    # 获取随机答案字符串
    random_answer_two = random.choice(scalc_answer)
    # 获取第2题的元素
    getanswer_two = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_two + "']")
    getanswer_two.click()
    sleep(2)

    # 获取随机答案字符串
    random_answer_three = random.choice(scalc_answer)
    # 获取第3题的元素
    getanswer_three = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_three + "']")
    getanswer_three.click()
    sleep(2)

    # 获取随机答案字符串
    random_answer_four = random.choice(scalc_answer)
    # 获取第4题的元素
    getanswer_four = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_four + "']")
    getanswer_four.click()
    sleep(2)

    # 获取随机答案字符串
    random_answer_five = random.choice(scalc_answer)
    # 获取第5题的元素
    getanswer_five = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_five + "']")
    getanswer_five.click()
    sleep(2)

    # 获取随机答案字符串
    random_answer_six = random.choice(scalc_answer)
    # 获取第6题的元素
    getanswer_six = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_six + "']")
    getanswer_six.click()
    sleep(2)

    # 获取随机答案字符串
    random_answer_seven = random.choice(scalc_answer)
    # 获取第7题的元素
    getanswer_seven = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_seven + "']")
    getanswer_seven.click()
    sleep(2)

    # 获取随机答案字符串
    random_answer_eight = random.choice(scalc_answer)
    # 获取第8题的元素
    getanswer_eight = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_eight + "']")
    getanswer_eight.click()
    sleep(2)

    # 获取随机答案字符串
    random_answer_nine = random.choice(scalc_answer)
    # 获取第9题的元素
    getanswer_nine = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_nine + "']")
    getanswer_nine.click()
    sleep(2)

    # 获取随机答案字符串
    random_answer_ten = random.choice(scalc_answer)
    # 获取第10题的元素
    getanswer_ten = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_ten + "']")
    getanswer_ten.click()
    sleep(2)

    # 获取随机答案字符串
    random_answer_eleven = random.choice(scalc_answer)
    # 获取第11题的元素
    getanswer_eleven = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_eleven + "']")
    getanswer_eleven.click()
    sleep(2)

    # 获取随机答案字符串
    random_answer_twelve = random.choice(scalc_answer)
    # 获取第12题的元素
    getanswer_twelve = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_twelve + "']")
    getanswer_twelve.click()
    sleep(2)

    # 获取随机答案字符串
    random_answer_thirteen = random.choice(scalc_answer)
    # 获取第13题的元素
    getanswer_thirteen = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_thirteen + "']")
    getanswer_thirteen.click()
    sleep(2)

    # 获取随机答案字符串
    random_answer_fourteen = random.choice(scalc_answer)
    # 获取第14题的元素
    getanswer_fourteen = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_fourteen + "']")
    getanswer_fourteen.click()
    sleep(2)

    # 获取随机答案字符串
    random_answer_fiveteen = random.choice(scalc_answer)
    # 获取第15题的元素
    getanswer_fiveteen = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_fiveteen + "']")
    getanswer_fiveteen.click()
    sleep(2)

    # 获取随机答案字符串
    random_answer_sixteen = random.choice(scalc_answer)
    # 获取第16题的元素
    getanswer_sixteen = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_sixteen + "']")
    getanswer_sixteen.click()
    sleep(2)

    # 获取随机答案字符串
    random_answer_seventeen = random.choice(scalc_answer)
    # 获取第17题的元素
    getanswer_seventeen = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_seventeen + "']")
    getanswer_seventeen.click()
    sleep(2)

    # 获取随机答案字符串
    random_answer_eighteen = random.choice(scalc_answer)
    # 获取第18题的元素
    getanswer_eighteen = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_eighteen + "']")
    getanswer_eighteen.click()
    sleep(2)

    # 获取随机答案字符串
    random_answer_nineteen = random.choice(scalc_answer)
    # 获取第19题的元素
    getanswer_nineteen = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_nineteen + "']")
    getanswer_nineteen.click()
    sleep(2)

    # 获取随机答案字符串
    random_answer_twenty = random.choice(scalc_answer)
    # 获取第20题的元素
    getanswer_twenty = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[3]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_twenty + "']")
    getanswer_twenty.click()
    sleep(2)

    # 点击确认按钮
    clickComfirm = self.driver.find_element_by_xpath(
        "//android.widget.TextView[contains(@resource-id,'include_title_tv_save')]")
    clickComfirm.click()
    print 'you finish 抑郁自评量表SDS scalc!!'