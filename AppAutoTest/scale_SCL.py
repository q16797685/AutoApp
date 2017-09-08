#!/usr/bin/python
# coding:utf-8

"""
Created on 2017-07-05

@author: Wangchenyang

@功能：回答量表抑郁自评量表SCL-90
"""

from time import sleep
import random

scl_answer = ['无', '轻度', '中度', '偏重', '严重']


def answerScalc_SCL(self):
    """ SCL-90 """
    # 获取随机答案字符串
    random_answer_one = random.choice(scl_answer)
    # 获取第1题的元素
    getanswer_one = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_one + "']")
    getanswer_one.click()
    sleep(2)

    # 获取随机答案字符串
    random_answer_two = random.choice(scl_answer)
    # 获取第2题的元素
    getanswer_two = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_two + "']")
    getanswer_two.click()
    sleep(2)

    # 获取随机答案字符串
    random_answer_three = random.choice(scl_answer)
    # 获取第3题的元素
    getanswer_three = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_three + "']")
    getanswer_three.click()
    sleep(2)

    # 获取随机答案字符串
    random_answer_four = random.choice(scl_answer)
    # 获取第4题的元素
    getanswer_four = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_four + "']")
    getanswer_four.click()
    sleep(2)

    # 获取随机答案字符串
    random_answer_five = random.choice(scl_answer)
    # 获取第5题的元素
    getanswer_five = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_five + "']")
    getanswer_five.click()
    sleep(2)

    # 获取随机答案字符串
    random_answer_six = random.choice(scl_answer)
    # 获取第6题的元素
    getanswer_six = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_six + "']")
    getanswer_six.click()
    sleep(2)

    # 获取随机答案字符串
    random_answer_seven = random.choice(scl_answer)
    # 获取第7题的元素
    getanswer_seven = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_seven + "']")
    getanswer_seven.click()
    sleep(2)

    # 获取随机答案字符串
    random_answer_eight = random.choice(scl_answer)
    # 获取第8题的元素
    getanswer_eight = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_eight + "']")
    getanswer_eight.click()
    sleep(2)

    # 获取随机答案字符串
    random_answer_nine = random.choice(scl_answer)
    # 获取第9题的元素
    getanswer_nine = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_nine + "']")
    getanswer_nine.click()
    sleep(2)

    # 获取随机答案字符串
    random_answer_ten = random.choice(scl_answer)
    # 获取第10题的元素
    getanswer_ten = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_ten + "']")
    getanswer_ten.click()
    sleep(2)

    # 获取随机答案字符串
    random_answer_eleven = random.choice(scl_answer)
    # 获取第11题的元素
    getanswer_eleven = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_eleven + "']")
    getanswer_eleven.click()
    sleep(2)

    # 获取随机答案字符串
    random_answer_twelve = random.choice(scl_answer)
    # 获取第12题的元素
    getanswer_twelve = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_twelve + "']")
    getanswer_twelve.click()
    sleep(2)

    # 获取随机答案字符串
    random_answer_thirteen = random.choice(scl_answer)
    # 获取第13题的元素
    getanswer_thirteen = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_thirteen + "']")
    getanswer_thirteen.click()
    sleep(2)

    # 获取随机答案字符串
    random_answer_fourteen = random.choice(scl_answer)
    # 获取第14题的元素
    getanswer_fourteen = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_fourteen + "']")
    getanswer_fourteen.click()
    sleep(2)

    # 获取随机答案字符串
    random_answer_fiveteen = random.choice(scl_answer)
    # 获取第15题的元素
    getanswer_fiveteen = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_fiveteen + "']")
    getanswer_fiveteen.click()
    sleep(2)

    # 获取随机答案字符串
    random_answer_sixteen = random.choice(scl_answer)
    # 获取第16题的元素
    getanswer_sixteen = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_sixteen + "']")
    getanswer_sixteen.click()
    sleep(2)

    # 获取随机答案字符串
    random_answer_seventeen = random.choice(scl_answer)
    # 获取第17题的元素
    getanswer_seventeen = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_seventeen + "']")
    getanswer_seventeen.click()
    sleep(2)

    # 获取随机答案字符串
    random_answer_eighteen = random.choice(scl_answer)
    # 获取第18题的元素
    getanswer_eighteen = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_eighteen + "']")
    getanswer_eighteen.click()
    sleep(2)

    # 获取随机答案字符串
    random_answer_nineteen = random.choice(scl_answer)
    # 获取第19题的元素
    getanswer_nineteen = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_nineteen + "']")
    getanswer_nineteen.click()
    sleep(2)

    # 获取随机答案字符串
    random_answer_twenty = random.choice(scl_answer)
    # 获取第20题的元素
    getanswer_twenty = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_twenty + "']")
    getanswer_twenty.click()
    sleep(2)

    # 获取随机答案字符串
    random_answer_twenty_one = random.choice(scl_answer)
    # 获取第21题的元素
    getanswer_twenty_one = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_twenty_one + "']")
    getanswer_twenty_one.click()
    sleep(2)

    # 获取随机答案字符串
    random_answer_twenty_two = random.choice(scl_answer)
    # 获取第22题的元素
    getanswer_twenty_two = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_twenty_two + "']")
    getanswer_twenty_two.click()
    sleep(2)

    # 获取随机答案字符串
    random_answer_twenty_three = random.choice(scl_answer)
    # 获取第23题的元素
    getanswer_twenty_three = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_twenty_three + "']")
    getanswer_twenty_three.click()
    sleep(2)

    # 获取随机答案字符串
    random_answer_twenty_four = random.choice(scl_answer)
    # 获取第24题的元素
    getanswer_twenty_four = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_twenty_four + "']")
    getanswer_twenty_four.click()
    sleep(2)

    # 获取随机答案字符串
    random_answer_twenty_five = random.choice(scl_answer)
    # 获取第25题的元素
    getanswer_twenty_five = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_twenty_five + "']")
    getanswer_twenty_five.click()
    sleep(2)

    # 获取随机答案字符串
    random_answer_twenty_six = random.choice(scl_answer)
    # 获取第26题的元素
    getanswer_twenty_six = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_twenty_six + "']")
    getanswer_twenty_six.click()
    sleep(2)

    # 获取随机答案字符串
    random_answer_twenty_seven = random.choice(scl_answer)
    # 获取第27题的元素
    getanswer_twenty_seven = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_twenty_seven + "']")
    getanswer_twenty_seven.click()
    sleep(2)

    # 获取随机答案字符串
    random_answer_twenty_eight = random.choice(scl_answer)
    # 获取第28题的元素
    getanswer_twenty_eight = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_twenty_eight + "']")
    getanswer_twenty_eight.click()
    sleep(2)

    # 获取随机答案字符串
    random_answer_twenty_nine = random.choice(scl_answer)
    # 获取第29题的元素
    getanswer_twenty_nine = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_twenty_nine + "']")
    getanswer_twenty_nine.click()
    sleep(2)

    # 获取随机答案字符串
    random_answer_thirty = random.choice(scl_answer)
    # 获取第30题的元素
    getanswer_thirty = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_thirty + "']")
    getanswer_thirty.click()
    sleep(2)

    # 获取随机答案字符串
    random_answer_thirty_one = random.choice(scl_answer)
    # 获取第31题的元素
    getanswer_thirty_one = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_thirty_one + "']")
    getanswer_thirty_one.click()
    sleep(2)

    # 获取随机答案字符串
    random_answer_thirty_two = random.choice(scl_answer)
    # 获取第32题的元素
    getanswer_thirty_two = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_thirty_two + "']")
    getanswer_thirty_two.click()
    sleep(2)

    # 获取随机答案字符串
    random_answer_thirty_three = random.choice(scl_answer)
    # 获取第33题的元素
    getanswer_thirty_three = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_thirty_three + "']")
    getanswer_thirty_three.click()
    sleep(2)

    # 获取随机答案字符串
    random_answer_thirty_four = random.choice(scl_answer)
    # 获取第34题的元素
    getanswer_thirty_four = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_thirty_four + "']")
    getanswer_thirty_four.click()
    sleep(2)

    # 获取随机答案字符串
    random_answer_thirty_five = random.choice(scl_answer)
    # 获取第35题的元素
    getanswer_thirty_five = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_thirty_five + "']")
    getanswer_thirty_five.click()
    sleep(2)

    # 获取随机答案字符串
    random_answer_thirty_six = random.choice(scl_answer)
    # 获取第36题的元素
    getanswer_thirty_six = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_thirty_six + "']")
    getanswer_thirty_six.click()
    sleep(2)

    # 获取随机答案字符串
    random_answer_thirty_seven = random.choice(scl_answer)
    # 获取第37题的元素
    getanswer_thirty_seven = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_thirty_seven + "']")
    getanswer_thirty_seven.click()
    sleep(2)

    # 获取随机答案字符串
    random_answer_thirty_eight = random.choice(scl_answer)
    # 获取第38题的元素
    getanswer_thirty_eight = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_thirty_eight + "']")
    getanswer_thirty_eight.click()
    sleep(2)

    # 获取随机答案字符串
    random_answer_thirty_nine = random.choice(scl_answer)
    # 获取第39题的元素
    getanswer_thirty_nine = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_thirty_nine + "']")
    getanswer_thirty_nine.click()
    sleep(2)

    # 获取随机答案字符串
    random_answer_fourty = random.choice(scl_answer)
    # 获取第40题的元素
    getanswer_fourty = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_fourty + "']")
    getanswer_fourty.click()
    sleep(2)

    # 获取随机答案字符串
    random_answer_fourty_one = random.choice(scl_answer)
    # 获取第41题的元素
    getanswer_fourty_one = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_fourty_one + "']")
    getanswer_fourty_one.click()
    sleep(2)

    # 获取随机答案字符串
    random_answer_fourty_two = random.choice(scl_answer)
    # 获取第42题的元素
    getanswer_fourty_two = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_fourty_two + "']")
    getanswer_fourty_two.click()
    sleep(2)

    # 获取随机答案字符串
    random_answer_fourty_three = random.choice(scl_answer)
    # 获取第43题的元素
    getanswer_fourty_three = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_fourty_three + "']")
    getanswer_fourty_three.click()
    sleep(2)

    # 获取随机答案字符串
    random_answer_fourty_four = random.choice(scl_answer)
    # 获取第44题的元素
    getanswer_fourty_four = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_fourty_four + "']")
    getanswer_fourty_four.click()
    sleep(2)

    # 获取随机答案字符串
    random_answer_fourty_five = random.choice(scl_answer)
    # 获取第45题的元素
    getanswer_fourty_five = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_fourty_five + "']")
    getanswer_fourty_five.click()
    sleep(1)

    # 获取随机答案字符串
    random_answer_46 = random.choice(scl_answer)
    # 获取第46题的元素
    getanswer_46 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_46 + "']")
    getanswer_46.click()
    sleep(1)

    # 获取随机答案字符串
    random_answer_47 = random.choice(scl_answer)
    # 获取第47题的元素
    getanswer_47 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_47 + "']")
    getanswer_47.click()
    sleep(1)

    # 获取随机答案字符串
    random_answer_48 = random.choice(scl_answer)
    # 获取第48题的元素
    getanswer_48 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_48 + "']")
    getanswer_48.click()
    sleep(1)

    # 获取随机答案字符串
    random_answer_49 = random.choice(scl_answer)
    # 获取第49题的元素
    getanswer_49 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_49 + "']")
    getanswer_49.click()
    sleep(1)

    # 获取随机答案字符串
    random_answer_50 = random.choice(scl_answer)
    # 获取第50题的元素
    getanswer_50 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_50 + "']")
    getanswer_50.click()
    sleep(1)

    # 获取随机答案字符串
    random_answer_51 = random.choice(scl_answer)
    # 获取第51题的元素
    getanswer_51 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_51 + "']")
    getanswer_51.click()
    sleep(1)

    # 获取随机答案字符串
    random_answer_52 = random.choice(scl_answer)
    # 获取第52题的元素
    getanswer_52 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_52 + "']")
    getanswer_52.click()
    sleep(1)

    # 获取随机答案字符串
    random_answer_53 = random.choice(scl_answer)
    # 获取第53题的元素
    getanswer_53 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_53 + "']")
    getanswer_53.click()
    sleep(1)

    # 获取随机答案字符串
    random_answer_54 = random.choice(scl_answer)
    # 获取第54题的元素
    getanswer_54 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_54 + "']")
    getanswer_54.click()
    sleep(1)

    # 获取随机答案字符串
    random_answer_55 = random.choice(scl_answer)
    # 获取第55题的元素
    getanswer_55 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_55 + "']")
    getanswer_55.click()
    sleep(1)

    # 获取随机答案字符串
    random_answer_56 = random.choice(scl_answer)
    # 获取第56题的元素
    getanswer_56 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_56 + "']")
    getanswer_56.click()
    sleep(1)

    # 获取随机答案字符串
    random_answer_57 = random.choice(scl_answer)
    # 获取第57题的元素
    getanswer_57 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_57 + "']")
    getanswer_57.click()
    sleep(1)

    # 获取随机答案字符串
    random_answer_58 = random.choice(scl_answer)
    # 获取第58题的元素
    getanswer_58 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_58 + "']")
    getanswer_58.click()
    sleep(1)

    # 获取随机答案字符串
    random_answer_59 = random.choice(scl_answer)
    # 获取第59题的元素
    getanswer_59 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_59 + "']")
    getanswer_59.click()
    sleep(1)

    # 获取随机答案字符串
    random_answer_60 = random.choice(scl_answer)
    # 获取第60题的元素
    getanswer_60 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_60 + "']")
    getanswer_60.click()
    sleep(1)

    # 获取随机答案字符串
    random_answer_61 = random.choice(scl_answer)
    # 获取第61题的元素
    getanswer_61 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_61 + "']")
    getanswer_61.click()
    sleep(1)

    # 获取随机答案字符串
    random_answer_62 = random.choice(scl_answer)
    # 获取第62题的元素
    getanswer_62 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_62 + "']")
    getanswer_62.click()
    sleep(1)

    # 获取随机答案字符串
    random_answer_63 = random.choice(scl_answer)
    # 获取第63题的元素
    getanswer_63 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_63 + "']")
    getanswer_63.click()
    sleep(1)

    # 获取随机答案字符串
    random_answer_64 = random.choice(scl_answer)
    # 获取第64题的元素
    getanswer_64 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_64 + "']")
    getanswer_64.click()
    sleep(1)

    # 获取随机答案字符串
    random_answer_65 = random.choice(scl_answer)
    # 获取第65题的元素
    getanswer_65 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_65 + "']")
    getanswer_65.click()
    sleep(1)

    # 获取随机答案字符串
    random_answer_66 = random.choice(scl_answer)
    # 获取第66题的元素
    getanswer_66 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_66 + "']")
    getanswer_66.click()
    sleep(1)

    # 获取随机答案字符串
    random_answer_67 = random.choice(scl_answer)
    # 获取第67题的元素
    getanswer_67 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_67 + "']")
    getanswer_67.click()
    sleep(1)

    # 获取随机答案字符串
    random_answer_68 = random.choice(scl_answer)
    # 获取第68题的元素
    getanswer_68 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_68 + "']")
    getanswer_68.click()
    sleep(1)

    # 获取随机答案字符串
    random_answer_69 = random.choice(scl_answer)
    # 获取第69题的元素
    getanswer_69 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_69 + "']")
    getanswer_69.click()
    sleep(1)

    # 获取随机答案字符串
    random_answer_70 = random.choice(scl_answer)
    # 获取第70题的元素
    getanswer_70 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_70 + "']")
    getanswer_70.click()
    sleep(1)

    # 获取随机答案字符串
    random_answer_71 = random.choice(scl_answer)
    # 获取第71题的元素
    getanswer_71 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_71 + "']")
    getanswer_71.click()
    sleep(1)

    # 获取随机答案字符串
    random_answer_72 = random.choice(scl_answer)
    # 获取第72题的元素
    getanswer_72 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_72 + "']")
    getanswer_72.click()
    sleep(1)

    # 获取随机答案字符串
    random_answer_73 = random.choice(scl_answer)
    # 获取第73题的元素
    getanswer_73 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_73 + "']")
    getanswer_73.click()
    sleep(1)

    # 获取随机答案字符串
    random_answer_74 = random.choice(scl_answer)
    # 获取第74题的元素
    getanswer_74 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_74 + "']")
    getanswer_74.click()
    sleep(1)

    # 获取随机答案字符串
    random_answer_75 = random.choice(scl_answer)
    # 获取第75题的元素
    getanswer_75 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_75 + "']")
    getanswer_75.click()
    sleep(1)

    # 获取随机答案字符串
    random_answer_76 = random.choice(scl_answer)
    # 获取第76题的元素
    getanswer_76 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_76 + "']")
    getanswer_76.click()
    sleep(1)

    # 获取随机答案字符串
    random_answer_77 = random.choice(scl_answer)
    # 获取第77题的元素
    getanswer_77 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_77 + "']")
    getanswer_77.click()
    sleep(1)

    # 获取随机答案字符串
    random_answer_78 = random.choice(scl_answer)
    # 获取第78题的元素
    getanswer_78 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_78 + "']")
    getanswer_78.click()
    sleep(1)

    # 获取随机答案字符串
    random_answer_79 = random.choice(scl_answer)
    # 获取第79题的元素
    getanswer_79 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_79 + "']")
    getanswer_79.click()
    sleep(1)

    # 获取随机答案字符串
    random_answer_80 = random.choice(scl_answer)
    # 获取第80题的元素
    getanswer_80 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_80 + "']")
    getanswer_80.click()
    sleep(1)

    # 获取随机答案字符串
    random_answer_81 = random.choice(scl_answer)
    # 获取第81题的元素
    getanswer_81 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_81 + "']")
    getanswer_81.click()
    sleep(1)

    # 获取随机答案字符串
    random_answer_82 = random.choice(scl_answer)
    # 获取第82题的元素
    getanswer_82 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_82 + "']")
    getanswer_82.click()
    sleep(1)

    # 获取随机答案字符串
    random_answer_83 = random.choice(scl_answer)
    # 获取第83题的元素
    getanswer_83 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_83 + "']")
    getanswer_83.click()
    sleep(1)

    # 获取随机答案字符串
    random_answer_84 = random.choice(scl_answer)
    # 获取第84题的元素
    getanswer_84 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_84 + "']")
    getanswer_84.click()
    sleep(1)

    # 获取随机答案字符串
    random_answer_85 = random.choice(scl_answer)
    # 获取第85题的元素
    getanswer_85 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_85 + "']")
    getanswer_85.click()
    sleep(1)

    # 获取随机答案字符串
    random_answer_86 = random.choice(scl_answer)
    # 获取第86题的元素
    getanswer_86 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_86 + "']")
    getanswer_86.click()
    sleep(1)

    # 获取随机答案字符串
    random_answer_87 = random.choice(scl_answer)
    # 获取第87题的元素
    getanswer_87 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_87 + "']")
    getanswer_87.click()
    sleep(1)

    # 获取随机答案字符串
    random_answer_88 = random.choice(scl_answer)
    # 获取第88题的元素
    getanswer_88 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_88 + "']")
    getanswer_88.click()
    sleep(1)

    # 获取随机答案字符串
    random_answer_89 = random.choice(scl_answer)
    # 获取第89题的元素
    getanswer_89 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_89 + "']")
    getanswer_89.click()
    sleep(1)

    # 获取随机答案字符串
    random_answer_90 = random.choice(scl_answer)
    # 获取第90题的元素
    getanswer_90 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[3]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_90 + "']")
    getanswer_90.click()
    sleep(1)

    # 点击确认按钮
    clickComfirm = self.driver.find_element_by_xpath(
        "//android.widget.TextView[contains(@resource-id,'include_title_tv_save')]")
    clickComfirm.click()
    print 'you finish SCL scalc!'