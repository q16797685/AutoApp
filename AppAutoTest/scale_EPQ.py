#!/usr/bin/python
# coding:utf-8

"""
Created on 2017-07-13

@author: Wangchenyang

@功能：艾森克个性测验EPQ
"""

from time import sleep
import random


EPQ_Answer = ['是', '否']


def answerScale_EPQ(self):
    """ 艾森克个性测验EPQ """
    # 获取随机答案字符串
    random_answer_1 = random.choice(EPQ_Answer)
    # 获取第1题的元素
    getanswer_1 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_1 + "']")
    getanswer_1.click()
    sleep(1)

    random_answer_2 = random.choice(EPQ_Answer)
    # 获取第2题的元素
    getanswer_2 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_2 + "']")
    getanswer_2.click()
    sleep(1)

    random_answer_3 = random.choice(EPQ_Answer)
    # 获取第3题的元素
    getanswer_3 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_3 + "']")
    getanswer_3.click()
    sleep(1)

    random_answer_4 = random.choice(EPQ_Answer)
    # 获取第4题的元素
    getanswer_4 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_4 + "']")
    getanswer_4.click()
    sleep(1)

    random_answer_5 = random.choice(EPQ_Answer)
    # 获取第5题的元素
    getanswer_5 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_5 + "']")
    getanswer_5.click()
    sleep(1)

    random_answer_6 = random.choice(EPQ_Answer)
    # 获取第6题的元素
    getanswer_6 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_6 + "']")
    getanswer_6.click()
    sleep(1)

    random_answer_7 = random.choice(EPQ_Answer)
    # 获取第7题的元素
    getanswer_7 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_7 + "']")
    getanswer_7.click()
    sleep(1)

    random_answer_8 = random.choice(EPQ_Answer)
    # 获取第8题的元素
    getanswer_8 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_8 + "']")
    getanswer_8.click()
    sleep(1)

    random_answer_9 = random.choice(EPQ_Answer)
    # 获取第9题的元素
    getanswer_9 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_9 + "']")
    getanswer_9.click()
    sleep(1)

    random_answer_10 = random.choice(EPQ_Answer)
    # 获取第10题的元素
    getanswer_10 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_10 + "']")
    getanswer_10.click()
    sleep(1)

    random_answer_11 = random.choice(EPQ_Answer)
    # 获取第11题的元素
    getanswer_11 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_11 + "']")
    getanswer_11.click()
    sleep(1)

    random_answer_12 = random.choice(EPQ_Answer)
    # 获取第12题的元素
    getanswer_12 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_12 + "']")
    getanswer_12.click()
    sleep(1)

    random_answer_13 = random.choice(EPQ_Answer)
    # 获取第13题的元素
    getanswer_13 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_13 + "']")
    getanswer_13.click()
    sleep(1)

    random_answer_14 = random.choice(EPQ_Answer)
    # 获取第14题的元素
    getanswer_14 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_14 + "']")
    getanswer_14.click()
    sleep(1)

    random_answer_15 = random.choice(EPQ_Answer)
    # 获取第15题的元素
    getanswer_15 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_15 + "']")
    getanswer_15.click()
    sleep(1)

    random_answer_16 = random.choice(EPQ_Answer)
    # 获取第16题的元素
    getanswer_16 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_16 + "']")
    getanswer_16.click()
    sleep(1)

    random_answer_17 = random.choice(EPQ_Answer)
    # 获取第17题的元素
    getanswer_17 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_17 + "']")
    getanswer_17.click()
    sleep(1)

    random_answer_18 = random.choice(EPQ_Answer)
    # 获取第18题的元素
    getanswer_18 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_18 + "']")
    getanswer_18.click()
    sleep(1)

    random_answer_19 = random.choice(EPQ_Answer)
    # 获取第19题的元素
    getanswer_19 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_19 + "']")
    getanswer_19.click()
    sleep(1)

    random_answer_20 = random.choice(EPQ_Answer)
    # 获取第20题的元素
    getanswer_20 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_20 + "']")
    getanswer_20.click()
    sleep(1)

    random_answer_21 = random.choice(EPQ_Answer)
    # 获取第21题的元素
    getanswer_21 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_21 + "']")
    getanswer_21.click()
    sleep(1)

    random_answer_22 = random.choice(EPQ_Answer)
    # 获取第22题的元素
    getanswer_22 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_22 + "']")
    getanswer_22.click()
    sleep(1)

    random_answer_23 = random.choice(EPQ_Answer)
    # 获取第23题的元素
    getanswer_23 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_23 + "']")
    getanswer_23.click()
    sleep(1)

    random_answer_24 = random.choice(EPQ_Answer)
    # 获取第24题的元素
    getanswer_24 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_24 + "']")
    getanswer_24.click()
    sleep(1)

    random_answer_25 = random.choice(EPQ_Answer)
    # 获取第25题的元素
    getanswer_25 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_25 + "']")
    getanswer_25.click()
    sleep(1)

    random_answer_26 = random.choice(EPQ_Answer)
    # 获取第26题的元素
    getanswer_26 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_26 + "']")
    getanswer_26.click()
    sleep(1)

    random_answer_27 = random.choice(EPQ_Answer)
    # 获取第27题的元素
    getanswer_27 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_27 + "']")
    getanswer_27.click()
    sleep(1)

    random_answer_28 = random.choice(EPQ_Answer)
    # 获取第28题的元素
    getanswer_28 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_28 + "']")
    getanswer_28.click()
    sleep(1)

    random_answer_29 = random.choice(EPQ_Answer)
    # 获取第29题的元素
    getanswer_29 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_29 + "']")
    getanswer_29.click()
    sleep(1)

    random_answer_30 = random.choice(EPQ_Answer)
    # 获取第30题的元素
    getanswer_30 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_30 + "']")
    getanswer_30.click()
    sleep(1)

    random_answer_31 = random.choice(EPQ_Answer)
    # 获取第31题的元素
    getanswer_31 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_31 + "']")
    getanswer_31.click()
    sleep(1)

    random_answer_32 = random.choice(EPQ_Answer)
    # 获取第32题的元素
    getanswer_32 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_32 + "']")
    getanswer_32.click()
    sleep(1)

    random_answer_33 = random.choice(EPQ_Answer)
    # 获取第33题的元素
    getanswer_33 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_33 + "']")
    getanswer_33.click()
    sleep(1)

    random_answer_34 = random.choice(EPQ_Answer)
    # 获取第34题的元素
    getanswer_34 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_34 + "']")
    getanswer_34.click()
    sleep(1)

    random_answer_35 = random.choice(EPQ_Answer)
    # 获取第35题的元素
    getanswer_35 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_35 + "']")
    getanswer_35.click()
    sleep(1)

    random_answer_36 = random.choice(EPQ_Answer)
    # 获取第36题的元素
    getanswer_36 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_36 + "']")
    getanswer_36.click()
    sleep(1)

    random_answer_37 = random.choice(EPQ_Answer)
    # 获取第37题的元素
    getanswer_37 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_37 + "']")
    getanswer_37.click()
    sleep(1)

    random_answer_38 = random.choice(EPQ_Answer)
    # 获取第38题的元素
    getanswer_38 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_38 + "']")
    getanswer_38.click()
    sleep(1)

    random_answer_39 = random.choice(EPQ_Answer)
    # 获取第39题的元素
    getanswer_39 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_39 + "']")
    getanswer_39.click()
    sleep(1)

    random_answer_40 = random.choice(EPQ_Answer)
    # 获取第40题的元素
    getanswer_40 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_40 + "']")
    getanswer_40.click()
    sleep(1)

    random_answer_41 = random.choice(EPQ_Answer)
    # 获取第41题的元素
    getanswer_41 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_41 + "']")
    getanswer_41.click()
    sleep(1)

    random_answer_42 = random.choice(EPQ_Answer)
    # 获取第42题的元素
    getanswer_42 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_42 + "']")
    getanswer_42.click()
    sleep(1)

    random_answer_43 = random.choice(EPQ_Answer)
    # 获取第43题的元素
    getanswer_43 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_43 + "']")
    getanswer_43.click()
    sleep(1)

    random_answer_44 = random.choice(EPQ_Answer)
    # 获取第44题的元素
    getanswer_44 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_44 + "']")
    getanswer_44.click()
    sleep(1)

    random_answer_45 = random.choice(EPQ_Answer)
    # 获取第45题的元素
    getanswer_45 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_45 + "']")
    getanswer_45.click()
    sleep(1)

    random_answer_46 = random.choice(EPQ_Answer)
    # 获取第46题的元素
    getanswer_46 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_46 + "']")
    getanswer_46.click()
    sleep(1)

    random_answer_47 = random.choice(EPQ_Answer)
    # 获取第47题的元素
    getanswer_47 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_47 + "']")
    getanswer_47.click()
    sleep(1)

    random_answer_48 = random.choice(EPQ_Answer)
    # 获取第48题的元素
    getanswer_48 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_48 + "']")
    getanswer_48.click()
    sleep(1)

    random_answer_49 = random.choice(EPQ_Answer)
    # 获取第49题的元素
    getanswer_49 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_49 + "']")
    getanswer_49.click()
    sleep(1)

    random_answer_50 = random.choice(EPQ_Answer)
    # 获取第50题的元素
    getanswer_50 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_50 + "']")
    getanswer_50.click()
    sleep(1)

    random_answer_51 = random.choice(EPQ_Answer)
    # 获取第51题的元素
    getanswer_51 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_51 + "']")
    getanswer_51.click()
    sleep(1)

    random_answer_52 = random.choice(EPQ_Answer)
    # 获取第52题的元素
    getanswer_52 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_52 + "']")
    getanswer_52.click()
    sleep(1)

    random_answer_53 = random.choice(EPQ_Answer)
    # 获取第53题的元素
    getanswer_53 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_53 + "']")
    getanswer_53.click()
    sleep(1)

    random_answer_54 = random.choice(EPQ_Answer)
    # 获取第54题的元素
    getanswer_54 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_54 + "']")
    getanswer_54.click()
    sleep(1)

    random_answer_55 = random.choice(EPQ_Answer)
    # 获取第55题的元素
    getanswer_55 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_55 + "']")
    getanswer_55.click()
    sleep(1)

    random_answer_56 = random.choice(EPQ_Answer)
    # 获取第56题的元素
    getanswer_56 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_56 + "']")
    getanswer_56.click()
    sleep(1)

    random_answer_57 = random.choice(EPQ_Answer)
    # 获取第57题的元素
    getanswer_57 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_57 + "']")
    getanswer_57.click()
    sleep(1)

    random_answer_58 = random.choice(EPQ_Answer)
    # 获取第58题的元素
    getanswer_58 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_58 + "']")
    getanswer_58.click()
    sleep(1)

    random_answer_59 = random.choice(EPQ_Answer)
    # 获取第59题的元素
    getanswer_59 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_59 + "']")
    getanswer_59.click()
    sleep(1)

    random_answer_60 = random.choice(EPQ_Answer)
    # 获取第60题的元素
    getanswer_60 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_60 + "']")
    getanswer_60.click()
    sleep(1)

    random_answer_61 = random.choice(EPQ_Answer)
    # 获取第61题的元素
    getanswer_61 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_61 + "']")
    getanswer_61.click()
    sleep(1)

    random_answer_62 = random.choice(EPQ_Answer)
    # 获取第62题的元素
    getanswer_62 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_62 + "']")
    getanswer_62.click()
    sleep(1)

    random_answer_63 = random.choice(EPQ_Answer)
    # 获取第63题的元素
    getanswer_63 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_63 + "']")
    getanswer_63.click()
    sleep(1)

    random_answer_64 = random.choice(EPQ_Answer)
    # 获取第64题的元素
    getanswer_64 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_64 + "']")
    getanswer_64.click()
    sleep(1)

    random_answer_65 = random.choice(EPQ_Answer)
    # 获取第65题的元素
    getanswer_65 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_65 + "']")
    getanswer_65.click()
    sleep(1)

    random_answer_66 = random.choice(EPQ_Answer)
    # 获取第66题的元素
    getanswer_66 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_66 + "']")
    getanswer_66.click()
    sleep(1)

    random_answer_67 = random.choice(EPQ_Answer)
    # 获取第67题的元素
    getanswer_67 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_67 + "']")
    getanswer_67.click()
    sleep(1)

    random_answer_68 = random.choice(EPQ_Answer)
    # 获取第68题的元素
    getanswer_68 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_68 + "']")
    getanswer_68.click()
    sleep(1)

    random_answer_69 = random.choice(EPQ_Answer)
    # 获取第69题的元素
    getanswer_69 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_69 + "']")
    getanswer_69.click()
    sleep(1)

    random_answer_70 = random.choice(EPQ_Answer)
    # 获取第70题的元素
    getanswer_70 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_70 + "']")
    getanswer_70.click()
    sleep(1)

    random_answer_71 = random.choice(EPQ_Answer)
    # 获取第71题的元素
    getanswer_71 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_71 + "']")
    getanswer_71.click()
    sleep(1)

    random_answer_72 = random.choice(EPQ_Answer)
    # 获取第72题的元素
    getanswer_72 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_72 + "']")
    getanswer_72.click()
    sleep(1)

    random_answer_73 = random.choice(EPQ_Answer)
    # 获取第73题的元素
    getanswer_73 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_73 + "']")
    getanswer_73.click()
    sleep(1)

    random_answer_74 = random.choice(EPQ_Answer)
    # 获取第74题的元素
    getanswer_74 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_74 + "']")
    getanswer_74.click()
    sleep(1)

    random_answer_75 = random.choice(EPQ_Answer)
    # 获取第75题的元素
    getanswer_75 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_75 + "']")
    getanswer_75.click()
    sleep(1)

    random_answer_76 = random.choice(EPQ_Answer)
    # 获取第76题的元素
    getanswer_76 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_76 + "']")
    getanswer_76.click()
    sleep(1)

    random_answer_77 = random.choice(EPQ_Answer)
    # 获取第77题的元素
    getanswer_77 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_77 + "']")
    getanswer_77.click()
    sleep(1)

    random_answer_78 = random.choice(EPQ_Answer)
    # 获取第78题的元素
    getanswer_78 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_78 + "']")
    getanswer_78.click()
    sleep(1)

    random_answer_79 = random.choice(EPQ_Answer)
    # 获取第79题的元素
    getanswer_79 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_79 + "']")
    getanswer_79.click()
    sleep(1)

    random_answer_80 = random.choice(EPQ_Answer)
    # 获取第80题的元素
    getanswer_80 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_80 + "']")
    getanswer_80.click()
    sleep(1)

    random_answer_81 = random.choice(EPQ_Answer)
    # 获取第81题的元素
    getanswer_81 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_81 + "']")
    getanswer_81.click()
    sleep(1)

    random_answer_82 = random.choice(EPQ_Answer)
    # 获取第82题的元素
    getanswer_82 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_82 + "']")
    getanswer_82.click()
    sleep(1)

    random_answer_83 = random.choice(EPQ_Answer)
    # 获取第83题的元素
    getanswer_83 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_83 + "']")
    getanswer_83.click()
    sleep(1)

    random_answer_84 = random.choice(EPQ_Answer)
    # 获取第84题的元素
    getanswer_84 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_84 + "']")
    getanswer_84.click()
    sleep(1)

    random_answer_85 = random.choice(EPQ_Answer)
    # 获取第85题的元素
    getanswer_85 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_85 + "']")
    getanswer_85.click()
    sleep(1)

    random_answer_86 = random.choice(EPQ_Answer)
    # 获取第86题的元素
    getanswer_86 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_86 + "']")
    getanswer_86.click()
    sleep(1)

    random_answer_87 = random.choice(EPQ_Answer)
    # 获取第87题的元素
    getanswer_87 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[3]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_87 + "']")
    getanswer_87.click()
    sleep(1)

    random_answer_88 = random.choice(EPQ_Answer)
    # 获取第4题的元素
    getanswer_88 = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[5]/android.widget.LinearLayout[3]/android.widget.LinearLayout"
        "/android.widget.RadioButton[contains(@resource-id,'rb1') and @text='" + random_answer_88 + "']")
    getanswer_88.click()
    sleep(1)

    # 点击确认按钮
    clickComfirm = self.driver.find_element_by_xpath(
        "//android.widget.TextView[contains(@resource-id,'include_title_tv_save')]")
    clickComfirm.click()
    print 'you finish 艾森克个性测验EPQ scalc!'