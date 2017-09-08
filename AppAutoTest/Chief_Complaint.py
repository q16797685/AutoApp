#!/usr/bin/python
# coding:utf-8

"""
Created on 2017-07-17

@author: Wangchenyang

@回答问卷主诉
"""


from selenium.webdriver.support.wait import WebDriverWait
import random

question_one = ['喜欢胡思乱想，与别人说话有点儿紧张。别人不按我说的做我很生气', '睡不好人累头痛困疲惫做恶梦', '晚上失眠，脑袋总是在想东西',
                '不开心,往坏处想事,抗压力差', '头晕头痛失眠喜欢胡思乱想', '失眠', '喜欢胡思乱想，与别人说话有点儿紧张。别人不按我说的做我很生气',
                '失眠，晚上睡不着，偶尔耳边有声音']
question_two = ['一周', '两周', '一个月', '半个月', '三个月', '半年', '一年', '三年', '五年', '十年', '不记得']


def answerChief_Complaint(self):
    # 主诉
    # 简要描述来就医的最不舒服的症状或表现？（限12个字）
    # 第1题的获取的答案
    ran_char_one = random.choice(question_one)
    # 获取第1题，文本
    answer_one = WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath(
        "//android.widget.EditText[contains(@resource-id,'et_answer')]"))
    answer_one.send_keys(ran_char_one.decode('utf-8'))
    send_wb = self.driver.find_element_by_xpath("//android.widget.Button[contains(@resource-id,'btn_send_wb')]")
    send_wb.click()

    ''' 简要描述来就医的最不舒服的症状或表现？（限12个字）'''
    # 第2题的获取的答案
    ran_char_two = random.choice(question_two)
    # 获取第2题，文本
    answer_two = WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_xpath(
        "//android.widget.EditText[contains(@resource-id,'et_answer')]"))
    answer_two.send_keys(ran_char_two.decode('utf-8'))
    send_wb.click()
    print '完成主诉'
