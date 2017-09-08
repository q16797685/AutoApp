#!/usr/bin/python
# coding:utf-8

"""
Created on 2017-xx-xx

@author: Wangchenyang

@功能：公共方法
"""

from time import sleep
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import userdict
import log
import moveAppScreen

slc_answer = ['无', '轻度', '中度', '偏重', '严重']


def openApp(self):
    """ 启动App """
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '4.4.2'
    desired_caps['deviceName'] = 'Android Emulator'
    desired_caps['appPackage'] = 'com.fulcruminfo.patient'
    desired_caps['appActivity'] = 'com.fulcurum.patient.view.splash.Splash'
    desired_caps["unicodeKeyboard"] = "True"  # Appium输入中文
    desired_caps["resetKeyboard"] = "True"  # Appium输入中文

    self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    self.driver.implicitly_wait(10)

    exist_username = self.driver.find_element_by_xpath(
        "//android.widget.Button[contains(@resource-id,'button2')]")
    exist_username.click()
    phonenumber = self.driver.find_element_by_xpath(
        "//android.widget.EditText[contains(@resource-id,'et_phonenumber')]")  # 定位手机元素
    log.recordLog(phonenumber.text, phonenumber.tag_name)
    phonenumber.send_keys(userdict.phnumber)
    password = WebDriverWait(self.driver, 5).until(lambda x: x.find_element_by_xpath(
        "//android.widget.EditText[contains(@resource-id,'et_password')]"))
    log.recordLog(password.text, password.tag_name)
    password.send_keys('123456')
    self.driver.find_element_by_xpath(
        "//android.widget.Button[contains(@resource-id,'btn_login')]").click()  # 点击登录按钮
    sleep(2)
    print '登录成功'


def enterJzzb(self):
    """ 点击就诊准备图标,进入挂号列表"""
    clickjzzb = WebDriverWait(self.driver, 5).until(lambda x: x.find_element_by_xpath(
        "//android.widget.LinearLayout[contains(@resource-id,'lay_jzzb')]"))
    clickjzzb.click()


def chooseGhlb(self):
    """ 选择未开始状态挂号列表"""
    clickghlb = self.driver.find_element_by_xpath(
        "//android.widget.TextView[contains(@resource-id,'tv_state') and @text='未开始']")
    log.recordLog(clickghlb)
    clickghlb.click()
    sleep(2)


def chooseFirst(self):
    """ 未开始状态，进入补充就诊信息,选择初诊"""
    """ 选择未开始状态挂号列表，点击下一步"""
    clickfirst = self.driver.find_element_by_xpath(
        "//android.widget.TextView[contains(@resource-id,'include_title_tv_save')]")
    clickfirst.click()
    sleep(2)


def chooseSecond(self):
    """ 未开始状态，进入补充就诊信息,选择复诊"""
    clicksecond = self.driver.find_element_by_xpath(
        "//android.widget.Button[contains(@resource-id,'btn_fz')]")
    clicksecond.click()
    sleep(2)


def clickZnwz(self):
    """ 进入就诊准备,点击智能问诊"""
    wjdc = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[contains(@resource-id,'lay_questionnaire')]")
    wjdc.click()
    sleep(2)


def clickScfj(self):
    """ 进入就诊准备,点击上传附件"""
    scfj = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[contains(@resource-id,'lay_accessory')]")
    scfj.click()
    sleep(2)


def clickYysq(self):
    """ 进入就诊准备,点击用药申请"""
    yysq = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[contains(@resource-id,'lay_apply_pharmacy')]")
    yysq.click()
    sleep(2)


def clickConfirm(self):
    """ 点击确定按钮"""
    clickconfirm = self.driver.find_element_by_xpath(
        "//android.widget.Button[contains(@resource-id,'button1')]")
    log.recordLog(clickconfirm)
    clickconfirm.click()
    sleep(2)


def clickCancel(self):
    """ 点击确定按钮"""
    clickcancel = self.driver.find_element_by_xpath(
        "//android.widget.Button[contains(@resource-id,'button2')]")
    clickcancel.click()
    sleep(2)


def enterGh(self):
    """ 进入关怀模块"""
    gh = self.driver.find_element_by_xpath(
        "//android.widget.LinearLayout[contains(@resource-id,'lay_sz')]")
    gh.click()
    sleep(2)


def enterScaleList(self):
    """ 进入量表列表"""
    scalclist = self.driver.find_element_by_xpath(
        "//android.widget.TextView[contains(@resource-id,'tv_doctor_name') and @text = '李卫晖']")
    scalclist.click()
    sleep(2)


def chooseScale_SCL(self):
    """ 进入量表列表,选择SCL量表"""
    enterscale = self.driver.find_element_by_xpath(
        "//android.widget.TextView[contains(@resource-id,'tv_scale_name') and @text='SCL-90']")
    enterscale.click()
    sleep(2)


def chooseScale_SAS(self):
    """ 进入量表列表,选择SAS量表"""
    enterscale = self.driver.find_element_by_xpath(
        "//android.widget.TextView[contains(@resource-id,'tv_scale_name') and @text='焦虑自评量表SAS']")
    enterscale.click()
    sleep(2)


def chooseScale_SDS(self):
    """ 进入量表列表,选择SDS量表"""
    enterscale = self.driver.find_element_by_xpath(
        "//android.widget.TextView[contains(@resource-id,'tv_scale_name') and @text='抑郁自评量表SDS']")
    enterscale.click()
    sleep(2)


def chooseScale_DBAS(self):
    """ 进入量表列表,选择睡眠相关信念与态度量表DBAS"""
    enterscale = self.driver.find_element_by_xpath(
        "//android.widget.TextView[contains(@resource-id,'tv_scale_name') and @text='睡眠相关信念与态度量表DBAS']")
    enterscale.click()
    sleep(2)


def chooseScale_ISI(self):
    """ 进入量表列表,选择失眠严重指数ISI"""
    enterscale = self.driver.find_element_by_xpath(
        "//android.widget.TextView[contains(@resource-id,'tv_scale_name') and @text='失眠严重指数ISI']")
    enterscale.click()
    sleep(2)


def chooseScale_SRBQ(self):
    """ 进入量表列表,选择睡眠相关行为问卷SRBQ"""
    enterscale = self.driver.find_element_by_xpath(
        "//android.widget.TextView[contains(@resource-id,'tv_scale_name') and @text='睡眠相关行为问卷SRBQ']")
    enterscale.click()
    sleep(2)


def chooseScale_PSQI(self):
    """ 进入量表列表,选择匹兹堡睡眠质量指数问卷PSQI"""
    enterscale = self.driver.find_element_by_xpath(
        "//android.widget.TextView[contains(@resource-id,'tv_scale_name') and @text='匹兹堡睡眠质量指数问卷PSQI']")
    enterscale.click()
    sleep(2)


def chooseScale_EPQ(self):
    """ 进入量表列表,选择艾森克个性测验EPQ"""
    enterscale = self.driver.find_element_by_xpath(
        "//android.widget.TextView[contains(@resource-id,'tv_scale_name') and @text='艾森克个性测验EPQ']")
    enterscale.click()
    sleep(2)


def click_Confirm(self):
    """ 选择医生后，点击里面确认按钮"""
    click_Confirm = self.driver.find_element_by_xpath(
        "//android.widget.TextView[contains(@resource-id,'tv_confirm')]")
    click_Confirm.click()
    sleep(2)


def choose_Doctor(self):
    """ 选择医生，并往下移动"""
    chooseDoctor = self.driver.find_element_by_xpath(
        "//android.widget.TextView[contains(@resource-id,'tv_q2') and @text='李卫晖']")
    chooseDoctor.click()
    moveAppScreen.getSize(self)
    moveAppScreen.swipeUp(self, 1000)
    sleep(2)


def clickWb(self):
    """ 回答问卷后，点击发送按钮"""
    send_wb = self.driver.find_element_by_xpath(
        "//android.widget.Button[contains(@resource-id,'btn_send_wb')]")
    send_wb.click()


def clickXz(self):
    """ 回答问卷后，点击发送按钮"""
    send_xz = self.driver.find_element_by_xpath(
        "//android.widget.Button[contains(@resource-id,'btn_send_xz')]")
    send_xz.click()