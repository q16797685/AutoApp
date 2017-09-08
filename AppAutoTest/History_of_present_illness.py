#!/usr/bin/python
# coding:utf-8

"""
Created on 2017-7-17

@author: Wangchenyang

@回答现病史
"""


from selenium.webdriver.support.wait import WebDriverWait
import random
from commonMethod import clickXz
from commonMethod import clickWb


question_six = ['湘雅附二', '湘雅附一', '脑科医院', '不记得了']
question_eight = ['舍曲林片', '奥氮平', '文拉法辛胶囊', '启维', '思瑞康', '维思通', '丙戊酸钠片', '不记得了']
question_nine = ['不想做事，总觉得有人要害自己', '感觉身上有异味', '自我评价低', '不想和任何能说话交谈', '说不清楚']
question_eleven = ['1周', '2周', '3周']
question_nineteen = ['1周', '2周', '3周']

much_choose_context = \
    ['家庭原因',
     '工作和学业压力',
     '经济压力',
     '夫妻感情不好',
     '意外事故',
     '外伤导致的',
     '无明显原因'
     ]

checkbox_context = \
    ['有想死的念头',
     '心情不好，不开心',
     '对任何事情都提不起来兴趣，感觉生活没有意思',
     '有过自杀或者伤害自己的表现',
     '睡眠不好，难以入睡',
     '早醒，凌晨就醒来，难以再次入睡',
     '感觉自己很了不起，很厉害',
     '感觉脑子变聪明了，反应更快了',
     '脾气大，很容易被激怒',
     '有伤害他人的想法或行为'
     ]

checkbox_second_context = \
    ['有想死的念头',
     '心情不好，不开心',
     '对任何事情都提不起来兴趣，感觉生活没有意思',
     '有过自杀或者伤害自己的表现',
     '睡眠不好，难以入睡',
     '早醒，凌晨就醒来，难以再次入睡',
     '感觉自己很了不起，很厉害',
     '感觉脑子变聪明了，反应更快了',
     '脾气大，很容易被激怒',
     '与首次发病症状相同'
     ]

question_choice = ['1', '2']


def answerHistory_of_present_illness(self):
    # 现病史
    # 针对你的病情，是否是第一次到医院就诊？
    randomchoice_one = random.choice(question_choice)
    print randomchoice_one
    answer_three = self.driver.find_element_by_xpath(
        "//android.widget.TextView[contains(@resource-id,'item_tv1') and contains(@text,'" + randomchoice_one + "')]")
    print answer_three.text
    answer_three.click()
    # send_xz = self.driver.find_element_by_xpath("//android.widget.Button[contains(@resource-id,'btn_send_xz')]")
    clickXz(self)

    if randomchoice_one == '2':
        # 最早出现这种不舒服的时候有哪些表现？
        answer_four = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(
            "//android.widget.TextView[contains(@resource-id,'item_tv1') and @text='1']"))
        answer_four.click()
        question_four_choice = random.choice(checkbox_context)
        much_choice = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(
            "//android.widget.CheckBox[contains(@resource-id,'checkBox') and @text='" + question_four_choice + "']"))
        print much_choice.text
        much_choice.click()
        comfirm = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(
            "//android.widget.TextView[contains(@resource-id,'include_title_tv_save')]"))
        comfirm.click()

        # 最早出现这种不舒服的时候是否到医院就诊？
        answer_five = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(
            "//android.widget.TextView[contains(@resource-id,'item_tv1') and @text='1']"))
        print answer_five.text
        answer_five.click()
        clickXz(self)

        # 请输入当时就诊医院的名字
        ran_char_six = random.choice(question_six)
        # 获取第6题，文本
        answer_six = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(
            "//android.widget.EditText[contains(@resource-id,'et_answer')]"))
        print answer_six.text
        answer_six.send_keys(ran_char_six.decode('utf-8'))
        clickWb(self)

        # 最早出现这种不舒服的时候进行过哪些治疗
        answer_seven = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(
            "//android.widget.TextView[contains(@resource-id,'item_tv1') and @text='1']"))
        print answer_seven.text
        answer_seven.click()
        clickXz(self)

        # 使用的药物或手术名称是
        ran_char_eight = random.choice(question_eight)
        # 获取第8题，文本
        answer_eight = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(
            "//android.widget.EditText[contains(@resource-id,'et_answer')]"))
        print answer_eight.text
        answer_eight.send_keys(ran_char_eight.decode('utf-8'))
        clickWb(self)

        # 治疗的效果怎样
        answer_nine = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(
            "//android.widget.TextView[contains(@resource-id,'item_tv1') and @text='1']"))
        print answer_nine.text
        answer_nine.click()
        clickXz(self)

        # 从最早出现这种不舒服的表现至今，中间有没有好过？
        answer_ten = self.driver.find_element_by_xpath(
            "//android.widget.TextView[contains(@resource-id,'item_tv1') and @text='1']")
        print answer_ten.text
        answer_ten.click()
        clickXz(self)

        # 第二次发病至今多少天（或多少月？或多少年）？（要求准确）
        ran_char_eleven = random.choice(question_eleven)
        # 获取第11题，文本
        answer_eleven = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(
            "//android.widget.EditText[contains(@resource-id,'et_answer')]"))
        print answer_eleven.text
        answer_eleven.send_keys(ran_char_eleven.decode('utf-8'))
        clickWb(self)

        # 与首次发病相比，第二次发病时有哪些不一样的症状
        answer_thirteen = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(
            "//android.widget.TextView[contains(@resource-id,'item_tv1') and @text='1']"))
        print answer_thirteen.text
        answer_thirteen.click()
        question_thirtenn_choice = random.choice(checkbox_second_context)
        much_choice = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(
            "//android.widget.CheckBox[contains(@resource-id,'checkBox') and @text='" + question_thirtenn_choice + "']"))
        print much_choice.text
        much_choice.click()
        comfirm.click()

        # 第二次发病时是否到医院就诊
        answer_thirteen = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(
            "//android.widget.TextView[contains(@resource-id,'item_tv1') and @text='1']"))
        print answer_thirteen.text
        answer_thirteen.click()
        clickXz(self)

        # 请输入第二次就诊医院的名字
        ran_char_fourteen = random.choice(question_six)
        # 获取第14题，文本
        answer_fourteen = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(
            "//android.widget.EditText[contains(@resource-id,'et_answer')]"))
        print answer_fourteen.text
        answer_fourteen.send_keys(ran_char_fourteen.decode('utf-8'))
        clickWb(self)

        # 第二次发病时进行过哪些治疗
        answer_fiveteen = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(
            "//android.widget.TextView[contains(@resource-id,'item_tv1') and @text='1']"))
        print answer_fiveteen.text
        answer_fiveteen.click()
        clickXz(self)

        # 请输入第二次治疗时使用的药物或手术名称
        ran_char_sixteen = random.choice(question_eight)
        # 获取第16题，文本
        answer_sixteen = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(
            "//android.widget.EditText[contains(@resource-id,'et_answer')]"))
        print answer_sixteen.text
        answer_sixteen.send_keys(ran_char_sixteen.decode('utf-8'))
        clickWb(self)

        # 治疗的效果怎样
        answer_seventeen = self.driver.find_element_by_xpath(
            "//android.widget.TextView[contains(@resource-id,'item_tv1') and @text='2']")
        print answer_seventeen.text
        answer_seventeen.click()
        clickXz(self)

        # 本次发病与第二次发病的症状一样吗
        answer_eightteen = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(
            "//android.widget.TextView[contains(@resource-id,'item_tv1') and @text='1']"))
        print answer_eightteen.text
        answer_eightteen.click()
        clickXz(self)

        # 本次发病至今多少天（或多少月？或多少年）？（要求准确）
        ran_char_nineteen = random.choice(question_nineteen)
        # 获取第19题，文本
        answer_nineteen = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(
            "//android.widget.EditText[contains(@resource-id,'et_answer')]"))
        print answer_nineteen.text
        answer_nineteen.send_keys(ran_char_nineteen.decode('utf-8'))
        clickWb(self)

        # 这次发病有哪些主要症状
        answer_twenty = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(
            "//android.widget.TextView[contains(@resource-id,'item_tv1') and @text='1']"))
        answer_twenty.click()
        much_choice = self.driver.find_element_by_xpath(
            "//android.widget.CheckBox[contains(@resource-id,'checkBox') and @text='" + question_four_choice + "']")
        print much_choice.text
        much_choice.click()
        comfirm.click()

        # 您是由于什么原因导致了这些情况
        randomchoice_twenty_one = random.choice(much_choose_context)
        answer_twenty_one = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(
            "//android.widget.TextView[contains(@resource-id,'item_tv1') and contains(@text,'"+ randomchoice_twenty_one +"')]"))
        print answer_twenty_one.text
        answer_twenty_one.click()
        clickXz(self)

        # 现在是否还在工作和学习
        answer_twenty_two = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(
            "//android.widget.TextView[contains(@resource-id,'item_tv1') and @text='1']"))
        print answer_twenty_two.text
        answer_twenty_two.click()
        clickXz(self)

        # 工作和学习能力是否有下降
        answer_twenty_three = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(
            "//android.widget.TextView[contains(@resource-id,'item_tv1') and @text='1']"))
        print answer_twenty_three.text
        answer_twenty_three.click()
        clickXz(self)

        # 多久了
        answer_twenty_four = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(
            "//android.widget.TextView[contains(@resource-id,'item_tv1') and @text='1']"))
        print answer_twenty_four.text
        answer_twenty_four.click()
        clickXz(self)

        # 目前有伤人毁物的想法或行动吗
        answer_twenty_five = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(
            "//android.widget.TextView[contains(@resource-id,'item_tv1') and @text='1']"))
        print answer_twenty_five.text
        answer_twenty_five.click()
        clickXz(self)

        # 有轻生的想法或行为吗
        answer_twenty_six = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(
            "//android.widget.TextView[contains(@resource-id,'item_tv1') and @text='1']"))
        print answer_twenty_six.text
        answer_twenty_six.click()
        clickXz(self)

        # 近期是否有感冒、发烧？
        answer_twenty_seven = self.driver.find_element_by_xpath(
            "//android.widget.TextView[contains(@resource-id,'item_tv1') and contains(@text,'1')]")
        print answer_twenty_seven.text
        answer_twenty_seven.click()
        clickXz(self)

        # 睡眠情况如何
        answer_twenty_eight = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(
            "//android.widget.TextView[contains(@resource-id,'item_tv1') and @text='1']"))
        print answer_twenty_eight.text
        answer_twenty_eight.click()
        clickXz(self)

        # 做梦多吗
        answer_twenty_nine = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(
            "//android.widget.TextView[contains(@resource-id,'item_tv1') and @text='1']"))
        print answer_twenty_nine.text
        answer_twenty_nine.click()
        clickXz(self)

        # 饮食情况怎样
        answer_thirty = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(
            "//android.widget.TextView[contains(@resource-id,'item_tv1') and @text='1']"))
        print answer_thirty.text
        answer_thirty.click()
        clickXz(self)

        # 大小便是否正常
        answer_thirty_one = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(
            "//android.widget.TextView[contains(@resource-id,'item_tv1') and @text='2']"))
        print answer_thirty_one.text
        answer_thirty_one.click()
        clickXz(self)
        print '完成现病史'
    else:
        # 这次发病有哪些主要症状
        answer_twenty = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(
            "//android.widget.TextView[contains(@resource-id,'item_tv1') and @text='1']"))
        answer_twenty.click()
        question_twenty_choice = random.choice(checkbox_context)
        much_choice = self.driver.find_element_by_xpath(
            "//android.widget.CheckBox[contains(@resource-id,'checkBox') and @text='" + question_twenty_choice + "']")
        print much_choice.text
        much_choice.click()
        comfirm = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(
            "//android.widget.TextView[contains(@resource-id,'include_title_tv_save')]"))
        comfirm.click()

        # 您是由于什么原因导致了这些情况
        randomchoice_twenty_one = random.choice(much_choose_context)
        answer_twenty_one = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(
            "//android.widget.TextView[contains(@resource-id,'item_tv1') and contains(@text,'"+ randomchoice_twenty_one +"')]"))
        print answer_twenty_one.text
        answer_twenty_one.click()
        clickXz(self)

        # 现在是否还在工作和学习
        answer_twenty_two = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(
            "//android.widget.TextView[contains(@resource-id,'item_tv1') and @text='1']"))
        print answer_twenty_two.text
        answer_twenty_two.click()
        clickXz(self)

        # 工作和学习能力是否有下降
        answer_twenty_three = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(
            "//android.widget.TextView[contains(@resource-id,'item_tv1') and @text='1']"))
        print answer_twenty_three.text
        answer_twenty_three.click()
        clickXz(self)

        # 多久了
        answer_twenty_four = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(
            "//android.widget.TextView[contains(@resource-id,'item_tv1') and @text='1']"))
        print answer_twenty_four.text
        answer_twenty_four.click()
        clickXz(self)

        # 目前有伤人毁物的想法或行动吗
        answer_twenty_five = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(
            "//android.widget.TextView[contains(@resource-id,'item_tv1') and @text='1']"))
        print answer_twenty_five.text
        answer_twenty_five.click()
        clickXz(self)

        # 有轻生的想法或行为吗
        answer_twenty_six = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(
            "//android.widget.TextView[contains(@resource-id,'item_tv1') and @text='1']"))
        print answer_twenty_six.text
        answer_twenty_six.click()
        clickXz(self)

        # 近期是否有感冒、发烧？
        answer_twenty_seven = self.driver.find_element_by_xpath(
            "//android.widget.TextView[contains(@resource-id,'item_tv1') and @text='1']")
        print answer_twenty_seven.text
        answer_twenty_seven.click()
        clickXz(self)

        # 睡眠情况如何
        answer_twenty_eight = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(
            "//android.widget.TextView[contains(@resource-id,'item_tv1') and @text='1']"))
        print answer_twenty_eight.text
        answer_twenty_eight.click()
        clickXz(self)

        # 做梦多吗
        answer_twenty_nine = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(
            "//android.widget.TextView[contains(@resource-id,'item_tv1') and @text='1']"))
        print answer_twenty_nine.text
        answer_twenty_nine.click()
        clickXz(self)

        # 饮食情况怎样
        answer_thirty = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(
            "//android.widget.TextView[contains(@resource-id,'item_tv1') and @text='1']"))
        print answer_thirty.text
        answer_thirty.click()
        clickXz(self)

        # 大小便是否正常
        answer_thirty_one = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(
            "//android.widget.TextView[contains(@resource-id,'item_tv1') and @text='2']"))
        print answer_thirty_one.text
        answer_thirty_one.click()
        clickXz(self)
        print '完成现病史'