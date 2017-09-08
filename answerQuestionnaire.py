#!/usr/bin/python
#coding:utf-8

'''
Created on 2017-xx-xx

@author: Wangchenyang
'''


from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
import random

question_one = ['喜欢胡思乱想，与别人说话有点儿紧张。别人不按我说的做我很生气','睡不好人累头痛困疲惫做恶梦','晚上失眠，脑袋总是在想东西',
                '不开心,往坏处想事,抗压力差','头晕头痛失眠喜欢胡思乱想','失眠','喜欢胡思乱想，与别人说话有点儿紧张。别人不按我说的做我很生气',
                '失眠，晚上睡不着，偶尔耳边有声音']
question_two = ['一周','两周','一个月','半个月','三个月','半年','一年','三年','五年','十年','不记得']
question_six = ['湘雅附二','湘雅附一','脑科医院','不记得了']
question_eight = ['盐酸舍曲林片','氯氮平','安乐嗪棕榈酸酯','奥氮平','奥沙西泮片','维思通','氯普唑仑','不记得了']
question_nine = ['不想做事，总觉得有人要害自己','感觉身上有异味','自我评价低','不想和任何能说话交谈','说不清楚']
question_eleven = ['1周','2周','3周']
question_nineteen = ['1周','2周','3周']
question_twenty_one  = ['没有力气','睡不醒','想打人','想骂人']
question_twenty_three = ['有冲动想打人','有冲动想骂人','摔自己的物品']
question_twenty_five = ['有冲动想跳楼','有冲动想杀人','对世界没有留恋的']
#   仅限女性
question_fourty_three = ['11','12','13','不记得了']
userdict = {'phone':['15071001668',2]}      #       1：代表男   2   ：代表女
phnumber = userdict['phone'][0]
gender = userdict['phone'][1]
scalc_answer = ['绝大部分或全部时间','少部分时间','相当多时间','绝大部分或全部时间']


def questinNaire(self):
#   主诉
    # 第1题的获取的答案
    ran_char_one = random.choice(question_one)
    # 获取第1题，文本
    # answer_one = self.driver.find_element_by_xpath("//android.widget.EditText[contains(@resource-id,'et_answer')]")
    # answer_one.send_keys(ran_char_one.decode('utf-8'))
    # send_wb = self.driver.find_element_by_xpath("//android.widget.Button[contains(@resource-id,'btn_send_wb')]")
    # send_wb.click()
    # sleep(3)


    answer_one = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath("//android.widget.EditText[contains(@resource-id,'et_answer')]"))
    answer_one.send_keys(ran_char_one.decode('utf-8'))
    send_wb = self.driver.find_element_by_xpath("//android.widget.Button[contains(@resource-id,'btn_send_wb')]")
    send_wb.click()

    # 第2题的获取的答案
    ran_char_two = random.choice(question_two)
    # 获取第2题，文本
    answer_two = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath("//android.widget.EditText[contains(@resource-id,'et_answer')]"))
    answer_two.send_keys(ran_char_two.decode('utf-8'))
    send_wb.click()
    print '完成主诉'

### 现病史
    #获取第3题，单选
    answer_three = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath("//android.widget.TextView[contains(@resource-id,'item_tv1') and @text='2']"))
    answer_three.click()
    send_xz = self.driver.find_element_by_xpath("//android.widget.Button[contains(@resource-id,'btn_send_xz')]")
    send_xz.click()

    #获取第4题，多选修改后的
    answer_four = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath("//android.widget.TextView[contains(@resource-id,'item_tv1') and @text='1']"))
    answer_four.click()
    sleep(2)
    much_choice = self.driver.find_element_by_xpath("//android.widget.TextView[contains(@resource-id,'textView1') and @text='有想死的念头']")
    much_choice.click()
    comfirm = self.driver.find_element_by_xpath("//android.widget.TextView[contains(@resource-id,'include_title_tv_save')]")
    comfirm.click()

    #获取第10题，单选
    answer_five = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath("//android.widget.TextView[contains(@resource-id,'item_tv1') and @text='1']"))
    answer_five.click()
    send_xz.click()

    # 第6题的获取的答案
    ran_char_six = random.choice(question_six)
    # 获取第6题，文本
    answer_six = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath("//android.widget.EditText[contains(@resource-id,'et_answer')]"))
    answer_six.send_keys(ran_char_six.decode('utf-8'))
    send_wb.click()

    #获取第7题，单选
    answer_seven = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath("//android.widget.TextView[contains(@resource-id,'item_tv1') and @text='1']"))
    answer_seven.click()
    send_xz.click()

    # 第8题的获取的答案
    ran_char_eight = random.choice(question_eight)
    # 获取第8题，文本
    answer_eight = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath("//android.widget.EditText[contains(@resource-id,'et_answer')]"))
    answer_eight.send_keys(ran_char_eight.decode('utf-8'))
    send_wb.click()

    # 获取第9题，单选
    answer_nine = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath("//android.widget.TextView[contains(@resource-id,'item_tv1') and @text='1']"))
    answer_nine.click()
    send_xz.click()

    #获取第10题，单选
    answer_ten = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath("//android.widget.TextView[contains(@resource-id,'item_tv1') and @text='1']"))
    answer_ten.click()
    send_xz.click()

    # 第11题的获取的答案
    ran_char_eleven = random.choice(question_eleven)
    # 获取第11题，文本
    answer_eleven = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath("//android.widget.EditText[contains(@resource-id,'et_answer')]"))
    answer_eleven.send_keys(ran_char_eleven.decode('utf-8'))
    send_wb.click()

    # 获取第12题，多选
    answer_thirteen = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath("//android.widget.TextView[contains(@resource-id,'item_tv1') and @text='1']"))
    answer_thirteen.click()
    much_choice = self.driver.find_element_by_xpath("//android.widget.TextView[contains(@resource-id,'textView1') and @text='早醒，凌晨就醒来，难以再次入睡']")
    much_choice.click()
    comfirm.click()

    #获取第13题，单选
    answer_thirteen = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath("//android.widget.TextView[contains(@resource-id,'item_tv1') and @text='1']"))
    answer_thirteen.click()
    send_xz.click()

    # 第14题的获取的答案
    ran_char_fourteen = random.choice(question_six)
    # 获取第14题，文本
    answer_fourteen = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath("//android.widget.EditText[contains(@resource-id,'et_answer')]"))
    answer_fourteen.send_keys(ran_char_fourteen.decode('utf-8'))
    send_wb.click()

    #获取第110题，单选
    answer_fiveteen = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath("//android.widget.TextView[contains(@resource-id,'item_tv1') and @text='1']"))
    answer_fiveteen.click()
    send_xz.click()

    # 第16题的获取的答案
    ran_char_sixteen = random.choice(question_eight)
    # 获取第16题，文本
    answer_sixteen = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath("//android.widget.EditText[contains(@resource-id,'et_answer')]"))
    answer_sixteen.send_keys(ran_char_sixteen.decode('utf-8'))
    send_wb.click()

    #获取第17题，单选
    answer_seventeen = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath("//android.widget.TextView[contains(@resource-id,'item_tv1') and @text='1']"))
    answer_seventeen.click()
    send_xz.click()
    sleep(3)

    #获取第18题，单选
    answer_eightteen = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath("//android.widget.TextView[contains(@resource-id,'item_tv1') and @text='1']"))
    answer_eightteen.click()
    send_xz.click()
    sleep(3)

    # 第19题的获取的答案
    ran_char_nineteen = random.choice(question_nineteen)
    # 获取第19题，文本
    answer_nineteen = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath("//android.widget.EditText[contains(@resource-id,'et_answer')]"))
    answer_nineteen.send_keys(ran_char_nineteen.decode('utf-8'))
    send_wb.click()
    sleep(3)

    # 获取第20题，多选
    answer_twenty = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath("//android.widget.TextView[contains(@resource-id,'item_tv1') and @text='1']"))
    answer_twenty.click()
    sleep(3)
    much_choice = self.driver.find_element_by_xpath(
        "//android.widget.TextView[contains(@resource-id,'textView1') and @text='睡眠不好，难以入睡']")
    much_choice.click()
    comfirm.click()

    #获取第21题，单选
    answer_twenty_one = self.driver.find_element_by_xpath("//android.widget.TextView[contains(@resource-id,'item_tv1') and @text='1']")
    answer_twenty_one.click()
    send_xz.click()

    #获取第22题，单选
    answer_twenty_two = self.driver.find_element_by_xpath("//android.widget.TextView[contains(@resource-id,'item_tv1') and @text='1']")
    answer_twenty_two.click()
    send_xz.click()

    #获取第23题，单选
    answer_twenty_three = self.driver.find_element_by_xpath("//android.widget.TextView[contains(@resource-id,'item_tv1') and @text='1']")
    answer_twenty_three.click()
    send_xz.click()

    #获取第24题，单选
    answer_twenty_four = self.driver.find_element_by_xpath("//android.widget.TextView[contains(@resource-id,'item_tv1') and @text='1']")
    answer_twenty_four.click()
    send_xz.click()

    #获取第210题，单选
    answer_twenty_five = self.driver.find_element_by_xpath("//android.widget.TextView[contains(@resource-id,'item_tv1') and @text='1']")
    answer_twenty_five.click()
    send_xz.click()

    #获取第26题，单选
    answer_twenty_six = self.driver.find_element_by_xpath("//android.widget.TextView[contains(@resource-id,'item_tv1') and @text='1']")
    answer_twenty_six.click()
    send_xz.click()

    #获取第27题，单选
    answer_twenty_seven = self.driver.find_element_by_xpath("//android.widget.LinearLayout[2]/android.widget.TextView[contains(@resource-id,'item_tv1') and @text='1']")
    print answer_twenty_seven.text
    print answer_twenty_seven.tag_name
    answer_twenty_seven.click()
    send_xz.click()


    #获取第28题，单选
    answer_twenty_eight = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath("//android.widget.TextView[contains(@resource-id,'item_tv1') and @text='1']"))
    answer_twenty_eight.click()
    send_xz.click()

    #获取第29题，单选
    answer_twenty_nine = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath("//android.widget.TextView[contains(@resource-id,'item_tv1') and @text='1']"))
    answer_twenty_nine.click()
    send_xz.click()

    #获取第30题，单选
    answer_thirty = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath("//android.widget.TextView[contains(@resource-id,'item_tv1') and @text='1']"))
    answer_thirty.click()
    send_xz.click()

    #获取第31题，单选
    answer_thirty_one = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath("//android.widget.TextView[contains(@resource-id,'item_tv1') and @text='2']"))
    answer_thirty_one.click()
    send_xz.click()
    print '完成现病史'

### 既往史

# 获取第32题，多选
    answer_thirty_two = self.driver.find_element_by_xpath(
    "//android.widget.TextView[contains(@resource-id,'item_tv1') and @text='1']")
    answer_thirty_two.click()
    sleep(2)
    much_choice = self.driver.find_element_by_xpath(
        "//android.widget.TextView[contains(@resource-id,'textView1') and @text='没有']")
    much_choice.click()
    comfirm = self.driver.find_element_by_id("include_title_tv_save")
    comfirm.click()
    sleep(2)

    # 获取第33题，多选
    answer_thirty_three = self.driver.find_element_by_xpath(
    "//android.widget.TextView[contains(@resource-id,'item_tv1') and @text='1']")
    answer_thirty_three.click()
    send_xz.click()
    sleep(2)

    # 获取第34题，单选
    answer_thirty_four = self.driver.find_element_by_xpath(
    "//android.widget.TextView[contains(@resource-id,'item_tv1') and @text='1']")
    answer_thirty_four.click()
    send_xz.click()
    sleep(2)

    # 获取第35题，单选
    answer_thirty_five = self.driver.find_element_by_xpath(
    "//android.widget.TextView[contains(@resource-id,'item_tv1') and @text='1']")
    answer_thirty_five.click()
    send_xz.click()
    sleep(2)

    # 获取第36题，单选
    answer_thirty_six = self.driver.find_element_by_xpath(
    "//android.widget.TextView[contains(@resource-id,'item_tv1') and @text='2']")
    answer_thirty_six.click()
    send_xz.click()
    sleep(2)
    print '完成既往史'

### 个人史
        #获取第37题，单选
    answer_thirty_seven = self.driver.find_element_by_xpath("//android.widget.TextView[contains(@resource-id,'item_tv1') and @text='2']")
    answer_thirty_seven.click()
    send_xz.click()
    sleep(2)

        #获取第38题，单选
    answer_thirty_eight = self.driver.find_element_by_xpath("//android.widget.TextView[contains(@resource-id,'item_tv1') and @text='2']")
    answer_thirty_eight.click()
    send_xz.click()
    sleep(2)

### 家族史
        #获取第39题，单选
    answer_thirty_nine = self.driver.find_element_by_xpath("//android.widget.TextView[contains(@resource-id,'item_tv1') and @text='2']")
    answer_thirty_nine.click()
    send_xz.click()
    sleep(2)

### 婚姻史
        #获取第40题，单选
    answer_fourty = self.driver.find_element_by_xpath("//android.widget.TextView[contains(@resource-id,'item_tv1') and @text='2']")
    answer_fourty.click()
    send_xz.click()
    sleep(10)

        #获取第41题，单选
    answer_fourty_one = self.driver.find_element_by_xpath("//android.widget.TextView[contains(@resource-id,'item_tv1') and @text='2']")
    answer_fourty_one.click()
    send_xz.click()

    # 回答完问题分支
    if gender == 1:
        print '已完成'
        sleep(3)
    else:
        print '未完成'
        ran_char_fourty_three = random.choice(question_fourty_three)
        answer_fourty_three = self.driver.find_element_by_xpath("//android.widget.EditText[contains(@resource-id,'et_answer')]")
        answer_fourty_three.send_keys(ran_char_fourty_three.decode('utf-8'))
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